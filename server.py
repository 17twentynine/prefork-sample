import time
import datetime
import tornado.web
from tornado.ioloop import IOLoop
from tornado import gen
import tornado.wsgi

count = 0

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        global count
        self.write("Going to sleep...")
        yield gen.Task(IOLoop.instance().add_timeout, time.time() + 5)
        count += 1

        #time.sleep(5)
        self.write("Counter: %d, Time: %s" % (count, datetime.datetime.now()))
        self.write("I'm awake!")
        self.finish()

app = tornado.web.Application([
    (r"/", MainHandler),
    ])


#if __name__ == "__main__":
    #application.listen(8888)
    #IOLoop.instance().start()
