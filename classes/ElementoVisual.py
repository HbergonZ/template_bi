import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, date
class ElementoVisual:
    def __init__(self, id):
        self.elemento = dbc.Col(id=id)
        self.id = id

    def add_card(self, titulo="Título", descricao="Descrição"):
        self.elemento = dbc.Card(
                    [
                        dbc.CardBody(
                            [   
                                html.H4(titulo, className="card-title"),
                                html.P(descricao, className="card-text", style={"font-size": "0.8rem", "color": "black"}),
                            ]
                        )
                    ],
                    style={"text-align": "center", "margin": "5px"}
                )
    
    def add_imagem(self):
        self.elemento =dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                 html.Img(src='/assets/qualidade_ar.png', style={"width":"700px", "height":"495px"})
                            ]
                        )
                    ],
                    style={"text-align": "center", "margin": "5px"},
                )
    
    def add_filtro_datas(self):
        
        data_hoje = datetime.now().date()
        self.elemento = html.Div(
            dcc.DatePickerRange(
                id='data-range',
                display_format='DD/MM/YYYY',
                min_date_allowed=date(2024, 1, 1),
                max_date_allowed=data_hoje,
                start_date=date(2024, 1, 1),
                end_date=data_hoje,
                calendar_orientation='vertical',
            ), className="mt-3", style={"text-align": "left", "margin": "5px"}

        )
    
    def add_filtro_status(self):
        
        self.elemento = html.Div(
            dcc.Dropdown(
                [
                    'Extinto', 
                    'Não Determinado',
                    'Nenhuma detecção nas ultimas 24h',
                    'Ativo'
                 ],
                placeholder="Selecione um status",
                id='status-input', 
                ), 
            className="mt-3 w-25", 
            style={"text-align": "center", "margin": "5px"}
        )
        
    
    def add_mapa(self):
        self.elemento = dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                html.H5("Focos únicos de incêndio ao longo do ano", className="card-title", style={'textAlign': 'left'}),
                                html.Iframe(src='/assets/output.html', style={'height': '600px', 'width': '100%'})
                            ],style={'width': '100%'}
                        )
                    ],
                   style={"text-align": "center", "margin": "5px"}
                )
    
    def get_elemento(self):
        return self.elemento