# usr/bin/python
import hashlib
import time
import datetime
import json # store data in the blockchain
from dataclasses import dataclass
import random as rnd

@dataclass
class VoxBlockChain:
    
    block_number=0
    previous_hash_block='0'
    chain = []
    block_content=''


    def add_block(self,element):
        return self.chain.append(element)

    @classmethod
    def create_block(self, proof, previous_hash, block_data ):
            
        self.block_number+=1
        block = {
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': self.previous_hash_block,
                 'block_number': self.block_number,
                 'content': block_data }
    
        self.previous_hash_block = hashlib.sha256(block_data.encode()).hexdigest() # compute next block hash

        self.chain.append(block) # append block data to the dataframe
        return block

    def init_chain(self):
        block = self.create_block(proof=1, previous_hash= self.previous_hash_block, block_data='initialization')
        self.chain.append(block)
        return block
        
    def show_last_block(self):
        print(""" block number {0} time {1} content {2} """.format(self.block_number,self.chain[-1]['timestamp'],self.chain[-1]['content'] ))
    

if __name__ == '__main__':

    # Users
    users = ['Jhon','Malcom','Selly','David','Linda','Andy','Margaret','Lisa','Simon']       
    timing_between_block = 2 # seconds
    
    # KEYS
    # admin_key = 'dCXoi1290sa21n9a' # future improvement
    proof = 42

    # Start blockchain
    blockchain = VoxBlockChain() # object creation
    first_block = blockchain.init_chain() # parameters initialization
    blockchain.add_block(first_block)

    print('Blockchain up and running ...')

    while True:
        if new_transaction==True:

            # This part is generated form random users just for simulation
            # this part to be integrated such P2P servers for get() and post() block data into the shared blockchain
            # containing the real data for the sender, reciver and the amount.
            sender = rnd.choice(users) # RANDOM BLOCKCHAIN CONTENT , this could be a transaction, strat/end of some service or another DeFi App
            reciver = rnd.choice(users)
            amount=rnd.random()


            # message in the blockchain
            block_content = '{0} has send to {1}  \t\t {2} of vox coin'.format(sender,reciver,round(amount,7))
            
            # compute next block of the blockchain
            next_block = blockchain.create_block(proof, previous_hash=blockchain.previous_hash_block, block_data=block_content) 
            
            # add block to the blockchain
            blockchain.add_block(next_block)

            # show me 
            blockchain.show_last_block()
            
            # block time in the blockchain 
            time.sleep(timing_between_block)
