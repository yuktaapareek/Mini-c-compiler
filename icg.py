class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []
        self.label_count = 0

    def generate(self, ast):
        """Generate intermediate code from an AST"""
        for node in ast.children:
            self._generate_node(node)
        return self.code

    def _generate_node(self, node):
        if node.type == 'Declaration':
            var_name = node.children[1].value
            if len(node.children) > 2 and node.children[2].type == 'Assignment':
                expr_node = node.children[2].children[0]
                expr = expr_node.value
                if any(op in expr for op in ['+', '-', '*', '/']):
                    result = self._generate_expression(expr)
                    self.code.append(f"STORE {result} {var_name}")
                else:
                    self.code.append(f"STORE {expr} {var_name}")
        elif node.type == 'Assignment':
            var_name = node.children[0].value
            expr_node = node.children[1]
            expr = expr_node.value
            if any(op in expr for op in ['+', '-', '*', '/']):
                result = self._generate_expression(expr)
                self.code.append(f"STORE {result} {var_name}")
            else:
                self.code.append(f"STORE {expr} {var_name}")

    def _generate_expression(self, expr):
        for op in ['+', '-', '*', '/']:
            if op in expr:
                parts = expr.split(op, 1)
                left = parts[0].strip()
                right = parts[1].strip()
                left_temp = self._generate_operand(left)
                right_temp = self._generate_operand(right)
                result_temp = self._new_temp()
                op_code = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}[op]
                self.code.append(f"{op_code} {left_temp} {right_temp} {result_temp}")
                return result_temp
        return expr

    def _generate_operand(self, operand):
        operand = operand.strip()
        if operand.isdigit() or (operand.replace('.', '', 1).isdigit() and '.' in operand):
            temp = self._new_temp()
            self.code.append(f"LOAD {operand} {temp}")
            return temp
        return operand

    def _new_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def _new_label(self):
        label = f"L{self.label_count}"
        self.label_count += 1
        return label
