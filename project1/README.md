# Project Compilers

## Instructions:

The build script is ***buildscript.sh*** (present in the project folder). This allows to generate the python classes (ANTLR).
The test script, which runs all the test in the testfiles folder, and puts the output in the ast_files folder, is ***testscript.sh*** (present in the project folder).
You can simply run ./testscript.sh in the project1/ folder. In the terminal, you will get an overview of which file outputs were correct.

## Testfiles information:

| Testfile       | Functionality                                                 |
|----------------|---------------------------------------------------------------|
| A_inputfile2.c | Example code from second assignment sheet (P2)                | 
| A_inputfile3.c | Example code from third assignment sheet (P3)                 |
| inputfile0.c   | Binary operations and unary operations                        |
| inputfile1.c   | Logical operations                                            |
| inputfile2.c   | Comparison operators                                          |
| inputfile3.c   | Types, reserved words, variables                              |
| inputfile4.c   | Identifier Operations                                         |
| inputfile5.c   | Comments and printf                                           |
| inputfile6.c   | Error outputs: Redeclaration of an existing variable.         |
| inputfile7.c   | Error outputs: Use of an undefined or uninitialized variable. |
| inputfile8.c   | Error outputs: Use of an undefined or uninitialized variable. |
| inputfile9.c   | Error outputs: Assignment to a const variable.                |
| inputfile10.c  | (Syntax) Error outputs: Mismatched input.                     |

***note***: Semantic errors (Operations or assignments of incompatible types) are done throughout the testfiles.

## Progress:

### Implementation status:

V: Working. \
-: Partially working with known problems (described below).  
X: Not working or not implemented.  
(blanco): TODO.

| Project | Functionality                                                      | Status |
|---------|--------------------------------------------------------------------|--------|
| 1       | (mandatory) Binary operations +, -, *, and /.                      | V      |
|         | (mandatory) Binary operations >, <, and ==.                        | V      |
|         | (mandatory) Unary operators + and -.                               | V      |
|         | (mandatory) Brackets to overwrite the order of operations.         | V      |
|         | (mandatory) Logical operators AND, OR, and NOT.                    | V      |
|         | (optional) Comparison operators >=, <=, and !=.                    | V      |
|         | (optional) Binary operator %.                                      | V      |
|         | 2.2 Abstract Syntax Tree                                           | V      |
|         | 2.3 Visualization                                                  | V      |
|         | 2.4 Constant Folding                                               | V      |
| 2       | (mandatory) Types.                                                 | V      |
|         | (mandatory) Reserved words.                                        | V      |
|         | (mandatory) Variables.                                             | V      |
|         | (mandatory) Pointer Operations.                                    | V      |
|         | (optional) Identifier Operations.                                  | V      |
|         | (optional) Conversions.                                            | -      |
|         | 1.2 Abstract Syntax Tree                                           | V      |
|         | 1.3 Visualization                                                  | V      |
|         | 1.4 Constant Propagation                                           | V      |
|         | 2 Error Analysis                                                   | V      |
|         | 2.1 Syntax Errors                                                  | V      |
|         | 2.2 Semantic Errors                                                | V      |
|         | Symbol table creation                                              | V      |
| 3       | (mandatory) Comments.                                              | V      |
|         | Optional comment stuff                                             | X      |
|         | (mandatory) Printf.                                                | V      |
|         | 1.2 Abstract Syntax Tree                                           | V      |
|         | 1.3 Visualization                                                  | V      |
|         | 2 Code Generation: LLVM                                            | V      |
| 4       | (mandatory) Reserved words (if, else, while, for, break, continue) | V      |
|         | (optional) switch, case and default.                               | X      |
|         | (mandatory) Scopes.                                                | V      |
|         | 1.2 Abstract Syntax Tree                                           | V      |
|         | 1.3 Visualization                                                  | V      |
|         | 1.4 Semantic Analysis                                              | V      |
|         | 1.5 Code Generation: LLVM                                          | V      |
| 5       | (mandatory) Reserved words (return and void)                       | V      |
|         | (mandatory) Scopes                                                 | V      |
|         | (mandatory) Local and global variables                             | V      |
|         | (mandatory) Functions                                              | V      |
|         | 1.2 Abstract Syntax Tree                                           | V      |
|         | 1.3 Visualization                                                  | V      |
|         | 1.4 Semantic Analysis                                              | V      |
|         | 1.5 Optimizations (mandatory) (Unreachable code and dead code)     | -      |
|         | (mandatory) after break or continue                                | -      |
|         | (optional) Unused variables                                        | -      |
|         | (optional) Untrue conditionals                                     | V      |
|         | 1.6 Code Generation: LLVM                                          | V      |
| 6       | (mandatory) Arrays                                                 | V      |
|         | (optional) multi-dimensional arrays.                               | V      |
|         | (optional) assignments of complete arrays or array rows            | V      |
|         | (optional) dynamic arrays.                                         | -      |
|         | (mandatory) Import                                                 | V      |
|         | 1.2 Abstract Syntax Tree                                           | V      |
|         | 1.3 Visualization                                                  | V      |
|         | 1.4 Code Generation: LLVM                                          | V      |

**Known problems:**\
P2: Conversions: Right now, all (implicit) conversions (e.g. int to float too) raise a warning (=>semantic analysis). This can/will be fixed in the future.
We also haven't paid any attention to assignment between pointers and type checking when assigning a pointer yet.
We don't know what dynamic arrays are supposed to be.
**Extra functionality, not described in the assignment sheet:** \
/

## Sources (Bibliography):
- http://marvin.cs.uidaho.edu/Teaching/CS445/c-Grammar.pdf
- https://www.lysator.liu.se/c/ANSI-C-grammar-y.html

- https://graphviz.org/doc/info/lang.html

- https://en.cppreference.com/w/c/language/operator_precedence