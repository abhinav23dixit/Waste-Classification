# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 16:10:29 2018

@author: John
"""
from keras.models import Sequential
from keras.layers import Dense,Convolution2D,MaxPooling2D,Flatten,BatchNormalization
from keras.layers.noise import GaussianNoise

import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json  



json_file = open('C:\\Users\\John\\Desktop\\Project Final\\256x256_files\\model_94%(256x256).json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("C:\\Users\\John\\Desktop\\Project Final\\256x256_files\\model_94%(256x256).h5")
print("Loaded model from disk")
pred = []

from PIL import Image

img2 = Image.open('C:\\xampp\\htdocs\\uploads\\file.jpg')
img2 = img2.resize((256,256), Image.ANTIALIAS)
img2.save('C:\\xampp\\htdocs\\uploads\\file_resized.jpg') 



img = image.load_img("C:\\xampp\\htdocs\\uploads\\file_resized.jpg",target_size=(256,256))
#plt.imshow(img)
img = image.img_to_array(img)
img = img/255.
img = np.expand_dims(img,axis=0)
prediction = loaded_model.predict_proba(img)
pred.append(prediction)

a=pred[0][0][0]
b=pred[0][0][1]
c=pred[0][0][2]
d=pred[0][0][3]
e=pred[0][0][4]
s_a='{:.5f}'.format(a)
s_b='{:.5f}'.format(b)
s_c='{:.5f}'.format(c)
s_d='{:.5f}'.format(d)
s_e='{:.5f}'.format(e)

file = open("C:\\Users\\John\\Desktop\\new.txt",'w+') 
 
file.write(s_a + "\n" + s_b + "\n" + s_c + "\n" + s_d + "\n" + s_e) 
file.close() 
