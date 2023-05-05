from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
import keras
from keras.models import load_model
import keras.utils as image
import numpy as np
import tensorflow as tf
import json
from tensorflow import Graph


# Create your views here.




#ken tla3lek erreur 3al image dimensions baddelhom hne
img_height, img_width=180,180

#
model = keras.models.load_model('./models/model.h5')

# Create your views here.
def patientHomeView(request):
    return render (request,'patient/home.html')
def index(request):
    context={'a':1}
    return render(request,'index.html',context)


def predictImage(request):
      if request.method == 'GET':
           return render(request,'patient/index.html')
      elif request.method == 'POST':
        # get the uploaded file from the POST request
        fileObj = request.FILES.get('file')
        if fileObj is not None:
            # save the file to the media directory
            fs = FileSystemStorage()
            filePathName = fs.save(fileObj.name, fileObj)
            filePathName = fs.url(filePathName)
            testimage = '.' + filePathName
            # load and preprocess the image using tensorflow
            img = tf.keras.utils.load_img(testimage, target_size=(img_height, img_width))
            x = tf.keras.utils.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            # perform model inference
            predictions = model.predict(x)
            score = tf.nn.softmax(predictions[0])
            predictedLabel = ["NORMAL", "PNEUMONIA"]
            # prepare the context for rendering the response template
            context = {'filePathName': filePathName, 'predictedLabel': predictedLabel[np.argmax(score)], 'percentage': 100 * np.max(score)}
            # render the response template with the context
            return render(request, 'patient/index.html', context)
  
  
def viewDataBase(request):
    import os
    listOfImages=os.listdir('./media/')
    listOfImagesPath=['./media/'+i for i in listOfImages]
    context={'listOfImagesPath':listOfImagesPath}
    return render(request,'viewDB.html',context) 