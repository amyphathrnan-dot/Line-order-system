from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.webhooks import MessageEvent, TextMessageContent
import config
from line_handler import handle_text

print("CONFIG SECRET =", repr(config.LINE_CHANNEL_SECRET))

app = Flask(__name__)

handler = WebhookHandler(config.LINE_CHANNEL_SECRET)


@app.route("/")
def home():
    return "LINE Order System Running"


@handler.add(MessageEvent, message=TextMessageContent)
def message(event):
    handle_text(event)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature")

    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except Exception as e:
        print(e)
        abort(400)

    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)