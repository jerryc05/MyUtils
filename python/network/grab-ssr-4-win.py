import os.path as path


def log_s(s):
    print(f'{s} '.ljust(50, '.') + ' DONE √')


# download from internet
import shutil as su
import urllib.request as rq
file_name = 'ShadowsocksR-dotnet4.0.exe'
if not path.isfile(file_name):
    if (input('SSR not found in current folder, download from internet? (Y/N)\n'\
        ' ** MAKE SURE YOU PLACE THE DOWNLOADED FILE HERE!! **'
              ).strip().upper() == 'Y'):
        release_url = 'https://github.com/shadowsocksrr/shadowsocksr-csharp/releases'

        # get latest version
        with rq.urlopen(release_url) as r:
            version = r.read()
            version = version[version.index(b'tree/') + 5:]
            version = version[:version.index(b'"')].decode()
            log_s(f'SSR requesting latest version {version}')

        # download
        downloaded_file = f'ShadowsocksR-win-{version}.zip'
        print('Download the file to current folder...')
        import webbrowser as br
        br.open_new(f'{release_url}/download/{version}/{downloaded_file}')
        while not path.isfile(downloaded_file):
            input('Downloading... (Press ENTER when finished)')
        log_s('SSR core download')

        # unzip
        import zipfile as zf
        with zf.ZipFile(downloaded_file) as f:
            f.extractall()
            import glob as gl
            for file_path in gl.glob(
                    downloaded_file[:downloaded_file.find(".zip")] + '/*'):
                try:
                    su.move(file_path, '.')
                except:
                    pass
            try:
                su.rmtree(downloaded_file[:downloaded_file.find(".zip")])
            except:
                pass
            log_s('SSR unzip')

# backup config
config_file_name = 'gui-config.json'
if path.isfile(config_file_name):
    backup_dir = 'backup'
    if not path.isdir(backup_dir):
        import os
        os.mkdir(backup_dir)
    import datetime as dt
    su.copy2(
        config_file_name,
        f'{backup_dir}/{config_file_name}.{dt.datetime.today().strftime("%Y%m%d%H%M%S")}.bak'
    )
log_s('Config file backup')

# read and init config
import json as js
with open(config_file_name, 'w+') as f:
    try:
        json: dict = js.load(f)
    except:
        json = {}
json['balanceAlgorithm'] = 'FastDownloadSpeed'
json['shareOverLan'] = True
json['autoBan'] = True
json['sysProxyMode'] = 2
json['proxyRuleMode'] = 2

ssr_dict = {}
if 'configs' not in json:
    json['configs'] = []
else:
    for ssr in json['configs']:
        ssr_dict[f'{ssr["server"]}:{ssr["server_port"]}'] = ssr


def add_to_ssr_dict(ssr: dict):
    if 'port' in ssr:
        ssr['server_port'] = int(ssr['port'])
        del ssr['port']
    server_ip_port = f'{ssr["server"]}:{ssr["server_port"]}'
    if server_ip_port not in ssr_dict:
        ssr_dict[server_ip_port] = ssr
        id = hash(server_ip_port)
        while id < 0:
            id = (id + 0xf**32) % 0xf**32
        ssr_dict[server_ip_port]['id'] = f'{id:032X}'
    else:
        ssr_dict.update({server_ip_port: ssr})


def b64decode_safe(s) -> bytes:
    import base64 as b64
    count_down = 6
    while count_down:
        try:
            return b64.urlsafe_b64decode(s)
        except:
            if count_down == 0:
                print(s)
                raise Exception()
            s += b"=" if isinstance(s, bytes) else '='
            count_down -= 1

    return b''  # just to make type checker happy


def parse_ssr(s: bytes) -> dict:
    import base64 as b64
    parsed = b64decode_safe(s).decode().split(':')
    result = {
        'server': parsed[0],
        'port': parsed[1],
        'protocal': parsed[2],
        'method': parsed[3],
        'obfs': parsed[4]
    }
    parsed = parsed[5].split('/?')

    result['password'] = b64decode_safe(parsed[0]).decode()
    if len(parsed) > 1:
        for param in parsed[1].split('&'):
            param = param.split('=')
            if param[0] == 'protoparam':
                param[0] = 'protocalparam'
            elif param[0] == 'remarks':
                param[0] = 'remarks_base64'
            elif param[0] == 'group':
                param[1] = b64decode_safe(param[1]).decode()
            result[param[0]] = param[1]
    return result


def extract_ssr(s: bytes, split_char: bytes = b'"'):
    index = s.find(b'ssr://')
    while index > -1:
        s = s[index:]
        try:
            add_to_ssr_dict(parse_ssr(s[6:s.find(split_char)]))
        except:
            pass
        index = s.find(b'ssr://', 6)


timeout = 10


def f1():
    log_s('Starting func 1')
    try:
        with rq.urlopen(
                'https://raw.githubusercontent.com/wangzhenjjcn/ssr-address-free/master/ssServer.txt',
                timeout=timeout) as r1:
            r1 = r1.readlines()
        for line in r1:
            add_to_ssr_dict(js.loads(line.decode().replace("'", '"')))
    except Exception as e:
        print('Func 1 not working!', e)


def f2():
    log_s('Starting func 2')
    try:
        with rq.urlopen(
                'https://raw.githubusercontent.com/nulastudio/Freedom/master/docs/index.html',
                timeout=timeout) as r2:
            r2 = r2.read()
        extract_ssr(r2)
    except Exception as e:
        print('Func 2 not working!', e)


def f3():
    log_s('Starting func 3')
    try:
        with rq.urlopen(
                'https://raw.githubusercontent.com/Steve-ShadowsocksR/-SSR-/master/%E5%B0%8F%E9%A3%9E%E6%9C%BA%E7%BA%AF%E5%85%AC%E7%9B%8ASSR%E5%88%86%E4%BA%AB%EF%BC%81',
                timeout=timeout) as r3:
            r3 = r3.read()
        extract_ssr(r3, b'\n')
    except Exception as e:
        print('Func 3 not working!', e)


def f4():
    log_s('Starting func 4')
    try:
        with rq.urlopen(
                rq.Request('https://flywind.ml/free-ssr', headers=\
                            {
                                'User-Agent':
                                'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
                            }), timeout=5*timeout) as r4:
            r4 = r4.read()
        extract_ssr(r4)
    except Exception as e:
        print('Func 4 not working!', e)


def f5():
    log_s('Starting func 5')
    try:
        with rq.urlopen(
                'https://raw.githubusercontent.com/voken100g/AutoSSR/master/online',
                timeout=timeout) as r5:
            r5 = r5.read()
        extract_ssr(b64decode_safe(r5), b'\n')
    except Exception as e:
        print('Func 5 not working!', e)


def f6():
    log_s('Starting func 6')
    try:
        with rq.urlopen(
                'https://raw.githubusercontent.com/voken100g/AutoSSR/master/recent',
                timeout=timeout) as r6:
            r6 = r6.read()
        extract_ssr(b64decode_safe(r6), b'\n')
    except Exception as e:
        print('Func 6 not working!', e)


def f7():
    log_s('Starting func 7')
    try:
        with rq.urlopen(
                'https://raw.githubusercontent.com/voken100g/AutoSSR/master/stable',
                timeout=timeout) as r7:
            r7 = r7.read()
        extract_ssr(b64decode_safe(r7), b'\n')
    except Exception as e:
        print('Func 7 not working!', e)


def f8():
    log_s('Starting func 8')
    try:
        with rq.urlopen('https://lncn.org/api/lncn', b'', 2 * timeout) as r8:
            r8 = r8.read()
        extract_ssr(r8, b'\\"')
    except Exception as e:
        print('Func 8 not working!', e)


import threading as tr

tasks = [f1, f2, f3, f4, f5, f6, f7, f8]
tasks = [tr.Thread(target=x) for x in tasks]
log_s(f'Preparing SSR sources')

for x in tasks:
    x.start()
for x in tasks:
    x.join()
log_s('SSR url fetching')

# write config
json['configs'] = list(ssr_dict.values())

with open(config_file_name, 'w') as f:
    js.dump(json, f, ensure_ascii=False, indent='\t')
log_s('Config file saved')

# start SSR
import subprocess as sp
sp.Popen(file_name)

count_down = 5
import time
while count_down:
    print(end=f'All DONE! Exiting in {count_down}s\r')
    time.sleep(1)
    count_down -= 1
