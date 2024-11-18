# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''MetricNode <- function(data=NULL) {
    
    props <- list(data=data)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MetricNode',
        namespace = 'dash_flow',
        propNames = c('data'),
        package = 'dashFlow'
        )

    structure(component, class = c('dash_component', 'list'))
}
