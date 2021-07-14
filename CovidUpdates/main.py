import requests
import datetime
import re

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

if first_line[18:20] != today:
   with open('old_data.txt', 'r+') as fi:
      old_line = fi.readline()
      fi.seek(0)
      fi.write(re.sub(r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", first_line))
      fi.truncate()
      fi.close()

   print(f"Data: {r_dict['data']}")
   print(f"Ricoverati con sintomi: {r_dict['ricoverati_con_sintomi']} Differenza: Nessun aggiornamento")
   print(f"Terapia intensiva: {r_dict['terapia_intensiva']} Differenza: Nessun aggiornamento")
   print(f"Isolamento domiciliare: {r_dict['isolamento_domiciliare']} Differenza: Nessun aggiornamento")
   print(f"Totale positivi: {r_dict['totale_positivi']} Differenza: Nessun aggiornamento")
   print(f"Dimessi guariti: {color.GREEN + color.UNDERLINE}{r_dict['dimessi_guariti']}{color.END} Differenza: Nessun aggiornamento")
   print(f"Deceduti: {color.PURPLE}{r_dict['deceduti']}{color.END} Differenza: Nessun aggiornamento")
   print(f"Totale casi: {r_dict['totale_casi']} Differenza: Nessun aggiornamento")
   print(f"Tamponi: {r_dict['tamponi']} Differenza: Nessun aggiornamento")
   print(f"Casi testati: {r_dict['casi_testati']} Differenza: Nessun aggiornamento")
   print(f"Totale positivi test molecolare{r_dict['totale_positivi_test_molecolare']} Differenza: Nessun aggiornamento")
   print(f"Totale positivi test antigenico rapido: {r_dict['totale_positivi_test_antigenico_rapido']} Differenza: Nessun aggiornamento")
   print(f"Tamponi test molecolare: {r_dict['tamponi_test_molecolare']} Differenza: Nessun aggiornamento")
   print(f"Tamponi test antigenico rapido: {r_dict['tamponi_test_antigenico_rapido']} Differenza: Nessun aggiornamento")

elif first_line[18:20] == today:
   with open('new_data.txt', 'r+') as f:
      f.seek(0)
      f.write(re.sub(r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", first_line))
      f.truncate()
      f.close()
   
   with open('old_data.txt', 'r+') as fi:
      old_line = fi.readline()

   print(f"Data: {r_dict['data']}")
   print(f"Ricoverati con sintomi: {r_dict['ricoverati_con_sintomi']} Differenza: {int(r_dict['ricoverati_con_sintomi']) - int(old_line[74:78])}")
   print(f"Terapia intensiva: {r_dict['terapia_intensiva']} Differenza: {int(r_dict['terapia_intensiva']) - int(old_line[101:104])}")
   print(f"Isolamento domiciliare: {r_dict['isolamento_domiciliare']} Differenza: {int(r_dict['isolamento_domiciliare']) - int(old_line[162:166])}")
   print(f"Totale positivi: {r_dict['totale_positivi']} Differenza: {int(r_dict['totale_positivi']) - int(old_line[188:193])}")
   print(f"Dimessi guariti: {color.GREEN + color.UNDERLINE}{r_dict['dimessi_guariti']}{color.END} Differenza: {int(r_dict['dimessi_guariti']) - int(old_line[273:280])}")
   print(f"Deceduti: {color.PURPLE}{r_dict['deceduti']}{color.END} Differenza: {int(r_dict['deceduti']) - int(old_line[294:300])}")
   print(f"Totale casi: {r_dict['totale_casi']} Differenza: {int(r_dict['totale_casi']) - int(old_line[378:385])}")
   print(f"Tamponi: {r_dict['tamponi']} Differenza: {int(r_dict['tamponi']) - int(old_line[398:406])}")
   print(f"Casi testati: {r_dict['casi_testati']} Differenza: {int(r_dict['casi_testati']) - int(old_line[424:432])}")
   print(f"Totale positivi test molecolare {r_dict['totale_positivi_test_molecolare']} Differenza: {int(r_dict['totale_positivi_test_molecolare']) - int(old_line[548:555])}")
   print(f"Totale positivi test antigenico rapido: {r_dict['totale_positivi_test_antigenico_rapido']} Differenza: {int(r_dict['totale_positivi_test_antigenico_rapido']) - int(old_line[599:605])}")
   print(f"Tamponi test molecolare: {r_dict['tamponi_test_molecolare']} Differenza: {int(r_dict['tamponi_test_molecolare']) - int(old_line[634:642])}")
   print(f"Tamponi test antigenico rapido: {r_dict['tamponi_test_antigenico_rapido']} Differenza: {int(r_dict['tamponi_test_antigenico_rapido']) - int(old_line[678:686])}")
