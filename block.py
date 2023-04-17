from hashlib import sha256

from config import ZEROS


class Block:
    required_fields = ["from", "to", "amount"]
    def __init__(self, data: dict) -> None:
        self.__data = data
        self.__validate()

    def __validate(self) -> None:
        if set(Block.required_fields).difference(self.__data.keys()):
            raise ValueError("Invalid block")

    def evaluate_nonce(self) -> None:
        block_id = self.__data["id"]
        block_from = self.__data["from"]
        block_to = self.__data["to"]
        block_amount = self.__data["amount"]
        block_prev_block_relation = self.__data["prev_block_relation"]
        block_data = f"{block_id}{block_from}{block_to}{block_amount}{block_prev_block_relation}"
        block_nonce = 0
        while not sha256(f"{block_data}{block_nonce}".encode()).hexdigest().startswith("0" * ZEROS):
            block_nonce += 1
        self.__data["nonce"] = block_nonce

    def __str__(self):
        block_id = self.__data["id"]
        block_from = self.__data["from"]
        block_to = self.__data["to"]
        block_amount = self.__data["amount"]
        block_prev_block_relation = self.__data["prev_block_relation"]
        block_nonce = self.__data["nonce"]
        block_data = f"{block_id}{block_from}{block_to}{block_amount}{block_prev_block_relation}{block_nonce}"
        #
        return sha256(f"{block_data}".encode()).hexdigest()

    @property
    def data(self) -> dict:
        return self.__data
