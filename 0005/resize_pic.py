#!C:/Python310/python.exe
# -*- coding: UTF-8 -*-

import os
import sys
from PIL import Image, ImageDraw, ImageFont
import fnmatch  

#要设定自己的图片目录
BASE_DIR='~/Pictures'
WIDTH_MAX=1136
HEIGHT_MAX=640
RADIO=round(WIDTH_MAX / HEIGHT_MAX, 2)
#要设定缩小后图片的存放目录
BACKUP_DIR='/tmp/new_pics'

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_new_pic(image,new_width, new_height,filename):
    try:
        
        resized_image = image.resize((new_width, new_height))
        filepath = os.path.join(BACKUP_DIR, filename) 
        resized_image.save(filepath)
        image.close()
    except ValueError as error:
        print(error)      

    
def resize_img(root, filename):
    filepath = os.path.join(root, filename) 
    image = Image.open(filepath)  
    width, height = image.size 
    radio_orig = round(width / height,3) 
    new_width,new_height = width, height
    # 宽和高都小于的话就不用做什么了
    if (width<WIDTH_MAX and height<HEIGHT_MAX):
        pass
    # 宽大于高，就是横幅的情况，等比例到iphone5后，高不会超过640d
    # 以iphone5的宽为标准,等比例缩小
    elif radio_orig>1 and radio_orig>RADIO :
        new_width = WIDTH_MAX
        new_height = round( WIDTH_MAX/radio_orig)
    elif radio_orig>1 and radio_orig <=RADIO:    
        new_height = HEIGHT_MAX
        new_width = round( HEIGHT_MAX*radio_orig)
    elif radio_orig<=1 and radio_orig>RADIO :
        new_width = HEIGHT_MAX
        new_height = round( new_width/radio_orig)        
    elif radio_orig<=1 and radio_orig<RADIO :
        new_height = WIDTH_MAX
        new_width = round( new_height*radio_orig)        

    if new_height>0 and new_width>0:
        save_new_pic(image,new_width, new_height,filename)
    else: 
        print(f'Filename: {filepath}: {width}, {height}, {new_width}, {new_height} ')
    
def find_images(directory, extensions):  
    for root, dirs, files in os.walk(directory):  
        for filename in files:  
            if any(fnmatch.fnmatch(filename, "*.{}".format(ext)) for ext in extensions):  
                #print(os.path.join(root, filename))  
                resize_img(root, filename)

extensions = ["jpg", "png", "jpeg", "gif", "bmp", "tiff"]  

create_dir(BACKUP_DIR)
find_images(BASE_DIR, extensions)