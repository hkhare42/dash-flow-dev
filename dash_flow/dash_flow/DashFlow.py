# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashFlow(Component):
    """A DashFlow component.


Keyword arguments:

- id (string; optional)

- elements (dict; optional)

- fitView (boolean; optional)

- layout (boolean; optional)

- onConnect (dict; optional)

- onEdgesChange (list; optional)

- onElementsRemove (list; optional)

- onNodeClick (string; optional)

- onNodeDragStop (dict; optional)

- onNodesChange (list; optional)

- onPaneClick (dict; optional)

    `onPaneClick` is a dict with keys:

    - x (number; optional)

    - y (number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flow'
    _type = 'DashFlow'
    @_explicitize_args
    def __init__(self, elements=Component.UNDEFINED, id=Component.UNDEFINED, layout=Component.UNDEFINED, fitView=Component.UNDEFINED, onNodesChange=Component.UNDEFINED, onEdgesChange=Component.UNDEFINED, onConnect=Component.UNDEFINED, onElementsRemove=Component.UNDEFINED, onNodeDragStop=Component.UNDEFINED, onNodeClick=Component.UNDEFINED, onPaneClick=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'elements', 'fitView', 'layout', 'onConnect', 'onEdgesChange', 'onElementsRemove', 'onNodeClick', 'onNodeDragStop', 'onNodesChange', 'onPaneClick']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'elements', 'fitView', 'layout', 'onConnect', 'onEdgesChange', 'onElementsRemove', 'onNodeClick', 'onNodeDragStop', 'onNodesChange', 'onPaneClick']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashFlow, self).__init__(**args)
