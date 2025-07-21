import socket
import threading

SERVER_IP = input("Enter server IP: ")
PORT = 5555

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            if data:
                print(f"\n{data}")
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))

    recv_thread = threading.Thread(target=receive_messages, args=(client,))
    recv_thread.daemon = True
    recv_thread.start()

    while True:
        msg = input()
        if msg:
            client.sendall(msg.encode())

if __name__ == "__main__":
    main()
