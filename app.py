import os
from tornado import websocket, web, ioloop
import json
buttons = '0000'
cl = []
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),

}

print settings['static_path']
class IndexHandler(web.RequestHandler):
    def get(self):

        self.render("index.html", buttons = buttons)

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)

class ApiHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, *args):
        self.finish()


        value = self.get_argument("value")
        global buttons
        buttons= value
        print buttons
        data = {"value" : buttons }

        data = json.dumps(data)
        for c in cl:
            c.write_message(data)



    @web.asynchronous
    def post(self):
        pass



app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/api', ApiHandler),
    (r'/static/(.*)', web.StaticFileHandler, {"path" : settings['static_path']})

])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
