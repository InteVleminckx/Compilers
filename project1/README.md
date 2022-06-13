# Project Compilers

## Instructions:

The build script is ***buildscript.sh*** (present in the project folder). This allows to generate the python classes (ANTLR).
The test script, which runs all the test in the files folder, and puts the output in the folder that is provide for the generated files, is ***script.sh*** (present in the project folder).
You can simply run ./script.sh in the project1/ folder. In the terminal, you will get an overview of which file outputs were correct.
The folder "files" provide all codes in separate folders that can be executed for LLVM, MIPS and syntax. The other folders contain the generated code from the presentation and the correct code to compare
the generated code.
For executing the file you need to give 3 arguments: argv[1] = file, argv[2] = boolean, that says we want to generate LLVM or MIPS and argv[3] = boolean, thats says we just want to control syntax.  

## Progress:

### Implementation status:

V: Working. \
-: Partially working with known problems (described below).  
X: Not working or not implemented.  
(blanco): TODO.

| Project | Functionality                                                      | Status | LLVM | MIPS |
|---------|--------------------------------------------------------------------|--------|------|------|
| 1       | (mandatory) Binary operations +, -, *, and /.                      | V      | V    | V    |
|         | (mandatory) Binary operations >, <, and ==.                        | V      | V    | V    |
|         | (mandatory) Unary operators + and -.                               | V      | V    | V    |
|         | (mandatory) Brackets to overwrite the order of operations.         | V      | V    | V    |
|         | (mandatory) Logical operators AND, OR, and NOT.                    | V      | V    | V    |
|         | (optional) Comparison operators >=, <=, and !=.                    | V      | V    | V    |
|         | (optional) Binary operator %.                                      | V      | V    | V    |
|         | 2.2 Abstract Syntax Tree                                           | V      | V    | V    |
|         | 2.3 Visualization                                                  | V      | V    | V    |
|         | 2.4 Constant Folding                                               | V      | V    | V    |
| 2       | (mandatory) Types.                                                 | V      | V    | V    |
|         | (mandatory) Reserved words.                                        | V      | V    | V    |
|         | (mandatory) Variables.                                             | V      | V    | V    |
|         | (mandatory) Pointer Operations.                                    | V      | V    | V    |
|         | (optional) Identifier Operations.                                  | V      | V    | V    |
|         | (optional) Conversions.                                            | -      | V    | V    |
|         | 1.2 Abstract Syntax Tree                                           | V      | V    | V    |
|         | 1.3 Visualization                                                  | V      | V    | V    |
|         | 1.4 Constant Propagation                                           | V      | V    | V    |
|         | 2 Error Analysis                                                   | V      | V    | V    |
|         | 2.1 Syntax Errors                                                  | V      | V    | V    |
|         | 2.2 Semantic Errors                                                | V      | V    | V    |
|         | Symbol table creation                                              | V      | V    | V    |
| 3       | (mandatory) Comments.                                              | V      | V    | V    |
|         | Optional comment stuff                                             | X      | V    | V    |
|         | (mandatory) Printf.                                                | V      | V    | V    |
|         | 1.2 Abstract Syntax Tree                                           | V      | V    | V    |
|         | 1.3 Visualization                                                  | V      | V    | V    |
|         | 2 Code Generation: LLVM                                            | V      | V    | V    |
| 4       | (mandatory) Reserved words (if, else, while, for, break, continue) | V      | V    | V    |
|         | (optional) switch, case and default.                               | X      | X    | X    |
|         | (mandatory) Scopes.                                                | V      | V    | V    |
|         | 1.2 Abstract Syntax Tree                                           | V      | V    | V    |
|         | 1.3 Visualization                                                  | V      | V    | V    |
|         | 1.4 Semantic Analysis                                              | V      | V    | V    |
|         | 1.5 Code Generation: LLVM                                          | V      | V    | V    |
| 5       | (mandatory) Reserved words (return and void)                       | V      | V    | V    |
|         | (mandatory) Scopes                                                 | V      | V    | V    |
|         | (mandatory) Local and global variables                             | V      | V    | V    |
|         | (mandatory) Functions                                              | V      | V    | V    |
|         | 1.2 Abstract Syntax Tree                                           | V      | V    | V    |
|         | 1.3 Visualization                                                  | V      | V    | V    |
|         | 1.4 Semantic Analysis                                              | V      | V    | V    |
|         | 1.5 Optimizations (mandatory) (Unreachable code and dead code)     | X      | -    | -    |
|         | (mandatory) after break or continue                                | X      | X    | X    |
|         | (optional) Unused variables                                        | -      | X    | X    |
|         | (optional) Untrue conditionals                                     | V      | V    | V    |
|         | 1.6 Code Generation: LLVM                                          | V      | V    | V    |
| 6       | (mandatory) Arrays                                                 | V      | V    | -    |
|         | (optional) multi-dimensional arrays.                               | V      | X    | X    |
|         | (optional) assignments of complete arrays or array rows            | V      | X    | X    |
|         | (optional) dynamic arrays.                                         | -      | X    | X    |
|         | (mandatory) Import                                                 | V      | V    | V    |
|         | 1.2 Abstract Syntax Tree                                           | V      | V    | V    |
|         | 1.3 Visualization                                                  | V      | V    | V    |
|         | 1.4 Code Generation: LLVM                                          | -      | V    | V    |

**Known problems:**\
We don't know what dynamic arrays are supposed to be.

MIPS: with arrays, if you use expressions inside the [] brackets, it doesn't work (same for identifiers) and using an array value on the RHS isn't supported (there were no benchmarks for this), and those are the things here, together with the usage (excluding declaration) of global arrays that doesn't work (for arrays).
LLVM/MIPS: dereference assignment and pointer argument (because of pointer dereference mostly) don't work properly. We support pointers though.


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