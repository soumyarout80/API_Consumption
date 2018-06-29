import os
import json
from os import listdir
from os.path import isfile, join , isdir
lis=[]
onlyfiles = [f for f in listdir('/opt') if isfile(join('/opt', f))]
onlydirectory = [f for f in listdir('/opt') if isdir(join('/opt', f))]
if len(onlydirectory) >0:
    for i in onlydirectory[1:]:
         fullpath1 = '/opt' + "/" + i
         files = os.listdir(fullpath1)
         for file_name in files:
            fullpath = fullpath1 + "/" + file_name
            if os.path.isfile(fullpath):
                file_size = os.path.getsize(fullpath)
                lis.append([fullpath,file_size])
         newdict = {'files':lis}
         print(json.dumps(newdict))
