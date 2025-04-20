from symbol_table import SymbolTable
from utils import optimize_expression

class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.children = children or []
        self.value = value

    def __repr__(self):
        return f"{self.type}: {self.value}" if self.value else self.type

class ParserError(Exception):
    def __init__(self, message, line=None, column=None):
        super().__init__(f"Line {line}, Column {column}: {message}" if line else message)

def parse(tokens):
    ast = ASTNode('Program')
    symtab = SymbolTable()
    i = 0

    while i < len(tokens):
        token_type, value, line, col = tokens[i]

        if token_type == 'KEYWORD':
            var_type = value
            i += 1
            if i >= len(tokens) or tokens[i][0] != 'ID':
                i += 1
                continue  # Skip invalid declaration

            var_name = tokens[i][1]
            i += 1
            decl_node = ASTNode('Declaration', [
                ASTNode('Type', value=var_type),
                ASTNode('Identifier', value=var_name)
            ])

            if i < len(tokens) and tokens[i][0] == 'ASSIGN':
                i += 1
                expr_tokens = []  # FIX: Initialize before loop
                expr_start = i
                while i < len(tokens) and tokens[i][0] not in ['SEMI']:
                    expr_tokens.append(tokens[i][1])
                    i += 1

                if not expr_tokens:
                    if i < len(tokens) and tokens[i][0] == 'SEMI':
                        i += 1
                    continue

                expr = ' '.join(expr_tokens)
                optimized = optimize_expression(expr)
                symtab.declare(var_type, var_name, optimized)

                expr_node = ASTNode('Expression', value=expr)
                if expr != optimized:
                    expr_node.children.append(ASTNode('Optimized', value=optimized))

                assign_node = ASTNode('Assignment')
                assign_node.children.append(expr_node)
                decl_node.children.append(assign_node)
            else:
                symtab.declare(var_type, var_name)

            if i >= len(tokens) or tokens[i][0] != 'SEMI':
                i += 1
                continue
            i += 1
            ast.children.append(decl_node)

        elif token_type == 'ID':
            var_name = value
            i += 1
            if i < len(tokens) and tokens[i][0] == 'ASSIGN':
                i += 1
                expr_tokens = []  # FIX: Initialize before loop
                expr_start = i
                while i < len(tokens) and tokens[i][0] not in ['SEMI']:
                    expr_tokens.append(tokens[i][1])
                    i += 1

                if not expr_tokens:
                    if i < len(tokens) and tokens[i][0] == 'SEMI':
                        i += 1
                    continue

                expr = ' '.join(expr_tokens)
                optimized = optimize_expression(expr)
                symtab.update(var_name, optimized)

                expr_node = ASTNode('Expression', value=expr)
                if expr != optimized:
                    expr_node.children.append(ASTNode('Optimized', value=optimized))

                assign_node = ASTNode('Assignment')
                assign_node.children.append(ASTNode('Identifier', value=var_name))
                assign_node.children.append(expr_node)

                if i < len(tokens) and tokens[i][0] == 'SEMI':
                    i += 1
                ast.children.append(assign_node)
            else:
                if i < len(tokens) and tokens[i][0] == 'SEMI':
                    i += 1
                continue
        else:
            i += 1
            continue

    symtab.display()
    return ast
