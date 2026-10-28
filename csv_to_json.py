"""Rebuild schedule.json course entries using schedule.csv, keeping closures and exceptions."""
import csv,json
from pathlib import Path
root=Path(__file__).parent
with (root/'schedule.csv').open(encoding='utf-8-sig', newline='') as f:
    rows=list(csv.DictReader(f))
data=json.loads((root/'schedule.json').read_text(encoding='utf8'))
data['courses']=rows
(root/'schedule.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(f'Updated schedule.json ({len(rows)} entries).')
