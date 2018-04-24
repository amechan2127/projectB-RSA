#base64なしで通信可能
#だけどclientとserverで作成しているrsaが異なるので、画像をうまく復号できない
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


#address = ('192.168.11.2', 10000)
address = ('127.0.0.1', 10000)
max_size = 1024*5

if os.path.isfile('text1.jpg'):
    os.remove('text1.jpg')

def dec_rsa(rsa,encrypto):
    rsa_private_key = RSA.construct((rsa.n, rsa.e, rsa.d))
    decrypto = rsa_private_key.decrypt( encrypto )
    return decrypto


print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, addr = server.accept()

rsa = RSA.generate(1024, RANDOM.RandomPool().get_bytes )


num = client.recv(max_size)
client.send(num)
 
allsize=unpack('H',num)
print(allsize)

#rsa = RSA.generate(1024, RANDOM.RandomPool().get_bytes )

#復号して書き込み
f=open('text1.jpg', 'ab') # 書き込みモードで開く

for i in range(allsize[0]):
    data = client.recv(max_size)
    j = pack('H',i)
    print(i)
    dec=dec_rsa(rsa,data)
    print(dec)
    client.send(j)
    f.write(dec)

#    x=base64.b64decode(dec)
#    f.write(x) # 引数の文字列をファイルに書き込む

f.close() # ファイルを閉じる
client.sendall(b"Finish")
client.close()
server.close()