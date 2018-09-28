import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self, *args, **kwargs):
        self.write("hello")


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler)
    ], debug=True)
    # 创建了一个HTTP服务器实例http_server
    http_server = tornado.httpserver.HTTPServer(app)
    # 绑定服务器端口，默认开启一个进程
    # http_server.listen(8000)
    # 将服务器绑定到指定端口
    http_server.bind(8000)
    # http_server.start(num_processes=1)方法指定开启几个进程，参数num_processes默认值为1，即默认仅开启一个进程；如果num_processes为None或者<=0，则自动根据机器硬件的cpu核芯数创建同等数目的子进程
    http_server.start(1)
    # 启动监听
    tornado.ioloop.IOLoop.current().start()
