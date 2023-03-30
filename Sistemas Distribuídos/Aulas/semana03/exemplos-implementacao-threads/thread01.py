import threading 
from time import sleep 
  
class MinhaThread(threading.Thread):  
    def __init__(self, thread_name, thread_ID):  
        threading.Thread.__init__(self)  
        self.thread_name = thread_name  
        self.thread_ID = thread_ID          
    def run(self):  
        for i in range(20):
            print("#"+str(i)+"    "+str(self.thread_name) +" "+ str(self.thread_ID));
            sleep(2)

if __name__ == '__main__':

    thread1 = MinhaThread("Thread 01", 1000)  
    thread2 = MinhaThread("Thread 02", 2000);  
  
    thread1.start()  
    thread2.start()  

    thread1.join()
    thread2.join()
  
    print("Exit")  