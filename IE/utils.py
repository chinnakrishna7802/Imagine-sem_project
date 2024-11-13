import cv2
import numpy as np

def loadimg(img,shape):
    filestr = img.read()
    #convert string data to numpy array
    file_bytes = np.fromstring(filestr, np.uint8)
    # convert numpy array to image
    img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img= cv2.resize(img, shape)
    return img


def get_data(path):
    # X=[]
    Y=[]
    # for folder in glob.glob(path+ str('/*')):
    #     for img_path in glob.glob(folder+ str('/*')):      
    #         if folder == os.path.join(path, 'HR'):
    #             X.append(load(img_path, (384, 384)))
    #         elif folder == os.path.join(path, 'LR'):
    Y.append(loadimg(path, (96,96)))

    # X= np.array(X)
    Y= np.array(Y)
    # print(Y)
    return Y/255.0