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


def FaceApi(file):

	#サブスクリプションキーの設定
	KEY = 'a3f5affaebb549449f69ccd3106d3e75'

	#エンドポイント設定
	ENDPOINT = 'https://japaneast.api.cognitive.microsoft.com/face/v1.0'

	#画像のurl
	image_url = file

	CF.Key.set(KEY)
	CF.BaseUrl.set(ENDPOINT)

	faces = CF.face.detect(image_url, attributes='emotion')
	# 出力結果を見やすく整形
	result_formated = json.dumps(faces, indent=4, separators=(',', ': '))
	print (codecs.decode(result_formated, 'unicode-escape'))

	f = open(faces, 'r')
	json_data = json.load(f)

	name_list = ["anger","contempt","disgust","fear","happiness","neutral","sadness","surprise"]


	for name in name_list:
		print('{0:6s} :{1} '.format(name,json_data["faceAttributes"]["emotion"][name],end='\t')
	#spotify_api.pyに画像感情データを渡す
	#spotify_api.SpotifyApi(result_formated["faceAttributes"])
	