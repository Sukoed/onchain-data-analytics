def track_whale_movement(tx_value, threshold=100):
    if tx_value >= threshold:
        return f"🚨 Whale Alert: {tx_value} ETH transferred!"
    return "Small transaction detected."

if __name__ == "__main__":
    print(track_whale_movement(150)) # Test
