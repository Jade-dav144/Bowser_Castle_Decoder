class CastleArchive:
    def __init__(self):
        self.data = {
            11: 237,
            3: 383,
            14: 297,
            0: 317,
            8: 234,
            5: 255,
            15: 278,
            2: 369,
            10: 322,
            1: 313,
            13: 295,
            6: 284,
            4: 217,
            12: 236,
            7: 277,
            9: 278,
            17: 429,
            16: 262
        }

        self.keys = {
            0: 5,
            1: 7,
            2: 3
        }

    def getValue(self, index):
        return self.data[index]

    def getKey(self, index):
        return self.keys[index % len(self.keys)]

class CastleDecoder(CastleArchive):
    def decode(self):
        message = ""

        for i in self.data:
            value = self.getValue(i)
            key = self.getKey(i + 1)
            message = message + chr((value - key) // 3)
        return message

decoder = CastleDecoder()
result = decoder.decode()

if len(result) == 18 and sum(ord(x) for x in result) == 1578:
    print(result)
else:
    print("Castle Data Corrupted.")
