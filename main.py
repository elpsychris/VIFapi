# import the necessary packages

from PIL import Image
import pytesseract
import argparse
import cv2
import os


# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image to be OCR'd")
# ap.add_argument("-p", "--preprocess", type=str, default="thresh",
# 	help="type of preprocessing to be done")
# args = vars(ap.parse_args())
def main():
    # doOCR("7948.png")
    loadImage("thresh", "sample.png")


def loadImage(preprocess_mth, img_url):
    # load the example image and convert it to grayscale
    image = cv2.imread(img_url)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we should apply thresholding to preprocess the
    # image
    if preprocess_mth == "thresh":
        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove
    # noise
    elif preprocess_mth == "blur":
        gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}new.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    doOCR(image, gray, filename)


def doOCR(image, gray, filename):
    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    # show the output images
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)


if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
