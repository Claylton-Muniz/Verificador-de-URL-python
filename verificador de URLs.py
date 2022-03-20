from urllib.request import urlopen
from colorama import init
from menu import *

init()
cabecalho('Disboniblidade de url')
print('\033[33mExemplo: www.youtube.com / youtube.com')
print('{:^4}{:^17}\033[m'.format('↓', '↓'))
site = input('Url: ')
try:
    if 'http://' in site:
        urlopen(site)
    else:
        if 'www.' in site:
            urlopen('http://www.' + site)
        else:
            urlopen('http://' + site)
except:
    print('\033[31m')
    rodape('\tErro: Site inacessível!\nVerifique se Url foi digitada corretamente')
    print('\033[m')
else:
    print('\033[34m')
    rodape('Site pronto para ser executado!')
    print('\033[m')
