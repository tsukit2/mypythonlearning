import _thread as thread, time

def counter(myId, count):
   for i in range(count):
      time.sleep(1)
      mutex.acquire()
      print('[%s] => %s' % (myId, i))
      mutex.release()

mutex = thread.allocate_lock()
for i in range(5):
   thread.start_new_thread(counter, (i, 5))


print("I'm here already")
time.sleep(6)
print('Main process exiting.')

