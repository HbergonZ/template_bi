from pandasql import sqldf
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
import pandas as pd

class Conexao:
    def __init__(self):
        # ===========  Valores padrões  ========== #
        self.server = "172.16.1.16"
        self.database = "SentinelaDoFogoReports"
        self.uid = "airflow"
        self.password = "a83db15f15cec64cda21ae53c7b4608c6ebba7df"
        
        # ==============  Layout  ============== #
        from PIL import Image
        self.pil_image = Image.open('./img/logo-setic.png')

    def conectar(self, server=None, database=None, username=None, password=None):
        server = server or self.server
        database = database or self.database
        username = username or self.uid
        password = password or self.password

        conn_str = (
            f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=YES'
        )

        try:
            # Criação do engine SQLAlchemy
            engine = create_engine(conn_str)
            # print ('Conetado!')
            return engine
        except SQLAlchemyError as e:
            print(f'Falha na conexão: {e}')
            return None

    def obter_dataframe(self, tabela, campo_filtro=None, valores_filtro=None):
        engine = self.conectar()

        if engine is None:
            print("Não foi possível conectar ao banco de dados.")
            return None
        
        try:
            df = pd.read_sql_table(tabela, con=engine)
            
            if campo_filtro and valores_filtro:
                if isinstance(valores_filtro, list):
                    df = df[df[campo_filtro].isin(valores_filtro)]
                else:
                    df = df[df[campo_filtro] == valores_filtro]
                
            return df
        except Exception as e:
            print(f'Erro ao ler a tabela: {e}')
            return None
