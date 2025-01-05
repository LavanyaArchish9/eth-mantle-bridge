import logging
from decimal import Decimal, ROUND_DOWN
from src.core.bridge import Bridge
from src.config.config import Config
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - Transaction %(transaction_num)s - %(message)s'
)
logger = logging.getLogger(__name__)
logger = logging.LoggerAdapter(logger, {'transaction_num': 0})

def format_balance(balance):
    return Decimal(str(balance)).quantize(Decimal('0.0001'), rounding=ROUND_DOWN)

def monitor_balances(bridge, address, transaction_num):
    eth_balance = format_balance(bridge.get_balance(address, Config.ETH))
    logger.info(f"ETH Balance: {eth_balance} ETH", extra={'transaction_num': transaction_num})
    return eth_balance

def main():
    transaction_num = 1
    load_dotenv()
    bridge = Bridge()
    
    sender_address = os.getenv('SENDER_ADDRESS')
    recipient_address = os.getenv('RECIPIENT_ADDRESS')
    private_key = os.getenv('PRIVATE_KEY')
    
    logger.info("Checking initial balances...", extra={'transaction_num': transaction_num})
    eth_balance = monitor_balances(bridge, sender_address, transaction_num)
    
    if eth_balance == 0:
        logger.warning("Please fund your wallet with test ETH first", extra={'transaction_num': transaction_num})
        logger.info("Get test ETH from: https://www.ankr.com/rpc/eth/sepolia/faucet/", extra={'transaction_num': transaction_num})
        return
    
    amount = format_balance(Decimal('0.0001'))
    logger.info(f"Initiating transfer of {amount} ETH...", extra={'transaction_num': transaction_num})
    
    result = bridge.transfer(
        amount=amount,
        from_network=Config.ETH,
        to_network=Config.MANTLE,
        sender_address=sender_address,
        recipient_address=recipient_address,
        private_key=private_key
    )
    
    transaction_num += 1
    logger.info(f"Transfer initiated:", extra={'transaction_num': transaction_num})
    logger.info(f"Transaction Hash: {result['transaction_hash']}", extra={'transaction_num': transaction_num})
    logger.info(f"Status: {result['status']}", extra={'transaction_num': transaction_num})
    logger.info(f"From: {result['from_chain']}", extra={'transaction_num': transaction_num})
    logger.info(f"To: {result['to_chain']}", extra={'transaction_num': transaction_num})
    logger.info(f"Details: {result['details']}", extra={'transaction_num': transaction_num})
    
    mantle_status = bridge.get_transaction_status(result['transaction_hash'], Config.MANTLE)
    logger.info(f"Mantle Network Status: {mantle_status}", extra={'transaction_num': transaction_num})
    
    transaction_num += 1
    logger.info("Checking final ETH balance...", extra={'transaction_num': transaction_num})
    monitor_balances(bridge, sender_address, transaction_num)

if __name__ == "__main__":
    main()



# import logging
# from decimal import Decimal
# from src.core.bridge import Bridge
# from src.config.config import Config
# import os
# from dotenv import load_dotenv

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)

# def monitor_balances(bridge, address):
#     eth_balance = bridge.get_balance(address, Config.ETH)
#     logger.info(f"ETH Balance: {eth_balance} ETH")
#     return eth_balance

# def main():
#     # Load environment variables
#     load_dotenv()
    
#     # Initialize bridge
#     bridge = Bridge()
    
#     # Test parameters
#     sender_address = os.getenv('SENDER_ADDRESS')
#     recipient_address = os.getenv('RECIPIENT_ADDRESS')
#     private_key = os.getenv('PRIVATE_KEY')
    
#     # Monitor initial balances
#     logger.info("Checking initial balances...")
#     eth_balance = monitor_balances(bridge, sender_address)
    
#     if eth_balance == 0:
#         logger.warning("Please fund your wallet with test ETH first")
#         logger.info("Get test ETH from: https://www.ankr.com/rpc/eth/sepolia/faucet/")
#         return
    
#     # Set amount to a small fraction of the balance
#     amount = Decimal('0.00001')  # Very small test amount
    
#     # Execute transfer
#     logger.info(f"Initiating transfer of {amount} ETH...")
#     result = bridge.transfer(
#         amount=amount,
#         from_network=Config.ETH,
#         to_network=Config.MANTLE,
#         sender_address=sender_address,
#         recipient_address=recipient_address,
#         private_key=private_key
#     )
    
#     logger.info(f"Transfer initiated:")
#     logger.info(f"Transaction Hash: {result['transaction_hash']}")
#     logger.info(f"Status: {result['status']}")
#     logger.info(f"From: {result['from_chain']}")
#     logger.info(f"To: {result['to_chain']}")
#     logger.info(f"Details: {result['details']}")
    
#     # Monitor transaction status
#     mantle_status = bridge.get_transaction_status(result['transaction_hash'], Config.MANTLE)
#     logger.info(f"Mantle Network Status: {mantle_status}")
    
#     # Check final balances
#     logger.info("Checking final ETH balance...")
#     monitor_balances(bridge, sender_address)

# if __name__ == "__main__":
#     main()





# from decimal import Decimal
# from src.core.bridge import Bridge
# from src.config.config import Config
# import os
# from dotenv import load_dotenv

# def main():
#     # Load environment variables
#     load_dotenv()
    
#     # Initialize bridge
#     bridge = Bridge()
    
#     # Test parameters
#     sender_address = os.getenv('SENDER_ADDRESS')
#     recipient_address = os.getenv('RECIPIENT_ADDRESS')
#     private_key = os.getenv('PRIVATE_KEY')
    
#     # Check balance first
#     balance = bridge.get_balance(sender_address, Config.ETH)
#     print(f"Current balance: {balance} ETH")
    
#     if balance == 0:
#         print("Please fund your wallet with test ETH first")
#         print("Get test ETH from: https://www.ankr.com/rpc/eth/sepolia/faucet/")
#         return
    
#     # Set amount to a small fraction of the balance
#     amount = Decimal('0.00001')  # Very small test amount 
    
#     # Execute transfer
#     result = bridge.transfer(
#         amount=amount,
#         from_network=Config.ETH,
#         to_network=Config.MANTLE,
#         sender_address=sender_address,
#         recipient_address=recipient_address,
#         private_key=private_key
#     )
    
#     print(f"Transfer initiated:")
#     print(f"Transaction Hash: {result['transaction_hash']}")
#     print(f"Status: {result['status']}")
#     print(f"From: {result['from_chain']}")
#     print(f"To: {result['to_chain']}")
#     print(f"Details: {result['details']}")

#         # Add the monitoring code right here
#     # mantle_status = bridge.get_transaction_status(result['transaction_hash'], Config.MANTLE)
#     # print(f"Mantle Network Status: {mantle_status}")

# if __name__ == "__main__":
#     main()




