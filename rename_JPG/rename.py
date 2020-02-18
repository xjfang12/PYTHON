#!/bin/python3
# This Script is rename JPG format photo with capture time
# Which infomation exists in EXIF header.
# Usage: rename.py [fold name]
import exifread
import sys
import os
import hashlib  # used to  caculated md5

# pic_path = './tmp_JPG'
pic_path = sys.argv[1]
log_name = pic_path + '_rename.log'
fo = open(log_name, 'w')


def PIC_RENAME(origin_file_name):
    # make origin file path
    origin_file = pic_path + '/' + origin_file_name
    f = open(origin_file, 'rb')
    # Get EXIF information
    tags = exifread.process_file(f)
    # close open file
    f.close()
    # get EXIF DateTimeOriginal information
    if 'EXIF DateTimeOriginal' in tags.keys():
        tag = tags['EXIF DateTimeOriginal']
        newfile_str = str(tag).replace(':', '').replace(' ', '_')
        # print("The newfile_str is:'" + newfile_str + "'")
        # new_file = pic_path + '/' + newfile_str + '.JPG'

        # check whether new_file exists, if exists add a post-fix '_1'
        # if _1 exist then rename to _2
        new_file = add_postfix(newfile_str, origin_file)

        # check whether origin_file name is equal to new_file
        # or rename old to new
        # print("Origin file is: " + origin_file)
        # print("New file is: " + new_file)

        # origin file's md5
        # origin_md5 = Calcmd5(origin_file)
        # print("Origin file's md5=" + origin_md5)
        # new file's md5
        # new_md5 = Calcmd5(new_file)

        if new_file is False:
            print(origin_file + " have the right name")
            fo.write("\t" + origin_file + " have the right name\n")
        else:
            os.rename(origin_file, new_file)
            print(origin_file + '  =========>  ' + new_file)
            fo.write("\t" + origin_file + '  =========>  ' + new_file + "\n")
    else:
        print("There is no EXIF DateTimeOriginal in EXIF information")
        fo.write("\tThere is no EXIF DateTimeOriginal in EXIF information\n")


def LIST_JPG():
    file_list = os.listdir(pic_path)
    # print(file_list)
    for pic_file in file_list:
        if pic_file.endswith('.JPG'):
            print('Processing ' + pic_path + '/' + pic_file)
            fo.write('Processing ' + pic_path + '/' + pic_file + '\n')
            PIC_RENAME(pic_file)
            print("\n")
            fo.write('\n')


def add_postfix(filename_str, originfile):
    # Calculate origin file's md5
    origin_md5 = Calcmd5(originfile)
    print("Origin file's md5 is: " + origin_md5)
    fo.write("\tOrigin file's md5 is: " + origin_md5 + "\n")

    # Initiate the repeat name counter
    i = 0
    # Set the default newfile name
    newfile = pic_path + '/' + filename_str + '.JPG'

    while True:
        # check whether the newfile exists
        # if exists change newfile name by add postfix with counter
        if os.path.isfile(newfile):
            new_md5 = Calcmd5(newfile)
            print(newfile + "'s md5 is: " + new_md5)
            fo.write('\t' + newfile + "'s md5 is: " + new_md5 + '\n')
            if origin_md5 == new_md5:
                return False
            else:
                i += 1
                newfile = pic_path + '/' + filename_str + '_' + str(i) + '.JPG'
        else:
            return newfile


def Calcmd5(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.md5()
        sha1obj.update(f.read())
        md5 = sha1obj.hexdigest()
        # print(hash)
        return md5


# PIC_RENAME('IMG_9113.JPG')


LIST_JPG()
fo.close()
