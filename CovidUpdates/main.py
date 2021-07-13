import requests


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

r = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json')

r_dict = r.json()

r_dict = {k:v for element in r_dict for k,v in element.items()}

print(f"Data: {r_dict['data']}")
print(f"Ricoverati con sintomi: {r_dict['ricoverati_con_sintomi']}")
print(f"Terapia intensiva: {r_dict['terapia_intensiva']}")
print(f"Isolamento domiciliare: {r_dict['isolamento_domiciliare']}")
print(f"Totale positivi: {r_dict['totale_positivi']}")
print(f"Variazione totale positivi: {r_dict['variazione_totale_positivi']}")
print(f"Nuovi positivi: {r_dict['nuovi_positivi']}")
print(f"Dimessi guariti: {color.GREEN + color.UNDERLINE}{r_dict['dimessi_guariti']}{color.END}")
print(f"Deceduti: {color.PURPLE}{r_dict['deceduti']}{color.END}")
print(f"Totale casi: {r_dict['totale_casi']}")
print(f"Tamponi: {r_dict['tamponi']}")
print(f"Casi testati: {r_dict['casi_testati']}")
print(f"Totale positivi test molecolare{r_dict['totale_positivi_test_molecolare']}")
print(f"Totale positivi test antigenico rapido: {r_dict['totale_positivi_test_antigenico_rapido']}")
print(f"Tamponi test molecolare: {r_dict['tamponi_test_molecolare']}")
print(f"Tamponi test antigenico rapido: {r_dict['tamponi_test_antigenico_rapido']}")
