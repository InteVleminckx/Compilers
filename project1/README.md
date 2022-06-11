# Project Compilers

## Instructions:

The build script is ***buildscript.sh*** (present in the project folder). This allows to generate the python classes (ANTLR).
The test script, which runs all the test in the files folder, and puts the output in the folder that is provide for the generated files, is ***script.sh*** (present in the project folder).
You can simply run ./script.sh in the project1/ folder. In the terminal, you will get an overview of which file outputs were correct.

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
|         | 1.4 Code Generation: LLVM                                          | -      |

**Known problems:**\
P2: Conversions: Right now, all (implicit) conversions (e.g. int to float too) raise a warning (=>semantic analysis). This can/will be fixed in the future.
We also haven't paid any attention to assignment between pointers and type checking when assigning a pointer yet.
We don't know what dynamic arrays are supposed to be.

P3: LLVM: We don't fully support all llvm generation. The files that are provided in the folder project1/files/C_CodeLLVM contains the C code that we can convert to llvm.

**Extra functionality, not described in the assignment sheet:** \
/

## Sources (Bibliography):
- http://marvin.cs.uidaho.edu/Teaching/CS445/c-Grammar.pdf
- https://www.lysator.liu.se/c/ANSI-C-grammar-y.html
- https://graphviz.org/doc/info/lang.html
- https://en.cppreference.com/w/c/language/operator_precedence
- https://llvm.org/docs/LangRef.html
- https://www.d.umn.edu/~gshute/mips/data-comparison.xhtml#int-compare
- https://godbolt.org/ (for mips code inspiration)
- https://www.youtube.com/watch?v=ewpo1NERc3o&ab_channel=Intermation