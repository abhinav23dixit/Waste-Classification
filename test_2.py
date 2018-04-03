from keras.models import Sequential
from keras.layers import Dense,Convolution2D,MaxPooling2D,Flatten,BatchNormalization
from keras.layers.noise import GaussianNoise

classifier = Sequential()
classifier.add(GaussianNoise(0.1,input_shape=(128,128,3)))
classifier.add(Convolution2D(filters=64,kernel_size=(3,3),activation = 'relu'))
classifier.add(BatchNormalization())
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Flatten())

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

training_set = train_datagen.flow_from_directory('C:\\Users\\Abhishek\\Desktop\\dataset\\train_set',
                                                target_size=(128, 128),
                                                batch_size=16,
                                                class_mode='binary')

test_set = test_datagen.flow_from_directory('C:\\Users\\Abhishek\\Desktop\\dataset\\test_set',
                                            target_size=(128, 128),
                                            batch_size=16,
                                            class_mode='binary')


classifier.fit_generator(training_set,
                    steps_per_epoch=950,
                    epochs=15,
                    validation_data=test_set,
                    validation_steps = 459)
