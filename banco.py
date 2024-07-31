import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo CSV
caminho_arquivo = 'C:/Users/Davi Cruz/Desktop/meteorologiaaplicada/POWER_Point_Daily_19930101_20240730_005d64S_035d42W_LST.csv'

# Ler uma amostra menor dos dados
df = pd.read_csv(caminho_arquivo, skiprows=13, nrows=11400)

# Adicionar coluna de data
df['Data'] = pd.to_datetime(df['YEAR'].astype(str) + df['DOY'].astype(str).str.zfill(3), format='%Y%j')

# Verificar se há dados ausentes e removê-los
df = df.dropna()

# Calcular a média, o valor máximo e o valor mínimo de cada variável, excluindo a coluna 'Data'
media_variaveis = df.drop(columns=['Data']).mean()
max_variaveis = df.drop(columns=['Data']).max()
min_variaveis = df.drop(columns=['Data']).min()

# Exibir a média de cada variável
print("\nMédias das variáveis ao longo do período:")
print(media_variaveis)

# Função para calcular média móvel
def calcular_media_movel(series, janela=30):
    return series.rolling(window=janela).mean()

# Função para criar gráfico de dispersão com média móvel
def criar_grafico_dispercao_media(coluna, cor, titulo, xlabel, ylabel):
    plt.figure(figsize=(14, 8))
    plt.scatter(df['Data'], df[coluna], color=cor, s=5, label=f'{ylabel}')
    media_movel = calcular_media_movel(df[coluna])
    plt.plot(df['Data'], media_movel, color=cor, linewidth=2, label='Média Móvel (30 dias)')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()

# Gráficos de dispersão com média móvel
criar_grafico_dispercao_media('T2M', 'b', 'Temperatura ao longo do tempo', 'Data', 'Temperatura (°C)')
criar_grafico_dispercao_media('QV2M', 'g', 'Umidade Específica ao longo do tempo', 'Data', 'Umidade Específica (g/kg)')
criar_grafico_dispercao_media('PS', 'r', 'Pressão ao longo do tempo', 'Data', 'Pressão (kPa)')
criar_grafico_dispercao_media('WS2M_MAX', 'c', 'Velocidade do Vento Máxima ao longo do tempo', 'Data', 'Velocidade do Vento Máxima (m/s)')
criar_grafico_dispercao_media('ALLSKY_SFC_PAR_TOT', 'm', 'Radiação ao longo do tempo', 'Data', 'Radiação (W/m^2)')

# Função para criar histogramas com linha de média, máximo e mínimo e adicionar frequências
def criar_histograma(coluna, cor, titulo, xlabel, ylabel):
    plt.figure(figsize=(14, 8))
    
    # Calcular o histograma
    conteudo, bordas, patches = plt.hist(df[coluna], bins=50, color=cor, edgecolor='black', alpha=0.7)
    
    # Calcular a média, o máximo e o mínimo
    media = media_variaveis[coluna]
    maximo = max_variaveis[coluna]
    minimo = min_variaveis[coluna]
    
    # Adicionar linhas verticais para média, máximo e mínimo
    plt.axvline(media, color='red', linestyle='dashed', linewidth=1, label=f'Média = {media:.2f}')
    plt.axvline(maximo, color='green', linestyle='dashed', linewidth=1, label=f'Máximo = {maximo:.2f}')
    plt.axvline(minimo, color='blue', linestyle='dashed', linewidth=1, label=f'Mínimo = {minimo:.2f}')
    
    # Calcular a média, máximo e mínimo das frequências
    media_frequencia = conteudo.mean()
    max_frequencia = conteudo.max()
    min_frequencia = conteudo.min()
    
    # Adicionar linhas horizontais para média, máximo e mínimo de frequências
    plt.axhline(media_frequencia, color='orange', linestyle='dashed', linewidth=1, label=f'Média da Frequência = {media_frequencia:.2f}')
    plt.axhline(max_frequencia, color='purple', linestyle='dashed', linewidth=1, label=f'Máximo da Frequência = {max_frequencia:.2f}')
    plt.axhline(min_frequencia, color='pink', linestyle='dashed', linewidth=1, label=f'Mínimo da Frequência = {min_frequencia:.2f}')
    
    # Ajustar o título e rótulos
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()

# Criar histogramas para cada variável com linha de média, máximo e mínimo
criar_histograma('T2M', 'b', 'Distribuição da Temperatura (T2M)', 'Temperatura (°C)', 'Frequência')
criar_histograma('QV2M', 'g', 'Distribuição da Umidade Específica (QV2M)', 'Umidade Específica (g/kg)', 'Frequência')
criar_histograma('PS', 'r', 'Distribuição da Pressão (PS)', 'Pressão (kPa)', 'Frequência')
criar_histograma('WS2M_MAX', 'c', 'Distribuição da Velocidade do Vento Máxima (WS2M_MAX)', 'Velocidade do Vento Máxima (m/s)', 'Frequência')
criar_histograma('ALLSKY_SFC_PAR_TOT', 'm', 'Distribuição da Radiação (ALLSKY_SFC_PAR_TOT)', 'Radiação (W/m^2)', 'Frequência')
