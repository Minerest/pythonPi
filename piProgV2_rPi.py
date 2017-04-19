# Include the Dropbox SDK
import dropbox
import requests
import json
import os

dbx = dropbox.Dropbox("dbxKey")
pcPath = "/home/pi/Desktop/dbxFiles"

print("Begin loop")
def main():
        #download what's not on dropbox
    
    dbxDown()
        #Delete files that are saved locally but not on dropbox
    delFiles()

def delFiles(): #delete files locally if files aren't on dropbox
    pcFiles = [x for x in os.listdir(pcPath) if not x.endswith(".ini")]
    i = -1
    delFile = True
    while i < len(pcFiles)-1:
        i+=1
        print (pcFiles[i])
        for entry in dbx.files_list_folder('/rpi').entries:
            if entry.name == pcFiles[i]:
                delFile = False
                break;
        if delFile == True:
            print ("Deleting file: "+str(pcFiles[i]))
            #os.remove(pcPath+"/"+pcFiles[i])
            print(pcFiles[i]+" deleted")
        delFile = True            

def dbxDown():
    fileFnd = False
    pcFiles = [x for x in os.listdir(pcPath)]

    i = 0
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
            try:
                dbx.files_download_to_file(pcPath+"/"+entry.name,entry.path_lower, rev=None)
                pcFiles = [x for x in os.listdir(pcPath)]
            except:
                print(entry.name +" did not download. There was an error somewhere")
        i = 0
        fileFnd = False
        #end for

main() #execute main
