"""Create a provisional metadata-only Phase 1 batch from an inspected CSDB page.

Usage: py -3.11 scripts/reference_batch.py --html ../reference_cache/csdb.html
Never copies source images, prose, meshes or textures into the repository.
Writes normalized plan markers, source manifest, survey tasks and route summary.
Public pins locate callout labels, not architectural corners or physical dimensions.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
AREAS = ['T Spawn','Outside Long','Long Doors','Pit','Long A','A Site',
         'Short / Catwalk','Top Mid','Mid','CT Mid','CT Spawn','B Doors',
         'B Site','Upper Tunnels','Lower Tunnels','connectors/transition spaces']

def rows(path, columns, data):
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path, required=True)
    args=parser.parse_args()
    raw=args.html.read_bytes()
    pins=None
    for match in re.finditer(r'self\.__next_f\.push\((.*?)\)</script>', raw.decode('utf-8')):
        try:
            chunk=json.loads(match[1])[1]
            start=chunk.find('"pins":')
            if start >= 0:
                pins=json.JSONDecoder().raw_decode(chunk[start+7:])[0]
                break
        except (ValueError, IndexError, TypeError):
            continue
    if not pins or len({p['name'] for p in pins}) != len(pins):
        raise ValueError('Missing or duplicated pin metadata; input format changed')
    rows(ROOT/'reference/PLAN_LANDMARKS.csv',
         ['name','radar_u','radar_v','source_id','status'],
         [dict(name=p['name'],radar_u=p['x'],radar_v=p['y'],source_id='PLAN_CSDB',
               status='publisher-reported normalized label center; not metric survey') for p in pins])
    manifest=[]
    def entry(id,area,view,url,creator,use,confidence,notes):
        manifest.append(dict(id=id,area=area,view_direction=view,source_url_or_id=url,
            publisher_or_creator=creator,date_accessed='2026-10-01',intended_use=use,
            confidence=confidence,reuse_note='Metadata only; no source media redistributed',
            local_filename='',notes=notes))
    entry('BASELINE_LOCAL','all','metadata','installed:730/build/25640462','Valve',
          'revision','confirmed','Observed installed manifest and steam.inf; in-session version pending')
    entry('PLAN_CSDB','all','plan','https://csdb.gg/maps/dust2/','CSDB',
          'geometry','estimated','Radar inspected; label positions only; source build not pinned; page warns geometry freshness is not guaranteed')
    entry('PLAN_CALLER','all','plan','https://cs2caller.com/dust2/callouts','CS2 Caller',
          'geometry','estimated','Radar inspected as topology crosscheck; old descriptive claims require local validation')
    entry('TOOLS_PROTOCOL','all','metadata','https://github.com/theokyr/CS2RemoteConsole',
          'theokyr','tooling','confirmed','Implementation specifies tools mode; connection still unverified locally')
    for index,area in enumerate(AREAS,1):
        entry(f'AREA_PLAN_{index:02}',area,'plan','https://csdb.gg/maps/dust2/',
              'CSDB','geometry','estimated','Plan locator only. Does not satisfy forward/reverse/side/elevation coverage.')
    rows(ROOT/'reference/REFERENCE_MANIFEST.csv',list(manifest[0]),manifest)
    topology=json.loads((ROOT/'reference/TOPOLOGY.json').read_text(encoding='utf-8'))
    tasks=[]
    for edge in topology['edges']+topology['special_connections']:
        tasks.append(dict(id=edge['measurement'],area=edge['from']+' / '+edge['to'],
            feature='connection clearance and elevation',required_evidence='current-build endpoints and directional views',
            status='unresolved',value_cm='',source_id='',notes='Not a measured dimension'))
    extra=[('Long Doors','outer aperture width/height and door leaf clearance'),
           ('Long Doors','inner aperture width/height and chamber spans'),
           ('Mid Doors','wall aperture width/height and passage clearance'),
           ('B Doors','wall aperture width/height and passage clearance'),
           ('B Window','sill elevation and aperture width/height'),
           ('Short Stairs','width; count; rise; run; total elevation'),
           ('Tunnel Stairs','width; count; rise; run; total elevation'),
           ('A Ramp','width; horizontal run; rise; slope angle'),
           ('Pit','rim-to-floor depth and footprint'),
           ('A Site','platform span and floor datum'),
           ('B Site','courtyard spans; platform and cover dimensions'),
           ('Mid','Xbox cover width/depth/height and Catwalk relative elevation'),
           ('Long A','clear route width and Long-to-A sightline distance'),
           ('T Spawn','spawn spans; Mid wall/occlusion and drop height'),
           ('all','footprint; scale anchors; source-axis transform')]
    for i,(area,feature) in enumerate(extra,39):
        tasks.append(dict(id=f'D{i:03}',area=area,feature=feature,
            required_evidence='repeated source endpoints with source-unit and centimeter calibration',
            status='unresolved',value_cm='',source_id='',notes='Split compound tasks into atomic measurements during survey'))
    rows(ROOT/'reference/SURVEY_TASKS.csv',list(tasks[0]),tasks)
    text=['# Route Graph','','## Status','',topology['status']+'. Gate 1 has not passed.',
          '','Sources: PLAN_CSDB and PLAN_CALLER in REFERENCE_MANIFEST.csv.',
          'Nodes describe area relationships; they are not polygon outlines or route lengths.',
          '','## Area adjacency','','| Edge | From | To | Traversal | Direction | Elevation | Survey task |',
          '| --- | --- | --- | --- | --- | --- | --- |']
    for edge in topology['edges']:
        text.append('| '+' | '.join(str(edge[k]) for k in ['id','from','to','mode','direction','elevation','measurement'])+' |')
    text+=['','## Special traversal — independent validation required','',
           '| ID | From | To | Mode | Uncertainty | Survey task |','| --- | --- | --- | --- | --- | --- |']
    for edge in topology['special_connections']:
        text.append('| '+' | '.join(str(edge[k]) for k in ['id','from','to','mode','status','measurement'])+' |')
    text+=['','## Required topology checks','',
           '- Long Doors contains two apertures and a chamber; do not replace it with one portal.',
           '- Lower connects through Tunnel Stairs to Upper; do not add a direct outside-to-Lower doorway.',
           '- B Window is a raised traversal opening, distinct from B Doors.',
           '- Catwalk above Mid and Under A beneath A must survive plan/elevation validation.',
           '- Visibility across a wall or door gap does not establish a traversable connection.',
           '- Do not add the special traversal edges to the ordinary walking graph.',
           '- Audit exact forward/reverse affordances in the installed build before acceptance.',
           '','## Remaining uncertainty','','See UNCERTAINTY.md and SURVEY_TASKS.csv. No numeric width/elevation is yet accepted.','']
    (ROOT/'reference/ROUTE_GRAPH.md').write_text('\n'.join(text),encoding='utf-8')
    print(json.dumps({'source_html_sha256':hashlib.sha256(raw).hexdigest(),
                      'manifest_rows':len(manifest),'plan_markers':len(pins),
                      'survey_tasks':len(tasks),'gate':'NOT EVALUATED; no metric truth claim'},indent=2))

if __name__=='__main__':
    main()
