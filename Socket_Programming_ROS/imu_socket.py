import socket
from struct import *
from tf.transformations import quaternion_from_euler

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("192.168.1.29" , 9989))
print ("Server running... ")
while True:
 data , addr = server_socket.recvfrom(1024)
 print("Connected to client")
 a = float("%1.4f" %unpack_from ('!f', data, 36))
 b = float("%1.4f" %unpack_from ('!f', data, 40))
 c = float("%1.4f" %unpack_from ('!f', data, 44))        
 q1 = quaternion_from_euler(a, b, c)

print(str(q1[0]),str(q[1]),str(q[2]),str(q[3]))
            
