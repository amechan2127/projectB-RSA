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

if os.path.isfile('text1.jpg'):
    os.remove('text1.jpg')

def enc_rsa(rsa,message):
	rsa_pub_key = rsa.publickey()
	rsa_pub_key_send = rsa_pub_key.exportKey()
	print('rsa_pub_key_send')
	print(rsa_pub_key_send)
	rsa_pub_key_recv = RSA.importKey(rsa_pub_key_send)
	print('rsa_pub_key_recv')
	print(rsa_pub_key_recv)
	print('rsa_pub_key.n')
	print(rsa_pub_key.n)
	encrypto = rsa_pub_key.encrypt( message, "" )
	return encrypto

def dec_rsa(rsa,encrypto):
	rsa_pub_key = rsa.publickey()
	rsa_private_key = RSA.construct((rsa.n, rsa.e, rsa.d))
	decrypto = rsa_private_key.decrypt( encrypto ) 
	return decrypto

if __name__ == '__main__':
	f=open('./pyramid.jpg', 'rb') 
	message = f.read()
	f.close()

	rsa = RSA.generate(1024)


#分割
#sizeは128が限界
	size=124
	end=int(len(message)/size)+1
	f=open('text1.jpg', 'ab') # 書き込みモードで開く
	for d in range(end):
		raw=message[d*size:(d+1)*size]
		enc=enc_rsa(rsa,raw)	
		dec=dec_rsa(rsa,enc)
		print(d)
		print('raw')
		print(raw)
#		print('enc')	
#		print(enc)
		print('dec')
		print(dec)

		f.write(dec) # 引数の文字列をファイルに書き込む
	f.close() # ファイルを閉じる

