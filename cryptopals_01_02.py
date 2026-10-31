# https://cryptopals.com/sets/1/challenges/2

# Fixed XOR 
def fixed_xor(buffer1: bytes, buffer2: bytes) -> bytes:
    result = [buffer1[i] ^ buffer2[i] for i in range(len(buffer1))]
    return bytes(result)

a = bytes.fromhex('1c0111001f010100061a024b53535009181c')
b = bytes.fromhex('686974207468652062756c6c277320657965')

print(fixed_xor(a, b).hex())