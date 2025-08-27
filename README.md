# Blockchain-in-Insurance-Claim-Management
A Python-based blockchain for secure insurance claim management. It records claim requests, updates claim statuses, verifies integrity with cryptographic hashes, and ensures transparency and tamper-proof records for the insurance process.

## 🚀 Features
- Add new insurance claims with **claim ID, policy holder, amount, and reason**  
- Record claim status updates (**Approved/Rejected**) as separate transactions  
- Mine blocks using **Proof of Work** with SHA-256 hashing  
- View the **entire blockchain** in JSON format  
- **Validate blockchain** integrity for security  
- Command-line **interactive menu** for easy operations  

## 🛠️ Tech Stack
- **Python 3**  
- **Hashlib** for cryptographic hashing  
- **JSON** for structured data representation  

## ⚡ How It Works
1. **Claims** are added to a pending list before being confirmed.  
2. **Status updates** are recorded as new transactions instead of modifying old blocks.  
3. **Blocks** are mined using a Proof-of-Work algorithm, securing all pending transactions.  
4. Each block stores:
   - Index and timestamp  
   - List of claims and status updates  
   - Previous block's hash  
   - Current block's hash and nonce  

5. **Blockchain Validation** ensures all hashes are correct and the chain is untampered.

## 📥 Installation & Usage
1. **Clone the repository:**
```bash
git clone https://github.com/hariyegaappan/Blockchain-in-Insurance-Claim-Management.git
cd Blockchain-in-Insurance-Claim-Management
```

2. **Run the program:**
```bash
python blockchain.py
```

4. **Follow the interactive menu:**
- Add new claims
- Record status updates
- Mine blocks to confirm transactions
- View or validate the blockchain
