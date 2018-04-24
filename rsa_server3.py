#rsa_server2.pyを拡張
#rsaで公開鍵に使うのは、数式ではnとe。eはいつも同じだからnだけを送る
#nの数が大きすぎて送れない
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


#address = ('192.168.11.2', 10000)
address = ('127.0.0.1', 10000)
max_size = 1024*5

if os.path.isfile('text1.jpg'):
    os.remove('text1.jpg')

def dec_rsa(rsa,encrypto,x):
    rsa.n = x
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

#rsa送信
x=134208879708636825835766188478280880908400436807964641184684003444766064644914526924347212653776672062747302596982757178015151728699885786386073492970072503717305840373279444223120856326564689872653582445610518936762881085874103578860512730227692179797965548723354242003583362018686763166261448256590973469563
y=pack('H',x)
client.send(y)

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
    dec=dec_rsa(rsa,data,x)
    print(dec)
    client.send(j)
    f.write(dec)

#    x=base64.b64decode(dec)
#    f.write(x) # 引数の文字列をファイルに書き込む

f.close() # ファイルを閉じる
client.sendall(b"Finish")
client.close()
server.close()