from typing import Dict
from decimal import Decimal
from web3 import Web3
from eth_typing import Address
from src.config.config import Config, NetworkConfig
from .transaction import TransactionHandler
from .monitor import TransactionMonitor

class Bridge:
    def __init__(self):
        self.config = Config()
        if not self.config.validate():
            raise ValueError("Missing required configuration")
        
        # Initialize Web3 connections
        self.eth_web3 = Config.get_web3(Config.ETH)
        self.mantle_web3 = Config.get_web3(Config.MANTLE)
        
        # Initialize handlers
        self.eth_handler = TransactionHandler(self.eth_web3)
        self.mantle_handler = TransactionHandler(self.mantle_web3)
        self.monitor = TransactionMonitor(self.eth_web3)
    
    def transfer(
        self,
        amount: Decimal,
        from_network: NetworkConfig,
        to_network: NetworkConfig,
        sender_address: Address,
        recipient_address: Address,
        private_key: str
    ) -> Dict[str, str]:
        """
        Execute cross-chain transfer with monitoring
        """
        web3 = Config.get_web3(from_network)
        handler = self.eth_handler if from_network == Config.ETH else self.mantle_handler
        
        # Get current gas price
        gas_price = web3.eth.gas_price
        
        # Prepare transaction with optimized gas settings
        transaction = {
            'from': sender_address,
            'to': from_network.bridge_contract,
            'value': web3.to_wei(amount, 'ether'),
            'gas': 150000,  # Optimized gas limit
            'gasPrice': gas_price,
            'nonce': web3.eth.get_transaction_count(sender_address),
            'chainId': from_network.chain_id
        }
        
        # Execute transaction
        tx_hash = handler.execute_transaction(transaction, private_key)
        
        # Monitor transaction status
        result = self.monitor.monitor_transaction(tx_hash)
        
        return {
            'transaction_hash': tx_hash,
            'status': result.get('status', 'pending'),
            'from_chain': from_network.name,
            'to_chain': to_network.name,
            'details': {
                'gas_price': gas_price,
                'block_number': result.get('block_number'),
                'gas_used': result.get('gas_used')
            }
        }
    
    def get_transaction_status(self, tx_hash: str, network: NetworkConfig) -> Dict:
        """
        Get status of a specific transaction
        """
        handler = self.eth_handler if network == Config.ETH else self.mantle_handler
        return handler.get_transaction_status(tx_hash)
    
    def get_balance(self, address: str, network: NetworkConfig) -> Decimal:
        """
        Get wallet balance on specified network
        """
        web3 = Config.get_web3(network)
        balance_wei = web3.eth.get_balance(address)
        return Decimal(web3.from_wei(balance_wei, 'ether'))

