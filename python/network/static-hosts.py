import subprocess as sub
import typing as tp
import operator as op
import pprint as pp

# https://docs.microsoft.com/en-us/sysinternals/downloads/psping
ping = r'.\psping64.exe -q -i 0 -n 2s'

url = ''
while not url:
    url = input('URL: ').strip()
if url.startswith('http:'):
    url = url[7:]
elif url.startswith('https:'):
    url = url[8:]
slash = url.find('/')
if slash != -1:
    url = url[:slash]
del slash
result_dict: tp.Dict[str, float] = {}
error_set: tp.Set[str] = set()
dns_tuple_us = (
    '',
    '8.8.8.8',
    '8.8.4.4',
    '208.67.222.222',
    '208.67.220.220',
    '1.1.1.1',
    '1.0.0.1',
    '9.9.9.9',
    '149.112.112.112',
    '209.244.0.3',
    '209.244.0.4',
    '64.6.64.6',
    '64.6.65.6',
    '84.200.69.80',
    '84.200.70.40',
    '8.26.56.26',
    '8.20.247.20',
)
dns_tuple_cn = ('119.29.29.29', '119.28.28.28', '223.5.5.5', '223.6.6.6',
                '114.114.114.114', '114.114.115.115', '1.2.4.8', '210.2.4.8',
                '180.76.76.76', '117.50.11.11', '117.50.22.22',
                '112.124.47.27', '114.215.126.16', '101.226.4.6',
                '218.30.118.6')

for dns in dns_tuple_us:
    print(f'\nDNS {dns if dns else "DEFAULT"}:')
    ip = sub.check_output(f'nslookup {url} {dns}',
                          stderr=sub.DEVNULL).split(b'Address')[-1]
    ips: tp.List[str] = []
    if ip[:1] == b'e':
        for ip in ip[4:].split(b'\r\n'):
            ip = ip.strip()
            if ip and all(x not in ip for x in (b':', b'c', b'e')):
                ips.append(ip.decode())
    if ip[:1] == b':':
        ip = ip[3:ip.find(b'\r')]
        if ip and all(x not in ip for x in (b':', b'c', b'e')):
            ips.append(ip.decode())
    del ip

    for ip in ips:
        if ip in dns_tuple_us or ip in dns_tuple_cn:
            ips.remove(ip)
    if not ips:
        print(f'\t DOMAIN UNKNOWN!')
        continue

    for ip in ips:
        if ip not in result_dict and ip not in error_set:
            print(f'\tNew IP: {ip}')
            try:
                latency = sub.check_output(f'{ping} {ip}:443').split(
                    b'Average = ')[-1]
                latency = float(latency[:latency.find(b'ms')])
                if latency:
                    result_dict[ip] = latency
                else:
                    error_set.add(ip)
                print(f'\t\t\t\t\t {latency:3} ms')
            except Exception as e:
                error_set.add(ip)
                print('\t Error!', e)

if not result_dict:
    exit()

result_dict_sorted = sorted(result_dict.items(), key=op.itemgetter(1))
print('\n\n')
pp.pprint(result_dict_sorted)

with open('C:/Windows/System32/drivers/etc/hosts', 'r+') as hosts:
    hosts_dict: tp.Dict[str, tp.Tuple[str, str]] = {}
    for line in hosts.readlines():
        if not line:
            continue
        line = [x.replace('\t', '') for x in line.strip().split(' ') if x]
        if len(line) == 5 and line[2] == '#' and line[-1] == 'ms':
            hosts_dict[line[1]] = (line[0], line[-2])
        elif len(line) == 2:
            hosts_dict[line[1]] = (line[0], '')
        else:
            hosts_dict[' '.join(line)] = None
    hosts_dict[url] = (result_dict_sorted[0][0], result_dict_sorted[0][1])

    hosts.seek(0)
    hosts.truncate()
    for _url, ip in hosts_dict.items():
        if not ip:
            hosts.write(f'{_url}\n')
            continue

        hosts.write(f'{ip[0]:<15} {_url}')
        if ip[1] != '':
            hosts.write(f'\t # {ip[1]} ms')

        hosts.write('\n')

    for k, v in hosts_dict.items():
        print(k)
        print(f'\t{v}')

sub.Popen('ipconfig /flushdns')