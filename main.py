from flask import Flask, request, abort
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

import os
from io import ByteIO

app = Flask(__name__)

#herokuの環境変数に設定された、LINE DevelopersのアクセストークンとChannelSecretを
#取得するコード
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

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
    TextSendMessage(text="文字ですね"))


#送られてきたメッセージが画像の場合の処理
@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):

    message_id = event.message.id
    print(message_id)

    message_content = line_bot_api.get_message_content(message_id)
    print(message_content)

    image_bin = BytesIO(message_content.content)
    print(image_bin)

    image = image_bin.getvalue()
    print(image)
    #Face_api.pyに送られてきた画像を投げる


    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text="画像だね"))
    print("画像だよ")





# ポート番号の設定
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)