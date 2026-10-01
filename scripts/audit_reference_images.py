"""Verify registered study JPEG hashes and emit the explicit coverage review.

Run: py -3.11 scripts/audit_reference_images.py
Reads capture metadata and IMAGE_REVIEW.json. Never grants visual acceptance.
"""
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
    for identifier, record in records.items():
        path = root / record['repository_image_path']
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == record['jpeg_sha256'], str(path)
        exclusion = review['coverage_exclusions'].get(identifier)
        result.append(dict(id=identifier, area=record['area'],
            image=record['repository_image_path'], sha256=digest,
            coverage_status='EXCLUDED' if exclusion else 'PARTIAL',
            review=exclusion or record['review']))
    assert len(result) == review['expected_image_count']
    output = dict(review_date=review['review_date'], source_build='25640462',
        registered_images=len(result),
        coverage_excluded=sum(r['coverage_status']=='EXCLUDED' for r in result),
        complete_areas=0, gate_1='FAIL', images=result)
    (reference / 'IMAGE_AUDIT.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='images'}))


if __name__ == '__main__':
    audit(Path(__file__).resolve().parent.parent)
