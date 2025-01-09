import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from PIL import Image

class Modelo1:
    def __init__(self):
        # ===========  Valores padrões  ========== #
        self.titulo_card = "Título do Card"
        self.descricao_card = "Descrição do Card"
        
        # ==============  Layout  ============== #
        self.pil_image = Image.open('./img/logo-setic.png') 
    
    def create_layout(self, row_manager, borda="off"):
        rows = [linha.to_row(borda = borda) for linha in row_manager]
        if any(row.children for row in rows):
            cards_row = dbc.Row(rows, style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'center'})
        else:
            cards_row = dbc.Row([
                                    dbc.Col(html.Div(id='cards-container'), style={'height': '81.8vh'})
                                ])
        
        layout = dbc.Container(
            [
                
            # Coluna 2 - Demais elementos
                html.Div([   
                        
                    # Linha de cabeçalho
                    html.Div([
                        html.Div(
                            html.Div(
                                html.Div("Painel Sentinela e Qualidade do ar", style={"font-family": "Candara", "font-size": "35px", "font-weight": "bold", "display": "inline-block"})
                            ),
                            style={"background-color": "#D9D9D9"}, className="d-flex align-items-center"
                        ),
                                
                        html.Div(
                            html.Div(
                                html.Img(src=self.pil_image, style={'height': '8vh', "margin": "10px", "padding": "0", "display": "inline-block", "margin-left": "auto", "float": "right"})
                            ), style={"background-color": "#D9D9D9"}
                        )
                    ],id="cabecalho", className="d-flex justify-content-between"),
                    
                    # Linha dos Cards
                    cards_row,
                    
                    # Rodapé
                    dbc.Row(html.Div("2024 - Governo do Estado de Rondônia | Fonte: Painel do Fogo e aqicn.org"), style={"background-color":"#D9D9D9","height":"8vh"}, className="d-flex align-items-center")
                ])
            ], fluid=True, style={"background-color":"#F0F0F0"}
        )
        
        return layout
