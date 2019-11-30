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
                self._process_bit(bit)
                bits.append(bit)
                bit = []
            elif len(l) > 0:
                bit.append(line.strip())
            line = f.readline()
        f.close()
        if len(bit) > 0:
            self._process_bit(bit)
            bits.append(bit)
        return bits

    def _process_bit(self, raw_bit):
        for raw in raw_bit:
            if raw[:1] == '<':
                print("scenerio:" + raw)
            elif raw[:1] == '-':
                print("comment:" + raw)
            else:
                print("bit:" + raw)
