ETH-Mantle Bridge 🌉
A robust cross-chain bridge for transferring assets between Ethereum and Mantle networks with real-time balance monitoring and transaction tracking.



✨ Features
Seamless asset transfers between Ethereum (Sepolia) and Mantle networks
Real-time balance monitoring with 4 decimal precision
Detailed transaction status tracking
Secure private key management
Docker containerization support
Comprehensive logging system



## Docker Setup and Project Execution
Here's how the project runs in Docker, showing successful container initialization and service startup:
![Docker Setup](./docs/images/docker%20setup.png)
## Transaction Verification
The following images demonstrate a successful transfer with matching balances:

### MetaMask Wallet Balance
Current wallet balance showing the exact amount after transfer:
![MetaMask Balance](./docs/images/metamask2.png)### Transaction Confirmation
Transaction logs confirming the successful transfer with matching balance:
![Successful Transaction](./docs/images/succssful%20transcation.png)


As shown in both screenshots above, the final balance matches between MetaMask and the transaction logs, confirming the transfer's accuracy and success.
🚀 Quick Start
Prerequisites
Python 3.8+
Docker & Docker Compose
MetaMask wallet
Test ETH (for testnet) or real ETH (for mainnet)
Installation
Clone the repository:

git clone https://github.com/yourusername/eth-mantle-bridge
cd eth-mantle-bridge
Install dependencies:


pip install -r requirements.txt
Configure environment:


cp .env.example .env
🔐 MetaMask Setup
Install MetaMask from metamask.io.
Create a new wallet and securely store your seed phrase.
Obtain account details:
Public Address: Click on your account name to copy the address.
Private Key: Navigate to Account Details > Export Private Key.
💎 Getting Test ETH
Visit Google Cloud Web3 Faucet.
Connect your MetaMask wallet.
Request test ETH.
Wait for confirmation (usually 1–2 minutes).
🔄 Running Transfers
Test Network (Default)
Run the following command:


docker-compose up --build
Successful Transfer Confirmation:
Logs will display successful transfer details after execution.

Mainnet Configuration (Real ETH)
To use real ETH instead of test ETH:

Fund your MetaMask wallet with real ETH.

Modify the .env file:


ETH_RPC_URL=https://mainnet.infura.io/v3/YOUR_INFURA_KEY
MANTLE_RPC_URL=https://rpc.mantle.xyz
Uncomment the mainnet configuration in src/config/config.py:


ETH = NetworkConfig(
    rpc_url=os.getenv('ETH_RPC_URL'),
    chain_id=1,  # Ethereum Mainnet
    bridge_contract=os.getenv('ETH_BRIDGE_CONTRACT'),
    name='Ethereum'
)
📂 Environment Variables


ETH_RPC_URL=            # Ethereum RPC endpoint
MANTLE_RPC_URL=         # Mantle RPC endpoint
SENDER_ADDRESS=         # Your wallet address
RECIPIENT_ADDRESS=      # Recipient wallet address
PRIVATE_KEY=            # Your wallet private key
🌐 Network Settings
Testnet (Default)
Sepolia Testnet: Chain ID 11155111
Mantle Testnet: Chain ID 5001
Mainnet
Ethereum Mainnet: Chain ID 1
Mantle Mainnet: Chain ID 5000
🔍 Monitoring
The bridge provides detailed transaction monitoring:

Real-time balance updates
Transaction status tracking
Gas usage details
Network confirmation status
⚠️ Security Notes
Never commit private keys or sensitive data.
Use environment variables for sensitive information.
Test thoroughly on testnet before using the mainnet.
Keep your MetaMask wallet secure.
📈 Transaction Verification
Initial Balance Check: Verify the sender’s initial balance.
Transaction Execution: Check for successful transfer logs.
Final Balance Confirmation: Ensure balances match in MetaMask and the logs.
🤝 Contributing
Contributions are welcome! Please submit a Pull Request.

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
Ethereum Foundation
Mantle Network
Web3.py Team
