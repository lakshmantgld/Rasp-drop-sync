#!/usr/bin/python
import os
import dropbox
import yaml

with open("./config.yml", "r") as fd:
    info = yaml.load(fd)

print("starting point after access token retrieval from yaml file")

dbx = dropbox.Dropbox(info["app_token"])

list_of_directories_handler = dbx.files_list_folder("")

list_of_directories = [];

for entry in list_of_directories_handler.entries:
    list_of_directories.append(entry.name)

# print(list_of_directories)

os.chdir("../raspsync")

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
            print(dbx.files_download_to_file("/Users/lakshman/entaag/raspsync/" + directory + "/" + media, "/"+ directory + "/"+ media))
    if deletion_list:
        print("files to be deleted:")
        print(deletion_list)
        for media in deletion_list:
            os.remove("/Users/lakshman/entaag/raspsync/" + directory + "/" + media)
