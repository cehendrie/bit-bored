class Migrate(object):

    def __init__(self, filename):
        self.filename = filename

    def migrate(self):
        f = open(self.filename)
        line = f.readline()
        bits = []
        bit = []
        while line:
            l = line.strip()
            if l[:5] == '-----':
                bits.append(bit)
                bit = []
            elif len(l) > 0:
                bit.append(line.strip())
            line = f.readline()
        f.close()
        if len(bit) > 0:
            bits.append(bit)
        return bits
