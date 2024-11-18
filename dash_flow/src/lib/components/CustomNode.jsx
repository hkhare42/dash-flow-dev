
import React, { memo } from 'react';
import { Handle } from 'reactflow';

export default memo(({ data = { label: "" } }) => {  // Default value for data
    return (
        <div style={{ background: 'white', padding: 12 }}>
            <Handle type="target" position="top" />
            <div>{data.label}</div>
            <Handle type="source" position="bottom" id="a" />
            <Handle type="source" position="bottom" id="b" style={{ left: 40 }} />
        </div>
    );
});