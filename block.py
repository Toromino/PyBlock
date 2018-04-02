import hashlib
import jsonpickle

class Block(object):

    def __init__(self, _index, _timestamp, _data = [], _prevHash = '', _merkleHash = ''):
        self.index, self.timestamp, self.data, self.prevHash, self.merkleHash, self.nonce, self.hash = _index, _timestamp, _data, _prevHash, _merkleHash, 0, ''


    def calculateHash(self):
        hash = ''.join([str(self.index), str(self.prevHash), str(self.merkleHash), str(self.timestamp), jsonpickle.encode(self.data), str(self.nonce)])
        hash = hash.encode('utf-8')
        return hashlib.sha256(hash).hexdigest()

    def mine(self, _difficulty):
        s = []
        for i in range(0, _difficulty):
            s.append('0')
        s = ''.join(s)
        while self.hash[0:_difficulty] != s:
            self.nonce+=1
            self.hash = self.calculateHash()
        print("[Info] Block mined: ", self.hash)
