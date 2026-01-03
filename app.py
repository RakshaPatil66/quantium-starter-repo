from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/formatted_pink_morsel.csv')

df = df.sort_values(by="date")

app = Dash(__name__)

fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales Over Time",
              labels={"date": "Date of Sale", "sales": "Total Sales (Usd)"})

app.layout = html.Div(children=[

    html.H1(children='Pink Morsel Visualiser', style={'textAlign': 'center'}),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Visualiser', style={'textAlign': 'center'}),

    # Add the Region Picker here
    dcc.RadioItems(
        id='region-picker',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all', # Default selection
        inline=True,
        style={'textAlign': 'center', 'padding': '20px'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])


@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(selected_region):
    # 1. Start with the full dataset
    filtered_df = df

    # 2. Filter data if a specific region is chosen
    if selected_region != 'all':
        filtered_df = df[df['region'] == selected_region]

    # 3. Create a new figure with the filtered data
    new_fig = px.line(filtered_df, x="date", y="sales",
                      title=f"Pink Morsel Sales - {selected_region.upper()} Region",
                      labels={"date": "Date of Sale", "sales": "Total Sales (USD)"})

    return new_fig



if __name__ == '__main__':
    app.run(debug=True, port=8051)


