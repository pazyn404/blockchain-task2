from json import loads, dumps

from block import Block


class Blockchain:
    def __init__(self, ledger_path: str) -> None:
        self.__ledger_path = ledger_path

    def add_block(self, block_data: dict) -> None:
        with open(self.__ledger_path, "r") as ledger_file:
            ledger_data = ledger_file.read()

        ledger = loads(ledger_data)

        prev_block = Block(ledger[-1])

        block_data.update({"id": prev_block.data["id"] + 1, "prev_block_relation": str(prev_block)})
        block = Block(block_data)
        block.evaluate_nonce()

        ledger.append(block.data)
        with open(self.__ledger_path, "w") as ledger_file:
            ledger_file.write(dumps(ledger))
