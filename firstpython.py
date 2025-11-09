# corsurea 
!pip install yfinance
!pip install bs4
!pip install nbformat
!pip install --upgrade plotly
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renderers.default = "iframe"

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    from IPython.display import display, HTML
    fig_html = fig.to_html()
    display(HTML(fig_html))


# Question 1: Use yfinance to Extract Stock Data
# Create a ticker object for Tesla (TSLA)
tesla_ticker = yf.Ticker("TSLA")

# Extract stock data
tesla_data = tesla_ticker.history(period="max")

# Display the first few rows of the data
print("Tesla Stock Data - First 5 rows:")
print(tesla_data.head())

print("\nTesla Stock Data - Last 5 rows:")
print(tesla_data.tail())

print(f"\nShape of Tesla data: {tesla_data.shape}")

# Question 1: Use yfinance to Extract Stock Data
# Create a ticker object for Tesla (TSLA)
tesla_ticker = yf.Ticker("TSLA")

# Extract stock information with period set to "max"
tesla_data = tesla_ticker.history(period="max")

# Display information about the extracted data
print("Tesla Stock Data successfully extracted!")
print(f"Data range: {tesla_data.index.min()} to {tesla_data.index.max()}")
print(f"Shape of dataframe: {tesla_data.shape}")
print(f"Columns: {list(tesla_data.columns)}")
print("\nFirst 5 rows:")
print(tesla_data.head())


# Question 1: Use yfinance to Extract Stock Data
# Create a ticker object for Tesla (TSLA)
tesla_ticker = yf.Ticker("TSLA")

# Extract stock information with period set to "max"
tesla_data = tesla_ticker.history(period="max")

# Reset the index using reset_index(inplace=True)
tesla_data.reset_index(inplace=True)

# Display the first five rows of the tesla_data dataframe using the head function
print("Tesla Stock Data - First 5 rows after resetting index:")
tesla_data.head()


import requests

def extract_tesla_revenue():
    # URL de la página web
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

    try:
        # Descargar la página web
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        response.raise_for_status()

        # Guardar el texto de la respuesta en la variable html_data
        html_data = response.text

        print("¡Datos descargados exitosamente!")
        print(f"Longitud del contenido: {len(html_data)} caracteres")
        print(f"Primeros 500 caracteres:\n{html_data[:500]}")

        return html_data

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la página: {e}")
        return None

# Ejecutar la función
html_data = extract_tesla_revenue()

# Verificar que la variable se creó correctamente
if html_data is not None:
    print(f"\nVariable 'html_data' creada exitosamente")
    print(f"Tipo de dato: {type(html_data)}")
else:
    print("No se pudo obtener los datos")


  import requests
from bs4 import BeautifulSoup

# Descargar los datos
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text

# Parsear con BeautifulSoup usando html5lib
soup = BeautifulSoup(html_data, 'html5lib')

# O usando html.parser (elige una de las dos opciones)
# soup = BeautifulSoup(html_data, 'html.parser')

print("Parseo completado!")
print(f"Tipo de objeto: {type(soup)}")

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Descargar y parsear los datos
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
response = requests.get(url)
html_data = response.text
soup = BeautifulSoup(html_data, 'html5lib')

# Crear DataFrame vacío
tesla_revenue = pd.DataFrame(columns=['Date', 'Revenue'])

# Encontrar la tabla relevante (segundo tbody)
table_body = soup.find_all("tbody")[1]

# Iterar a través de las filas y extraer datos
for row in table_body.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) == 2:  # Asegurarse de que hay exactamente 2 columnas
        date = cols[0].get_text(strip=True)
        revenue = cols[1].get_text(strip=True)

        # Crear un nuevo DataFrame temporal y concatenar
        new_row = pd.DataFrame({'Date': [date], 'Revenue': [revenue]})
        tesla_revenue = pd.concat([tesla_revenue, new_row], ignore_index=True)

print("DataFrame creado exitosamente:")
print(tesla_revenue.head())
print(f"\nDimensiones del DataFrame: {tesla_revenue.shape}")

tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True)

tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


import yfinance as yf

# Crear el objeto Ticker para GameStop
GME = yf.Ticker("GME")

print("Objeto Ticker creado exitosamente para GameStop")
print(f"Ticker symbol: {GME.ticker}")
print(f"Nombre de la compañía: {GME.info.get('longName', 'GameStop Corp.')}")
print(f"Tipo de objeto: {type(GME)}")

import yfinance as yf
import pandas as pd

# Crear el objeto Ticker para GameStop
GME = yf.Ticker("GME")

# Extraer datos históricos con período máximo
gme_data = GME.history(period="max")

print("✅ Datos históricos de GameStop extraídos exitosamente")
print(f"Período: máximo disponible")
print(f"Dimensión del DataFrame: {gme_data.shape}")
print(f"Columnas: {list(gme_data.columns)}")

# Restablecer el índice del DataFrame gme_data
gme_data.reset_index(inplace=True)

print("✅ Índice restablecido exitosamente")
print(f"¿Tiene índice numérico ahora?: {gme_data.index.name is None}")
print(f"¿La fecha ahora es una columna?: {'Date' in gme_data.columns}")

import requests

def download_gme_revenue_page():
    # URL de la página web de ingresos de GameStop
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

    try:
        # Descargar la página web
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        response.raise_for_status()

        # Guardar el texto de la respuesta en la variable html_data_2
        html_data_2 = response.text

        print("✅ Página web descargada exitosamente")
        print(f"Longitud del contenido: {len(html_data_2)} caracteres")
        print(f"Tipo de dato: {type(html_data_2)}")
        print(f"Estado de la respuesta: {response.status_code}")

        return html_data_2
         except requests.exceptions.RequestException as e:
        print(f"❌ Error al descargar la página: {e}")
        return None

# Ejecutar la función y guardar en html_data_2
html_data_2 = download_gme_revenue_page()


from bs4 import BeautifulSoup

# Parsear los datos HTML usando BeautifulSoup con html5lib
soup_2 = BeautifulSoup(html_data_2, 'html5lib')

print("✅ HTML parseado exitosamente con html5lib")
print(f"Tipo del objeto soup: {type(soup_2)}")
print(f"Título de la página: {soup_2.title.string if soup_2.title else 'No encontrado'}")


import pandas as pd

# Usar read_html para extraer todas las tablas
tables = pd.read_html(html_data_2)

# La tabla de ingresos trimestrales está en el índice 1
gme_revenue = tables[1]

# Renombrar las columnas
gme_revenue.columns = ['Date', 'Revenue']

# Remover comas y signo de dólar de la columna Revenue
gme_revenue['Revenue'] = gme_revenue['Revenue'].str.replace('$', '').str.replace(',', '')

print("✅ DataFrame gme_revenue creado exitosamente con read_html")
print(gme_revenue.head())

print(gme_revenue.tail())


# Generar la gráfica de datos de Tesla usando la función make_graph
make_graph(tesla_data, tesla_revenue, 'Tesla')

# Generar la gráfica de datos de GameStop usando la función make_graph
make_graph(gme_data, gme_revenue, 'GameStop')




