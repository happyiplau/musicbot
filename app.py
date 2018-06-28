# encoding: utf-8
from linebot.models import *
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('g231E5+HPF2mBRfcXSGrAnV6BnWNOQWiaArtXg14JfOYN9jtYjW+ss1kHDNQGoazkGu57yFqU+sS5ai5dKg16HaDvmCNbh9yYjlb0H6F78RuXPeTP30EBiv3I26pRwucDB3PEaviOum8mRNLQ+BdhgdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('8cb7c221e6b68163823d99a73efa914f') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #message from user

    buttons_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ButtonsTemplate(
            title='請選擇以下服務',
            text='點選後顯示操作方式',
            thumbnail_image_url='https://storage.googleapis.com/biggg/f48c6734853348ff9f9f473f6d640ef1.gif',
            actions=[
                MessageTemplateAction(
                    label='搜歌模式',
                    
                   # text='搜歌模式'
                ),
                MessageTemplateAction(
                    label='心情模式',
                    #text='心情模式'
                ),
                MessageTemplateAction(
                    label='關於我們',
                    #text='關於我們'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, buttons_template)


import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])