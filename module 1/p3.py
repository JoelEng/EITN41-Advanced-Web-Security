import socket
import requests
from hashlib import sha256

class Block:
  def __init__(self, index, timestamp, data, prevhash, nonce):
     self.index = index
     self.timestamp = timestamp #this should be in format strftime(%Y-%m-%d, %H:%M:%S")
     self.data = data
     self.prevhash = prevhash
     self.nonce = nonce
     self.hash = sha256(f'{index}-{timestamp}-{data}-{prevhash}-{nonce}'.encode('utf-8')).hexdigest()

# s = socket.socket()
# s.connect(("eitn41.eit.lth.se", 3152))
# res = requests.post("https://eitn41.eit.lth.se:3152", 0000)
# print(res.json())