"""
This is responsible for handle incoming messages
"""
import os
import json
from tornado import websocket, web, ioloop
from SwitchingPWM import SwitchingPWM

pins = [13, 15, 16]
PORT1 = (3, 5, 7)
PORT2 = (33, 35, 37)
PORT3 = (26, 24, 22)

PORT = (PORT1, PORT2, PORT3)

BLUE, GREEN, RED = zip(PORT1, PORT2, PORT3)


color_pair = (BLUE, GREEN, RED )
# color_pair = dict(zip(('BLUE' , 'GREEN', 'RED'),(BLUE, GREEN, RED )))
buttons = '000'
cl = []
from Switching import Switching

switching = Switching(pins)
switchingPWM = SwitchingPWM()
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),

}
class IndexHandler(web.RequestHandler):
    """
    This is responsible for render view
    """
    def get(self):

        self.render("index.html", buttons=switching.get_state())


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

        for x in enumerate(pins,start=0):
            (index, pin) = x
            if buttons[index] == '1':

                #switching.turn_on(pin)
                switchingPWM(color_pair[index])

            elif buttons[index] == '0':
                pass
                #switching.turn_off(pin)


        data = {"value" : buttons}

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
