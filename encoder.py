import cv2
from PIL import Image
import numpy as np

dict = {
    "a": [0, 0, 255],
    "b": [0, 255, 0],
    "c": [255, 0, 0],
}

text = open("algotest.txt", 'r')

def encoder(dt, tt):
    length = 3
    height = 3
    doclen = len(tt.read())
    frameSize = (length, height)
    out = cv2.VideoWriter('test.avi',cv2.VideoWriter_fourcc(*'RGBA'), float(2), frameSize)

    i = 0
    while i < doclen:
        encodedArray = []
        for j in range(0, height):
            row = []
            for k in range(0, length):
                if i < doclen:
                    text.seek(i)
                    char = text.read(1)
                    row.append(dt[char])
                    i = i + 1
                else:
                    row.append([0, 0, 0])
            encodedArray.append(row)
        img = np.asarray(encodedArray, dtype = np.uint8)
        print(img)
        print("----")
        out.write(img)

    out.release()
    text.close()

encoder(dict, text)
        