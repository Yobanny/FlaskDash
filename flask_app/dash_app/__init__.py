from dash import Dash, html, dcc, Output, Input

from .apps.services import home_dash

def init_dash(flask_app):
    dash_app = Dash(server=flask_app,
                        routes_pathname_prefix='/dash/',)
    
    dash_app.layout = html.Main([
        dcc.Location(id="url", refresh=True),
        html.Div(id="page-content", children=[])
        
    ], className="container")
    init_callbacks(dash_app)
    return dash_app.server 


def init_callbacks(app):
    @app.callback(
        Output("page-content", "children" ),
        Input("url", "pathname")
    )
    def show_home(pathname):
        if pathname == "/dash/":
            return home_dash()