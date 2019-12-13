***
Для удаления в директории файлов с неугодныи расширениями 
***
import os
import shutil

input('Start?')

path = '.'
pattern_files = []
jpeg_files = []
trash_files = []
renamed = []
for rootdir, dirs, files in os.walk(path): 
    for file in files:
        if((file.split('.')[-1])=='JPG' or (file.split('.')[-1])=='MOV'):
            y = os.path.join(rootdir, file)
            jpeg_files.append(y)
        else:
            y = os.path.join(rootdir, file)
            trash_files.append(y)

for file in trash_files:
    os.remove(file)

print(trash_files)
input()
