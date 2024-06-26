import argparse
from swagtector.swagger_detector import SwaggerDetector

print('''
   _______          __     _____ _______ ______ _____ _______ ____  _____  
  / ____\ \        / /\   / ____|__   __|  ____/ ____|__   __/ __ \|  __ \ 
 | (___  \ \  /\  / /  \ | |  __   | |  | |__ | |       | | | |  | | |__) |
  \___ \  \ \/  \/ / /\ \| | |_ |  | |  |  __|| |       | | | |  | |  _  / 
  ____) |  \  /\  / ____ \ |__| |  | |  | |___| |____   | | | |__| | | \ \ 
 |_____/    \/  \/_/    \_\_____|  |_|  |______\_____|  |_|  \____/|_|  \_\                                                           
                                                                     v1.0.2              
''')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-U', '--url', dest='url',
        help="Url to scan."
    )

    parser.add_argument(
        '-F', '--file', dest='file',
        help='File to scan'
    )

    parser.add_argument(
        '-O', '--output', dest='output',
        help='Save the result to a file'
    )

    args = parser.parse_args()
    if not (args.url or args.file):
        parser.error(
            'Please specify an URL or a file path.')

    return args


def main():
    args = get_args()
    if args.url:
        url = (args.url).rstrip('/')
        detector = SwaggerDetector(url, args.output)
        detector.run()
    elif args.file:
        with open(args.file, 'r') as f:
            urls = f.read().splitlines()
        for url in urls:
            url = url.rstrip('/')
            print(f"[I] Checking {url}")
            detector = SwaggerDetector(url, args.output)
            detector.run()
    else:
        print('Please specify a URL or a file to scan.')


if __name__ == '__main__':
    main()
