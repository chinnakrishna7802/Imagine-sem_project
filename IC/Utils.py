import numpy as np
from PIL import Image
from skimage import color
import torch
import torch.nn.functional as F


#----------------------------
# UTILS
#----------------------------

def load_img(img_path):
	out_np = np.asarray(Image.open(img_path))
	if(out_np.ndim==2):
		out_np = np.tile(out_np[:,:,None],3)
	return out_np

def resize_img(img, HW=(256,256), resample=3):
	return np.asarray(Image.fromarray(img).resize((HW[1],HW[0]), resample=resample))

def preprocess_img(img_rgb_orig, HW=(256,256), resample=3):
	# return original size L and resized L as torch Tensors
	img_rgb_rs = resize_img(img_rgb_orig, HW=HW, resample=resample)
	
	img_lab_orig = color.rgb2lab(img_rgb_orig)
	img_lab_rs = color.rgb2lab(img_rgb_rs)

	img_l_orig = img_lab_orig[:,:,0]
	img_l_rs = img_lab_rs[:,:,0]

	tens_orig_l = torch.Tensor(img_l_orig)[None,None,:,:]
	tens_rs_l = torch.Tensor(img_l_rs)[None,None,:,:]

	return (tens_orig_l, tens_rs_l)

def postprocess_tens_new(tens_orig_l, out_ab, mode='bilinear'):
	# tens_orig_l 	Batchsize x 1 x H_orig x W_orig
	# out_ab 		Batchsize x 2 x H x W
    Batchsize = tens_orig_l.shape[0]

    output_ = []
    for i in range(Batchsize):
        tens_orig_l_i = tens_orig_l[i][np.newaxis, :, :, :]
        out_ab_i  = out_ab[i][np.newaxis, :, :, :]
        HW_orig_i = tens_orig_l_i.shape[2:]
        HW_i = out_ab_i.shape[2:]

        # call resize function if needed
        if(HW_orig_i[0]!=HW_i[0] or HW_orig_i[1]!=HW_i[1]):
            out_ab_orig_i = F.interpolate(out_ab_i, size=HW_orig_i, mode='bilinear')
        else:
            out_ab_orig_i = out_ab_i

        out_lab_orig_i = torch.cat((tens_orig_l_i, out_ab_orig_i), dim=1)
        output_.append(color.lab2rgb(out_lab_orig_i.data.cpu().numpy()[0,...].transpose((1,2,0))))
        # output_.append(color.lab2rgb(out_lab_orig_i.data.cpu().numpy()[0,...].transpose((1,2,0))).transpose((2,0,1)))
    return np.array(output_)