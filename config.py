import os

def post_fork(server, worker):
    print "Worker spawned (pid: %s)" % worker.pid

def pre_fork(server, worker):
    memory = 1024 * 1024 * 1024 * 2 * 'a'
    print "spawning Worker (worker: %s)" % worker

def pre_exec(server):
    print "Forked child, re-executing."

def when_ready(server):
    print "Server is ready. Spwawning workers"

def worker_int(worker):
    print "Worker interrupted %s" % worker

def get_workers():
    procs = os.sysconf('SC_NPROCESSORS_ONLN')
    return procs * 2 + 1 if procs > 0 else 3

workers = 2
bind = '0.0.0.0:8008'
backlog = 2048
debug = True
worker_class = 'tornado'

