import glob
import numpy as np
from PIL import Image
from torch.utils.data import Dataset
from IC.Utils import preprocess_img

#----------------------------
# Image Dataset
#----------------------------


# out_channels = 3

class ImageData(Dataset):
    def __init__(self, img, transform): 
        self.transform = transform
        self.img = img


    def __getitem__(self, index):
        
        img = self.img
        
        img_black = np.asarray(Image.open(img))
        if(img_black.ndim==2):
            img_black = np.tile(img_black[:,:,None],3)
        (tens_l_orig, tens_l_rs) = preprocess_img(img_black, HW=(400, 400))

        return {"black": tens_l_rs.squeeze(0), 'orig': tens_l_orig.squeeze(0)}#, "color": img_color}


    def __len__(self):
        return 1