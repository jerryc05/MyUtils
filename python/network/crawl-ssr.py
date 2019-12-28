from urllib.request import *
from base64 import *
from threading import *
from queue import *
import re

ssrs = Queue()
threads = []

urls = [
    'https://raw.githubusercontent.com/voken100g/AutoSSR/master/stable',
    'https://raw.githubusercontent.com/voken100g/AutoSSR/master/online',
    'https://raw.githubusercontent.com/voken100g/AutoSSR/master/recent'
]


def crawl(x: str, q: Queue):
    print(f'Opening [{x}]!')
    content = urlopen(x).read()
    print(f'Contents from [{x}] received!')
    content += b'=' * (-len(content) % 4)
    for x in b64decode(content).decode().splitlines():
        q.put(x)


for x in urls:
    threads.append(Thread(target=crawl, args=(x, ssrs)))
    threads[-1].setDaemon(True)
    threads[-1].start()

urls = [
    'https://github.com/goFindAlex/FreeSS/blob/master/list.txt',
    'https://github.com/nulastudio/Freedom/blob/master/docs/index.html'
]


def crawl2(x: str, q: Queue, pattern):
    print(f'Opening [{x}]!')
    content = urlopen(x).read().decode()
    print(f'Contents from [{x}] received!')
    for x in pattern.findall(content):
        x = x[1:-1]
        q.put(x)


for x in urls:
    threads.append(
        Thread(target=crawl2, args=(x, ssrs, re.compile('\Wssr?:\/\/\w+\W'))))
    threads[-1].setDaemon(True)
    threads[-1].start()

for x in threads:
    x.join(8)

if not ssrs.empty():
    with open('ssrs.txt', 'w') as f:
        while not ssrs.empty():
            x = ssrs.get()
            print(x, '\n\n')
            f.write(x + '\n')

print("All done!")
for x in threads:
    print(x)