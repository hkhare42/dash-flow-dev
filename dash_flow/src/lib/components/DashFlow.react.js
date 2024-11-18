import React, { useCallback, useState, useMemo, useRef, useEffect } from 'react';
import ReactFlow, {
    addEdge, applyEdgeChanges, applyNodeChanges,
    Background,
    Controls,
    ReactFlowProvider,
    ConnectionLineType,
    NodeTypes
} from 'reactflow';

// Custom Components
import CustomNode from './CustomNode.jsx';
import MetricNode from './MetricNode';
import DataNode from './DataNode';
import CustomEdge from './CustomEdge';

// Styles and Utils
import 'reactflow/dist/style.css';
import PropTypes from 'prop-types';
import { nanoid } from 'nanoid';
import Dagre from 'dagre-d3';



const nodeTypes = {
    custom: CustomNode,
    metric: MetricNode,
    data: DataNode,
};

const edgeTypes = {
    custom: CustomEdge,
};


const DashFlow = (props) => {
    const { setProps, layout, fitView, id } = props;
    const reactFlowWrapper = useRef(null);
    const [reactFlowInstance, setReactFlowInstance] = useState(null);
    const [elements, setElements] = useState({ nodes: [], edges: [] }); // Initialize as empty


    useEffect(() => {
      if (props.elements) { // Check if elements prop exists
          setElements(props.elements); // Set initial elements from prop
      }
  }, [props.elements]);  // Run only when props.elements changes

    const onNodesChange = useCallback((changes) => {
        setElements((els) => ({ ...els, nodes: applyNodeChanges(changes, els.nodes) }));
        setProps({ onNodesChange: changes });
    }, [setProps]);

    const onEdgesChange = useCallback((changes) => {
        setElements((els) => ({ ...els, edges: applyEdgeChanges(changes, els.edges) }));
        setProps({ onEdgesChange: changes });
    }, [setProps]);

    const onConnect = useCallback((params) => {
        setElements((els) => ({ ...els, edges: addEdge(params, els.edges) }));
        setProps({ onConnect: params });
    }, [setProps]);

    const onElementsRemove = useCallback((elementsToRemove) => {
        setElements((els) => ({
            nodes: els.nodes.filter(node => !elementsToRemove.some(el => el.id === node.id)),
            edges: els.edges.filter(edge => !elementsToRemove.some(el => el.id === edge.id))
        }));
        setProps({ onElementsRemove: elementsToRemove });
    }, [setProps]);

    const onNodeDragStop = useCallback((event, node) => {
        setProps({ onNodeDragStop: node });
    }, [setProps]);

    const onNodeClick = useCallback((event, node) => {
        setProps({ onNodeClick: node.id });
    }, [setProps]);

    const onPaneClick = useCallback((event) => {
        if (reactFlowInstance) {
            const position = reactFlowInstance.project({ x: event.clientX, y: event.clientY });
            setProps({ onPaneClick: position });
        }
    }, [reactFlowInstance, setProps]);

    const dagreGraph = new Dagre.graphlib.Graph();
    dagreGraph.setDefaultEdgeLabel(() => ({}));

    const applyDagreLayout = useCallback(() => {
        if (!elements.nodes || elements.nodes.length === 0) return elements;

        elements.nodes.forEach((node) => {
            dagreGraph.setNode(node.id, { width: node.width || 150, height: node.height || 50 });
        });

        elements.edges.forEach((edge) => {
            if(edge.source && edge.target){ // check for valid edge definitions before adding to dagre
                dagreGraph.setEdge(edge.source, edge.target);
            }

        });


        Dagre.layout(dagreGraph);

        const layoutedNodes = elements.nodes.map((node) => {
            const nodeWithPosition = dagreGraph.node(node.id);
            return {
                ...node,
                position: { x: nodeWithPosition.x, y: nodeWithPosition.y },
                width: nodeWithPosition.width,
                height: nodeWithPosition.height,
            };
        });

        return { nodes: layoutedNodes, edges: elements.edges };

    }, [elements]);


    const flowProps = useMemo(() => {
        const currentElements = layout ? applyDagreLayout() : elements;


        return {
            nodes: currentElements.nodes,
            edges: currentElements.edges,
            nodeTypes: nodeTypes,
            edgeTypes: edgeTypes,
            onNodesChange,
            onEdgesChange,
            onConnect,
            onElementsRemove,
            onNodeDragStop,
            onNodeClick,
            onPaneClick,
            onInit: (instance) => {
                setReactFlowInstance(instance);
                if (fitView) {
                    instance.fitView();
                }
            }
        };
    }, [
        elements, layout, applyDagreLayout, onNodesChange, onEdgesChange,
        onConnect, onElementsRemove, onNodeDragStop, onNodeClick, onPaneClick, fitView
    ]);


    return (
        <div style={{ height: '500px', width: '500px' }} ref={reactFlowWrapper}>
            <ReactFlowProvider>
                <ReactFlow {...flowProps} >
                    <Controls />
                    <Background />
                </ReactFlow>
            </ReactFlowProvider>
        </div>
    );
}

DashFlow.propTypes = {
    elements: PropTypes.object,
    id: PropTypes.string,
    setProps: PropTypes.func,
    layout: PropTypes.bool,
    fitView: PropTypes.bool,
    onNodesChange: PropTypes.array,
    onEdgesChange: PropTypes.array,
    onConnect: PropTypes.object,
    onElementsRemove: PropTypes.array,
    onNodeDragStop: PropTypes.object,
    onNodeClick: PropTypes.string,
    onPaneClick: PropTypes.exact({
        x: PropTypes.number,
        y: PropTypes.number
    }),
};


export default DashFlow;