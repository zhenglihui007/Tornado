import tornado.web
import tornado.ioloop
import tornado.httpserver
import json
from tornado.web import RequestHandler
from tornado.web import url
from tornado.options import define,options


tornado.options.define('port', default=8000, type=int, help('服务器端口'))


class InfoHandler(RequestHandler):
    # 此方法用来设置默认的响应头headers字段
    def set_default_headers(self):
        # 在HTTP处理方法中使用set_header()方法会覆盖掉在set_default_headers()方法中设置的同名header
        self.set_header("Content-Type", "application/json; charset=UTF-8")

    def get(self):
        stu = {"name":"zhangsan", "age":24, "gender":1,}
        # 手动做成json序列化
        # stu_json = json.dumps(stu)
        # write方法是写到缓冲区的，我们可以像写文件一样多次使用write方法不断追加响应内容，最终所有写到缓冲区的内容一起作为本次请求的响应输出
        # 可以不用自己手动去做json序列化，当write方法检测到我们传入的chunk参数是字典类型后，会自动帮我们转换为json字符串
        self.write(stu)
        # 手动设置一个名为name、值为value的响应头header字段
        self.set_header('name', 'value')


if __name__ == '__main__':
    app = tornado.web.Application(
        [
        (r'/', InfoHandler),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    tornado.ioloop.IOLoop.current().start()