import argparse
import os
import webbrowser

import requests
from fake_headers import Headers


def main():
    argsparser = argparse.ArgumentParser(description='Requests')
    argsparser.add_argument('-o', help='open in chrome')
    arguments = argsparser.parse_known_args()

    if arguments[0].o != None:
        response = requests.get(url=arguments[0].o)

        with open('index.html', 'w') as file:
            file.write(response.text)

        chrome_path = '/usr/bin/google-chrome-stable %s'
        file_pash = os.path.abspath('index.html')
        webbrowser.get(chrome_path).open(file_pash)

    if len(arguments[1]) != 0:
        response = requests.get(url=arguments[1][0])
        print(response)


if __name__ == '__main__':
    main()
