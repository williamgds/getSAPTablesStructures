import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

def scrape_table(table_name):
    url = "https://leanx.eu/en/sap/table/"
    table = f"{table_name}.html"
    web_text = requests.get(url + table)

    bs = soup(web_text.content, "html.parser")

    # Encuentra la tabla de interés utilizando atributos específicos si es posible
    target_table = bs.select('[class*="table-responsive"]')

    # Verifica si se encontró la tabla
    if target_table:
        # Utiliza Pandas para convertir los datos en una tabla
        df = pd.read_html(str(target_table[0]))[0]

        # Retorna el DataFrame de Pandas
        return df
    else:
        print(f"No se encontró la tabla {table_name}.")
        return None

# Lista de nombres de tablas a extraer
tables_to_scrape = ["AFVC", "AUFK", "CDHDR", "CDPOS", "JCDS", "QMEL"]

# Itera sobre la lista de nombres de tablas y realiza el web scraping
for table_name in tables_to_scrape:
    scraped_data = scrape_table(table_name)
    if scraped_data is not None:
        print(f"Datos de la tabla {table_name}:")
        scraped_data.to_excel(f'{table_name}.xlsx')
