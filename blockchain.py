import time, json, sys

from block import Block

class Blockchain(object):

    def __init__(self, _startDifficulty, _maxBlockSize,_nodes = []):
        self.chain, self.difficulty, self.nodes, self.latestData, self.maxBlockSize = [self.createGenesisBlock()], _startDifficulty, _nodes, [], _maxBlockSize

    def addData(self, _data):
        self.latestData.append(_data)

        return self.getLatestBlock().index + 1

    def createGenesisBlock(self):
        block = Block(0, time.ctime(), "Genesis block")
        block.hash = block.calculateHash();
        self.addLocalBlockFile(block)
        return block

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def addBlock(self, _block):
        if sys.getsizeof(self.latestData) >= self.maxBlockSize:
            if len(self.chain) % 1000 == 0:
                self.difficulty += 1
            _block.prevHash = self.getLatestBlock().hash
            _block.mine(self.difficulty)
            _block.data = self.latestData

            self.addLocalBlockFile(_block)

            self.chain.append(_block)
            self.latestData = []

    def addLocalBlockFile(self, _block):
        with open(''.join(['blocks/',_block.hash, '.tbf']), 'a') as outfile:
            json.dump([str(_block.index),
            str(_block.prevHash),
            str(_block.merkleHash),
            str(_block.timestamp),
            str(_block.data),
            str(_block.nonce)], outfile, ensure_ascii=False)

    def addNode(self, _url):
        self.nodes.append(urlparse(_url))

    def isValid(self):
        for i in range(1, len(self.chain)):
            currentBlock = self.chain[i]
            prevBlock = self.chain[i-1]

            if currentBlock.hash != currentBlock.calculateHash() or  currentBlock.prevHash != prevBlock.hash:
                return False

        return True

    def restoreValidity(self):

        return True

    def compareToFullChain(self):
        if self.restoreValidity == True:
            return True
