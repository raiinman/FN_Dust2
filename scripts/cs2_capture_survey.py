"""Capture a configured directional survey through the existing worker.

--plan JSON --session QUEUE --addon PATH --output PRIVATE_DIRECTORY.
Stops on first helper failure. Completed IDs may be resumed; incomplete attempts
require inspection and a new ID. Captures still require visual review/upload.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys

def main(a):
    plan=json.loads(a.plan.read_text(encoding='utf-8'))
    a.output.mkdir(parents=True,exist_ok=True)
    progress=dict(status='capturing; not reviewed',completed=[],total=len(plan['captures']))
    status=a.output/'survey_progress.json'
    for c in plan['captures']:
        existing=a.output/(c['id']+'.json')
        if existing.exists():
            r=json.loads(existing.read_text())
            if r['requested_pose']!=c['pose']:
                raise RuntimeError('Existing capture pose differs from plan')
        else:
            cmd=[sys.executable,str(Path(__file__).with_name('cs2_capture.py')),c['id'],
                '--session',str(a.session),'--addon',str(a.addon),'--output',str(a.output),
                '--pose',*[str(v) for v in c['pose']]]
            r=subprocess.run(cmd,capture_output=True,text=True)
            if r.returncode:
                progress.update(status='failed; inspect attempt before continuing',failed_id=c['id'],error=r.stderr)
                status.write_text(json.dumps(progress,indent=2),encoding='utf-8')
                raise RuntimeError(r.stderr)
        progress['completed'].append(c['id'])
        status.write_text(json.dumps(progress,indent=2),encoding='utf-8')
        print(json.dumps(dict(captured=c['id'],area=c['area'],completed=len(progress['completed']),total=progress['total'])),flush=True)
    progress['status']='capture complete; visual review and upload pending'
    status.write_text(json.dumps(progress,indent=2),encoding='utf-8')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan',type=Path,required=True)
    p.add_argument('--session',type=Path,required=True)
    p.add_argument('--addon',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    main(p.parse_args())
