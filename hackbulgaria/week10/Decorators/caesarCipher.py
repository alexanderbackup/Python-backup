from string import ascii_lowercase

class CaesarCypther:

    L2I = dict(zip(ascii_lowercase, range(26)))
    I2L = dict(zip(range(26), ascii_lowercase))

    def __init__(self, key, plaintext):
        self.key = key
        self.plaintext = plaintext
        self.result = ""

    def encipher(self):
        for c in self.plaintext.lower():
            if c.isalpha(): 
                self.result += CaesarCypther.I2L[(CaesarCypther.L2I[c] + self.key)%26]
            else: 
                self.result += c

    def decipher(self):
        for c in self.plaintext.lower():
            if c.isalpha(): 
                self.result += CaesarCypther.I2L[(CaesarCypther.L2I[c] - self.key)%26]
            else: 
                self.result += c



