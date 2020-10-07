import numpy as np
import cv2

def invert(imgfile):
    filename=imgfile.split("/")[-1]
    img= cv2.imread(imgfile)
    inv_img=np.fliplr(img)
    cv2.imwrite("output/{}".format(filename),inv_img)
    return inv_img

def show(img):
    print("Press \"Esc\" to exit:  ")
    cv2.imshow("Mirror Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Exited")

if __name__ == '__main__':
    img_PATH = './input/bslashlogo.png'
    show(invert(img_PATH))