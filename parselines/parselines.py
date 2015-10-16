import subprocess
import re

files = [
    ['user@host1', '/path/to/logfile'],
    ['user@host2', '/path/to/logfile'],
]


def get_lines(search_key):
    for item in enumerate(files):
        server = item[1][0]
        logfile = item[1][1]
        ssh = subprocess.Popen(['ssh', server, 'cat', logfile],
                               stdout=subprocess.PIPE)
        for line in iter(ssh.stdout.readlines()):
            line=str(line, encoding='UTF-8')
            if re.search(search_key, line):
                print(line)


def main():
    get_lines("needle")


if __name__ == "__main__":
    main()
