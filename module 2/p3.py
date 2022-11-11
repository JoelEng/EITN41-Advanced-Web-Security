import socket
from random import randint
from hashlib import sha1

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
soc.connect(("eitn41.eit.lth.se", 1337))

p = int('FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF', 16)
g = 2
pw = "eitn41 <3"

##########################
#### Helper Functions ####
##########################
def receive():
  return soc.recv(4096).decode('utf8').strip()

def receive_int():
  return int(receive(), 16)

def send(m: str):
  soc.send(format(m, "x").encode('utf8'))

def rand_g(x: int):
  r = randint(1, p)
  return pow(x, r, p), r

def printb(s: str):
  "Prints blue, underscored, bold text"
  print('\033[4m\033[1m\033[94m' + s + '\033[0m')

##########################
#### D-H Key Exchange ####
##########################
printb("D-H Key Exchange")

g_x1 = receive_int()
g_x2, x2 = rand_g(g)
send(g_x2)
print ('sent g_x2:', receive())

##########################
## Socialist Millionare ##
##########################
printb("\nSocialist Millionare")

g1_a2 = receive_int()
g1_b2, b2 = rand_g(g)
send(g1_b2)
print('sent g1_b2:', receive())

g1_a3 = receive_int()
g1_b3, b3 = rand_g(g)
send(g1_b3)
print('sent g1_b3:', receive())

Pa = receive_int()
g3 = pow(g1_a3, b3, p)
Pb, b = rand_g(g3)

send(Pb)
print('sent Pb:', receive())

Qa = receive_int()
g2 = pow(g1_a2, b2, p)
g1_x1x2 = pow(g_x1, x2, p)
g1_x1x2_bytes = g1_x1x2.to_bytes((g1_x1x2.bit_length() + 7) // 8, "big")
y = sha1(g1_x1x2_bytes + pw.encode("utf-8")).hexdigest()
Qb = pow(g, b, p) * pow(g2, int(y, 16), p)
send(Qb)
print('sent Qb:', receive())

Ra = receive_int()
Rb = pow(Qa * pow(Qb, -1, p), b3, p)
send(Rb)
print('sent Rb:', receive())
print('Authentication:', receive())

##########################
###### Secure Chat #######
##########################
printb("\nSecure Chat Response:")
msg = int("404dfc45eab74833561f74adef08977b625007df", 16)
send(msg ^ g1_x1x2)
print(receive())
