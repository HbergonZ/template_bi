import dash_bootstrap_components as dbc
from dash import html

class Row:
    
    def __init__(self, ehFiltro=False):
        self.elementos = []
        self.ehFiltro=ehFiltro
    
    def get_elementos(self):
        return self.elementos
    
    def add_elementos(self, elementos):
        # Certifique-se de adicionar componentes diretamente, não listas de componentes
        if isinstance(elementos[0], (list, tuple)):
            for elem in elementos:
                self.elementos.extend(elem)
        else:
            self.elementos.extend(elementos)
    
    def to_row(self, borda="off"):
        # Converte a lista de elementos em uma linha do Dash
        if(not self.ehFiltro):
            if borda == "on":
                style={"border-style": "solid", "border-width": "1px"}
            else:
                style={}            
            return dbc.Row(self.elementos, style=style)
        else:
            if borda == "on":
                style={"border-style": "solid", "border-width": "1px"}
            else:
                style={}          
            return html.Div(self.elementos, style=style, className="d-flex justify-content-start")
    def limpar_elementos(self):
    # Limpa todos os elementos da lista
        self.elementos.clear()
