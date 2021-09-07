import qrcode
import cv2
import numpy as np
import pytesseract
from PIL import Image

# !!!!!! the image needs to contain text or numbers

def readTextOnAnIMage(input):
    img = cv2.imread(input)
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    binary_image = cv2.threshold(gray_image,130,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    inverted_bin = cv2.bitwise_not(binary_image)
    kernel = np.ones((2,2),np.uint8)
    proccessed_img = cv2.erode(inverted_bin,kernel,iterations = 1)
    proccessed_img = cv2.dilate(proccessed_img,kernel,iterations = 1)
    return proccessed_img

def generateQRCodefromText(input):
    text = pytesseract.image_to_string(input)
    print(text)
    QR = qrcode.make(text)
    return QR

def generateQRCodeFromImageWithText(input):
    text = readTextOnAnIMage(input)
    QR = generateQRCodefromText(text)
    QR.show()

input = 'img1.png'

if __name__ == "__main__":
    run = generateQRCodeFromImageWithText(input)
