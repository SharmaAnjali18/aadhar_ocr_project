import json
import pytesseract
import cv2
import numpy as np
import sys
import re
import os
from PIL import Image
import ftfy
import aadhaar_read_data
# import aadhar_face_match
import io

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

# Image Extraction
# path_f = input('Enter the path of front image->', )
# path_b = input('Enter the path of back image->', )

# path_f = 'Images/front.jpg'
# path_b = 'Images/back.jpg'
#
# img_f = cv2.imread(path_f)
# img_b = cv2.imread(path_b)
#
# # process front image
# img_f = cv2.resize(img_f, (600, 400), interpolation=cv2.INTER_CUBIC)
# img_f = cv2.cvtColor(img_f, cv2.COLOR_BGR2GRAY)
# var_f = cv2.Laplacian(img_f, cv2.CV_64F).var()
#
# if var_f < 50:
#     print(var_f)
#     print("Front Image is Too Blurry....")
#     k= input('Press Enter to Exit.')
#     exit(1)
#
# # process back image
#
# img_b = cv2.resize(img_b, (600, 400), interpolation=cv2.INTER_CUBIC)
# img_b = cv2.cvtColor(img_b, cv2.COLOR_BGR2GRAY)
# var_b = cv2.Laplacian(img_b, cv2.CV_64F).var()
#
# if var_b < 50:
#     print(var_b)
#     print("Back Image is Too Blurry....")
#     k= input('Press Enter to Exit.')
#     exit(1)


def extract(img_f, img_b):
    # Text Extraction using Tesseract and fixing the text

    # text_f = pytesseract.image_to_string(Image.open(path_f), lang='eng')
    # text_b = pytesseract.image_to_string(Image.open(path_b), lang='eng')

    text_f = pytesseract.image_to_string(img_f, lang='eng')
    text_b = pytesseract.image_to_string(img_b, lang='eng')

    # writing the text of both images
    text_output = open('output.txt', 'w', encoding='utf-8')
    # text_output.write("Data Of Front Image")
    text_output.write(text_f)

    # text_output.write("Data Of Back Image")
    text_output.write(text_b)

    text_output.close()

    file = open('output.txt', 'r', encoding='utf-8')
    text = file.read()

    text = ftfy.fix_text(text)
    text = ftfy.fix_encoding(text)

    if "income" in text.lower() or "tax" in text.lower() or "department" in text.lower():
        pass

    elif "male" in text.lower():
        data = aadhaar_read_data.adhaar_read(text)

    return data

    # Writing for JSON

    # to_unicode = str
    #
    # with io.open('info.json', 'w', encoding='utf-8') as outfile:
    #     data = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
    #     outfile.write(to_unicode(data))
    #
    # # Reading JSON data
    #
    # with open('info.json', encoding='utf-8') as data:
    #     data_loaded = json.load(data)
    #
    # # Printing The Data
    #
    # if data_loaded['ID Type'] == 'ADHAAR':
    #     print("\n---------- ADHAAR Details ----------")
    #     print("\nADHAAR Number: ", data_loaded['Adhaar Number'])
    #     print("\nName: ", data_loaded['Name'])
    #     print("\nDate Of Birth: ", data_loaded['Date of Birth'])
    #     print("\nSex: ", data_loaded['Sex'])
    #     print("\n------------------------------------")
    #     k = input("\n\nPress Enter To EXIT")
    # exit(0)


# def face_match(img_f, img_b):
#     import cv2
#     import numpy as np
#     from PIL import Image
#     from numpy import asarray
#     import face_recognition
#     from datetime import datetime
#
#     ti = datetime.now()
#
#     # import pytesseract
#     p = 0
#     match = None
#     # read image using pillow
#     # image = Image.open(img_f)
#
#     # converting image to numpy array
#     # numpydata = asarray(image)
#     img_f = cv2.cvtColor(img_f, cv2.COLOR_BGR2RGB)
#     # encode the image
#     encode = face_recognition.face_encodings(img_f)[0]
#     encodeListKnown = [encode]
#     # reading the face
#     cap = cv2.VideoCapture(0)
#     while True:
#         success, img = cap.read()
#         # img = captureScreen()
#         imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
#         facesCurFrame = face_recognition.face_locations(imgS)
#         encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
#         for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
#             matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#             faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#             matchIndex = np.argmin(faceDis)
#
#             if matches[matchIndex]:
#                 extract(img_f, img_b)

#
# face_match(img_f, img_b)

# print(extract(img_f, img_b))