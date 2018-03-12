import os
 
def parent_child():
    
 
  
    for x in range(1,100):
    	n = os.fork()
        print("Parent process and id is : ", os.getpid())
 
    
    else:
        print("Child process and id is : ", os.getpid())
         

parent_child()