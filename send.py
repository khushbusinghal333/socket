import  socket

ip="192.168.10.101"
port=9090   #  port >6000  are generally free to use 
rec_ip="127.0.0.1"
rec_port=9090   #  port >6000  are generally free to use 

#  calling  UDP  protocol 
#             socket.AF_INET--->ipv4         , socket.SOCK_DGRAM--->  UDP @@ -13,7 +13,10 @@

while  True:
	data=raw_input("type your message :  ")
	s.sendto(data,(ip,port))
        #  it will send data to receiver as well as create own socket (own ip and any random port)
	s.sendto(data,(rec_ip,rec_port))
	#  this is for receiving from  sender 
	print  s.recvfrom(10)