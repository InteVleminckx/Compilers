grammar mathGrammer;

math
        : import_stat_list? statement* EOF
        ;

import_stat_list
        : import_statement*
        ;
import_statement
        : HASHTAG INCLUDE COMP_OP (.|'.')*? COMP_OP
        ;

statement
        : extern_decl
        | LBRACKET_CURLY statement* RBRACKET_CURLY
        ;

extern_decl
        : stat
        | function_def
        | declaration
        ;

scan_stmt
        : SCANF LPARENTH TEXT print_values RPARENTH
        ;

print_stmt
        : PRINTF LPARENTH TEXT print_values RPARENTH
        ;

print_values
        : (COMMA (log_op1 | TEXT))*
        ;

function_def
//        : decl_spec declarator declaration_list comp_stat
        : decl_spec declarator comp_stat
//        | declarator declaration_list comp_stat
        | declarator comp_stat
        ;

stat
        : comp_stat
        | expr_statement
        | sel_statement
        | it_statement
        | j_statement
        | print_stmt SEMICOLON
        | scan_stmt SEMICOLON
        ;

comp_stat
        : LBRACKET_CURLY (declaration | stat)* RBRACKET_CURLY
        ;

it_statement
        : WHILE LPARENTH log_op1 RPARENTH stat
        | FOR LPARENTH declaration expr_statement log_op1 RPARENTH stat
        ;

sel_statement
        : IF LPARENTH log_op1 RPARENTH stat
        | IF LPARENTH log_op1 RPARENTH stat ELSE stat
        ;

j_statement
        : CONTINUE SEMICOLON
        | BREAK SEMICOLON
        | RETURN SEMICOLON
        | RETURN log_op1 SEMICOLON
        ;

expr_statement
        : log_op1 SEMICOLON
        | SEMICOLON
        ;

declaration
        : func_call SEMICOLON
        | decl_spec SEMICOLON
        | decl_spec init_decl_list SEMICOLON
        ;

init_declarator
        : declarator
        | declarator EQ_OP_S initializer
        ;

decl_spec
        :
        | ttype
        | CONST
        | CONST decl_spec
        ;

init_decl_list
        : init_declarator
        | init_decl_list COMMA init_declarator
        ;

declarator
//        : pointer direct_declarator
//        | reference direct_declarator
        : direct_declarator
        ;
initializer
        : log_op1
        | LBRACKET_CURLY initializer_list RBRACKET_CURLY
        | LBRACKET_CURLY initializer_list COMMA RBRACKET_CURLY
        ;

initializer_list
        : initializer
        | initializer_list COMMA initializer
        ;

func_call
        : IDENTIFIER LPARENTH func_call_par_list? RPARENTH
        ;

direct_declarator
        : IDENTIFIER
        | pointer IDENTIFIER
        | reference IDENTIFIER
        | ttype IDENTIFIER
        | ttype pointer IDENTIFIER
        | ttype reference IDENTIFIER
        | direct_declarator LPARENTH parameter_type_list RPARENTH
        | direct_declarator (LBRACKET_SQUARE log_op1 RBRACKET_SQUARE)+
        | direct_declarator LBRACKET_SQUARE RBRACKET_SQUARE
        | direct_declarator LPARENTH identifier_list RPARENTH
        | direct_declarator LPARENTH RPARENTH
        ;

identifier_list
        : IDENTIFIER
        | identifier_list COMMA IDENTIFIER
        ;

parameter_type_list
        : parameter_decl (COMMA parameter_decl)*
        ;

parameter_decl
        : decl_spec declarator
        | decl_spec
        ;

ttype
        : CHAR_KEY
        | INT_KEY
        | FLOAT_KEY
        | VOID
        ;

pointer
        : pointersign
        | pointersign type_qualifier_list
        | pointersign pointer
        | pointersign type_qualifier_list pointer
        ;

reference
        : ampersandsign
        | ampersandsign type_qualifier_list
        | ampersandsign reference
        | ampersandsign type_qualifier_list reference
        ;

type_qualifier_list
        : CONST
        | type_qualifier_list CONST
        ;

comp_expr
        : comp_expr1 EQ_OP comp_expr
        | comp_expr1
        ;
comp_expr1
        : expr COMP_OP expr
        | expr
        ;

expr
        : expr (PLUS | MIN) factor
        | factor
        ;

factor
        : factor (MUL_SIGN | DIV_SIGN | MOD_SIGN) term
		| term
		;

term
        : (PLUS | MIN | pointersign | ampersandsign)* var
        | (DOUBLE_PLUS | DOUBLE_MINUS) var
        | var (DOUBLE_PLUS | DOUBLE_MINUS)
		;

pointersign
        : MUL_SIGN
        ;

ampersandsign
        : AMPERSAND
        ;

log_op1
        : log_op2 (LOG_OR log_op2)*
		;

log_op2
        : log_op3 (LOG_AND log_op3)*
		;

log_op3
        : LOG_NOT log_op3
		| comp_expr
		;

var
	    : CHAR
        | INT
        | FLOAT
		| LPARENTH log_op1 RPARENTH
		| IDENTIFIER
		| IDENTIFIER (LBRACKET_SQUARE log_op1 RBRACKET_SQUARE)+
		| func_call
		;

func_call_par_list
        : log_op1 (COMMA log_op1)*
        ;

HASHTAG
        : '#'
        ;

INCLUDE
        : 'include'
        ;

SEMICOLON
        : ';'
        ;

COMMA
        : ','
        ;

LPARENTH
        : '('
        ;

RPARENTH
        : ')'
        ;

LBRACKET_CURLY
        : '{'
        ;

RBRACKET_CURLY
        : '}'
        ;

LBRACKET_SQUARE
        : '['
        ;

RBRACKET_SQUARE
        : ']'
        ;

IF
        : 'if'
        ;

ELSE
        : 'else'
        ;

WHILE
        : 'while'
        ;

PRINTF
        : 'printf'
        ;

SCANF
        : 'scanf'
        ;


FOR
        : 'for'
        ;

BREAK
        : 'break'
        ;

CONTINUE
        : 'continue'
        ;

RETURN
        : 'return'
        ;

EQ_OP_S
        : '='
        ;

CHAR_KEY
        : 'char'
        ;

INT_KEY
        : 'int'
        ;

FLOAT_KEY
        : 'float'
        ;

VOID
        : 'void'
        ;

CHAR
        : '\'' . '\''
        ;

INT
        : [0-9]+
        ;

FLOAT
        : ([0-9]+([.][0-9]*)?|[.][0-9]+)
        ;

CONST
        : 'const'
        ;

AMPERSAND
        : '&'
        ;

MUL_SIGN
        : '*'
        ;

DIV_SIGN
        : '/'
        ;

MOD_SIGN
        : '%'
        ;

DOUBLE_PLUS
        : '++'
        ;

DOUBLE_MINUS
        : '--'
        ;

PLUS
        : '+'
        ;

MIN
        : '-'
        ;

LOG_OR
        : '||'
        ;

LOG_AND
        : '&&'
        ;

LOG_NOT
        : '!'
        ;

COMP_OP
        : '>'
        | '<'
        | '<='
        | '>='
        ;

EQ_OP
        : '=='
        | '!='
        ;

TEXT
    : '"'(.*?)'"'
    ;

SINGLE_COMMENT
        : '//' ~[\r\n]* -> skip
        ;

MULTI_COMMENT
        : '/*' .*? '*/' -> skip
        ;


IDENTIFIER
        : [_a-zA-Z][_a-zA-Z0-9]*
        ;

WS
        : [ \n\t\r]+ -> skip
        ;
