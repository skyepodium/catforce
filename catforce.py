import sys
import requests
import argparse


def request(request_url):
    print("request_url", request_url)
    r = requests.get(request_url, allow_redirects=False)
    print(r.status_code)
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
    # 1. exeption
    target = target if target[len(target) - 1] == "/" else f"{target}/"

    file_extension = file_extension if file_extension[0] == "." else f".{file_extension}"

    return f"{target}{path}{file_extension}"

def main(target, word_path, file_extension):
    print("main", target, word_path, file_extension)
    
    word_list = get_world_list(word_path)

    contents_list = []
    redirect_list = []    

    for path in word_list:
        request_url = make_path(target, path, file_extension)
        result_code = request(request_url)

        str_result_code = str(result_code)
        first_char = str_result_code[0]

        if len(str_result_code) == 3:
            if first_char == "2":
                contents_list.append(path)
            elif first_char == "3":
                redirect_list.append(path)      

    print("contents_list", contents_list)
    print("redirect_list", redirect_list)


def get_arguments():
    # 1. init
    parser = argparse.ArgumentParser()

    # 2. options
    parser.add_argument('-t', required=True, help='target', dest="target")
    parser.add_argument('-w', required=False, default='./wordlist.txt', help='word_path', dest="word_path")
    parser.add_argument('-f', required=False, default='', help='file_extension', dest="file_extension")

    # 3. parse
    return parser.parse_args()

if __name__ == '__main__':
    args = get_arguments()
    main(args.target, args.word_path, args.file_extension)