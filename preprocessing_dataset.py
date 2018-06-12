#coding:utf-8
import os
from PIL import Image
import numpy as np

def resize(dir,savePath,num,openUrl):
    files = os.listdir(dir)
    files.sort()
    print('****************')
    print('input :',dir)
    print('start...')
    for file in files:
        fileType = os.path.splitext(file)
        if fileType[1] == '.png':
            new_png = Image.open(openUrl+str(int(num))+'/'+file) #打开图片
            new_png = new_png.resize((20, 20),Image.ANTIALIAS) #改变图片大小
            # matrix = 255-np.asarray(new_png) #图像转矩阵 并反色
            # new_png = Image.fromarray(matrix) #矩阵转图像
            new_png.save(savePath+'/'+str(int(num))+'/'+file) #保存图片
    print('down!')
    print('****************')

if __name__ == '__main__':
    # 待处理图片地址
    dataPath = 'D:\\BankCardOCR\\dataset\digit_dataSet\\training_images\\'
    #打开图片时使用的地址
    openUrl = 'D:/BankCardOCR/dataset/digit_dataSet/training_images/'
    #保存图片的地址
    savePath = 'D:/BankCardOCR/dataset/digit_dataSet/training_images'
    for num in range(10):
        print(str(int(num)))
        resize(dataPath+str(int(num)),savePath,num,openUrl)