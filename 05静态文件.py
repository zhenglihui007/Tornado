import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define,options
from tornado.web import RequestHandler, url, StaticFileHandler
import os

tornado.options.define('port', default=8000, type=int)


class IndexHandler(RequestHandler):
    def get(self):
        self.write('hello')


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application(
        [
            (r'/(.*)$', StaticFileHandler, {'path':os.path.join(current_path, 'statics/html'), 'default_filename':'index.html'}),
        ],
        static_path=os.path.join(current_path, 'statics'),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()