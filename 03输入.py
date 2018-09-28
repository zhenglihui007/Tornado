import tornado.web
import tornado.ioloop
import tornado.httpserver
# import tornado.options
from tornado.options import define,options
from tornado.web import RequestHandler,url


tornado.options.define("port", type=int, default=8000, help="服务器端口")


class IndexHandler(RequestHandler):
    """主路由处理类"""
    def post(self):
        # 从请求的查询字符串中返回指定参数name的值，如果出现多个同名参数，则返回最后一个的值。
        # query = self.get_query_argument('q', default='haha')
        # 从请求的查询字符串中返回指定参数name的值，注意返回的是list列表
        # query = self.get_query_arguments('q')
        # 从请求体中返回指定参数name的值，如果出现多个同名参数，则返回最后一个的值。
        # body = self.get_body_argument('q', default='haha')
        # 从请求体中返回指定参数name的值，注意返回的是list列表
        # body = self.get_body_arguments('q')
        # 从请求体和查询字符串中返回指定参数name的值，如果出现多个同名参数，则返回最后一个的值。
        # arg = self.get_argument('q', default='haha')
        # 从请求体和查询字符串中返回指定参数name的值，注意返回的是list列表
        arg = self.get_arguments('q')
        # 其他请求信息的获取方式
        # self.request.method     HTTP的请求方式，如GET或POST
        # self.request.host       被请求的主机名
        # self.request.uri        请求的完整资源标示，包括路径和查询字符串
        # self.request.path       请求的路径部分
        # self.request.query      请求的查询字符串部分
        # self.request.version    使用的HTTP版本
        # self.request.headers    请求的协议头，是类字典型的对象，支持关键字索引的方式获取特定协议头信息，例如：request.headers["Content-Type"]
        # self.request.body       请求体数据
        # self.request.remote_ip  客户端的IP地址
        # self.request.files      用户上传的文件，为字典类型

        self.write(str(arg))


class UploadHandler(RequestHandler):
    def post(self):
        # 获取用户上传文件，字典:{'img': [{'filename': 'goods_detail.jpg', 'body': b'\xff\xd8\文件内容},],}
        files = self.request.files
        # 提取对应关键字的值：列表
        img_files = files.get('img')
        if img_files:
            # 提取文件内容：列表里面的字典
            img_file = img_files[0]['body']
            with open('./img', 'w+') as file:
                file.write(img_file)
            self.write('ok')


if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r"/", IndexHandler),
            (r'/upload', UploadHandler)
        ], debug=True
    )
    # 创建了一个HTTP服务器实例http_server
    http_server = tornado.httpserver.HTTPServer(app)
    # 绑定服务器端口，默认开启一个进程
    http_server.listen(options.port)
    # 将服务器绑定到指定端口
    # http_server.bind(8000)
    # http_server.start(num_processes=1)方法指定开启几个进程，参数num_processes默认值为1，即默认仅开启一个进程；如果num_processes为None或者<=0，则自动根据机器硬件的cpu核芯数创建同等数目的子进程
    # http_server.start(1)
    # 启动监听
    tornado.ioloop.IOLoop.current().start()
