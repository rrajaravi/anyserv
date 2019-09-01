import argparse
import json

from anyserv import StoreJson, register, run


parser = argparse.ArgumentParser(description='Serve any static data by providing json file as an input. Refer config.json available in github \
repository example directory for the file format')
parser.add_argument('-f', '--file', action=StoreJson, required=True)
parser.add_argument('--host', action="store", default='0.0.0.0')
parser.add_argument('-p', '--port', action="store", default='8080')


def main():
    args = parser.parse_args()
    register(args.file)
    run(host=args.host,port=args.port)
    
if __name__ == '__main__':
    main()

