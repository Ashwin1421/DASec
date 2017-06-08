import socket

l = ['127.0.0.1' , '2605:6001:e14d:5f0:464:4cbf:1ba1:973c' , 'list']
for i in l:
        socket.inet_aton(i)
        print('true')
