import cv2
import os

def getFiles(path):
    Filelist = []
    for home, dirs, files in os.walk(path):
        for file in files:
            # 文件名列表，包含完整路径
            file_path = os.path.join(home, file).replace('\\', '/')
            Filelist.append(file_path)
            #Filelist.append(file)
    return Filelist

files = getFiles('C:/Users/Administrator/Desktop/ex2/chem/')
for i in files:
    img = cv2.imread(i)
    h, w, c = img.shape
    #print(h, w, c)
    if h != 1500 or w != 1300:
        print(i)
        img = cv2.resize(img, (1300, 1500))
        #cv2.imwrite(i, img)