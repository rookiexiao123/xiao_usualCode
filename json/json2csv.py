# -*- coding:utf8 -*-

"""
1.标注了一批json文件，删除没有标注的img
2.把json文件转成csv
"""
import os
import shutil
import cv2
import csv
import json

def getFiles(path):
    filesList = []
    for home, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(home, file).replace('\\', '/')
            #file_path = os.path.join(file).replace('\\', '/')
            filesList.append(file_path)

    return filesList

# 去掉没有化学式的图像

r"""
jsons_path = r'C:\Users\Administrator\Desktop\ex2\json\\'.replace('\\', '/')
print(jsons_path)
json_files = getFiles(jsons_path)
print(len(json_files))

img_path = r'C:\Users\Administrator\Desktop\ex2\pics\\'.replace('\\', '/')
img_files = getFiles(img_path)

for i in json_files:
    name = os.path.split(i)[1].replace('json', 'png')

    if name in img_files:
        #shutil.copy(img_path + name, 'C:/Users/Administrator/Desktop/ex2/chem/')
        print(img_path + name)
"""

# 把json转成csv
json_files = getFiles('C:/Users/Administrator/Desktop/ex2/json/')
print(len(json_files))
"""
for file in json_files:
    with open(file, 'r') as load_f:
        f = json.load(load_f)

        image_name = os.path.split(f['imagePath'])[1]

        img = cv2.imread('C:/Users/Administrator/Desktop/ex2/chem/' + image_name)
        boxes = ''
        if len(f['shapes']) == 0:
            continue
        for index, i in enumerate(f['shapes']):
            x1, y1 = int(i['points'][0][0]), int(i['points'][0][1])
            x2, y2 = int(i['points'][1][0]), int(i['points'][1][1])

            x1_left = min(x1, x2)
            y1_left = min(y1, y2)

            x2_right = max(x1, x2)
            y2_right = max(y1, y2)


            cv2.rectangle(img, (x1_left, y1_left), (x2_right, y2_right), (0, 0, 255), 1)
            if index == len(f['shapes']) - 1:
                boxes = boxes + ('W' + str(x1_left) + ',' + 'H' + str(y1_left) + ',' + 'W' + str(x2_right) + ',' + 'H' + str(y2_right))
            else:
                boxes = boxes + ('W' + str(x1_left) + ',' + 'H' + str(y1_left) + ',' + 'W' + str(x2_right) + ',' + 'H' + str(y2_right) + '|')
        with open('C:/Users/Administrator/Desktop/ex2/extent_test_jmc.csv', 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([image_name, boxes])


        cv2.imwrite('C:/Users/Administrator/Desktop/ex2/gtbox/' + image_name, img)
"""