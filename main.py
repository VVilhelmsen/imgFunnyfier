#!/usr/bin/env python3
import os
import random
from os import scandir

nouns = []
adjectives = []
rootdir = '/path/to/picture/folder'

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi",".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
                    
with open('nouns.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nouns.append(line.replace('\n',''))
    
with open('adjectives.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        adjectives.append(line.replace('\n','').replace(' ',''))

for entries in os.scandir(rootdir):
    if entries.is_dir():
        folder_name = entries.name
        with scandir(entries) as entries:
            for entry in entries:
                filename = entry.name
                for image_extension in image_extensions:
                    if filename.lower().endswith(image_extension):
                        os.system(f"mv '{rootdir}{folder_name}/{filename}' '{rootdir}{folder_name}/{''.join(random.choice(adjectives))}_{random.choice(nouns)}{image_extension}'")
    else:
        for entry in scandir(rootdir):
            filename = entry.name
            for image_extension in image_extensions:
                if filename.lower().endswith(image_extension):
                    os.system(f"mv '{rootdir}{filename}' '{rootdir}{''.join(random.choice(adjectives))}{random.choice(nouns)}{image_extension}'")