import cv2
import os
import glob

# make a mov video of all images from ./frames/Dream/*
def makeVideo():
    img_array = []
    filenames = glob.glob('./frames/Dream/*.png')
    filenames.sort(key=os.path.getctime)
    for filename in filenames:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter('dream.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

# make a mov video of all images from ./frames/Mem/*
def makeVideoMem():
    img_array = []
    filenames = glob.glob('./frames/Mem/*.png')
    filenames.sort(key=os.path.getctime)
    for filename in filenames:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter('mem.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

# make a mov video of all images from ./frames/R/*
def makeVideoR():
    img_array = []
    filenames = glob.glob('./frames/R/*.png')
    filenames.sort(key=os.path.getctime)
    for filename in filenames:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter('R.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

# make a mov video of all images from ./frames/G/*
def makeVideoG():
    img_array = []
    filenames = glob.glob('./frames/G/*.png')
    filenames.sort(key=os.path.getctime)
    for filename in filenames:
        print(filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    out = cv2.VideoWriter('G.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

makeVideo()
makeVideoMem()
makeVideoR()
makeVideoG()