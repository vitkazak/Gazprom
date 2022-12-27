import requests


if __name__ == '__main__':
    f = open('log.txt', 'w')
    f.write("ver:1.1.1" + '\n')
    while True:
        req = requests.get("https://github.com/vitkazak/Gazpromres")
        f.write(str(req) + '\n')
        print(str(req))

