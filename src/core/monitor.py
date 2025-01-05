from typing import Dict, Callable, Optional
import time
from web3 import Web3

class TransactionMonitor:
    def __init__(self, web3: Web3):
        self.web3 = web3
    
    def monitor_transaction(
        self,
        tx_hash: str,
        callback: Optional[Callable] = None,
        timeout: int = 300
    ) -> Dict:
        """
        Monitor transaction until completion or timeout
        """
        start_time = time.time()
        while True:
            try:
                receipt = self.web3.eth.get_transaction_receipt(tx_hash)
                if receipt:
                    status = 'success' if receipt['status'] == 1 else 'failed'
                    result = {
                        'status': status,
                        'block_number': receipt['blockNumber'],
                        'gas_used': receipt['gasUsed']
                    }
                    if callback:
                        callback(result)
                    return result
            except:
                if time.time() - start_time > timeout:
                    return {'status': 'timeout'}
            time.sleep(5)
