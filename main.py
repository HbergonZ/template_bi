from pandasql import sqldf
from flask import Flask, render_template
from datetime import datetime, date
import dash
import dash_bootstrap_components as dbc
from classes.Modelo import Modelo1
from classes.Row import Row
from classes.ComponenteGrafico import ComponenteGrafico
from classes.ElementoVisual import ElementoVisual
from classes.Conexao import Conexao
from classes.Consultas import Consultas
from dash.dependencies import Input, Output, State

server = Flask(__name__)

conexao = Conexao()

# Criando modelo do dashboard a partir de um template definido
dashboard = Modelo1()


# Criando as linhas dentro do espaço
filtros = Row(ehFiltro=True)

linha1 = Row()
linha2 = Row()
linha3 = Row()
linha4 = Row()
linha5 = Row()
linha6 = Row()
linha7 = Row()
linha8 = Row()
linha9 = Row()
linha10 = Row()

# Definindo Conexões
# df_eventos = conexao.obter_dataframe('eventos')
# df_qualidade_do_ar = conexao.obter_dataframe('qualidade_do_ar')
consultas = Consultas(conexao)

# Criando elementos das linhas
filtroData = ElementoVisual(id="filtroData")
filtroStatus = ElementoVisual(id="filtroStatus")

card1 = ElementoVisual(id="card1")
card2 = ElementoVisual(id="card2")
card3 = ElementoVisual(id="card3")
card4 = ElementoVisual(id="card4")
card5 = ElementoVisual(id="card5")
card6 = ElementoVisual(id="card6")
grafico1 = ComponenteGrafico(id="grafico1")
grafico2 = ComponenteGrafico(id="grafico2")
grafico3 = ComponenteGrafico(id="grafico3")
grafico4 = ComponenteGrafico(id="grafico4")
grafico5 = ComponenteGrafico(id="grafico5")
grafico6 = ComponenteGrafico(id="grafico6")
grafico7 = ComponenteGrafico(id="grafico7")
grafico8 = ComponenteGrafico(id="grafico8")
grafico9 = ComponenteGrafico(id="grafico9")
imagem1 = ElementoVisual(id="imagem1")
mapa1 = ElementoVisual(id="mapa")




filtroData.add_filtro_datas()
filtroStatus.add_filtro_status()

# Atribuir Gráficos nas linhas
filtros.add_elementos([filtroData.get_elemento(), filtroStatus.get_elemento()])

linha1.add_elementos([card1.get_elemento(), card2.get_elemento()])
linha2.add_elementos([card4.get_elemento(), card5.get_elemento(), card6.get_elemento()])
linha3.add_elementos([grafico1.get_elemento(), grafico2.get_elemento()])
linha4.add_elementos([grafico3.get_elemento()])
linha5.add_elementos([grafico4.get_elemento(), grafico5.get_elemento()])
linha6.add_elementos([grafico7.get_elemento()])
linha7.add_elementos([grafico6.get_elemento()])
linha8.add_elementos([imagem1.get_elemento(), grafico8.get_elemento()])
linha9.add_elementos([grafico9.get_elemento()])
linha10.add_elementos([mapa1.get_elemento()])


# Armazenando as linhas em uma lista
linhas = [filtros, linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10]

# Inicializa o app Dash
app = dash.Dash(server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do aplicativo
app.layout = dashboard.create_layout(linhas, borda="off")

@app.callback(
    [
        Output('card1', 'children'),
        Output('card2', 'children'),
        Output('card4', 'children'),
        Output('card5', 'children'),
        Output('card6', 'children'),
        Output('grafico1', 'children'),
        Output('grafico2', 'children'),
        Output('grafico3', 'children'),
        Output('grafico4', 'children'),
        Output('grafico5', 'children'),
        Output('grafico6', 'children'),
        Output('grafico7', 'children'),
        Output('grafico8', 'children'),
        Output('grafico9', 'children'),
        Output('imagem1', 'children'),
        Output('mapa', 'children'),
    ],
    [
        Input('data-range', 'start_date'),
        Input('data-range', 'end_date'),
        Input('status-input', 'value')
    ],
)
def aplicar_filtros(start_date, end_date, valor):
    
    df_eventos = consultas.getEvento()
    
    if valor:
        df_eventos = df_eventos[df_eventos['status'] == valor]
        consultas.updateEvento(df_eventos)
        
    else:
        df_eventos = consultas.getEvento()
    
    df_eventos_hoje = df_eventos
    
    df_eventos = df_eventos[
        (df_eventos['dt_minima'] >= start_date) & 
        (df_eventos['ultima_deteccao'] <= end_date)
    ]
    

    data_hoje2 = datetime.now().date().strftime('%Y-%m-%d')

    # Consultas SQL
    card1_valor = consultas.card1()
    card2_valor = consultas.card2()
    card3_valor = consultas.card3()
    card4_valor = consultas.card4()
    card5_valor = consultas.card5()
    card6_valor = consultas.card6()
    grafico1_table = consultas.grafico1()
    grafico2_table = consultas.grafico2()
    grafico3_table = consultas.grafico3()
    grafico4_table = consultas.grafico4()
    grafico5_table = consultas.grafico5()
    grafico6_table = consultas.grafico6()
    grafico7_table = consultas.grafico7()
    grafico8_table = consultas.grafico8()
    grafico9_table = consultas.grafico9()


    # Atualizar os componentes
    card1.add_card(titulo=card1_valor['quantidade_registros'].sum(), descricao="Registros hoje - Sentinela")
    card2.add_card(titulo=card2_valor['quantidade_registros'].sum(), descricao="Registros totais (Janeiro/2024 - Setembro/2024) - Sentinela")
    # card3.add_card(titulo=card3_valor['total_deteccoes'].values[0], descricao="Detecções totais - Sentinela")
    card4.add_card(titulo=f'{card4_valor["media_persistencia"].values[0]:.2f}', descricao="Persistência média em dias - Sentinela")
    card5.add_card(titulo=f'{card5_valor["media_severidade"].values[0]:.2f}', descricao="Índice de severidade médio - Sentinela")
    card6.add_card(titulo=card6_valor['total_area'].values[0], descricao="Área total afetada (km²) - Sentinela")

    grafico1.add_grafico_barra(title="Quantidade de queimadas por tipo de área", data_frame=grafico1_table, orientation="h", y='tipo_de_area', x='contagem', text_auto=True)
    grafico2.add_grafico_barra(title="Percentual de queimadas por status", data_frame=grafico2_table, orientation="h", y='status', x='percentual', text_auto=True, text='contagem', labels={'status': 'Status', 'percentual': 'Percentual', 'contagem': 'Contagem'}, exibir_eixo_x=False, texttemplate='%{x:.2f}%')
    grafico3.add_grafico_linha(title="Índice de severidade ao longo do ano", data_frame=grafico3_table, y='indice_severidade_maximo', x='data')
    grafico4.add_grafico_pizza(sm=4, title="Recorrência dos registros", data_frame=grafico4_table, values='total', names='recorrente')
    grafico5.add_grafico_barra(sm=8, title="Variação do número de eventos ao longo do ano", data_frame=grafico5_table, y='quantidade_eventos', x='data')
    grafico6.add_tabela(sm=12, data_frame=grafico6_table, title="Registros de queimada")
    grafico7.add_grafico_linha(sm=12, title="Variação de áreas afetadas por dia", data_frame=grafico7_table, y='soma_area', x='data')
    grafico8.add_grafico_linha(sm=6, markers=True, title="Número máximo de partículas pm25 por dia em Porto Velho", data_frame=grafico8_table, y='pm25', x='data', text="pm25")
    grafico9.add_grafico_linha(sm=6, markers=True, title="Número máximo de partículas pm10 por dia em Porto Velho", data_frame=grafico9_table, y='pm10', x='data', text="pm10")
    
    imagem1.add_imagem()
    mapa1.add_mapa()


    # Retornar elementos atualizados
    return (
        card1.get_elemento(),
        card2.get_elemento(),
        # card3.get_elemento(),
        card4.get_elemento(),
        card5.get_elemento(),
        card6.get_elemento(),
        grafico1.get_elemento(),
        grafico2.get_elemento(),
        grafico3.get_elemento(),
        grafico4.get_elemento(),
        grafico5.get_elemento(),
        grafico6.get_elemento(),
        grafico7.get_elemento(),
        grafico8.get_elemento(),
        grafico9.get_elemento(),
        imagem1.get_elemento(),
        mapa1.get_elemento()
    )


if __name__ == '__main__':
    app.run_server(debug=True)
