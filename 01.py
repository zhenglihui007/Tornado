import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """主页处理类"""
    def get(self, *args, **kwargs):
        """get请求方式"""
        self.write("hello")



if __name__ == '__main__':
    app = tornado.web.Application([(r"/", IndexHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()