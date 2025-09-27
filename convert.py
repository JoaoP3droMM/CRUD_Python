import glob
import pandas as pd
import sqlite3

# Nomes das colunas da tabela existente no SQLite
colunas = ['cnpj_basico', 'identificador_socio', 'razao_social', 'cnpj', 'qualificacao_socio', 'data_entrada_sociedade', 'pais', 'representante_legal_cpf', 'representante_legal_nome', 'representante_legal_qualificacao', 'faixa_etaria']

csv_files = glob.glob('*.SOCIOCSV')
conn = sqlite3.connect('banco.db')

for file in csv_files:
    chunk_iter = pd.read_csv(file, delimiter=';', quotechar='"', encoding='latin1', header=None, chunksize=1000000)
    for chunk in chunk_iter:
        chunk.columns = colunas  # define nomes iguais ao da tabela
        chunk.to_sql('socio', conn, if_exists='append', index=False)
        print(f'Importado chunk do arquivo {file}')

conn.close()
print("Importação finalizada")
