from typing import Dict
from web3 import Web3

class TransactionHandler:
    def __init__(self, web3: Web3):
        self.web3 = web3
    
    def execute_transaction(
        self, 
        transaction: Dict,
        private_key: str
    ) -> str:
        """
        Execute and sign transaction
        Returns transaction hash
        """
        signed_txn = self.web3.eth.account.sign_transaction(
            transaction,
            private_key=private_key
        )
        # Using raw_transaction instead of rawTransaction
        tx_hash = self.web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        return tx_hash.hex()
    
    def get_transaction_status(self, tx_hash: str) -> Dict:
        """
        Get current status of transaction
        """
        try:
            receipt = self.web3.eth.get_transaction_receipt(tx_hash)
            return {
                'status': 'success' if receipt['status'] == 1 else 'failed',
                'block_number': receipt['blockNumber'],
                'gas_used': receipt['gasUsed']
            }
        except:
            return {'status': 'pending'}
