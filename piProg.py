# Include the Dropbox SDK
import dropbox
import requests
import json
import os
dbx = dropbox.Dropbox("apiAcsTkn")
pcPath = "C:\\Users\\ericd\\Desktop\\rPi\\Python\\dbx"
fileFnd = False
pcFiles = [x for x in os.listdir(pcPath)]
i = 0
#files_download_to_file(download_path, path, rev=None)
for entry in dbx.files_list_folder('/rpi').entries:
    while i < len(pcFiles):
        if entry.name == pcFiles[i]:
            print (entry.name + " found at " + pcPath)
            fileFnd = True
            break
        i+=1
        #end while
    if not fileFnd:
        print (entry.name + " was not found on PC, attempting download")
        dbx.files_download_to_file(pcPath,entry.path_lower, rev=None)
    i = 0
    fileFnd = False
    #end for
'''  
        for file in files:
            if file == entry.name:
                boo = True
                print ("File was found both on dropbox and this pc at " + a)
        if not boo:
            print(str(entry.name) + " was not found on this pc")         
    boo = False
'''
