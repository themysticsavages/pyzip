import zipfile, os, time
from os import listdir
from os.path import isfile, join

# Keeps track of files
num = 0

# Goes to specified directory and stores list of files
path=input('Path: ')
os.chdir(path)
files = [f for f in listdir(path) if isfile(join(path, f))]

# Creates zip client.
name = input('File name (adds .zip to end): ')
zipper = zipfile.ZipFile(name + '.zip', 'w')

print('Now zipping ', files, 'to ', name + '.zip')

# Uses list to zip files.
for file in files:
    zipper.write(files[num])
    num = num + 1

print('Finished.')
zipper.close()

time.sleep(3)
