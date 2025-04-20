def visualize_ast(node, level=0):
    """Create a text-based visualization of the AST"""
    result = ""
    if level == 0:
        result += "🌳 Abstract Syntax Tree:\n"
    prefix = "  " * level
    result += f"{prefix}├─ {node.type}"
    if node.value:
        result += f" ({node.value})"
    result += "\n"
    for child in node.children:
        result += visualize_ast(child, level+1)
    return result

def generate_dot(ast):
    """Generate a DOT representation of the AST for Graphviz"""
    dot = ["digraph AST {", "  node [shape=box];"]
    node_ids = {}
    def add_nodes(node, parent=None):
        node_id = f"node{len(node_ids)}"
        label = node.value if node.value else node.type
        dot.append(f'  {node_id} [label="{node.type}\\n{label if node.value else ""}"];')
        node_ids[node] = node_id
        if parent:
            dot.append(f'  {node_ids[parent]} -> {node_id};')
        for child in node.children:
            add_nodes(child, node)
    add_nodes(ast)
    dot.append("}")
    return "\n".join(dot)
