__author__ = 'fthiele'

data = {
    'level 1-1':
        {
            'level 1-1-1':
                {
                    'a': 1,
                    'b': 2,
                    'c': 3,
                },
            'level 1-1-2':
                {
                    'd': 4,
                    'e': 5,
                    'f': 6,
                },
        },
    'level 1-2':
        {
            'level 1-2-1':
                {
                    'g': 7,
                    'h': 8,
                    'i': 9,
                },
            'level 1-2-2':
                {
                    'j': 10,
                    'k': 11,
                    'l': 12,
                    'm': [
                        13, 14, 15, 16
                    ]
                }
        }
}


def walkdict(data):
    for k, v in data.items():
        if isinstance(v, dict):
            walkdict(v)
        elif isinstance(v, list):
            print("{0}: ".format(k), end='')
            for item in v:
                print(" {0}".format(item), end='')

            print(" ")
        else:
            print("{0} : {1}".format(k, v))


def main():
    walkdict(data)


if __name__ == "__main__":
    main()
