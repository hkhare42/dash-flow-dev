# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''CustomEdge <- function(style=NULL) {
    
    props <- list(style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'CustomEdge',
        namespace = 'dash_flow',
        propNames = c('style'),
        package = 'dashFlow'
        )

    structure(component, class = c('dash_component', 'list'))
}
