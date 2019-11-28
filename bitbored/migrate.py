class Migrate(object):

    def __init__(self, filename):
        self.filename = filename

    def migrate(self):
        f = open(self.filename)
        line = f.readline()
        bits = []
        bit = []
        while line:
            bit.append(line.strip())
            if line.strip() == '-----':
                bits.append(bit)
                bit = []
            line = f.readline()
        f.close()
        return bits
