# https://cryptopals.com/sets/1/challenges/5

# repeating key xor

def repeating_key_xor(ciphertext: bytes, key: str) -> hex:
    repeating_keys = [ord(c) for c in key]
    n = len(repeating_keys)
    
    result = []
    for i, byte in enumerate(ciphertext):
        result.append(byte ^ repeating_keys[i % n])
    return bytes(result).hex()

def main():
    ciphertext = "Burning 'em, if you ain't quick and nimble" \
    "I go crazy when I hear a cymbal"
    print(repeating_key_xor(ciphertext.encode('ascii'), "ICE"))

if __name__ == "__main__":
    main()