from urllib.request import *

url = "http://www.pudim.com.br/"

try:
    urlopen(url)
    print('\033[0:32mConectado\033[m')
except:
    print('\033[0:31mInativo')
