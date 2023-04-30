from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai

CHANNEL_ACCESS_TOKEN = ''
CHANNEL_SECRET = ''

messages = [{"role": "system", "content": "You are a helpful assistant"}]
app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(body)                         # json 格式化訊息內容
        line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)              # 確認 token 是否正確
        handler = WebhookHandler(CHANNEL_SECRET)                     # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            print(msg)                                       # 印出內容
            reply = msg
        else:
            reply = '你傳的不是文字呦～'
        print(reply)
        line_bot_api.reply_message(tk,TextSendMessage(reply))# 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'       

def send_remind_msg(text):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Bearer ' + CHANNEL_ACCESS_TOKEN,
    }
    payload = {
        'to': group_id,
        'messages': format_text_message(text),
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

def sendLineFlexMessage(text):
    message = {
        "type": "flex",
        "altText": (current_date.month + 1) + "/" + current_date.day + "請假名單",
        "contents": {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": (current_date.month + 1) + "/" + current_date.day + "請假名單",
                        "weight": "bold",
                        "size": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "size": "sm",
                                        "flex": 1,
                                        "text": text,
                                        "wrap": True
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    }
    payload = {
        "to": group_id, # 请填写你要发送的用户 ID
        "messages": [message]
    }
    headers = {
        "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN
    }
    response = requests.post("https://api.line.me/v2/bot/message/push", headers=headers, data=json.dumps(payload))                                       # 驗證 Webhook 使用，不能省略


if __name__ == "__main__":
    app.run()
