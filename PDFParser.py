import os
import sys
import fitz
print(fitz.__doc__)

# 文件必须和.py文件同目录
file = sys.argv[1]
doc = fitz.open(file)

for page in doc:
    print(page.firstAnnot.info)

