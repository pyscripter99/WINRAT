import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 9876))
s.listen(5)

def handle_client(conn: socket.socket):
    print(conn.recv(1024))
    conn.send(b"Ok!")
    conn.close

while True:
    conn, addr = s.accept()
    threading.Thread(target=handle_client, args=(conn,)).start()