import os

images = os.listdir("../images")

for img_name in images:
    print("![{}](../images/{})".format(img_name, img_name))