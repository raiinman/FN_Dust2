"""Audit current-build route evidence links, without inferring untested paths.

Run: py -3.11 scripts/audit_route_topology.py. Reads reviewed WALK_PROBES,
TRAVERSAL_PROBES and TOPOLOGY. Writes evidence/TOPOLOGY_AUDIT.json. A successful
audit validates evidence linkage and recorded collision/cleanup preconditions;
manual landing/direction reviews remain in those source registers. It cannot
prove universal reverse impossibility or grant dimensional/Gate1 acceptance.
"""
import json
from pathlib import Path


def audit(root):
    ref = root / 'reference'
    top, walks, traversals = [json.loads((ref / name).read_text()) for name in
        ['TOPOLOGY.json', 'WALK_PROBES.json', 'TRAVERSAL_PROBES.json']]
    walk_reports = {a['report']['id']: a['report'] for a in walks['attempts']}
    traversal_reports = {a['report']['id']: a['report'] for a in traversals['attempts']}
    directions = {d['id']: d for d in traversals['accepted_directions']}
    assert len(directions) == len(traversals['accepted_directions'])

    def collision_checked(report):
        prints = [s.strip() for c in report.get('commands', [])
                  for s in c.get('received_prints', [])]
        assert report.get('collision_mode_reply') == 'noclip OFF' or 'noclip OFF' in prints
        assert report['source_build'] == traversals['source_build'] == '25640462'
        assert report['teleports_during_route'] == 0
        assert 'cleanup_error' not in report

    covered = {}
    for path in walks['accepted_paths']:
        assert path['direction'] == 'both'
        for key in ['forward_report', 'reverse_report']:
            report = walk_reports[path[key]]
            collision_checked(report)
            assert report['status'] == 'completed collision walk'
            assert report['restored_speed'] == 320
        for edge in path.get('edges', []):
            covered.setdefault(edge, []).append(path['id'])
    for direction in directions.values():
        assert direction['reports'] and direction['limits']
        for name in direction['reports']:
            report = traversal_reports[name]
            collision_checked(report)
            assert report['status'].startswith('completed ')

    def traversal_refs(text):
        prefix = 'TRAVERSAL_PROBES.json/'
        assert text.startswith(prefix)
        ids = text[len(prefix):].split(';')
        assert all(name in directions for name in ids)
        return ids

    edges = []
    for edge in top['edges']:
        refs = covered.get(edge['id'], [])
        if edge['id'] not in covered:
            refs = traversal_refs(edge['traversal_evidence'])
        if edge['id'] in ['E11', 'E27']:
            reverse = traversal_refs(edge['reverse_test_evidence'])
            assert len(directions[reverse[0]]['reports']) == 2
            assert directions[reverse[0]]['status'].startswith('accepted observed blocked ')
            refs = refs + reverse
        edges.append(dict(id=edge['id'], mode=edge['mode'], direction=edge['direction'],
                          accepted_evidence=refs))
    specials = [dict(id=s['id'], status=s['status'],
        accepted_evidence=traversal_refs(s['traversal_evidence']))
        for s in top['special_connections']]
    assert len({e['id'] for e in edges}) == len(edges) == 34
    assert len(specials) == 4
    result = dict(source_build='25640462', source_map='de_dust2',
        status='PASS for evidence-linked listed current-build connections',
        scope='Twenty-four reviewed both-direction ground paths; observed special traversal and blocked unsupported reverse jumps at surveyed crossings. Manual stable-landing/direction reviews are owned by source registers. No exhaustive alternative launch/partner test or geometric footprint certification.',
        ground_paths=len(walks['accepted_paths']), edges=edges, special_connections=specials,
        gate_1='FAIL; full critical dimensions, layered architectural footprint and uncertainty remain incomplete')
    (root / 'evidence/TOPOLOGY_AUDIT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(status=result['status'], edges=len(edges), specials=len(specials),
                         ground_paths=result['ground_paths'], gate_1=result['gate_1'])))


if __name__ == '__main__':
    audit(Path(__file__).resolve().parent.parent)
