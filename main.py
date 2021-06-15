import requests
import sys

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'
HEADER = '\033[95m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'


def test(proxy_file, out):
    test_url = 'http://ifconfig.me/ip'
    print(G + "\n[+] " + C + 'testing proxies...\n')
    prx_file = open(proxy_file, "r")
    for i in prx_file:
        i = i.split(" ")
        proxy = i[0].replace("\n","")
        try:
            proxy_test = {'http': proxy, 'https': proxy}
            requests.get(test_url, proxies=proxy_test, timeout=5)
            print(G + "[+] " + HEADER + "good proxy.....  " + W + "[" + G + proxy + W + "]")
            with open(out, "a") as http:
                http.write(proxy + "\n")
        except:
            print(R + "[!]" + WARNING + " bad proxy ...... " + W + "[" + R + proxy + W + "]")

    prx_file.close()
    print(G + "\n[>] " + C + "done")


if __name__ == '__main__':
    if len(sys.argv) == 3:
    	fl = sys.argv[1]
    	o = sys.argv[2]
    	test(fl, o)
    else:
    	print("Usage: python main.py [proxy path] [output path]\n\nExample:\n\tpython main.py proxies.txt output.txt")
