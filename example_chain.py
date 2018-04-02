import time

from block import Block
from blockchain import Blockchain

testBlockchain = Blockchain(4, 42)

for i in range(100):

    block = Block(len(testBlockchain.chain), time.ctime())
    print("".join(["[Info] Mining block ", str(block.index), " with difficulty ", str(testBlockchain.difficulty), "... "]))
    testBlockchain.addBlock(block)

    if testBlockchain.isValid():
        print("\n[Info] Is blockchain valid? ", str(testBlockchain.isValid()))
    else:
        print("\n[Error] Is blockchain valid? ",str(testBlockchain.isValid()))
