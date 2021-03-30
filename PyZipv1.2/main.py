import zipfile, os, time, shutil
from os import listdir
from os.path import isdir, isfile, join

# Ref1: https://stackoverflow.com/a/25650295
# Ref2: https://stackoverflow.com/q/8933237

def zip():
    clear = lambda: os.system('cls')
    clear()

    # Keeps track of files
    num = 0

    # Goes to specified directory and stores list of files
    path = input('Path: ')
    os.chdir(path)
    files = [f for f in listdir(path) if isfile(join(path, f))]
    dirs = [f for f in listdir(path) if isdir(join(path, f))]

    # Creates zip client.
    name = input('File name (adds .zip to end): ')

    # Checks for existing file name
    if os.path.isfile(name + '.zip'):
        print('This file already exists.')
        time.sleep(2)
        zip()

    zipper = zipfile.ZipFile(name + '.zip', 'w')

    clear()

    # Uses list to zip files.
    for file in files:
        
        print('Zipping contents...')
        
        shutil.make_archive(name, 'zip', path)
        zipper.write(files[num])

        num = num + 1

    print('')
    print('Finished. Saved at ' + path)
    
    zipper.close()
    time.sleep(3)
    
zip()
