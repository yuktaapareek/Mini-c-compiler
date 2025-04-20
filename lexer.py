# lexer.py (expanded)
import re

TOKEN_PATTERNS = [
    ('COMMENT', r'//.*|/\*[\s\S]*?\*/'),
    ('WHITESPACE', r'\s+'),
    ('KEYWORD', r'\b(?:int|float|char|bool|void|if|else|while|for|return|break|continue|struct|typedef)\b'),
    ('BOOL', r'\b(?:true|false)\b'),
    ('FLOAT', r'\b\d+\.\d+\b'),
    ('NUM', r'\b\d+\b'),
    ('CHAR', r"'\\?.'"),
    ('STRING', r'"([^"\\]|\\.)*"'),
    ('DOUBLE_OP', r'(==|!=|<=|>=|\+\+|\-\-|<<|>>)'),
    ('LOGICAL_OP', r'(&&|\|\|)'),
    ('OP', r'[+\-*/%&|^~]'),
    ('ASSIGN', r'='),
    ('SEMI', r';'),
    ('COMMA', r','),
    ('COLON', r':'),
    ('TERNARY', r'\?'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('LBRACKET', r'\['),
    ('RBRACKET', r'\]'),
    ('DOT', r'\.'),
    ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('REL_OP', r'==|!=|<=|>=|<|>'),  
    ('ARITH_OP', r'[+\-*/]'),
  

]

def tokenize(code):
    tokens = []
    position = 0
    line = 1
    column = 1
    while position < len(code):
        match = None
        for token_type, pattern in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                value = match.group(0)
                if token_type == 'COMMENT':
                    pass  # Skip comments
                elif token_type != 'WHITESPACE':
                    tokens.append((token_type, value, line, column))
                
                # Update position tracking
                lines = value.split('\n')
                if len(lines) > 1:
                    line += len(lines) - 1
                    column = len(lines[-1]) + 1
                else:
                    column += match.end() - position
                position = match.end()
                break
        if not match:
            raise SyntaxError(f"Unexpected character '{code[position]}' at line {line}, column {column}")
    return tokens
