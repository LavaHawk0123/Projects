import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9999))
s.listen(5)
print("looking for connections")

while True:
    c, address = s.accept()
    print("connection established")
    c.send(bytes("121311231232132421AIANDAUTOMATION12131243214325124").encode("utf-8"))
    c.close()