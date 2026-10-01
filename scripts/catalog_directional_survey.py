"""Catalog reviewed native captures and JPEG derivatives, without copying private logs.

Usage: py -3.11 scripts/catalog_directional_survey.py --captures PRIVATE_DIRECTORY
Requires CAPTURE_PLAN_GATE1.json, DIRECTIONAL_REVIEW_GATE1.json and prepared JPEGs.
Re-running replaces this batch's register rows; it does not duplicate them.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path

FOLDERS=dict(CTSPAWN='ct_spawn',CTMID='ct_mid',TOPMID='mid',LONGA='long_a',
    SHORT='short',UPTUN='upper_tunnels',LOWTUN='lower_tunnels',BSITE='b_site',
    SIDEPIT='side_pit',TSPAWN='t_spawn',ASITE='a_site')

def catalog(root, captures):
    reference=root/'reference'
    plan=json.loads((reference/'CAPTURE_PLAN_GATE1.json').read_text())
    review=json.loads((reference/'DIRECTIONAL_REVIEW_GATE1.json').read_text())
    records=[]
    keep=('id','timestamp_utc','engine_capture_basename','pose_command','pose_unit',
          'width','height','requested_pose','tga_sha256','png_sha256')
    for item in plan['captures']:
        identifier=item['id'];key=identifier.split('_')[1]
        record=json.loads((captures/(identifier+'.json')).read_text())
        assert record['requested_pose']==item['pose']
        assert record['width']==1280 and record['height']==720
        raw=(captures/(identifier+'.png')).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==record['png_sha256']
        path='reference/images/'+FOLDERS[key]+'/'+identifier+'.jpg'
        image=(root/path).read_bytes()
        row={k:record[k] for k in keep}
        row.update(area=item['area'],source_build=plan['source_build'],source_map='de_dust2',
            view=item['view'],floor_datum_id=item['datum_id'],
            review=review['areas'][key][review['view_order'].index(item['view'])],
            status='visually inspected; partial coverage',repository_image_path=path,
            jpeg_sha256=hashlib.sha256(image).hexdigest(),
            jpeg_git_blob_sha=hashlib.sha1(b'blob '+str(len(image)).encode()+b'\0'+image).hexdigest(),
            fov_cs_debug_parameter=90,aspect_ratio='16:9',
            limitations='Native source units; effective FOV and physical conversion unresolved; no inferred boundaries')
        records.append(row)
    payload=dict(source_build=plan['source_build'],gate_1='FAIL',captures=records,
        review_record='DIRECTIONAL_REVIEW_GATE1.json',
        physical_scale='unresolved',rights='User-authorized internal study screenshots; no public release or extracted assets')
    (reference/'CAPTURE_DIRECTIONAL_GATE1.json').write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    ids={r['id'] for r in records}
    for filename in ('SOURCE_CAMERAS.csv','REFERENCE_MANIFEST.csv'):
        with (reference/filename).open(encoding='utf-8',newline='') as stream:
            reader=csv.DictReader(stream);fields=reader.fieldnames;rows=[r for r in reader if r['id'] not in ids]
        for r in records:
            if filename=='SOURCE_CAMERAS.csv':
                p=r['requested_pose']
                row=dict(id=r['id'],area=r['area'],source_x=p[0],source_y=p[1],source_z=p[2],
                    source_pitch=p[3],source_yaw=p[4],source_roll=0,unit='source_units',
                    fov_cs_debug=90,image_path=r['repository_image_path'],status='REFERENCE_PARTIAL')
            else:
                row=dict(id=r['id'],area=r['area'],view_direction=r['view'],
                    source_url_or_id='installed:730/build/25640462/map/de_dust2/capture/'+r['engine_capture_basename'],
                    publisher_or_creator='Valve source; Codex self-capture',date_accessed='2026-10-01',
                    intended_use='geometry/material/lighting/prop',confidence='confirmed native capture; partial coverage',
                    reuse_note='User-authorized internal study screenshot; not extracted asset or public-release clearance',
                    local_filename=r['repository_image_path'],notes=r['review'])
            rows.append(row)
        with (reference/filename).open('w',encoding='utf-8',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)
    readme=reference/'images/README.md'
    text=readme.read_text(encoding='utf-8').split('\n## Directional survey - 2026-10-01')[0]
    text+='\n## Directional survey - 2026-10-01\n\n55 reviewed 1280x720 JPEG references. [Poses, hashes and per-image limits](../CAPTURE_DIRECTIONAL_GATE1.json). Source-axis headings are not a geographic compass. Partial references do not certify Gate 1 coverage.\n\n| Area | +Y | -Y | +X | -X | Down |\n| --- | --- | --- | --- | --- | --- |\n'
    for offset in range(0,len(records),5):
        group=records[offset:offset+5]
        text+='| '+group[0]['area']+' | '+' | '.join('[Image]('+r['repository_image_path'].split('reference/images/')[1]+')' for r in group)+' |\n'
    readme.write_text(text,encoding='utf-8')
    print(json.dumps(dict(reviewed=len(records),total_images=len(list((reference/'images').rglob('*.jpg'))))))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--captures',type=Path,required=True)
    catalog(Path(__file__).resolve().parent.parent,p.parse_args().captures)
