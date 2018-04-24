#rsa_client3.pyを拡張
#力技で、rsaの数式に出てくる変数を全部固定する
#公開鍵として使うn、eをclient側でも固定する
#通信はできてるっぽいけどうまく復号されない
#原因はたぶん、clientで固定しているはずのnがなぜか変化してしまうこと
#なぜかわからない
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

start = time.time()

#address = ('192.168.11.2', 10000)
address = ('127.0.0.1', 10000)
max_size = 4096
size=500

def enc_rsa(message):
#	rsa_pub_key = rsa.publickey()
	rsa = RSA.generate(1024, RANDOM.RandomPool().get_bytes )
	rsa_pub_key=rsa.publickey()
	rsa_pub_key.n=145471325565137272885782581039688149428232444669081670130562887504720589945224856535922663715912109010927552603613192335809372301855527754295948685977606233230830293484559809494872642754838525110340427705495371805952848626596076943737994354649406602042592969617559716470638070888599314074058154791892769802391
	rsa_pub_key.e=65537
	print('rsa_pub_key.n')
	print(rsa_pub_key.n)
	encrypto = rsa_pub_key.encrypt( message, "" )
	return encrypto


print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
f=open('./pyramid.jpg', 'rb') 
message = f.read()
f.close()


#分割
#sizeは128が限界
size=124
end=int(len(message)/size)+1
l=pack('H',end)
client.send(l)
a=client.recv(max_size)

for d in range(end):
	raw=message[d*size:(d+1)*size]
	enc=enc_rsa(raw)
	client.send(enc[0])
	r=client.recv(max_size)
	print(unpack('H',r))
	print('raw')
	print(raw)


print('finish')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()

elapsed_time= time.time() -start
print("elapsed_time:{0}".format(elapsed_time)+"{sec}")
