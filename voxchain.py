# usr/bin/python
import hashlib
import time

class VoxCoinBlock:

    def __init__(self, previous_hash_block, transactions):
        self.previous_hash_block = previous_hash_block
        self.transactions = transactions
        self.block_data = previous_hash_block + ' - '.join(transactions)
        
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


    def get_last_block(self):
        pass

    def reinitialize_blockchain(self):
        pass



# start blockchain
blockchain = VoxCoinBlock()

while True:
    time.sleep(60)
    blockchain.get_last_block() 