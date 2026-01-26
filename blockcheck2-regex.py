import re

with open('/tmp/blockcheck2.txt', 'r') as f:
    text = f.read();
    matchDomain = re.search(r'port block tests ipv4 (.*)', text)

    if (matchDomain is None):
        print('Didnt find domain name')
        exit(0)

    domain = matchDomain.group(1).split(':')[0]
    strats = re.findall(r'-.*(?=\n!!!!! AVAILABLE !!!!!)', text, re.MULTILINE)

with open(f'zapret-strategies/{domain}.txt', 'w') as f:
    f.write('\n'.join(strats))
