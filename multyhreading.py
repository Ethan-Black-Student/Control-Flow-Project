import threading
import time


print("hi")
users = "hi"
def game():
    global users
    users = input("enter Win or no")

def timer():
    for i in range(120,-1,-10):
        print("\n"+str(i))
        
        if i == 0:
            print("you lost")
            exit(0)
        elif users == "Win":
            print("Win")
            exit(0)
        else:
            time.sleep(10)


thread1 = threading.Thread(target=game)
thread2 = threading.Thread(target=timer)

thread1.start()
thread2.start()


thread1.join()
thread2.join()