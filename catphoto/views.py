from django.shortcuts import render, redirect
from .models import *
from .forms import ImageForm
import numpy as np
from PIL import Image
import tensorflow as tf
import os
# Create your views here.
def show_catphoto(request):
    # 코딩합시다.
    if request.method == 'POST': #이미지 Post
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            img = form.save()
            image = form.cleaned_data['image']
            CL_v3 = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), 'CL_3.h5'))
            image = Image.open(image).resize((300,300))
            target = np.asarray(image) / 255.0
            target = np.expand_dims(target, axis=0)
            tf.keras.backend.clear_session()
            predict = CL_v3(target)

            return render(request, 'catphoto/result.html', context={'predict':predict, 'image':image})


    elif request.method == 'GET': #단순한 Get
        form = ImageForm()

        return render(request, 'catphoto/photo.html', context={'form':form})