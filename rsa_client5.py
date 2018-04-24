#公開鍵の送受信には成功
#pyramidは送信可能(2バイト足りないけど、一応画像としては見れる)
#sao_1.jpgは見れない(30バイト足りない)
import Crypto.PublicKey.RSA as RSA
import Crypto.Util.randpool  as RANDOM
import datetime,time
import time
import socket
from datetime import datetime
from struct import *
import time
import os

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)


if os.path.isfile('text1.jpg'):
    os.remove('text1.jpg')

start = time.time()

#address = ('192.168.11.2', 10000)
address = ('127.0.0.1', 10000)
max_size = 4096
size=500

"""def enc_rsa(rsa,message):
	rsa_pub_key = rsa.publickey()
	encrypto = rsa_pub_key.encrypt( message, "" )
	return encrypto
"""

def enc_rsa(pub_key,message):
	encrypto = pub_key.encrypt( message, "" )
	return encrypto

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
f=open('./pyramid.jpg', 'rb') 
message = f.read()
f.close()

#rsa = RSA.generate(1024, RANDOM.RandomPool().get_bytes )
#公開鍵の受信
rsa_pub_key_recv = RSA.importKey(client.recv(max_size))
print('rsa_pub_key_recv')
print(rsa_pub_key_recv)

#分割
#sizeは128が限界
size=124
end=int(len(message)/size)+1
l=pack('H',end)
client.send(l)
a=client.recv(max_size)

for d in range(end):
	raw=message[d*size:(d+1)*size]
	enc=enc_rsa(rsa_pub_key_recv,raw)
	client.send(enc[0])
	r=client.recv(max_size)
	print(unpack('H',r))


print('finish')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()

elapsed_time= time.time() -start
print("elapsed_time:{0}".format(elapsed_time)+"{sec}")
