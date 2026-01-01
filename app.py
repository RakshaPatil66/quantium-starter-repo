import pandas as pd
from dash import Dash, html, dcc

# Initialize the Dash app
app = Dash(__name__)

# Basic layout to verify the workbench
app.layout = html.Div([
    html.H1("Quantium Data Workbench"),
    html.P("Environment and libraries are successfully installed."),
    dcc.Graph(id='example-graph')
])

if __name__ == '__main__':
    app.run(debug=True)