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


	return result_formated[0]{0}{1}
'''
	f = open(faces, 'r')
	json_data = json.load(f)

	name_list = ["anger","contempt","disgust","fear","happiness","neutral","sadness","surprise"]


	for name in name_list:
		print("{0:6s} ：{1}".format(name,json_data["faceAttributes"]["emotion"][name]),end="\t")
	#spotify_api.pyに画像感情データを渡す
	#spotify_api.SpotifyApi(result_formated["faceAttributes"])






# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

headers = {'Ocp-Apim-Subscription-Key': KEY}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

#JSON出力
try:
	response = requests.post(ENDPOINT, params=params,
                         headers=headers, json={"url": image_url}, timeout=0.1)
	print(json.dumps(response.json()))

except requests.exceptions.ConnectTimeout:
	print('エラー！')




single_image_name = os.path.basename(single_face_image_url)
detected_faces = face_client.face.detect_with_url(url=single_face_image_url)
if not detected_faces:
    raise Exception('No face detected from image {}'.format(single_image_name))

# Display the detected face ID in the first single-face image.
# Face IDs are used for comparison to faces (their IDs) detected in other images.
print('Detected face ID from', single_image_name, ':')
for face in detected_faces: print (face.face_id)
print()

# Save this ID for use in Find Similar
first_image_face_ID = detected_faces[0].face_id

'''