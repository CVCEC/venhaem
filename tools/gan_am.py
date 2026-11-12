#!/usr/bin/env python3
"""Ghi vao-bep/am-ai.js: câu nào đã có file giọng AI (vao-bep/am-ai/<mã>.mp3) thì trang Vào Bếp dùng file đó,
câu nào chưa có thì trang vẫn đọc bằng giọng máy của thiết bị."""
import json, pathlib, unicodedata
ROOT = pathlib.Path(__file__).resolve().parent.parent
AM = ROOT / 'vao-bep/am-ai'
m = {}
for l in (ROOT / 'giong-ai/can-doc.tsv').read_text(encoding='utf-8').splitlines()[1:]:
    ma, giong, chu = (l.split('\t') + ['', '', ''])[:3]
    if ma and (AM / (ma + '.mp3')).exists():
        m[unicodedata.normalize('NFC', chu)] = ma
(ROOT / 'vao-bep/am-ai.js').write_text('/* Giọng đọc AI cho Vào Bếp Nhà Em – do tools/gan_am.py tạo, đừng sửa tay */\nwindow.AM_AI = '
    + json.dumps(m, ensure_ascii=False, sort_keys=True, indent=0) + ';\n', encoding='utf-8')
print(len(m), 'câu đã có giọng AI')
