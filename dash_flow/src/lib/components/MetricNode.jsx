import React from 'react';
import { Handle } from 'reactflow';

function MetricNode({ data = { label: "", goal: 0, completion: 0} }) {  // Default values provided
    return (
        <div className="metric-node">
            <h3>{data.label}</h3>
            <p>
                Goal: {data.goal} - {data.completion}% complete
            </p>
            <Handle type="source" position="right" id="a" />
        </div>
    );
}

export default MetricNode;