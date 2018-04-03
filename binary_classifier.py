from keras.models import Sequential
from keras.layers import Dense,Convolution2D,MaxPooling2D,Flatten,BatchNormalization
from keras.layers.noise import GaussianNoise

classifier = Sequential()
classifier.add(GaussianNoise(0.1,input_shape=(128,128,3)))
classifier.add(Convolution2D(filters=64,kernel_size=(3,3),activation = 'relu'))
classifier.add(BatchNormalization())
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Convolution2D(filters=64,kernel_size=(3,3),activation = 'relu'))
classifier.add(BatchNormalization())
classifier.add(MaxPooling2D(pool_size=(2,2)))


classifier.add(Convolution2D(filters=64,kernel_size=(3,3),activation = 'relu'))
classifier.add(BatchNormalization())
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Flatten())

classifier.add(Dense(output_dim=256,activation='relu'))
classifier.add(Dense(output_dim=128,activation='relu'))
classifier.add(Dense(output_dim=1,activation='sigmoid'))

classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('C:\\Users\\Ishaan\\Desktop\\Project\\train_set',
                                                target_size=(128, 128),
                                                batch_size=32
                                                ,
                                                class_mode='binary')

test_set = test_datagen.flow_from_directory('C:\\Users\\Ishaan\\Desktop\\Project\\test_set',
                                            target_size=(128, 128),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit_generator(training_set,
                    steps_per_epoch=950,
                    epochs=15,
                    validation_data=test_set,
                    validation_steps=459)


from sklearn.externals import joblib


import numpy as np
from keras.preprocessing import image
pred = []
import matplotlib.pyplot as plt
for i in range(0,213):
    img = image.load_img('C:\\Users\\Ishaan\\Desktop\\Project\\test_set\\cardboard\\' + str(i) + '.jpg',target_size=(128,128))
    #plt.imshow(img)
    img = image.img_to_array(img)
    img = img/255.
    img = np.expand_dims(img,axis=0)
    prediction = classifier.predict_proba(img)
    training_set.class_indices
    pred.append(prediction)
    print(prediction)
pred2 = []
for i in range(0,57):
    img = image.load_img('C:\\Users\\Ishaan\\Desktop\\test_set\\metal\\' + str(i) + '.jpg',target_size=(128,128))
    #plt.imshow(img)
    img = image.img_to_array(img)
    img = img/255.
    img = np.expand_dims(img,axis=0)
    prediction = classifier.predict_proba(img)
    training_set.class_indices
    pred2.append(prediction)
    print(prediction)
    

    
    
from keras.models import model_from_json  

model_json = classifier.to_json()
with open("C:\\Users\\Ishaan\\Desktop\\Project\\model_80%_binary.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("C:\\Users\\Ishaan\\Desktop\\Project\\model_80%_binary.h5")
print("Saved model to disk")




