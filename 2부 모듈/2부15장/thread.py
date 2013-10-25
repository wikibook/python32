from threading import Thread, Lock
import time

count = 10
lock = Lock()

class developer( Thread ):
  def __init__(self, name):
    Thread.__init__(self)
    self.name = name
    self.fixed = 0
  def run(self):
    global count
    while 1:
      lock.acquire()
      if count>0:
        count -= 1
        lock.release()
        self.fixed +=1
        time.sleep(0.1)
      else:
        lock.release()
        break
    
dev_list = []
for name in ['Shin', 'Woo','Choi']:
  dev = developer(name)
  dev_list.append( dev )
  dev.start()

for dev in dev_list:
  dev.join()
  print(dev.name, 'fixed', dev.fixed)

