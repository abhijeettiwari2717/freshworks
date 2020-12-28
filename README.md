# freshworks
A file-based key-value data store that supports basic CRD operations task using python. This data meant to be stored in a local storage for one single process on one laptop. The data  store must be exposed as a library to clients that can instantiate a class and work with data store
You can run the task_freshworks.py file in command prompt or terminal of your system by entering into python environment and after that you can use following procedure to perfrom the task:

import task_freshworks as task

task.create("key_name",value,time-to-live)

task.read("key_name")

task.update("key_name",new_value)

task.delete("key_name")

t=Thread(target=(create or read or delete),args=(key_name,value,timeout))

t.start()

t.sleep()

tnew=Thread(target=(create or read or delete),args=(key_name,value,timeout))

tnew.start()

tnew.sleep()
