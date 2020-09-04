from flask import Flask, request, abort
import pandas as pd
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent
    )
from PIL import Image
import os
import io
from io import BytesIO
import requests,json

import face_api
import spotify_api



app = Flask(__name__)

#herokuの環境変数に設定された、LINE DevelopersのアクセストークンとChannelSecretを
#取得するコード
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

header = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + LINE_CHANNEL_ACCESS_TOKEN
}

#herokuへのデプロイが成功したかどうかを確認するためのコード
@app.route("/")
def hello_world():
    return "hello world!"


#LINE DevelopersのWebhookにURLを指定してWebhookからURLにイベントが送られるようにする
@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得
    signature = request.headers['X-Line-Signature']

    # リクエストボディを取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 署名を検証し、問題なければhandleに定義されている関数を呼ぶ
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


#以下でWebhookから送られてきたイベントをどのように処理するかを記述する
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    print("文字だよ")
    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text="顔写真を送ってみてね！"))


#送られてきたメッセージが画像の場合の処理
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):

    message_id = event.message.id
    print(message_id)

    #face_api.pyで画像分析
    face1 = face_api.FaceApi1(getImageLine(message_id))
    face2 = face_api.FaceApi2(getImageLine(message_id))
    print(face1)
    print(face2)

    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='あなたの感情は、' + 
        str(face1[0][0])  + '：' + str(face1[0][1]) + '、' + 
        str(face2[0]) + '：' + str(face2[1]) + 
        str(face1[1][0] + str(face1[1][1]) + str(face1[1][2]))))
    #TextSendMessage(text=spotify_api.SpotifyApi())
    print("画像だよ")

def getImageLine(id):
    #送られてきた画像のurl
    line_url = 'https://api.line.me/v2/bot/message/' + id + '/content/'

    # 画像の取得
    result = requests.get(line_url, headers=header)
    print(result)

    # 画像の保存
    im = Image.open(BytesIO(result.content))
    filename = '/tmp/' + id + '.jpg'
    print(filename)
    im.save(filename)

    return filename







'''
    message_content = line_bot_api.get_message_content(message_id)
    print(message_content)

    image_bin = BytesIO(message_content.content)
    print(image_bin)

    #image = image_bin.getvalue()
    #print(image)
    #Face_api.pyに送られてきた画像を投げる
    print(event.contentProvider.originalContentUrl)
'''


# ポート番号の設定
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)