#!/usr/bin/python
# 
#
#
#
#


from __future__ import division
import os
import dropbox
import yaml

with open("/Users/lakshman/entaag/lddroprasp/config.yml", "r") as fd:
    info = yaml.load(fd)
try:
    print("starting point after access token retrieval from yaml file")

    dbx = dropbox.Dropbox(info["app_token"])

    list_of_directories_handler = dbx.files_list_folder("")

    list_of_directories = [];

    for entry in list_of_directories_handler.entries:
        list_of_directories.append(entry.name)
except:
    print " error in access token and listing files from dropbox"

# print(list_of_directories)

os.chdir("/Users/lakshman/entaag/raspsync")

for directory in list_of_directories:
    print(directory)
    if not os.path.exists("/Users/lakshman/entaag/raspsync/" + directory):
        os.mkdir("/Users/lakshman/entaag/raspsync/" + directory, 0755)

    local_files = os.listdir("/Users/lakshman/entaag/raspsync/" + directory)
    print("local_files  ")
    print(local_files)
    dropbox_files = []
    addition_list = []
    deletion_list = []
    try:
        for media in dbx.files_list_folder("/"+ directory).entries:
            dropbox_files.append(media.name)
        print("dropbox_files   ")
        print(dropbox_files)
        deletion_list = list(set(local_files) - set(dropbox_files))
        addition_list = list(set(dropbox_files) - set(local_files))
        if addition_list:
            print("files to be downloaded:")
            print(addition_list)
            for media in addition_list:
                filename = open("/Users/lakshman/entaag/raspsync/" + directory + "/" + media, "wb")
                try:
                    metadata, req  = dbx.files_download("/"+ directory + "/"+ media)
                    print(metadata.size)
                    total = 0
                    while total < metadata.size:
                        filename.write(req.raw.read(4096))
                        total += 4096
                        print("percentage completed:")
                        print (int(((total/int(metadata.size)) * 100)))
            # print("the request object is ")
            # print(req.content)
            # req.read(4096);
                    if deletion_list:
                        print("files to be deleted:")
                        print(deletion_list)
                        for media in deletion_list:
                            os.remove("/Users/lakshman/entaag/raspsync/" + directory + "/" + media)
                except:
                    os.remove("/Users/lakshman/entaag/raspsync/" + directory + "/" + media)
                    print "download error"
                else:
                    print "small try completed"
    except dropbox.exceptions.ApiError:
        print "error"
    else:
        print "Big try completed"
