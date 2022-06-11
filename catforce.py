import sys
import requests
import argparse
from tqdm import tqdm

def request(request_url):
    r = requests.get(request_url, allow_redirects=False)
    return r.status_code


def get_world_list(word_path):
    f = open(word_path, 'r')
    word_list = []

    while True:
        path = f.readline()
        if not path: break
        word_list.append(path.strip())

    f.close()

    return word_list

def make_path(target, path, file_extension):
    print("target, path, file_extension", target, path, file_extension)
    # 1. exeption
    target = target if target and target[len(target) - 1] == "/" else f"{target}/"

    if file_extension:
        file_extension = file_extension if file_extension[0] == "." else f".{file_extension}"
    else:
        file_extension = ""

    return f"{target}{path}{file_extension}"

def print_result(contents_list, redirect_list):
    print()
    print("=" * 50)
    print("""\
        _  __ __      ___
        |_)|_ (_ | ||   | 
        | \|____)|_||__ | 
                    """)    

    print("1. contents_list")
    for c in contents_list:
        print(c)
    print()
    print("2. redirect_list")
    for c in redirect_list:
        print(c)

    print("=" * 50)
    print()
    
def main(target, word_path, file_extension):
    print("main", target, word_path, file_extension)
    
    word_list = get_world_list(word_path)
    print()
    print("total world count:", len(word_list))
    print()
    contents_list = []
    redirect_list = []    

    for path in tqdm(word_list):
        request_url = make_path(target, path, file_extension)
        result_code = request(request_url)

        str_result_code = str(result_code)
        first_char = str_result_code[0]

        p = f"/{path}{file_extension}"

        if len(str_result_code) == 3:
            if first_char == "2":
                contents_list.append(p)
            elif first_char == "3":
                redirect_list.append(p)      
    
    print_result(contents_list, redirect_list)

def get_arguments():
    # 1. init
    parser = argparse.ArgumentParser()

    # 2. options
    parser.add_argument('-t', required=True, help='target', dest="target")
    parser.add_argument('-w', required=False, default='./wordlist.txt', help='word_path', dest="word_path")
    parser.add_argument('-f', required=False, default='', help='file_extension', dest="file_extension")

    # 3. parse
    return parser.parse_args()

def print_banner():
    print("""\

        _________  ______   __________  ____  ____________
        / ____/   |/_  __/  / ____/ __ \/ __ \/ ____/ ____/
        / /   / /| | / /    / /_  / / / / /_/ / /   / __/   
        / /___/ ___ |/ /    / __/ / /_/ / _, _/ /___/ /___   
        \____/_/  |_/_/    /_/    \____/_/ |_|\____/_____/ 

                    """)

if __name__ == '__main__':
    args = get_arguments()
    print_banner()

    main(args.target, args.word_path, args.file_extension)