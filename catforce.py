import sys
import requests
import argparse

base_url = "http://challs.nusgreyhats.org:14004"
file_type = ".php"

l = ["admin", "login", "index", "upload"]

def request(base_url, path, file_type):
    # 1. exeption
    base_url = base_url if base_url[len(base_url) - 1] == "/" else f"{base_url}/"

    # 1. init
    request_url = f"{base_url}{path}{file_type}"

    r = requests.get(request_url, allow_redirects=False)

    return r.status_code

contents_list = []
redirect_list = []

for path in l:
    result_code = request(base_url, path, file_type)
    str_result_code = str(result_code)
    first_char = str_result_code[0]

    if len(str_result_code) == 3:
        if first_char == "2":
            contents_list.append(path)
        elif first_char == "3":
            redirect_list.append(path)

print("contents_list", contents_list)

print("redirect_list", redirect_list)

def main(domain, wordlist):
    print("main", domain, wordlist)
    

def get_arguments():
    # 1. init
    parser = argparse.ArgumentParser()

    # 2. options
    parser.add_argument('-t', required=True, help='domain', dest="domain")
    parser.add_argument('-w', required=False, default='', help='wordlist', dest="wordlist")    

    # 3. parse
    args = parser.parse_args()
    filename_list = args.domain
    option_list = args.wordlist

    return args.domain, args.wordlist

if __name__ == '__main__':
    filename_list, option_list = get_arguments()
    main(filename_list, option_list)