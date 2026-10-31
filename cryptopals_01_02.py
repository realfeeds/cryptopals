# https://cryptopals.com/sets/1/challenges/1

# Convert hex to base64
import base64

def hex_to_base64(string):
    data = bytes.fromhex(string)
    return base64.b64encode(data)

# print(hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))

def fixed_xor(buffer1, buffer2):
    result = [buffer1[i] ^ buffer2[i] for i in range(len(buffer1))]
    return bytes(result)

a = bytes.fromhex('1c0111001f010100061a024b53535009181c')
b = bytes.fromhex('686974207468652062756c6c277320657965')
print(fixed_xor(a, b).hex())