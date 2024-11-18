# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''DashFlow <- function(id=NULL, elements=NULL, fitView=NULL, layout=NULL, onConnect=NULL, onEdgesChange=NULL, onElementsRemove=NULL, onNodeClick=NULL, onNodeDragStop=NULL, onNodesChange=NULL, onPaneClick=NULL) {
    
    props <- list(id=id, elements=elements, fitView=fitView, layout=layout, onConnect=onConnect, onEdgesChange=onEdgesChange, onElementsRemove=onElementsRemove, onNodeClick=onNodeClick, onNodeDragStop=onNodeDragStop, onNodesChange=onNodesChange, onPaneClick=onPaneClick)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashFlow',
        namespace = 'dash_flow',
        propNames = c('id', 'elements', 'fitView', 'layout', 'onConnect', 'onEdgesChange', 'onElementsRemove', 'onNodeClick', 'onNodeDragStop', 'onNodesChange', 'onPaneClick'),
        package = 'dashFlow'
        )

    structure(component, class = c('dash_component', 'list'))
}
