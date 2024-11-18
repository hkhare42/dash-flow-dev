
module DashFlow
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/''_customedge.jl")
include("jl/''_customnode.jl")
include("jl/''_dashflow.jl")
include("jl/''_datanode.jl")
include("jl/''_metricnode.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_flow",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_flow.min.js",
    external_url = "https://unpkg.com/dash_flow@0.0.1/dash_flow/dash_flow.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_flow.min.js.map",
    external_url = "https://unpkg.com/dash_flow@0.0.1/dash_flow/dash_flow.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
