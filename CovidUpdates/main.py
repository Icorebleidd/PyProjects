import requests
import datetime
import re
import ast
import argparse

parser = argparse.ArgumentParser(description='A test program.') #https://linuxhint.com/add_command_line_arguments_to_a_python_script/#:~:text=To%20add%20arguments%20to%20Python,are%20of%20proper%20%E2%80%9Ctype%E2%80%9D.

args = parser.parse_args()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

today = datetime.date.today()
today = str(today)
today = today[8:10]

r = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json')

r_dict = r.json()

r_dict = {k:v for element in r_dict for k,v in element.items()}

first_line = str(r_dict)

if first_line[18:20] == today:
   with open('old_data.txt', 'r+') as fi:
       with open('new_data.txt', 'r+') as f:
         old_line = f.readline()
         fi.seek(0)
         fi.write(re.sub(r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", old_line))
         fi.truncate()
         fi.close()
   with open('new_data.txt', 'r+') as f:
      f.seek(0)
      f.write(re.sub(r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", first_line))
      f.truncate()

      print(f"Data: {color.BOLD + color.YELLOW}{r_dict['data']}{color.END}")
      print(f"Ricoverati con sintomi: {color.CYAN}{r_dict['ricoverati_con_sintomi']}{color.END} Differenza: {color.CYAN}{int(r_dict['ricoverati_con_sintomi']) - int(old_line['ricoverati_con_sintomi'])}{color.END}")
      print(f"Terapia intensiva: {color.BLUE}{r_dict['terapia_intensiva']}{color.END} Differenza: {color.BLUE}{int(r_dict['terapia_intensiva']) - int(old_line['terapia_intensiva'])}{color.END}")
      print(f"Isolamento domiciliare: {color.DARKCYAN}{r_dict['isolamento_domiciliare']}{color.END} Differenza: {color.DARKCYAN}{int(r_dict['isolamento_domiciliare']) - int(old_line['isolamento_domiciliare'])}{color.END}")
      print(f"Totale positivi: {color.PURPLE}{r_dict['totale_positivi']}{color.END} Differenza: {color.PURPLE}{int(r_dict['totale_positivi']) - int(old_line['totale_positivi'])}{color.END}")
      print(f"Dimessi guariti: {color.GREEN}{r_dict['dimessi_guariti']}{color.END} Differenza: {color.GREEN}{int(r_dict['dimessi_guariti']) - int(old_line['dimessi_guariti'])}{color.END}")
      print(f"Deceduti: {color.RED}{r_dict['deceduti']}{color.END} Differenza: {color.RED}{int(r_dict['deceduti']) - int(old_line['deceduti'])}{color.END}")
      print(f"Totale casi: {color.RED}{r_dict['totale_casi']}{color.END} Differenza: {color.RED}{int(r_dict['totale_casi']) - int(old_line['totale_casi'])}{color.END}")
      print(f"Tamponi: {color.RED}{r_dict['tamponi']}{color.END} Differenza: {color.RED}{int(r_dict['tamponi']) - int(old_line['tamponi'])}{color.END}")
      print(f"Casi testati: {color.RED}{r_dict['casi_testati']}{color.END} Differenza: {color.RED}{int(r_dict['casi_testati']) - int(old_line['casi_testati'])}{color.END}")
      print(f"Totale positivi test molecolare {color.RED}{r_dict['totale_positivi_test_molecolare']}{color.END} Differenza: {color.RED}{int(r_dict['totale_positivi_test_molecolare']) - int(old_line['totale_positivi_test_molecolare'])}{color.END}")
      print(f"Totale positivi test antigenico rapido: {color.RED}{r_dict['totale_positivi_test_antigenico_rapido']}{color.END} Differenza: {color.RED}{int(r_dict['totale_positivi_test_antigenico_rapido']) - int(old_line['totale_positivi_test_antigenico_rapido'])}{color.END}")
      print(f"Tamponi test molecolare: {color.RED}{r_dict['tamponi_test_molecolare']}{color.END} Differenza: {color.RED}{int(r_dict['tamponi_test_molecolare']) - int(old_line['tamponi_test_molecolare'])}{color.END}")
      print(f"Tamponi test antigenico rapido: {color.RED}{r_dict['tamponi_test_antigenico_rapido']}{color.END} Differenza: {color.RED}{int(r_dict['tamponi_test_antigenico_rapido']) - int(old_line['tamponi_test_antigenico_rapido'])}{color.END}")
      f.close()
else:
   with open ('old_data.txt', 'r+') as f:
      old_line = f.readline()
      old_line = ast.literal_eval(old_line)
      print(f"Data: {color.BOLD + color.YELLOW}{r_dict['data']}{color.END}")
      print(f"Ricoverati con sintomi: {color.CYAN}{r_dict['ricoverati_con_sintomi']}{color.END} Differenza: {color.CYAN}{int(r_dict['ricoverati_con_sintomi']) - int(old_line['ricoverati_con_sintomi'])}{color.END}")
      print(f"Terapia intensiva: {color.BLUE}{r_dict['terapia_intensiva']}{color.END} Differenza: {color.BLUE}{int(r_dict['terapia_intensiva']) - int(old_line['terapia_intensiva'])}{color.END}")
      print(f"Isolamento domiciliare: {color.DARKCYAN}{r_dict['isolamento_domiciliare']}{color.END} Differenza: {color.DARKCYAN}{int(r_dict['isolamento_domiciliare']) - int(old_line['isolamento_domiciliare'])}{color.END}")
      print(f"Totale positivi: {color.PURPLE}{r_dict['totale_positivi']}{color.END} Differenza: {color.PURPLE}{int(r_dict['totale_positivi']) - int(old_line['totale_positivi'])}{color.END}")
      print(f"Dimessi guariti: {color.GREEN}{r_dict['dimessi_guariti']}{color.END} Differenza: {color.GREEN}{int(r_dict['dimessi_guariti']) - int(old_line['dimessi_guariti'])}{color.END}")
      print(f"Deceduti: {color.RED}{r_dict['deceduti']}{color.END} Differenza: {color.RED}{int(r_dict['deceduti']) - int(old_line['deceduti'])}{color.END}")
      print(f"Totale casi: {color.RED}{r_dict['totale_casi']}{color.END} Differenza: {color.RED}{int(r_dict['totale_casi']) - int(old_line['totale_casi'])}{color.END}")
      print(f"Tamponi: {color.RED}{r_dict['tamponi']}{color.END} Differenza: {color.RED}{int(r_dict['tamponi']) - int(old_line['tamponi'])}{color.END}")
      print(f"Casi testati: {color.RED}{r_dict['casi_testati']}{color.END} Differenza: {color.RED}{int(r_dict['casi_testati']) - int(old_line['casi_testati'])}{color.END}")
      print(f"Totale positivi test molecolare {color.RED}{r_dict['totale_positivi_test_molecolare']}{color.END} Differenza: {color.RED}{int(r_dict['totale_positivi_test_molecolare']) - int(old_line['totale_positivi_test_molecolare'])}{color.END}")
      print(f"Totale positivi test antigenico rapido: {color.RED}{r_dict['totale_positivi_test_antigenico_rapido']}{color.END} Differenza: {color.RED}{int(r_dict['totale_positivi_test_antigenico_rapido']) - int(old_line['totale_positivi_test_antigenico_rapido'])}{color.END}")
      print(f"Tamponi test molecolare: {color.RED}{r_dict['tamponi_test_molecolare']}{color.END} Differenza: {color.RED}{int(r_dict['tamponi_test_molecolare']) - int(old_line['tamponi_test_molecolare'])}{color.END}")
      print(f"Tamponi test antigenico rapido: {color.RED}{r_dict['tamponi_test_antigenico_rapido']}{color.END} Differenza: {color.RED}{int(r_dict['tamponi_test_antigenico_rapido']) - int(old_line['tamponi_test_antigenico_rapido'])}{color.END}")
      f.close()
