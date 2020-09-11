from socket import AF_INET, socket, SOCK_STREAM
from timeit import default_timer as timer
import sys, select, tkinter

def start_game():

    print("Enter name : ",end="")
    name=input()
    client_socket.send(bytes(name,"utf8"))
    client_socket.recv(1024).decode("utf8")
    client_socket.recv(1024).decode("utf8")

    while(1):
        question=client_socket.recv(1024).decode("utf8")
        print(question)
        if question=="END_OF_QUIZ" :
            return
        # print the question in proper format
        print("You have 60 seconds to answer!")
        start_time=timer()
        i, o, e = select.select( [sys.stdin], [], [], 60 )
        if (i):
            ans=sys.stdin.readline().strip()
            end_time=timer()
            time=end_time-start_time
            print("You said", ans)
        else:
            ans='e'
            print("Times up!")

        client_socket.send(bytes(str(ans),"utf8"))
        print("ans sent")
        client_socket.send(bytes(str(time),"utf8"))
        print("time sent")

        flag=client_socket.recv(1024).decode("utf8")

        if(int(flag)):
            print("Correct answer")
        else:
            print("Better luck next time")
            client_socket.close()
            return
        


if __name__ == "__main__":
    # HOST=input('Enter host: ')
    # PORT=input('Enter port: ')
    HOST='';PORT=33002
    BUFFERSIZE=1024
    ADDR=(HOST,PORT)
    client_socket=socket(AF_INET,SOCK_STREAM)
    client_socket.connect(ADDR)

    start_game()
    # receive_thread=Thread(target=start_game)
    # receive_thread.start()
    # tkinter.mainloop()


