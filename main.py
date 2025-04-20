from lexer import tokenize
from parser import parse, ParserError
from icg import IntermediateCodeGenerator
from tree_visualizer import visualize_ast, generate_dot
import os

def main():
    print("Enter your C-like code (end with empty line):")
    code_lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            code_lines.append(line)
        except EOFError:
            break
    code = '\n'.join(code_lines)
    try:
        # Lexical analysis
        tokens = tokenize(code)
        print("\n🔹 Lexical Analysis Results:")
        for token in tokens:
            print(f"{token[0]:<10} {token[1]:<15} Line {token[2]}:{token[3]}")
        # Parsing and AST generation
        ast = parse(tokens)
        print("\n" + visualize_ast(ast))
        # Generate DOT file for visualization
        with open('ast.dot', 'w') as f:
            f.write(generate_dot(ast))
        print("\n✅ Parse tree DOT file generated: ast.dot")
        print("  Run 'dot -Tpdf ast.dot -o ast.pdf' to visualize")
        # Intermediate code generation
        icg = IntermediateCodeGenerator()
        intermediate_code = icg.generate(ast)
        print("\n🔹 Intermediate Code:")
        for code_line in intermediate_code:
            print(code_line)
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
