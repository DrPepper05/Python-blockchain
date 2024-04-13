import hashlib
import json

def crypto_hash(*args):

    string_args = sorted(map(lambda data : json.dumps(data) , args))
        
    joined_data = ''.join(string_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"{crypto_hash('one' , 1 , '1' , [3])}")

if __name__ == '__main__':
    main()