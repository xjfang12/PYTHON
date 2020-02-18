import exifread
import os
import sys
import hashlib  # used to  caculated md5

# pic_path = './tmp_JPG'
pic_path = sys.argv[1]
log_name = pic_path + '_rename.log'
fo = open(log_name, 'w')


def LIST_JPG():
    file_list = os.listdir(pic_path)
    # print(file_list)
    for pic_file in file_list:
        if pic_file.endswith('.JPG'):
            print('Processing ' + pic_path + '/' + pic_file)
            fo.write('Processing ' + pic_path + '/' + pic_file + '\n')
            full_pic_path = pic_path + '/' + pic_file
            get_info(full_pic_path)
            print("\n")
            fo.write('\n')


def get_info(picfile):
    pic_md5 = Calcmd5(picfile)
    print(picfile + "'s md5 is: " + pic_md5)
    fo.write("\t" + picfile + "'s md5 is: " + pic_md5 + "\n")
    with open(picfile, 'rb') as f:
        tags = exifread.process_file(f)
        exists_and_print('Image Software', tags)
        exists_and_print('Image Orientation', tags)
        exists_and_print('EXIF ShutterSpeedValue', tags)
        exists_and_print('EXIF ApertureValue', tags)
        exists_and_print('EXIF BrightnessValue', tags)


def Calcmd5(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.md5()
        sha1obj.update(f.read())
        md5 = sha1obj.hexdigest()
        # print(hash)
        return md5


def exists_and_print(info_string, file_tags):
    if info_string in file_tags.keys():
        print("Photo's " + info_string + " is: " + str(file_tags[info_string]))
        fo.write("\tPhoto's " + info_string + " is: " + str(file_tags[info_string])+"\n")
    else:
        print("\tThere are no " + info_string + " in EXIF header")


LIST_JPG()
