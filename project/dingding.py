from dingtalkchatbot.chatbot import DingtalkChatbot

class SendMsg:
    def __init__(self):
        self.webtoken = 'you stoken'

    def send_msg(self, msg):
        webtoken = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(webtoken)

        res = DingtalkChatbot(webtoken)
        print(msg)
        res.send_text(msg+' ',is_at_all=False)
        if res['error']:
            print('发送失败')
            return
        else:
            print('send ok')
            return True