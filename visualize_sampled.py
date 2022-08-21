from PIL import Image
import numpy as np


data = np.load("/Users/matt/guided-diffusion/output/samples_16x64x64x3.npz")["arr_0"]
for image in data:
    img = Image.fromarray(image, 'RGB')
    img.show()
    input('')
    img.close()