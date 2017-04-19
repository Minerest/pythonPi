# Include the Dropbox SDK
import dropbox
import requests
import json
import os
dbx = dropbox.Dropbox("U_-09_UYjpAAAAAAAAAAGTXNlVAQpUXm1yHHPrnvPjWP3-wMZYMyA6IlB4RJwK5S")
pcPath = "C:\\Users\\ericd\\Desktop\\rPi\\Python\\dbx"

def main():
        #download what's not on dropbox
    usrChk = input("Do you want to check dropbox for downloads?[Y/N]")
    print (usrChk)
    if usrChk == "Y" or usrChk == "y":
        dbxDown()
        #Delete files that are saved locally but not on dropbox
    usrChk = input("Do you want to delete local files to match dropbox?[Y/N")
    if usrChk == "Y" or usrChk == "y":
        delFiles()
#=======================================================================

def delFiles(): #delete files locally if files aren't on dropbox
    print("Starting delFiles()")
    pcFiles = [x for x in os.listdir(pcPath) if not x.endswith(".ini")]
    i = -1
    delFile = True
    print("Scanning file:")
    while i < len(pcFiles)-1:
        i+=1
        print(pcFiles[i])
        for entry in dbx.files_list_folder('/rpi').entries:
            if entry.name == pcFiles[i]:
                delFile = False
                break;
        if delFile == True:
            print ("Deleting file: "+str(pcFiles[i]))
            os.remove(pcPath+"\\"+pcFiles[i])
            print(pcFiles[i]+" deleted")
        delFile = True
    return
#=======================================================================
        
def dbxDown():  #Download files that are on dbx but not locally
    print ("Starting dbxDown()")
    fileFnd = False
    pcFiles = [x for x in os.listdir(pcPath)]
    print("Scanning files:")
    i = 0
    for entry in dbx.files_list_folder('/rpi').entries:
        print(entry.name)
        while i < len(pcFiles):
            if entry.name == pcFiles[i]:
                fileFnd = True
                break
            i+=1
            #end while
        if not fileFnd:
            print (entry.name + " was not found on PC, attempting download")
            try:
                dbx.files_download_to_file(pcPath+"\\"+entry.name,entry.path_lower, rev=None)
                pcFiles = [x for x in os.listdir(pcPath)]
                print(entry.name + " downloaded")
            except:
                print(entry.name +" did not download. There was an error somewhere")
        i = 0
        fileFnd = False
        #end for
    return

main() #execute main
