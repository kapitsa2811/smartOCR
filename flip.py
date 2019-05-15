import cv2
import os

basePath="C:\\Users\Lenovo\PycharmProjects\IntelligentOCR\\allTables\\"

for img in os.listdir(basePath):
    image=cv2.imread(basePath+img)
    image=255-image

    cv2.imwrite(basePath+img,image)
