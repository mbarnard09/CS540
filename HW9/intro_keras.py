import tensorflow as tf
from tensorflow import keras
import numpy
from tensorflow.keras import layers
from tensorflow.keras import activations

def get_dataset(training=True):
    mnist = keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
    if training == True:
        return (train_images, train_labels)    
    else:
        return (test_images, test_labels)


def print_stats(train_images, train_labels):
    labels_dict = {}
    class_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    #making dict
    for x in class_names:
        labels_dict[x] = 0
    for x in range(0,len(labels_dict)):
        for y in train_labels:
            if x == y:
                labels_dict[class_names[x]] += 1
                        

    print(train_images.shape[0])
    print('{}x{}'.format(train_images.shape[1],train_images.shape[2]))
    for x in range(0,len(labels_dict)):
        print('{}. {} - {}'.format(x, class_names[x], labels_dict[class_names[x]]))


def build_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(10))
    opt = keras.optimizers.SGD(learning_rate=0.001)
    accuracy = tf.keras.metrics.Accuracy()
    model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), optimizer = opt, metrics = ['accuracy'])
    return model

def train_model(model, train_images, train_labels, T):
    model.fit(epochs= T, x = train_images, y = train_labels)

def evaluate_model(model,test_images,test_labels,show_loss=True):
    test_loss, test_accuracy = model.evaluate(x = test_images, y = test_labels, verbose=0)
    
    if show_loss == True:
        print('Loss: {}'.format(round(test_loss,4)))
        print('Accuracy: {}%'.format(round((test_accuracy*100),2)))
    else:
        print('Accuracy: {}%'.format(round((test_accuracy* 100),2)))
def predict_label(model,test_images,index):
    class_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    predict = model.predict(x= test_images)
    originalList = predict[index]
    tempList = numpy.sort(originalList)
    tempList = numpy.flip(tempList)
    firstP = tempList[0]
    secondP = tempList[1]
    thirdP = tempList[2]
    firstPIndex = numpy.where(originalList == firstP)
    secondPIndex = numpy.where(originalList == secondP)
    thirdPIndex = numpy.where(originalList == thirdP)
    print('{}: {}%'.format(class_names[firstPIndex[0][0]],round((firstP * 100), 2)))
    print('{}: {}%'.format(class_names[secondPIndex[0][0]],round((secondP * 100),2)))
    print('{}: {}%'.format(class_names[thirdPIndex[0][0]], round((thirdP * 100), 2)))

    
