import hashlib
import time
import json
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self) -> str:
        data_fields = (("Timestamp", self.timestamp),
                        ("Data", self.data),
                        ("Hash", self.hash),
                        ("Previous Hash", self.previous_hash))

        repr_str_parts = [f"{representation}: {data_field}" for representation, data_field in data_fields]
        return "\n".join(repr_str_parts)


class Blockchain:
    def __init__(self):
        self.chain = []

    def add_data(self, data):
        timestamp = get_current_gmt()
        previous_hash = 0
        if len(self.chain) != 0:
            previous_hash = self.chain[-1].hash
        block = Block(timestamp=timestamp, data=data, previous_hash=previous_hash)
        self.chain.append(block)

    def remove_data(self, data):
        block_to_pop = self._find_block_by_data(data)
        if block_to_pop is None:
            return
        if block_to_pop == self.chain[-1]:
            self.chain.pop()
            return

        index_block_to_pop = self.chain.index(block_to_pop)
        self.chain[index_block_to_pop+1].previous_hash = self.chain[index_block_to_pop].previous_hash
        self.chain.pop(index_block_to_pop)
        

    def __repr__(self) -> str:
        return f"# Blockchain:\n" + "\nv\n".join(map(str, self.chain)) + "\n"

    def _find_block_by_data(self, data):
        for block in self.chain:
            if block.data == data:
                return block

    @property
    def head(self):
        return self.chain[0]
    

def get_current_gmt():
    gmt_time = datetime.datetime.fromtimestamp(time.mktime(time.gmtime()))
    return gmt_time.isoformat()



if __name__ == "__main__":
    bc = Blockchain()
    bc.add_data("Alice pays Bob 0.001 BTC")
    bc.add_data("Bob pays Charlie 0.023 BTC")
    print(bc)

    b1 = Blockchain()
    b1.add_data("First")
    b1.add_data("Second")
    b1.add_data("Third")
    print(b1)               # should print three block data

    b1.remove_data("Second")
    b1.add_data("Fourth")
    print(b1)               # should print three block data after removing second and adding fourth

    b2 = Blockchain()
    print(b2)               # should print empty because there is no block in b2 chain

    b3 = Blockchain()
    b3.add_data("one")
    print(b3.head.timestamp)

    b3.add_data("two")
    print(b3.head.timestamp)
    
    b3.add_data("three")
    print(b3.head.timestamp)    # all the timestamps are same because they are declared at same time (Hrs:Min)
