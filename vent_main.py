# Importa as bibliotecas necessárias para a visualização de dados
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o arquivo CSV para um DataFrame
df = pd.read_csv('../ecommerce_estatistica.csv')

# --- NOVO PASSO: LIMPEZA DOS DADOS ---
# Limpa a coluna 'Qtd_Vendidos' para remover os textos
# Isso é necessário para que a correlação e outros gráficos funcionem
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].astype(str).str.replace('+', '', regex=False)
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].str.replace('mil', '000', regex=False)
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')

# --- 1. Gráfico de Histograma ---
# Analisa a distribuição da coluna 'Preço'
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Preço', bins=30, kde=True, color='skyblue')
plt.title('Distribuição de Preços dos Produtos')
plt.xlabel('Preço (R$)')
plt.ylabel('Frequência')
plt.show()

# --- 2. Gráfico de Dispersão ---
# Analisa a relação entre 'Preço' e 'Qtd_Vendidos'
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Preço', y='Qtd_Vendidos', alpha=0.6, color='darkgreen')
plt.title('Relação entre Preço e Quantidade de Itens Vendidos')
plt.xlabel('Preço (R$)')
plt.ylabel('Quantidade de Itens Vendidos')
plt.show()

# --- 3. Mapa de Calor ---
# Analisa a correlação entre as principais variáveis numéricas
colunas_para_correlacao = ['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos', 'Preço']
correlacao = df[colunas_para_correlacao].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

# --- 4. Gráfico de Barra ---
# Analisa a contagem de produtos por 'Gênero'
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Gênero', hue='Gênero', order=df['Gênero'].value_counts().index, palette='viridis', legend=False)
plt.title('Contagem de Produtos por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Número de Produtos')
plt.show()

# --- 5. Gráfico de Pizza ---
# Analisa a proporção de produtos por 'Gênero'
plt.figure(figsize=(8, 8))
proporcoes_genero = df['Gênero'].value_counts()
plt.pie(proporcoes_genero, labels=proporcoes_genero.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Proporção de Produtos por Gênero')
plt.show()

# --- 6. Gráfico de Densidade ---
# Visualiza a distribuição da 'Nota' de forma contínua
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x='Nota', fill=True, color='orange', alpha=0.7)
plt.title('Gráfico de Densidade da Nota dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Densidade')
plt.show()

# --- 7. Gráfico de Regressão ---
# Mostra a relação e a linha de tendência entre 'Preço' e 'Qtd_Vendidos'
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Preço', y='Qtd_Vendidos', scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title('Relação de Regressão entre Preço e Vendas')
plt.xlabel('Preço (R$)')
plt.ylabel('Quantidade de Itens Vendidos')
plt.show()