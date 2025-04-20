def optimize_expression(expr):
    operators = ['+', '-', '*', '/']
    # Check if this is a simple expression with operators
    for op in operators:
        if op in expr:
            try:
                parts = [p.strip() for p in expr.split(op, 1)]
                # Try to evaluate numeric expressions
                if len(parts) == 2:
                    # For integer expressions
                    if all(p.isdigit() for p in parts):
                        a, b = map(int, parts)
                        if op == '+': return str(a + b)
                        if op == '-': return str(a - b)
                        if op == '*': return str(a * b)
                        if op == '/': return str(a // b if b != 0 else "Error: Division by zero")
                    # For floating-point expressions
                    elif all(p.replace('.', '', 1).isdigit() for p in parts):
                        a, b = map(float, parts)
                        if op == '+': return str(a + b)
                        if op == '-': return str(a - b)
                        if op == '*': return str(a * b)
                        if op == '/': return str(a / b if b != 0 else "Error: Division by zero")
            except:
                pass
    return expr
