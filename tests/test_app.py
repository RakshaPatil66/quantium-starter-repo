from dash.testing.application_runners import import_app

def test_header_exists(dash_duo):
    # Start the app
    app = import_app("app")
    dash_duo.start_server(app)

    # 1. Check if the header is present
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Visualiser"

def test_visualization_exists(dash_duo):
    # Start the app
    app = import_app("app")
    dash_duo.start_server(app)

    # 2. Check if the graph exists
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_exists(dash_duo):
    # Start the app
    app = import_app("app")
    dash_duo.start_server(app)

    # 3. Check if the region picker exists
    picker = dash_duo.find_element("#region-picker")
    assert picker is not None