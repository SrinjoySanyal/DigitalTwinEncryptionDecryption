import cv2
import numpy as np

dict = {
    "a": [0, 0, 255],
    "b": [0, 255, 0],
    "c": [255, 0, 0],
}

def decoder(dt, vid):
    video = cv2.VideoCapture(vid)

    dectext = ""

    decrypt = open("decrypted.txt", "w")

    while(video.isOpened()):
        ret, frame = video.read()
        if ret:
            #converts frame to numpy array
            print(frame)
            print("--------")
            #loop through the rows of the frame
            for row in frame:
                #loop through the pixels of the row
                for pixel in row:
                    #find letter corresponding to pixel in the lookup table
                    for elem in dt:
                        correct = True
                        for i in range(0, 3):
                            if dt[elem][i] != pixel[i]:
                                correct = False 
                                break
                        if correct == True:
                            dectext += elem
                            break
        else:
            break
    decrypt.write(dectext)
    decrypt.close()

    video.release()

decoder(dict, "test.avi")