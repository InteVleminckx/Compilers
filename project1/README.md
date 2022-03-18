# Project Compilers

## Instructions:

## Testfiles information:

## Progress:

###Implementation status:

V: Working. \
-: Partially working with known problems (described below).  
X: Not working or not implemented.  
(blanco): TODO.

| Project | Functionality                                              | Status |
|---------|------------------------------------------------------------|--------|
| 1       | (mandatory) Binary operations +, -, *, and /.              | V      |
|         | (mandatory) Binary operations >, <, and ==.                | V      |
|         | (mandatory) Unary operators + and -.                       | V      |
|         | (mandatory) Brackets to overwrite the order of operations. | V      |
|         | (mandatory) Logical operators AND, OR, and NOT.            | V      |
|         | (optional) Comparison operators >=, <=, and !=.            | V      |
|         | (optional) Binary operator %.                              | V      |
|         | 2.2 Abstract Syntax Tree                                   | V      |
|         | 2.3 Visualization                                          | V      |
|         | 2.4 Constant Folding                                       | V      |
| 2       | (mandatory) Types.                                         | V      |
|         | (mandatory) Reserved words.                                | V      |
|         | (mandatory) Variables.                                     | V      |
|         | (mandatory) Pointer Operations.                            | V      |
|         | (optional) Identifier Operations.                          | V      |
|         | (optional) Conversions.                                    | -      |
|         | 1.2 Abstract Syntax Tree                                   | V      |
|         | 1.3 Visualization                                          | V      |
|         | 1.4 Constant Propagation                                   | V      |
|         | 2 Error Analysis                                           | V      |
|         | 2.1 Syntax Errors                                          | V      |
|         | 2.2 Semantic Errors                                        | V      |
|         | Symbol table creation                                      | V      |
| 3       | (mandatory) Comments.                                      | V      |
|         | Optional comment stuff                                     | X      |
|         | (mandatory) Printf.                                        | V      |
|         | 1.2 Abstract Syntax Tree                                   | V      |
|         | 1.3 Visualization                                          | V      |
|         | 2 Code Generation: LLVM                                    | -      |

**Known problems:**\
P2: Conversions: Right now, all (implicit) conversions (e.g. int to float too) raise a warning (=>semantic analysis). This can/will be fixed in the future.
P3: 2 Code Generation: LLVM: Check TODO in codeGeneration.py

**Extra functionality, not described in the assignment sheet:** \
/

## Sources (Bibliography):
- http://marvin.cs.uidaho.edu/Teaching/CS445/c-Grammar.pdf
- https://www.lysator.liu.se/c/ANSI-C-grammar-y.html

- https://graphviz.org/doc/info/lang.html

- https://en.cppreference.com/w/c/language/operator_precedence