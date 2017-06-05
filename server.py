import time
import datetime
import tornado.web
from tornado.ioloop import IOLoop
from tornado import gen
import tornado.wsgi
from tornado.httpclient import AsyncHTTPClient

count = 0


class SleepHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        global count
        self.write("Going to sleep... %s\n" % (datetime.datetime.now()))
        yield gen.Task(IOLoop.instance().add_timeout, time.time() + 5)
        count += 1

        http_client = AsyncHTTPClient()
        response = yield http_client.fetch("http://google.com")
        self.write(response.body[:10] + "\n")

        #time.sleep(5)
        self.write("Counter: %d, Time: %s \n" % (count, datetime.datetime.now()))
        self.finish()

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        http_client = AsyncHTTPClient()
        self.write("Time: %s \n" % (datetime.datetime.now()))
        response = yield http_client.fetch("http://localhost:8008/sleep")
        self.write(response.body + "\n")

        #time.sleep(5)
        self.write("Time: %s \n" % (datetime.datetime.now()))
        self.write("I'm awake! \n")
        self.finish()

app = tornado.web.Application([
    (r"/", MainHandler),
    (r"/sleep", SleepHandler),
    ])


#if __name__ == "__main__":
    #application.listen(8888)
    #IOLoop.instance().start()
