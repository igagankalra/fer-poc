#!usr/bin/env python

import os
import sys
from io import BytesIO
import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import patches
from matplotlib import style

import cognitive_face as CF
import urllib
import random
from PIL import Image
from operator import itemgetter
from db_operations import data_entry
from creds import KEY, BASE_URL
from save_to_flat_file import save_output_into_flat_file


style.use('fivethirtyeight')

# Replace with a valid Subscription Key in creds.py
CF.Key.set(KEY)

# Replace with your regional Base URL in creds.py
CF.BaseUrl.set(BASE_URL)

#using default group id for time being, this has to be dynamic i.e. Client name
personGroupId = 'LogRhythm'

#using static image for time being, has to be dynamic one, which will be generted every 30 seconds
absolute_path_string = 'IMG_20190915_123246.jpg'
img_url = absolute_path_string
img_data = absolute_path_string
print(img_url)

# Driver Code

#to get the no. of faces in the image with the emotion of those images.
face_ids = CF.face.detect(img_url, attributes='emotion')

# res = CF.person.create(personGroupId, 'user_abhi')
# print(face_ids, "\n")
# extractId = str(sys.argv[0])[-1:]
# print(extractId)

# result = CF.face.identify(img_url)

# print(res)
#printing the number of faces found.
print(len(face_ids))


# To get the emotion from the json result from the API for a given PIC
for face in face_ids:
    face_attribute = face['faceAttributes']['emotion']
    print(max(face_attribute, key=face_attribute.get))
    #This saves the data to a Flat File
    save_output_into_flat_file(personGroupId, img_url, face['faceId'], datetime.datetime.now())
    #This makes entry to the Database.
    data_entry(personGroupId, img_url, face['faceId'], datetime.datetime.now())
    print(face["faceId"], face_attribute)


# for index, value in enumerate(face_ids):
#     print(index, value)


# To Display the image with stats
def plot_image(img_url):
    """Method to plot the image with returned json result and save it to the disk

    Arguments:
        img_url {String} -- Image name or the path.
    """
    image_orig = open(img_url, "rb").read()
    image = Image.open(BytesIO(image_orig))

    plt.figure(figsize=(12, 12))
    ax = plt.imshow(image, alpha=1)
    for face in face_ids:
        fr = face["faceRectangle"]
        fa = face["faceAttributes"]
        origin = (fr["left"], fr["top"])
        p = patches.Rectangle(
            origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
        plt.text(origin[0], origin[1], "%s" % (fa["emotion"]),
                fontsize=8, color='w', weight="bold", va="bottom")
        ax.axes.add_patch(p)

    _ = plt.axis("off")
    plt.savefig('plots\\{}.jpg'.format(face['faceId']))
    plt.show()

#Uncomment this when you want to save output into staic image as well.
# plot_image(img_url)
