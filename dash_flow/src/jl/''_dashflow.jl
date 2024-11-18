# AUTO GENERATED FILE - DO NOT EDIT

export ''_dashflow

"""
    ''_dashflow(;kwargs...)

A DashFlow component.

Keyword arguments:
- `id` (String; optional)
- `elements` (Dict; optional)
- `fitView` (Bool; optional)
- `layout` (Bool; optional)
- `onConnect` (Dict; optional)
- `onEdgesChange` (Array; optional)
- `onElementsRemove` (Array; optional)
- `onNodeClick` (String; optional)
- `onNodeDragStop` (Dict; optional)
- `onNodesChange` (Array; optional)
- `onPaneClick` (optional): . onPaneClick has the following type: lists containing elements 'x', 'y'.
Those elements have the following types:
  - `x` (Real; optional)
  - `y` (Real; optional)
"""
function ''_dashflow(; kwargs...)
        available_props = Symbol[:id, :elements, :fitView, :layout, :onConnect, :onEdgesChange, :onElementsRemove, :onNodeClick, :onNodeDragStop, :onNodesChange, :onPaneClick]
        wild_props = Symbol[]
        return Component("''_dashflow", "DashFlow", "dash_flow", available_props, wild_props; kwargs...)
end

