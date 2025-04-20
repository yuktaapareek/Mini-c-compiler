# 🛠 Mini C-like Compiler

This project is a simple compiler for a C-like language, built in Python using the [PLY](http://www.dabeaz.com/ply/) (Python Lex-Yacc) library. It includes key compiler phases such as lexical analysis, parsing, semantic analysis, and intermediate code generation.

---

## 📁 Project Structure

├── lexer.py # Tokenizer using PLY (Lex) 

├── parser.py # Parser using PLY (Yacc) 

├── symbol_table.py # Manages symbol table entries 

├── utils.py # Helper functions 

├── icg.py # Intermediate Code Generator (3AC) 

├── tree_visualizer.py # Text-based AST visualization 

├── main.py # Driver script to run the compiler 

├── example.c # Sample C-like code input 

└── README.md # You're here!

---

## 🚀 Features

- Tokenization and Lexical Analysis  
- Parsing and Abstract Syntax Tree (AST) Generation  
- Semantic Analysis (Type Checking)  
- Symbol Table Management  
- Intermediate Code Generation (3-address code)  
- Text-based AST visualization  

---

## 🧪 Sample Code Input

Example example.c:

```c
int x = 5;
int y = 10;
int z = x + y;

▶ How to Run

//Install Requirements
pip install ply     
//Run the Compiler
python main.py
