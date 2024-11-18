import dash_flow
from dash import Dash, html, Input, Output, State, callback_context, dcc
import json
from dash.exceptions import PreventUpdate

app = Dash(__name__)

# Initial data (empty to be populated by callbacks or from dcc.Store)
# Initial elements structure with ALL required fields for nodes and edges.
initial_elements = {
    "nodes": [
        {"id": "1", "type": "custom", "position": {"x": 0, "y": 0}, "data": {"label": "Node 1"}, "width": 100, "height": 50},
        {"id": "2", "type": "metric", "position": {"x": 150, "y": 150}, "data": {"label": "Metric Node 1", "goal": 60000, "completion": 25}, "width": 200, "height": 100},
        {"id": "3", "type": "data", "position": {"x": 400, "y": 50}, "data": {"value": 1.234}, "width": 150, "height": 75},
    ],
    "edges": [
        {"id": "e1-2", "source": "1", "target": "2", "sourceHandle": None, "targetHandle": None, "type": "custom", "animated": True, "data": {}} # Use None instead of null
    ]
}



app.layout = html.Div([
    dash_flow.DashFlow(
        id='react-flow',
        fitView=True
    ),
    html.Div(id='output'),
    dcc.Store(id='store', data=initial_elements),  # Store to hold elements data
    html.Button('Dagre Layout', id='dagre-layout-button', n_clicks=0)
])


@app.callback(Output('store', 'data'),
              [Input('react-flow', 'onConnect'),
               Input('react-flow', 'onElementsRemove'),
               Input('react-flow', 'onNodesChange'),
               Input('react-flow', 'onEdgesChange'),
               Input('react-flow', 'onNodeClick'),
               Input('react-flow', 'onPaneClick'),
               Input('dagre-layout-button', 'n_clicks')],
              State('store', 'data'))
def update_elements(onConnect, onElementsRemove, onNodesChange, onEdgesChange, onNodeClick, onPaneClick, nClicks, elements):
    ctx = callback_context

    if not ctx.triggered:
        raise PreventUpdate

    triggered_prop_id = ctx.triggered[0]['prop_id'].split('.')[0]
    triggered_value = ctx.triggered[0]['value']

    if triggered_prop_id == "onConnect":
        elements['edges'].append(triggered_value)
    elif triggered_prop_id == "onElementsRemove":
        removed_ids = [element['id'] for element in triggered_value]
        elements['nodes'] = [node for node in elements['nodes'] if node['id'] not in removed_ids]
        elements['edges'] = [edge for edge in elements['edges'] if edge['id'] not in removed_ids]
    elif triggered_prop_id == "onNodesChange":
        for change in triggered_value:
            if change['type'] == 'position':
                node_id = change['id']
                for node in elements['nodes']: # Corrected iteration
                    if node['id'] == node_id:
                        node['position'] = change['position']
                        break  # Exit loop after updating the node
            # Handle other node change types here
    elif triggered_prop_id == "onEdgesChange":
        # Handle edge changes here
        pass  
    elif triggered_prop_id == 'onNodeClick':
        clicked_node_id = triggered_value
        print(f'Node clicked: {clicked_node_id}')

    elif triggered_prop_id == 'onPaneClick':
        click_position = triggered_value
        print(f'Pane clicked at: {click_position}')


    elif triggered_prop_id == 'dagre-layout-button':
        if nClicks:
            elements['layout'] = True
    else:
        print(f"Unhandled trigger: {triggered_prop_id}")


    return elements



@app.callback(Output('output', 'children'), Input('store', 'data'))
def display_output(elements):
    return f"Elements: {json.dumps(elements, indent=2)}"

@app.callback(Output('react-flow', 'elements'),
              Input('store', 'data'))  # Triggered by store data change
def initialize_elements(data):
    return data  # Return the data from the store

if __name__ == '__main__':
    app.run_server(debug=True)