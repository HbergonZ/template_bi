import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

class Grafico:
    def __init__(self, id, title, data_frame):
        self.id = id
        self.title = title
        self.data_frame = data_frame
        
        
class GraficoBarra(Grafico):
    def __init__(self, sm=6, data_frame=None, x=None, y=None, color=None, pattern_shape=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=0.5, hover_name=None, hover_data=None, custom_data=None, text=None, base=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, pattern_shape_sequence=None, pattern_shape_map=None, range_color=None, color_continuous_midpoint=None, opacity=None, orientation=None, barmode='relative', log_x=False, log_y=False, range_x=None, range_y=None, text_auto=False, title=None, template=None, width=None, height=None, exibir_eixo_x=True, texttemplate=None):
        super().__init__(id, title, data_frame)
        self.x = x
        self.y = y

    def get_elemento(self):
        fig = px.bar(self.data_frame, x=self.x, y=self.y, title=self.title)
        return dcc.Graph(id=self.id, figure=fig)  
    
class GraficoLinha(Grafico):
    def __init__(self, id, title, data_frame, x, y):
        super().__init__(id, title, data_frame)
        self.x = x
        self.y = y

    def get_elemento(self):
        fig = px.line(self.data_frame, x=self.x, y=self.y, title=self.title)
        return dcc.Graph(id=self.id, figure=fig)
    
class GraficoPizza(Grafico):
    def __init__(self, id, sm=6, data_frame=None, names=None, values=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, color_discrete_sequence=None, color_discrete_map=None, hover_name=None, hover_data=None, custom_data=None, category_orders=None, labels=None, title=None, template=None, width=None, height=None, opacity=None, hole=None):
        super().__init__(id, title, data_frame)
        self.names = names
        self.values = values 
    
    def get_elemento(self):
        fig = px.line(self.data_frame, x=self.x, y=self.y, title=self.title)
        return dcc.Graph(id=self.id, figure=fig)
    
    def atualizar_elemento(self):
        ...
        
class Tabela(Grafico):
    def __init__(self, id, title, data_frame, x, y):
        super().__init__(id, title, data_frame)
        self.x = x
        self.y = y

    def get_elemento(self):
        fig = px.line(self.data_frame, x=self.x, y=self.y, title=self.title)
        return dcc.Graph(id=self.id, figure=fig)
    
    def atualizar_elemento(self):
        ...
        
class Mapa(Grafico):
    def __init__(self, id, title, data_frame, x, y):
        super().__init__(id, title, data_frame)
        self.x = x
        self.y = y

    def get_elemento(self):
        fig = px.line(self.data_frame, x=self.x, y=self.y, title=self.title)
        return dcc.Graph(id=self.id, figure=fig)
    
    def atualizar_elemento(self):
        ...

class Card(Grafico):
    def __init__(self, id, title, data_frame, x, y):
        super().__init__(id, title, data_frame)
        self.x = x
        self.y = y

    def get_elemento(self):
        fig = px.line(self.data_frame, x=self.x, y=self.y, title=self.title)
        return dcc.Graph(id=self.id, figure=fig)
    
    def atualizar_elemento(self):
        ...

class Imagem(Grafico):
    def __init__(self, local, title=None, data_frame=None, x=None, y=None):
        super().__init__(id, title, data_frame)
        self.x = x
        self.y = y

    def get_elemento(self):
        fig = px.line(self.data_frame, x=self.x, y=self.y, title=self.title)
        return dcc.Graph(id=self.id, figure=fig)
    
    def atualizar_elemento(self):
        ...