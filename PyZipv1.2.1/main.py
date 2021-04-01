import zipfile, os, sys, time
from os import path

def start():
    clear = lambda: os.system('cls')
    clear()

    # Asks for input
    target_dir = input('Path: ')
    name = input('Name: ')

    os.chdir(target_dir)

    if os.path.isfile(name + '.zip'):
            print('WARNING! This file already exists. Do you want to overwrite? (y/n)')
            ans = input(': ')

            if ans == 'y':
                print('Continuing...')

            if ans == 'n':
                clear()
                exit()

    clear()

    def zipfolder(foldername, target_dir):            
        # Creates zip client
        zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
        rootlen = len(target_dir) + 1
        
        # Finds files in choses directory       
        for base, dirs, files in os.walk(target_dir):
            
            for file in files:
                fn = os.path.join(base, file)
                
                print('Zipping ', fn[rootlen:],)
                zipobj.write(fn, fn[rootlen:])
                

    zipfolder(name, target_dir)
    print('Finished successfully! Archive saved at', target_dir)
    sys.exit()
start()