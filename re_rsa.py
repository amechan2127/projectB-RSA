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
	encrypto = rsa_pub_key.encrypt( message, "" )
	return encrypto

def dec_rsa(rsa,encrypto):
	rsa_private_key = RSA.construct((rsa.n, rsa.e, rsa.d))
	decrypto = rsa_private_key.decrypt( encrypto ) 
	return decrypto

if __name__ == '__main__':
	f=open('./pyramid.jpg', 'rb') 
	g = f.read()
	message=base64.b64encode(g)
	f.close()

	rsa = RSA.generate(1024, RANDOM.RandomPool().get_bytes )

#分割
#sizeは128が限界
	size=128
	end=int(len(g)/size)+1
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

		f.write(raw) # 引数の文字列をファイルに書き込む
	f.close() # ファイルを閉じる
