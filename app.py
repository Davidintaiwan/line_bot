# SDK

# software development kit

# web app 


from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage, 
    StickerSendMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

app = Flask(__name__)

# 權杖 token & 秘密 access

configuration = Configuration(access_token='mFZmSsLchzBYh0pw4sjh0FmgyUK09JKe/tH/xd12L/YQAzmmgKNjYFq+U1bOR+xJ9m8LmORK87GcEqG/rjrH3xp2NaYhvTRdT1HwigimGnQu+VpjkkY9qqInfYITkLLM4tbu05p39ry/kahN+HDc5AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4802ac6a2c82f8c86c1209f85eb9c468')


@app.route("/callback", methods=['POST'])  # route 路徑 "/callback" 來敲門
def callback():  # 返回觸發條件
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)   # handle 會觸發下面@ handle的程式碼
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        msg = event.message.text
        r = '我看不懂你說甚麼'
        
        if '給我貼圖'in msg:
            sticker_message = StickerSendMessage(
                package_id='1', 
                sticker_id='3'
            )
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[sticker_message]
                ))

        return

        if msg in ['hi', 'Hi']:
            r = 'hi'
        elif msg == '你吃飯了嗎':
            r = '還沒'
        elif msg == '你是誰':
            r = '我是機器人'
        elif '訂位' in msg:
            r = '您想訂位是嗎'

        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=r)]
        
            )
        )

if __name__ == "__main__":  # 確保
    app.run()



