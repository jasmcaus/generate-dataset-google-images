import os
import cv2 as cv
import requests 

path_URLs = r''
output_DIR = r''

rows = open(path_URLs.read().strip().split('\n'))
total = 0

def loopURLs(rows):
    for url in rows:
        try:
            # Try to download the image from the URL
            request = requests.get(url, timeout=60)

            # save the image to disk
            downloaded = os.path.sep.join(output_DIR, f'{str(total).zfill(8)}.jpg')
            file = open(p, "wb")
            file.write(r.content)
            file.close()

            # update the counter
            print(f'Downloaded: {downloaded}')
            total += 1

        # handle if any exceptions are thrown during the download process
        except:
            print(f'Error downloading {downloaded}')

def doesExist(output_DIR):
    # loop over the image paths we just downloaded
    for imagePath in paths.list_images(output_DIR):
        delete = False

        # Attempting to load the image
        try:
            image = cv2.imread(imagePath)

            if image is None:
                delete = True

        # if OpenCV cannot load the image, then the image is likely corrupt so we delete it
        except:
            delete = True

        if delete:
            print(f'Deleting {imagePath}')
            os.remove(imagePath)

# Calling both functions
loopURLs(rows)
doesExist(output_DIR)