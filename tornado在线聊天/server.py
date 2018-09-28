import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import datetime
from tornado.web import RequestHandler
from tornado.options import define,options
from tornado.websocket import WebSocketHandler


define('port', default=8000, type=int)


class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class ChatHandler(WebSocketHandler):
    # 用来存放在线用户的容器
    users = []

    # 当一个WebSocket连接建立后被调用
    def open(self):
        # 建立链接后添加用户到容器
        self.users.append(self)
        # 向以在线用户发送消息
        for user in self.users:
            user.write_message(u"[%s]-[%s]-进入聊天室"%(
                    self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def on_message(self, message):
        # 向在线用户广播消息
        for user in self.users:
            user.write_message(u"[%s]-[%s]-说：%s" % (
                self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    def on_close(self):
        # 用户关闭连接后从容器中移除用户
        self.users.remove(self)
        for u in self.users:
            u.write_message(u"[%s]-[%s]-离开聊天室" % (
                self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def check_origin(self, origin):
        # 允许WebSocket的跨域请求
        return True


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [
            (r'/', IndexHandler),
            (r'/chat', ChatHandler),
        ],static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "template"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()