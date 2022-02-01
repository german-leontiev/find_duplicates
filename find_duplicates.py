import sys
from filecmp import cmp
from pathlib import Path
import shutil
import os


TARGET_FOLDER = Path(sys.argv[1])
TXT_FILENAME = str(sys.argv[2])


files = sorted(os.listdir(TARGET_FOLDER))
  
# List having the classes of documents
# with the same content
duplicateFiles = []
  
# comparison of the documents
for file_x in files:
  
    if_dupl = False
  
    for class_ in duplicateFiles:
        # Comparing files having same content using cmp()
        # class_[0] represents a class having same content
        if_dupl = cmp(
            TARGET_FOLDER / file_x,
            TARGET_FOLDER / class_[0],
            shallow=False
        )
        if if_dupl:
            class_.append(file_x)
            break
  
    if not if_dupl:
        duplicateFiles.append([file_x])

# Print results
with open(TXT_FILENAME, 'w') as f:
    for i in duplicateFiles:
        print(i)
        f.write(str(i) + '\n')
	
