#rsa_server3.pyを拡張
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


#address = ('192.168.11.2', 10000)
address = ('127.0.0.1', 10000)
max_size = 1024*5

if os.path.isfile('text1.jpg'):
    os.remove('text1.jpg')

def dec_rsa(encrypto):
    rsa = RSA.generate(1024, RANDOM.RandomPool().get_bytes )
    rsa.n=145471325565137272885782581039688149428232444669081670130562887504720589945224856535922663715912109010927552603613192335809372301855527754295948685977606233230830293484559809494872642754838525110340427705495371805952848626596076943737994354649406602042592969617559716470638070888599314074058154791892769802391
    rsa.e=65537
    rsa.d=21517601202808195726914206335333276173112674040955150681991495360952765596975903066347777622748248848008479102482968193590430674186909471750994500234476930448082061706047301016136608755418669760263728418550774979347859116947293576480638933146421447506419194772797598857419375571888971551074154487277961921937
    rsa.p=11444448290025606916724702822518266092555354869033384100260512949484030906682203805655960827455078445407498725745812188968143376548796960389934850463502557
    rsa.q=12711082428667409467280738736266707221075884674685463640039196795888245510768877737928973598498601428894094815378094110994961553740257214655445784230120963
    rsa.u=12213696054552591246008243178713852307335582484378605284341118185114591281487593461839382892684071842018263062496886067580686240642833174841748501441564395
    rsa_private_key = RSA.construct((rsa.n, rsa.e, rsa.d))
    decrypto = rsa_private_key.decrypt( encrypto )
#    print('rsa.n')
#    print(rsa.n)
    return decrypto


print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, addr = server.accept()

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
    dec=dec_rsa(data)
    print(dec)
    client.send(j)
    f.write(dec)

#    x=base64.b64decode(dec)
#    f.write(x) # 引数の文字列をファイルに書き込む

f.close() # ファイルを閉じる
client.sendall(b"Finish")
client.close()
server.close()