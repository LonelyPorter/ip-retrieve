#!/usr/bin/python3

import argparse
import re
import requests

URL = "https://ipinfo.io"
IP_PATTERN = r'\d+\.\d+\.\d+\.\d+'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve IPs.")
    parser.add_argument('file', nargs=1, type=str)
    args = parser.parse_args()

    ips = []
    output = []

    regex = re.compile(IP_PATTERN)

    try:
        with open(args.file[0], 'r', encoding="utf8") as f:
            data = f.read()
            ips = regex.findall(data)
    except FileNotFoundError as e:
        print(e)
        exit(1)

    for ip in ips:
        response = requests.get(URL + '/' + ip)
        result = response.json()

        s = result['ip'] + ': '
        s += ' '.join([result['city'], result['region'], result['country']])

        output.append(s)

    print('\n'.join(output))
