import React from 'react';
import { Handle } from 'reactflow';

function DataNode({ data = { value: "" } }) { // Provide default for data
    return (
        <div className="data-node">
            <p>{data.value}</p>
            <Handle type="target" position="left" id="a" /> 
        </div>
    );
}

export default DataNode;