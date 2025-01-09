from datetime import datetime
from pandasql import sqldf
import pandas as pd
from classes.Conexao import Conexao

class Consultas:
    def __init__(self, conexao):
        self.eventos = conexao.obter_dataframe(tabela='eventos')
        self.qualidade_do_ar = conexao.obter_dataframe(tabela='qualidade_do_ar')
        tabela = self.eventos
        self.eventos_filtrados = sqldf(f"""
        WITH classif AS (
            SELECT id_evento,
                indice_de_severidade,
                recorrente,
                visibilidade_no_painel_do_fogo,
                area_afetada,
                tipo_de_area,
                localidade,
                ultima_deteccao,
                status,
                quantidade_de_deteccoes,
                persistencia_em_dias,
                data_maxima,
                distancia_das_bases,
                geometry,
                dt_minima,
                dt_insert,
                ROW_NUMBER() OVER (PARTITION BY id_evento ORDER BY ultima_deteccao DESC) AS rn
            FROM tabela
        )
        SELECT id_evento,
            indice_de_severidade,
            recorrente,
            visibilidade_no_painel_do_fogo,
            area_afetada,
            tipo_de_area,
            localidade,
            ultima_deteccao,
            status,
            quantidade_de_deteccoes,
            persistencia_em_dias,
            data_maxima,
            distancia_das_bases,
            geometry,
            dt_minima,
            dt_insert
        FROM classif
        WHERE rn = 1
        ORDER BY ultima_deteccao DESC;
        """)
        
    def getEvento(self):
        return self.eventos
    
    def getEventoFiltrado(self):
        return self.eventos_filtrados
    
    def updateEvento(self, filtro):
        self.eventos_filtrados = filtro
    
    def card1(self):
        data_hoje2 = datetime.now().date().strftime('%Y-%m-%d')
        tabela = self.eventos_filtrados
        sql_query = f"""
        SELECT COUNT(*) AS quantidade_registros
        FROM tabela
        WHERE ultima_deteccao LIKE '{data_hoje2}%';
        """
        return sqldf(sql_query)
    
    def card2(self):
        tabela = self.eventos_filtrados
        sql_query = "SELECT COUNT(*) AS quantidade_registros FROM tabela"
        return sqldf(sql_query)
    
    def card3(self):
        tabela = self.eventos_filtrados
        sql_query = "SELECT SUM(quantidade_de_deteccoes) AS total_deteccoes FROM tabela"
        return sqldf(sql_query)
    
    def card4(self):
        tabela = self.eventos_filtrados
        sql_query = "SELECT AVG(persistencia_em_dias) AS media_persistencia FROM tabela"
        return sqldf(sql_query)
    
    def card5(self):
        tabela = self.eventos_filtrados
        sql_query = "SELECT AVG(indice_de_severidade) AS media_severidade FROM tabela"
        return sqldf(sql_query)
    
    def card6(self):
        tabela = self.eventos_filtrados
        sql_query = """
        SELECT ROUND((SUM(area_afetada)), 2) AS total_area
        FROM tabela
        WHERE status IN ('Extinto', 'Ativo')
        """
        return sqldf(sql_query)
    
    def grafico1(self):
        tabela = self.eventos_filtrados
        sql_query = """
        SELECT tipo_de_area, COUNT(*) AS contagem
        FROM tabela
        GROUP BY tipo_de_area
        ORDER BY contagem ASC
        """
        return sqldf(sql_query)
    
    def grafico2(self):
        tabela = self.eventos_filtrados
        sql_query = """
        WITH TotalEventos AS (
            SELECT COUNT(*) AS total
            FROM tabela
            WHERE status <> 'Nenhuma detecção nas ultimas 24h'
        ),
        StatusContagem AS (
            SELECT status, COUNT(*) AS contagem
            FROM tabela
            WHERE status <> 'Nenhuma detecção nas ultimas 24h'
            GROUP BY status
        )
        SELECT 
            status,
            contagem,
            ROUND((contagem * 100.0 / total), 2) AS percentual
        FROM 
            StatusContagem,
            TotalEventos
        ORDER BY 
            contagem ASC;
        """
        return sqldf(sql_query)
    
    def grafico3(self):
        tabela = self.eventos
        sql_query = """
        SELECT DATE(dt_minima) AS data, COALESCE(MAX(indice_de_severidade), 0) AS indice_severidade_maximo
        FROM tabela
        WHERE strftime('%Y', dt_minima) = '2024'
        GROUP BY DATE(dt_minima)
        ORDER BY data
        """
        return sqldf(sql_query)
    
    def grafico4(self):
        tabela = self.eventos_filtrados
        sql_query = """
        SELECT
            CASE
                WHEN recorrente = 'Sim' THEN 'Recorrente'
                WHEN recorrente = 'Não' THEN 'Não recorrente'
                ELSE 'Desconhecido'
            END AS recorrente,
            COUNT(*) AS total
        FROM
            tabela
        GROUP BY
            CASE
                WHEN recorrente = 'Sim' THEN 'Recorrente'
                WHEN recorrente = 'Não' THEN 'Não recorrente'
                ELSE 'Desconhecido'
            END
        """
        return sqldf(sql_query)
    
    def grafico5(self):
        tabela = self.eventos_filtrados
        sql_query = """
        SELECT DATE(dt_minima) AS data, COUNT(*) AS quantidade_eventos
        FROM tabela
        WHERE strftime('%Y', dt_minima) = '2024'
        GROUP BY DATE(dt_minima)
        ORDER BY data
        """
        return sqldf(sql_query)
    
    def grafico6(self):
        tabela = self.eventos_filtrados
        sql_query = """
        SELECT id_evento AS ID,
            ROUND(indice_de_severidade, 2) AS 'Índice de severidade',
            recorrente AS 'Recorrente',
            ROUND(area_afetada, 2) AS 'Área afetada (km²)',
            tipo_de_area AS 'Tipo de área',
            localidade AS 'Localidade',
            strftime('%d/%m/%Y', ultima_deteccao) AS 'Ultima detecção',
            status AS 'Status',
            quantidade_de_deteccoes AS 'Qtd detecções',
            persistencia_em_dias AS 'Persistência(dias)',
            strftime('%d/%m/%Y', data_maxima) AS 'Data máxima',
            strftime('%d/%m/%Y', dt_minima) AS 'Data mínima'
        FROM tabela
        ORDER BY dt_minima DESC
        """
        return sqldf(sql_query)
    
    def grafico7(self):
        tabela = self.eventos_filtrados
        sql_query = """
        SELECT DATE(dt_minima) AS data, SUM(area_afetada) AS soma_area
        FROM tabela
        WHERE strftime('%Y', dt_minima) = '2024'
        GROUP BY DATE(dt_minima)
        ORDER BY data
        """
        return sqldf(sql_query)
    
    def grafico8(self):
        tabela = self.qualidade_do_ar
        sql_query = """
        SELECT 
            DATE(Date) AS data, 
            COALESCE(MAX(pm25), 0) AS pm25
        FROM tabela
        WHERE City = 'Porto Velho'
        GROUP BY DATE(Date)
        ORDER BY DATE(Date) DESC;
        """
        return sqldf(sql_query)
    
    def grafico9(self):
        tabela = self.qualidade_do_ar
        sql_query = """
        SELECT 
            DATE(Date) AS data, 
            COALESCE(MAX(pm10), 0) AS pm10
        FROM tabela
        WHERE City = 'Porto Velho'
        GROUP BY DATE(Date)
        ORDER BY DATE(Date) DESC;
        """
        return sqldf(sql_query)