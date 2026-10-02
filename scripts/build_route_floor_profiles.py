"""Rebuild measured route floor sample CSV and elevation charts.

Reads reviewed ROUTE_FLOOR_PROFILES and corrected repeated connector floors.
Walking reports corroborate XY only. Charts connect sample order with dashes;
chainage sums XY sample chords and is never actual walking distance or floor
interpolation. No complete route clearance, grade or endpoint extent inferred.
"""
import csv,json,math
from pathlib import Path
from html import escape
from build_connector_profile import points

def build(root):
 ref=root/'reference';data=json.loads((ref/'ROUTE_FLOOR_PROFILES.json').read_text());profile=json.loads((ref/'CONNECTOR_SURFACE_PROFILES.json').read_text());p=points(profile);factor=json.loads((ref/'SCALE_CALIBRATION.json').read_text())['cm_per_source_unit'];assert factor==2.54 and data['source_build']==profile['source_build'];rows=[];charts=[]
 walking=json.loads((ref/'WALK_PROBES.json').read_text());walk_ids={a['report']['id'] for a in walking['attempts']}
 for group in data['groups']:
  assert group['source_walk_report'] in walk_ids and group['floor_reports']==[v['id'] for v in group['points']]
  chord=0;last=None;chart=[]
  for sample,id in zip(group['points'],group['floor_reports']):
   point=p[id];assert math.dist(point[:2],sample['xy'])<=.02
   if last is not None:chord+=math.dist(point[:2],last[:2])*factor
   row=dict(route=group['route'],id=id,source_walk_report=group['source_walk_report'],x_native=point[0],y_native=point[1],z_native=point[2],x_cm=round(point[0]*factor,4),y_cm=round(point[1]*factor,4),z_cm=round(point[2]*factor,4),sample_chord_chain_cm=round(chord,4),walk_origin_z_native=sample['source_walk_pose'][2],walk_minus_measured_floor_native=round(sample['source_walk_pose'][2]-point[2],6),confidence='confirmed repeated corrected collision-floor point',limits='Native floor supplies Z; walking telemetry selects origin only. Sample chord chain is not walking length or an interpolated floor surface.');rows.append(row);chart.append(row);last=point
  charts.append((group['route'],chart))
 with (ref/'ROUTE_FLOOR_SAMPLES.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
 height=150+math.ceil(len(charts)/2)*240+110;svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="{height}" viewBox="0 0 1500 {height}">','<rect width="1500" height="100%" fill="#12202b"/>','<g fill="#edf4f8" font-family="Arial">','<text x="35" y="38" font-size="25">Dust II — measured floor points on reviewed walking routes</text>','<text x="35" y="70" font-size="17">Build25640462 · 2.54cm/native · each point independently repeated · source walking feet are not floor elevations</text>','<text x="35" y="101" font-size="17">Horizontal axis: cumulative XY sample chords. Dashed links show order only; gaps and continuous floor remain unmeasured.</text>']
 for index,(route,chart) in enumerate(charts):
  left=55+(index%2)*745;top=165+(index//2)*240;length=chart[-1]['sample_chord_chain_cm'];low=min(r['z_cm'] for r in chart)-15;high=max(r['z_cm'] for r in chart)+15;span=high-low;x=lambda d:left+d/length*620;y=lambda z:top+155-(z-low)/span*155
  svg.append(f'<text x="{left}" y="{top-20}" font-size="18">{escape(route)}</text><path d="M{left},{top}V{top+155}H{left+620}" stroke="#6a879a" fill="none"/>')
  coords=[(x(r['sample_chord_chain_cm']),y(r['z_cm'])) for r in chart];svg.append('<path d="'+' '.join(('M' if i==0 else 'L')+f'{u:g},{v:g}' for i,(u,v) in enumerate(coords))+'" fill="none" stroke="#6a879a" stroke-dasharray="5 8"/>')
  for r,(u,v) in zip(chart,coords):svg.append(f'<g><title>{escape(r["id"])}: Z{r["z_cm"]}cm; sample XY chain{r["sample_chord_chain_cm"]}cm</title><circle cx="{u:g}" cy="{v:g}" r="4" fill="#72ddd3"/></g>')
  svg.append(f'<text x="{left}" y="{top+182}" font-size="13">0</text><text x="{left+620}" y="{top+182}" text-anchor="end" font-size="13">{length/100:.3f}m sample-chord chain</text><text x="{left+7}" y="{top+15}" font-size="13">Z{high/100:+.3f}m</text><text x="{left+7}" y="{top+145}" font-size="13">Z{low/100:+.3f}m</text>')
 svg.extend([f'<text x="35" y="{height-65}" font-size="18">{len(rows)} repeated floor points on{len(charts)} paths. Each chart uses its own vertical scale.</text>',f'<text x="35" y="{height-30}" font-size="16">Local point evidence only: critical transverse clearance, continuous grade, full terminals and architectural footprint require separate checks.</text>','</g></svg>']);(ref/'ROUTE_FLOOR_PROFILES.svg').write_text('\n'.join(svg)+'\n');print(len(rows),'repeated floor points;',len(charts),'paths;no continuous interpolation accepted')
if __name__=='__main__':build(Path(__file__).resolve().parent.parent)
