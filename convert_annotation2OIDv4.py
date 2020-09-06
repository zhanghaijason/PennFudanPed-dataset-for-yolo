# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 01:09:31 2020

@author: Haijie
"""
import os

def main():
    path = "Annotation"
    desti_path = "Label"
    if not os.path.isdir(desti_path):
        os.mkdir(desti_path)
    for dir,subdir,files in os.walk(path):
        for file in files:
            convert_annotation(path, desti_path, str(file))
    print("Annotation conversion done! They are in the same folder with this python file.")
    
    
def convert_annotation(folder, desti_path, filename):
    
    fullname = folder+"/"+filename
    
    new_filename = filename
    unwanted_chars = ['(', ")", '-', ',', '"', ':']
    with open(fullname) as f:
        content = f.readlines()
        for i, val in enumerate(content): 
            if(val.startswith('Bounding box for object ')):
                numbers = []
                for i in unwanted_chars:
                    val = val.replace(i, '')   # remove unwanted chars
                for x in val.split():          # split the string into substrings with space split
                    if(i == 0):
                        continue
                    if x.isdigit():
                        numbers.append(x)
                print(numbers)
                with open(os.path.join(desti_path, new_filename), 'a') as filehandle:
                    for i in range(len(numbers)):
                        if i == 0:
                            filehandle.write("Pedestrian ")
                        else:
                            filehandle.write(numbers[i]+" ")
                    filehandle.write("\n")
                    
                    

    
    


if __name__ == '__main__':
    main()

