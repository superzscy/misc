#!/usr/bin/python

import sys
import os
import hashlib

def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def check_for_duplicates(paths):
    hashes = {}
    hashobj = hashlib.sha1()
    fileNames = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hashobj.update(chunk)
                file_hash = hashobj.digest()
                contentDuplicateFile = hashes.get(file_hash, None)
                if contentDuplicateFile:
                    print "content duplicate found: [%s]  [%s]" % (full_path, contentDuplicateFile)
                else:
                    hashes[file_hash] = full_path

                # nameDuplicateFile = fileNames.get(filename, None)
                # if nameDuplicateFile:
                #     print "file name duplicate found: [%s]  [%s]" % (full_path, nameDuplicateFile)
                # else:
                #     fileNames[filename] = full_path

if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])
else:
    print "Please pass the paths to check as parameters to the script"
