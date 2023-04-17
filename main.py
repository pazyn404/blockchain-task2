from blockchain import Blockchain


blockchain = Blockchain("ledger.json")

blockchain.add_block({"from": "user5", "to": "user1", "amount": 5})



