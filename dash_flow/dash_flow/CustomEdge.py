# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CustomEdge(Component):
    """A CustomEdge component.


Keyword arguments:
"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_flow'
    _type = 'CustomEdge'
    @_explicitize_args
    def __init__(self, style=Component.UNDEFINED, **kwargs):
        self._prop_names = []
        self._valid_wildcard_attributes =            []
        self.available_properties = []
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(CustomEdge, self).__init__(**args)
