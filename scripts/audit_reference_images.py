"""Verify registered study JPEG hashes and emit the explicit coverage review.

Run: py -3.11 scripts/audit_reference_images.py
Reads capture metadata and IMAGE_REVIEW.json. Never grants visual acceptance.
"""
import csv
import hashlib
import json
from pathlib import Path


def audit(root):
    reference = root / 'reference'
    review = json.loads((reference / 'IMAGE_REVIEW.json').read_text())
    records = {}
    for name in review['capture_registers']:
        for record in json.loads((reference / name).read_text())['captures']:
            if record.get('repository_image_path'):
                assert record['id'] not in records, record['id']
                records[record['id']] = record
    result = []
    with (reference / 'REFERENCE_MANIFEST.csv').open(newline='',encoding='utf-8-sig') as handle:
        manifest = {r['id']:r for r in csv.DictReader(handle)}
    timestamp_dates_checked = 0
    for identifier, record in records.items():
        path = root / record['repository_image_path']
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == record['jpeg_sha256'], str(path)
        assert identifier in manifest and manifest[identifier]['local_filename']==record['repository_image_path'], identifier
        if record.get('timestamp_utc'):
            assert manifest[identifier]['date_accessed']==record['timestamp_utc'][:10], identifier
            timestamp_dates_checked += 1
        exclusion = review['coverage_exclusions'].get(identifier)
        result.append(dict(id=identifier, area=record['area'],
            image=record['repository_image_path'], sha256=digest,
            coverage_status='EXCLUDED' if exclusion else 'PARTIAL',
            review=exclusion or record['review']))
    assert len(result) == review['expected_image_count']
    view_sets = json.loads((reference / 'AREA_VIEW_REVIEW.json').read_text())
    accepted_sets = []
    for declared in view_sets['sets']:
        assert declared['status'] == 'accepted required views'
        assert view_sets['source_build'] == '25640462'
        assert declared['taxonomy_scope'] in ('critical_area', 'critical_subarea')
        if declared['taxonomy_scope'] == 'critical_subarea':
            assert declared.get('parent_area')
        for role in ('forward', 'reverse', 'wall_read', 'elevation'):
            assert declared['views'][role], (declared['area'], role)
            for identifier in declared['views'][role]:
                assert identifier in records, identifier
                assert records[identifier]['source_build'] == view_sets['source_build']
                assert identifier not in review['coverage_exclusions'], identifier
        assert declared['review'] and declared['remaining']
        accepted_sets.append(declared)
    output = dict(review_date=review['review_date'], source_build='25640462',
        registered_images=len(result),
        native_timestamp_dates_checked=timestamp_dates_checked,
        coverage_excluded=sum(r['coverage_status']=='EXCLUDED' for r in result),
        complete_areas=sum(s['taxonomy_scope']=='critical_area' for s in accepted_sets),
        complete_subareas=sum(s['taxonomy_scope']=='critical_subarea' for s in accepted_sets),
        declared_view_sets=accepted_sets,
        scope='Image integrity and declared combined-view reviews; no metric or topology acceptance',
        gate_1='FAIL', images=result)
    (reference / 'IMAGE_AUDIT.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k not in ('images', 'declared_view_sets')}))


if __name__ == '__main__':
    audit(Path(__file__).resolve().parent.parent)
