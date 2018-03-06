# -*- coding: utf-8 -*-
from PIL import Image
import subprocess


def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)

    #clean image 处理模糊图片，设置阈值
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    #调用系统的tesseract对图片进行识别
    subprocess.call(["tesseract", newFilePath, "output"])

    #打开文件读取结果
    outputfile = open("output.txt", 'r')
    print(outputfile.read())
    outputfile.close()


cleanFile('text.jpg', 'text2_clean.jpg')