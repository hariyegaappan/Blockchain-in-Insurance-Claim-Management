import hashlib
import json
import time

class InsuranceBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_claims = []
        self.create_block(previous_hash="0")  # Genesis block

    def create_block(self, previous_hash):
        """Create a new block and add it to the chain."""
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time.time(),
            "claims": self.pending_claims,
            "previous_hash": previous_hash,
            "hash": "",
            "nonce": 0
        }
        block["hash"] = self.proof_of_work(block)
        self.pending_claims = []
        self.chain.append(block)
        return block

    def add_claim(self, claim_id, policy_holder, amount, reason):
        """Add a new insurance claim to the pending list."""
        self.pending_claims.append({
            "type": "new_claim",
            "claim_id": claim_id,
            "policy_holder": policy_holder,
            "amount": amount,
            "reason": reason,
            "timestamp": time.time(),
            "status": "Pending"
        })

    def update_claim_status(self, claim_id, status):
        """
        Instead of modifying old blocks, add a new transaction
        indicating a status update.
        """
        self.pending_claims.append({
            "type": "status_update",
            "claim_id": claim_id,
            "new_status": status,
            "timestamp": time.time()
        })
        return True

    def proof_of_work(self, block, difficulty=3):
        """Simple Proof-of-Work: find a hash with leading zeros."""
        prefix = "0" * difficulty
        while True:
            block_str = json.dumps(block, sort_keys=True).encode()
            hash_val = hashlib.sha256(block_str).hexdigest()
            if hash_val.startswith(prefix):
                return hash_val
            block["nonce"] += 1

    def is_chain_valid(self):
        """Verify blockchain integrity."""
        for i in range(1, len(self.chain)):
            prev = self.chain[i - 1]
            curr = self.chain[i]
            if curr["previous_hash"] != prev["hash"]:
                return False
            if curr["hash"] != self.hash_block(curr):
                return False
        return True

    @staticmethod
    def hash_block(block):
        """Generate hash for a block (ignoring stored hash)."""
        block_copy = block.copy()
        block_copy["hash"] = ""
        return hashlib.sha256(json.dumps(block_copy, sort_keys=True).encode()).hexdigest()


# ----------- INTERACTIVE MENU -----------
if __name__ == "__main__":
    blockchain = InsuranceBlockchain()

    print("\nWelcome to the Insurance Claim Blockchain System")
    while True:
        print("\nOptions:")
        print("1. Add a new insurance claim")
        print("2. Mine a new block to confirm claims")
        print("3. Record claim status update (Approved/Rejected)")
        print("4. View blockchain")
        print("5. Validate blockchain")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            claim_id = input("Enter Claim ID: ").strip()
            holder = input("Enter Policy Holder Name: ").strip()
            amount = float(input("Enter Claim Amount: ").strip())
            reason = input("Enter Reason for Claim: ").strip()
            blockchain.add_claim(claim_id, holder, amount, reason)
            print("\nClaim added to pending list.")

        elif choice == "2":
            if blockchain.pending_claims:
                new_block = blockchain.create_block(blockchain.chain[-1]["hash"])
                print(f"\nBlock #{new_block['index']} mined successfully!")
                print(f"Hash: {new_block['hash']}")
            else:
                print("\nNo pending claims to mine.")

        elif choice == "3":
            claim_id = input("Enter Claim ID to update: ").strip()
            status = input("Enter new status (Approved/Rejected): ").strip()
            blockchain.update_claim_status(claim_id, status)
            print(f"\nStatus update for claim {claim_id} recorded as a new transaction.")

        elif choice == "4":
            print("\n--- Blockchain ---")
            for block in blockchain.chain:
                print(f"\nBlock #{block['index']} | Hash: {block['hash']}")
                print(json.dumps(block, indent=4))

        elif choice == "5":
            print("\nBlockchain valid?", blockchain.is_chain_valid())

        elif choice == "6":
            print("\nExiting... Goodbye!")
            break

        else:
            print("\nInvalid choice, try again.")
