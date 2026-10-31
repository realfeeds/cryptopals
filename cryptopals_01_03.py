# https://cryptopals.com/sets/1/challenges/3

# for frequency analysis
english_frequency = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074,
    ' ': 0.13000
}

# english_frequency_dec = {ord(key):english_frequency[key] for key in english_frequency.keys()}

def english_frequency_counter(text: str) -> dict:
    #result  = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz' + ' '}
    result = {}
    n = len(text)
    text = text.lower()

    for char in text:
        result[char] = result.get(char, 0) + 1
    for char in result:
        result[char] /= n
    return result

# score for heurestic
def frequency_metric(text: str, q: dict = english_frequency):
    dist = 0
    n = len(text)

    p = english_frequency_counter(text)
    for char in q.keys():
        observed = p.get(char, 0)
        expected = q[char]

        dist += ((observed - expected) ** 2) / expected

    # Penalize unusual characters
    unusual = sum(
        char not in "abcdefghijklmnopqrstuvwxyz '.,!?;:-"
        for char in text
    )

    dist += 10 * unusual / n

    return dist

# Single-byte XOR cipher
def single_byte_xor(ciphertext: bytes, key: int) -> bytes:
    result = [byte ^ key for byte in ciphertext]
    return bytes(result)

# best guess (lowest score), returns key, text, and score
def best_guess(ciphertext: bytes, n = 1):
    decryptedtexts = []
    for key in range(128):
        decryptedtext = single_byte_xor(ciphertext, key)
        score = frequency_metric(decryptedtext.decode('ascii', errors='replace'))

        decryptedtexts.append([key, decryptedtext, score])
        # print(f"Key: {key}, Text: {decryptedtext.decode('ascii')}, Score: {score}")

    decryptedtext_sorted = sorted(decryptedtexts,
                                  key=lambda item: item[2]
    )

    return decryptedtext_sorted[:n][0]

def main():
    ciphertext_hex = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ciphertext = bytes.fromhex(ciphertext_hex)

    decryptedtexts = []
    for key in range(128):
        decryptedtext = single_byte_xor(ciphertext, key)
        score = frequency_metric(decryptedtext.decode('ascii'))

        decryptedtexts.append([key, decryptedtext, score])
        # print(f"Key: {key}, Text: {decryptedtext.decode('ascii')}, Score: {score}")

    decryptedtext_sorted = sorted(
        decryptedtexts,
        key=lambda item: item[2]
    )

    for key, text, score in decryptedtext_sorted:
        print(f"Score: {round(score, 3)}, {text.decode('ascii', errors="replace")!r}, Key: {key} ")

    key, text, score = best_guess(ciphertext)
    print(f"Best Guess (Key: {key}, Score: {score}):")
    print(f"{text}")

if __name__ == "__main__":
    main()
