import math
from os import walk
import pygame

def dist(x1,y1,x2,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def hw():
    print("Hello World !")

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/'+ image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

def approx(num, targetNum, approximation):
   return num>targetNum-approximation and num<targetNum + approximation