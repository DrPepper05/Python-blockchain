import time 
from crypto_hash import crypto_hash

class Block:
   
    def __init__(self , timestamp , last_hash , hash , data):
        self.timestamp = timestamp
        self.hash = hash
        self.last_hash = last_hash
        self.data = data
   
    def __repr__(self):
        return (
            'Block - '
            f'{self.timestamp}, '
            f'{self.hash}, '
            f'{self.data})'
        )
    
    @staticmethod
    def mine_block(last_block , data):
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp , last_hash , data)
        data = data
        return Block(timestamp ,last_hash, hash , data )
    
    @staticmethod
    def genesis():
        return Block(1 , 'lhash'  , 'hash' , [])
    
def main():
    print("pepsi")

if __name__ == "__main__":
    main()