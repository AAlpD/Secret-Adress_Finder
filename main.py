import requests


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


target_url = input("[*] Enter Target URL: ")

file = open("common.txt", "r")
for line in file:
    print(line)
    word = line.strip()
    full_url = target_url + word
    response = request(full_url)
    if response:
        print("[+] Discovered Direction At This Link: " + full_url)
