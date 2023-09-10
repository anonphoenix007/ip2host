import socket as skt
from colorama import Fore as f
from sys import argv

ipadd = argv[1]
result = skt.gethostbyaddr(ipadd)
print(f.YELLOW + ipadd, "is " + f.GREEN, result)
