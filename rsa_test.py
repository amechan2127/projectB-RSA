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
#	rsa_pub_key.n = 134208879708636825835766188478280880908400436807964641184684003444766064644914526924347212653776672062747302596982757178015151728699885786386073492970072503717305840373279444223120856326564689872653582445610518936762881085874103578860512730227692179797965548723354242003583362018686763166261448256590973469563
	print('rsa_pub_key1.n')
	print(rsa_pub_key.n)
	encrypto = rsa_pub_key.encrypt( message, "" )
	return encrypto

def dec_rsa(rsa,encrypto):
	rsa_pub_key = rsa.publickey()
	print('rsa_pub_key2.n')
	print(rsa_pub_key.n)
	rsa_private_key = RSA.construct((rsa.n, rsa.e, rsa.d))
	decrypto = rsa_private_key.decrypt( encrypto ) 
	return decrypto

if __name__ == '__main__':
	f=open('./pyramid.jpg', 'rb') 
	message = f.read()
	f.close()

	rsa = RSA.generate(1024, RANDOM.RandomPool().get_bytes )


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

