import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

class ComponenteGrafico:
    def __init__(self, id):
        self.elemento = dbc.Col(id=id)
        self.id = id
        self.fig = None
        self.data_frame = None
        

        
    def add_grafico_barra(self, sm=6, data_frame=None, x=None, y=None, color=None, pattern_shape=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=0.5, hover_name=None, hover_data=None, custom_data=None, text=None, base=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, pattern_shape_sequence=None, pattern_shape_map=None, range_color=None, color_continuous_midpoint=None, opacity=None, orientation=None, barmode='relative', log_x=False, log_y=False, range_x=None, range_y=None, text_auto=False, title=None, template=None, width=None, height=None, exibir_eixo_x=True, texttemplate=None):
        # Preparar os dados e o gráfico
        self.xaxis = x
        self.yaxis = y
        self.data_frame = data_frame
        self.fig = px.bar(data_frame=data_frame, x=x, y=y, orientation=orientation, color=color, pattern_shape=pattern_shape, facet_row=facet_row, facet_col=facet_col, facet_col_wrap=facet_col_wrap, facet_row_spacing=facet_row_spacing, facet_col_spacing=facet_col_spacing, hover_name=hover_name, hover_data=hover_data, custom_data=custom_data, text=text, base=base, error_x=error_x, error_x_minus=error_x_minus, error_y=error_y, error_y_minus=error_y_minus, animation_frame=animation_frame, animation_group=animation_group, category_orders=category_orders, labels=labels, color_discrete_sequence=color_discrete_sequence, color_discrete_map=color_discrete_map, color_continuous_scale=color_continuous_scale, pattern_shape_sequence=pattern_shape_sequence, pattern_shape_map=pattern_shape_map, range_color=range_color, color_continuous_midpoint=color_continuous_midpoint, opacity=opacity, barmode=barmode, log_x=log_x, log_y=log_y, range_x=range_x, range_y=range_y, text_auto=text_auto, template=template, width=width, height=height)

        

        # Adicionar o gráfico como um elemento
        self.elemento = dbc.Card(
                    [
                        html.H5(title, className="card-title", style={'textAlign': 'left', 'margin': '10px'}),
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=self.fig)
                            ]
                        )
                    ], style={"text-align": "center", "margin": "5px"})
        
        self.fig.update_xaxes(showticklabels=exibir_eixo_x)
        
        # Configurar o texto com símbolo de porcentagem
        if texttemplate != None:
            self.fig.update_traces(texttemplate=texttemplate, textposition='inside')
        
        self.fig.update_layout(margin=go.layout.Margin(
            b=0,
            l=0,
            r=0,
            t=25,
            ),
            xaxis_title='',  # Título do eixo x
            yaxis_title='',  # Título do eixo y
        )
        
    def add_grafico_linha(self, sm=12, data_frame=None, x=None, y=None, line_group=None, color=None, line_dash=None, symbol=None, hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, color_discrete_sequence=None, color_discrete_map=None, line_dash_sequence=None, line_dash_map=None, symbol_sequence=None, symbol_map=None, markers=False, log_x=False, log_y=False, range_x=None, range_y=None, line_shape=None, render_mode='auto', title=None, template=None, width=None, height=None):
        
        fig = px.line(data_frame=data_frame, x=x, y=y, line_group=line_group, color=color, line_dash=line_dash, symbol=symbol, hover_name=hover_name, hover_data=hover_data, custom_data=custom_data, text=text, facet_row=facet_row, facet_col=facet_col, facet_col_wrap=facet_col_wrap, facet_row_spacing=facet_row_spacing, facet_col_spacing=facet_col_spacing, error_x=error_x, error_x_minus=error_x_minus, error_y=error_y, error_y_minus=error_y_minus, animation_frame=animation_frame, animation_group=animation_group, category_orders=category_orders, labels=labels, orientation=orientation, color_discrete_sequence=color_discrete_sequence, color_discrete_map=color_discrete_map, line_dash_sequence=line_dash_sequence, line_dash_map=line_dash_map, symbol_sequence=symbol_sequence, symbol_map=symbol_map, markers=markers, log_x=log_x, log_y=log_y, range_x=range_x, range_y=range_y, line_shape=line_shape, render_mode=render_mode, template=template, width=width, height=height
)
        
                
        # Adicionar o gráfico como um elemento
        self.elemento = dbc.Card(
                    [
                        html.H5(title, className="card-title", style={'textAlign': 'left', 'margin': '10px'}),
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=fig)
                            ]
                        )
                    ], style={"text-align": "center", "margin": "5px"})
        fig.update_traces(
            textposition="bottom right",
            )
        fig.update_layout(margin=go.layout.Margin(
            b=0,
            l=0,
            r=0,
            t=25
        ))
        
    def add_grafico_pizza(self, sm=6, data_frame=None, names=None, values=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, color_discrete_sequence=None, color_discrete_map=None, hover_name=None, hover_data=None, custom_data=None, category_orders=None, labels=None, title=None, template=None, width=None, height=None, opacity=None, hole=None):
        fig = px.pie(data_frame=data_frame, names=names, values=values, color=color, facet_row=facet_row, facet_col=facet_col, facet_col_wrap=facet_col_wrap, facet_row_spacing=facet_row_spacing, facet_col_spacing=facet_col_spacing, color_discrete_sequence=color_discrete_sequence, color_discrete_map=color_discrete_map, hover_name=hover_name, hover_data=hover_data, custom_data=custom_data, category_orders=category_orders, labels=labels, template=template, width=width, height=height, opacity=opacity, hole=hole
)       
        config = {'displayModeBar': False}
        
        
        
        # Adicionar o gráfico como um elemento
        self.elemento = dbc.Card(
                    [
                        html.H5(title, className="card-title", style={'textAlign': 'left', 'margin': '10px'}),
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=fig, config=config)
                            ]
                        )
                    ], style={"text-align": "center", "margin": "5px"})
        
        fig.update_layout(margin=go.layout.Margin(
            # b=0,
            # l=0,
            # r=0,
            t=0
        ))
    
    def add_grafico_bolhas(self, sm=6):
        df = px.data.gapminder()

        fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
                    size="pop", color="continent",
                        hover_name="country", log_x=True, size_max=60)
        
        # Adicionar o gráfico como um elemento
        self.elemento = dbc.Col(
            html.Div(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=fig)
                            ]
                        )
                    ],
                    style={"text-align": "center", "margin": "10px auto", "border-radius": "15px", "border-color": "transparent", "width": "100%"},
                )
            ),id=self.id, sm=sm
        )
        fig.update_layout(margin=go.layout.Margin(
            b=0,
            l=0,
            r=0,
            t=0
        ))
    
    def add_tabela(self, sm=6, data_frame=None, title=None):
        # Extrair os cabeçalhos das colunas
        header_values = list(data_frame.columns)
        
        # Extrair os valores das células como uma lista de listas
        cell_values = [data_frame[col].tolist() for col in data_frame.columns]
        
        # Criar a figura com o gráfico de tabela
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=header_values,
                fill_color='#636EFA',
                font=dict(color='white', size=12),
                align='center',
            ),
            cells=dict(
                values=cell_values,
                fill_color='lavender',
                align='left'
            )
        )])

        # Atualizar layout para ajustar o tamanho
        fig.update_layout(
            autosize=True,
            margin=dict(t=20, b=20, l=20, r=20)
        )
        
        # Adicionar o gráfico como um elemento
        self.elemento = dbc.Card(
                    [
                        html.H5(title, className="card-title", style={'textAlign': 'left', 'margin': '10px'}),
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=fig)
                            ]
                        ),
                    ],
                    style={"text-align": "center", "margin": "5px"}
                )

        fig.update_layout(margin=go.layout.Margin(
            b=0,
            l=0,
            r=0,
            t=0
        ))
    
    def add_grafico_violino(self, sm=6):
        df = px.data.tips()

        fig = px.violin(df, x="sex", y="total_bill", color="smoker")
          
        # Adicionar o gráfico como um elemento
        self.elemento = dbc.Col(
            html.Div(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=fig)
                            ]
                        )
                    ],
                    style={"text-align": "center", "margin": "10px auto", "border-radius": "15px", "border-color": "transparent", "width": "100%"},
                )
            ), sm=sm
        )
        fig.update_layout(margin=go.layout.Margin(
            b=0,
            l=0,
            r=0,
            t=0
        ))
        
    def add_mapa_coropletico(self, sm=6):
        df = px.data.election()
        geojson = px.data.election_geojson()

        fig = px.choropleth_mapbox(df, geojson=geojson, color="Bergeron",
                                locations="district", featureidkey="properties.district",
                                center={"lat": 45.5517, "lon": -73.7073},
                                mapbox_style="carto-positron", zoom=9)
          
        # Adicionar o gráfico como um elemento
        self.elemento = dbc.Col(
            html.Div(
                dbc.Card(
                    [
                        dbc.CardBody(
                            [
                                dcc.Graph(figure=fig)
                            ]
                        )
                    ],
                    style={"text-align": "center", "margin": "10px auto", "border-radius": "15px", "border-color": "transparent", "width": "100%"},
                )
            ),id=self.id,sm=sm,
        )
        fig.update_layout(margin=go.layout.Margin(
            b=0,
            l=0,
            r=0,
            t=0
        ))
        
    def add_grafico_scatter(self, sm=12, data_frame=None, x=None, y=None, line_group=None, color=None, line_dash=None, symbol=None, hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, color_discrete_sequence=None, color_discrete_map=None, symbol_sequence=None, symbol_map=None, markers=False, log_x=False, log_y=False, range_x=None, range_y=None, render_mode='auto', title=None, template=None, width=None, height=None):
    
        # Adicionar coluna de cores com base nos intervalos de valores
        def get_color(value):
            if value >= 300:
                return '#7E0023'
            elif 201 <= value < 300:
                return '#660099'
            else:
                return '#FFDE33'
        
        data_frame['marker_color'] = data_frame[y].apply(get_color)
        
        fig = px.scatter(
            data_frame=data_frame, 
            x=x, 
            y=y, 
            color='marker_color', 
            color_discrete_map={
                '#7E0023': '#7E0023', 
                '#660099': '#660099', 
                '#FFDE33': '#FFDE33'
            },
            symbol=symbol, 
            hover_name=hover_name, 
            hover_data=hover_data, 
            custom_data=custom_data, 
            text=text, 
            facet_row=facet_row, 
            facet_col=facet_col, 
            facet_col_wrap=facet_col_wrap, 
            facet_row_spacing=facet_row_spacing, 
            facet_col_spacing=facet_col_spacing, 
            error_x=error_x, 
            error_x_minus=error_x_minus, 
            error_y=error_y, 
            error_y_minus=error_y_minus, 
            animation_frame=animation_frame, 
            animation_group=animation_group, 
            category_orders=category_orders, 
            labels=labels, 
            orientation=orientation, 
            log_x=log_x, 
            log_y=log_y, 
            range_x=range_x, 
            range_y=range_y, 
            render_mode=render_mode, 
            template=template, 
            width=width, 
            height=height
        )
        
        # Atualizar as configurações do gráfico
        fig.update_traces(
            marker=dict(size=8),  # Ajuste o tamanho dos marcadores conforme necessário
            textposition="bottom right"
        )
        
        fig.update_layout(margin=go.layout.Margin(
            b=0,
            l=0,
            r=0,
            t=25
        ))
        
        # Adicionar o gráfico como um elemento
        self.elemento = dbc.Card(
            [
                html.H5(title, className="card-title", style={'textAlign': 'left', 'margin': '10px'}),
                dbc.CardBody(
                    [
                        dcc.Graph(figure=fig)
                    ]
                )
            ], style={"text-align": "center", "margin": "5px"}
        )
    
    def get_elemento(self):
        return self.elemento