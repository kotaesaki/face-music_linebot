import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
import json
import urllib3
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType
import cognitive_face as CF
import codecs
import spotify_api


#サブスクリプションキーの設定
KEY = 'a3f5affaebb549449f69ccd3106d3e75'

#エンドポイント設定
ENDPOINT = 'https://japaneast.api.cognitive.microsoft.com/face/v1.0'

CF.Key.set(KEY)
CF.BaseUrl.set(ENDPOINT)

#一番数値の高い感情を取得
def FaceApi1(file):

	#画像のurl
	image_url = file

	faces = CF.face.detect(image_url, face_id=True, landmarks=False, attributes='emotion')
	# 出力結果を見やすく整形
	print(type(faces))
	print (faces[0])

	total = faces[0]
	attr = total['faceAttributes']
	emotion = attr['emotion']
	anger = emotion['anger']
	contempt = emotion['contempt']
	disgust = emotion['disgust']
	fear = emotion['fear']
	happiness = emotion['happiness']
	neutral = emotion['neutral']
	sadness = emotion['sadness']
	surprise = emotion['surprise']

	attr_list = [happiness, neutral, sadness]
	print(type(attr_list))
	print(emotion)
	print(anger)
	print(contempt)
	print(disgust)
	print(fear)
	print(happiness)
	print(neutral)
	print(sadness)
	print(surprise)

	#数値が高いもので並べ替え
	emotion2 = max(emotion.items(), key=lambda x:x[1])
	print(emotion2)

	spotify_api.SpotifyApi(emotion2)

	return emotion2

#二番目に数値の高い感情を取得
def FaceApi2(file):

	#画像のurl
	image_url = file

	faces = CF.face.detect(image_url, face_id=True, landmarks=False, attributes='emotion')
	# 出力結果を見やすく整形
	print(type(faces))
	print (faces[0])

	total = faces[0]
	attr = total['faceAttributes']
	emotion = attr['emotion']
	anger = emotion['anger']
	contempt = emotion['contempt']
	disgust = emotion['disgust']
	fear = emotion['fear']
	happiness = emotion['happiness']
	neutral = emotion['neutral']
	sadness = emotion['sadness']
	surprise = emotion['surprise']

	count = 0 
	for emotion3 in sorted(emotion.items(), key=lambda x:x[1], reverse=True):
		if 1 == count:
			return emotion3 
		else: 
			count+=1
	print(emotion3)

	return emotion3
