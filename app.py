"""
This is responsible for handle incoming messages
"""
import os
import json
from tornado import websocket, web, ioloop

buttons = '0000'
cl = []
from Switching import Switching

switching = Switching()
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),

}

class IndexHandler(web.RequestHandler):
    """
    This is responsible for render view
    """
    def get(self):

        self.render("index.html", buttons=buttons)


class SocketHandler(websocket.WebSocketHandler):
    """
    This is responsible for register/unregistered client
    """
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)

    def on_close(self):
        if self in cl:
            cl.remove(self)

class ApiHandler(web.RequestHandler):
    """
    Accept the json data and pass to all clients
    """
    @web.asynchronous
    def get(self, *args):
        self.finish()
        value = self.get_argument("value")
        global buttons
        buttons = value
        print buttons
        data = {"value" : buttons}
        if buttons[0] =='1':

            switching.turnOn(3)

        elif buttons[0] =='0':
            switching.turnOff(3)

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
