import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
import uuid
from pydub import AudioSegment
from src.feature_extraction import extract_features
# Create your views here.

@api_view(['GET', 'POST'])
def feature_extraction(request):
    filename = str(uuid.uuid1())
    original_location = "Audio_Files/Uploaded_MP3/"+filename
    with open(original_location, 'wb') as f:
        f.write(request.body)
    sound = AudioSegment.from_file(original_location)
    location = "Audio_Files/WAV/"+filename+".wav"
    sound.export(location, format="wav") 
    if os.path.exists(original_location):
        os.remove(original_location)
    features = extract_features(location)
    print(features)
    data = {'a':1, 'b':2}
    return JsonResponse(data)
