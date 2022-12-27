import requests


if __name__ == '__main__':
    f = open('log.txt', 'w')
    while True:
        req = requests.get("https://github.com/vitkazak/Gazpromre")
        f.write(str(req) + '\n')
        print(str(req))

