#! /usr/bin/env python
# -*- coding: utf-8 -*-

import Crypto.PublicKey.RSA as RSA
import Crypto.Util.randpool  as RANDOM
import datetime,time
import time
def rsa(message):
	message = message.encode('utf-8')
	#鍵オブジェクト( 鍵を16ByteまでOKとする )
	rsa = RSA.generate(1024, RANDOM.RandomPool().get_bytes )
	#公開鍵
	rsa_pub_key = rsa.publickey()
	#秘密鍵
	rsa_private_key = RSA.construct((rsa.n, rsa.e, rsa.d))
	#messagez
	#message = "This is enc Test".encode('utf-8')
	#暗号化
	encrypto = rsa_pub_key.encrypt( message, "" )
	return encrypto
if __name__ == '__main__':
	message = "This is enc Test"
	for i in range(10):
		start = time.time()	
		a=rsa(message)
		elapsed_tme = time.time() - start
		print(elapsed_tme)






#復号化
#	decrypto = rsa_private_key.decrypt( encrypto ) 
#	elapsed_tme = time.time() - start
#	print(decrypto)
#	print(elapsed_tme)
#署名確認
"""digest = rsa_private_key.sign( message, "" )
digest_flag = rsa_pub_key.verify( message, digest )
html  = '''Content-Type: text/html; charset=UTF-8
<html>
<head>
<title>web-pro.appspot.com</title>
</head>
<body>
<table>
<tr><th>message     </th><td>%s </td></tr>
<tr><th>encrypto      </th><td>%s </td></tr>
<tr><th>decrypto  </th><td>%s </td></tr>
<tr><th>digest flag  </th><td>%s </td></tr>
</table>
</body>
<html>
'''"""