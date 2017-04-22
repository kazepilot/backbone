import json
from Queue import Queue


class Config(object):

    def __init__(self, filename):
        with open(filename) as json_data:
            self.data = json.load(json_data)

    def zones(self):
        return self.data['zones']

    def is_active(self, name):
        for item in self.data['classes']:
            if item['name'] == name:
                return item['active']
        return False

    def get_moves(self, name):
        moves = Queue()
        steps = []
        for item in self.data['classes']:
            if item['name'] == name:
                steps = item['moves']
                break

        for step in steps:
            moves.put(self.data['moves'][step])

        return moves

    def get_conditions(self, name):
        for item in self.data['classes']:
            if item['name'] == name:
                return item['conditions']
        return []

    def get_standard_conditions(self):
        return self.data['standard_conditions']


def main():
    config = Config('config.json')
    print config.data['moves']
    print config.data['standard_conditions']
    print config.data['zones']['LEFT']

    for item in config.data['classes']:
        if item['name'] == 'plyta':
            print item['active']

    for item in config.data['classes']:
        if item['name'] == 'stop':
            print item['conditions']

    for item in config.data['classes']:
        if item['name'] == 'stop':
            print item['moves']

    moves = config.get_moves('stop')
    while not moves.empty():
        print moves.get()

if __name__ == '__main__':
    main()
