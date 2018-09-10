################################################
# A File restoration script By Avinash Karhana #
################################################

#V 1.0

from pathlib import Path
import shutil
import datetime
n=datetime.datetime.now()
fp='/Users/avinashkarhana/Documents/GIT/pycron/testloc/testfile.txt' #destination file(the restoration folder with filename)
m=Path(fp)
s='/Users/avinashkarhana/Documents/GIT/pycron/testbackup/testfile.txt' #source file(backuped folder and file)
d='/Users/avinashkarhana/Documents/GIT/pycron/testloc' #destination folder(the restoration folder)
if not m.is_file():
    #shutil.copy2('/src/dir/file.ext', '/dst/dir/'+str(n)+'.ext')
    shutil.copy2(s,d)
