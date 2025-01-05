
from dataclasses import dataclass
from web3 import Web3
from dotenv import load_dotenv
import os
from typing import Optional

load_dotenv()

@dataclass
class NetworkConfig:
    rpc_url: str
    chain_id: int
    bridge_contract: str
    name: str

class Config:
    # Network Configurations
    ETH = NetworkConfig(
        rpc_url=os.getenv('ETH_RPC_URL'),
        chain_id=11155111,  # Sepolia Testnet
        bridge_contract=os.getenv('ETH_BRIDGE_CONTRACT'),
        name='Sepolia'
    )
    
    MANTLE = NetworkConfig(
        rpc_url=os.getenv('MANTLE_RPC_URL'),
        chain_id=5001,  # Mantle Testnet
        bridge_contract=os.getenv('MANTLE_BRIDGE_CONTRACT'),
        name='Mantle'
    )
#Uncomment if you to use real ethereum money in metamask
# @dataclass
# class NetworkConfig:
#     rpc_url: str
#     chain_id: int
#     bridge_contract: str
#     name: str

# class Config:
#     # Network Configurations
#     ETH = NetworkConfig(
#         rpc_url=os.getenv('ETH_RPC_URL'),
#         chain_id=1,  # Ethereum Mainnet
#         bridge_contract=os.getenv('ETH_BRIDGE_CONTRACT'),
#         name='Ethereum'
#     )
    
#     MANTLE = NetworkConfig(
#         rpc_url=os.getenv('MANTLE_RPC_URL'),
#         chain_id=5000,  # Mantle Mainnet
#         bridge_contract=os.getenv('MANTLE_BRIDGE_CONTRACT'),
#         name='Mantle'
#     )

    @staticmethod
    def get_web3(network: NetworkConfig) -> Web3:
        """Initialize Web3 instance for specified network"""
        return Web3(Web3.HTTPProvider(network.rpc_url))

    @staticmethod
    def validate() -> bool:
        """Validate all required configuration is present"""
        required_vars = [
            'ETH_RPC_URL',
            'MANTLE_RPC_URL',
            'ETH_BRIDGE_CONTRACT',
            'MANTLE_BRIDGE_CONTRACT'
        ]
        return all(os.getenv(var) for var in required_vars)


