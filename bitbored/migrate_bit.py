class MigrateBit(object):

    def __init__(self, raw_bit):
        self.raw_bit = raw_bit

    def to_json(self):
        json = {}
        for raw in self.raw_bit:
            if raw[:1] == '<':
                json['scenerio'] = raw
            elif raw[:1] == '-':
                if 'comments' in json:
                    json['comments'].append(raw)
                else:
                    json['comments'] = [raw]
            else:
                if 'bit' in json:
                    json['bit'].append(raw)
                else:
                    json['bit'] = [raw]
        if self._is_valid(json):
            return json
        else:
            raise Exception("invalid json: " + json)

    def _is_valid(self, json):
        if (len(json) == 0):
            return False
        elif 'bit' not in json:
            return False
        else:
            return True
