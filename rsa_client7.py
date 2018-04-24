#公開鍵の送受信には成功
#base64のエンコードに成功
#pyramidもsao_1.jpgも送信可能
#RSA完成
import Crypto.PublicKey.RSA as RSA
import Crypto.Util.randpool  as RANDOM
import datetime,time
import time
import socket
from datetime import datetime
from struct import *
import time
import os
import base64
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

if os.path.isfile('text1.jpg'):
    os.remove('text1.jpg')
	
#address = ('192.168.11.2', 10000)
address = ('127.0.0.1', 10000)
#address = ('169.254.17.32', 10000)
max_size = 4096
size=500

def enc_rsa(pub_key,message):
	encrypto = pub_key.encrypt( message, "" )
	return encrypto


if __name__ == '__main__':
	print('Starting the client at', datetime.now())
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(address)
	f=open('./pyramid.jpg', 'rb') 
	g = f.read()
	message=base64.b64encode(g)
	f.close()

	#公開鍵の受信
	rsa_pub_key_recv = RSA.importKey(client.recv(max_size))
	print('rsa_pub_key_recv')
	print(rsa_pub_key_recv)

	#分割
	#sizeは128が限界
	start = time.time()
	size=128
	end=int(len(message)/size)+1
	l=pack('H',end)
	client.send(l)
	a=client.recv(max_size)

	for d in range(end):
		raw=message[d*size:(d+1)*size]
		enc=enc_rsa(rsa_pub_key_recv,raw)
		client.send(enc[0])
		r=client.recv(max_size)
	#	print(unpack('H',r))

	elapsed_time= time.time() -start
	print("elapsed_time:{0}".format(elapsed_time)+"{sec}")
	print('finish')
	data = client.recv(max_size)
	print('At', datetime.now(), 'someone replied', data)
	client.close()

