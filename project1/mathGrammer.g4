grammar mathGrammer;

math
        : log_op1 ';' math
        | extern_decl
        | extern_decl math
        | comment math
        | EOF
        ;
extern_decl
        : function_def
        | declaration
        ;

comment
        : single_comment
        | multi_comment
        ;

single_comment
        : SINGLE_COMMENT
        ;

multi_comment
        : '/*' MULTI_COMMENT
        ;

print_stmt
        : 'printf' '(' log_op1 ')'
        ;

function_def
        : print_stmt
        ;

declaration
        : decl_spec ';'
        | decl_spec init_decl_list ';'
        ;

decl_spec
        :
        | ttype
        | CONST
        | CONST decl_spec
        ;

init_decl_list
        : init_declarator
        ;

init_declarator
        : declarator
        | declarator EQ_OP_S initializer
        ;

declarator
        : pointer direct_declarator
        | direct_declarator
        ;

initializer
        : log_op1
        ;

direct_declarator
        : IDENTIFIER
        ;

ttype
        : CHAR_KEY
        | INT_KEY
        | FLOAT_KEY
        ;

pointer
        : pointersign
        | pointersign type_qualifier_list
        | pointersign pointer
        | pointersign type_qualifier_list pointer
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
        : (PLUS | MIN | pointersign | AMPERSAND)* var
        | (DOUBLE_PLUS | DOUBLE_MINUS) var
        | var (DOUBLE_PLUS | DOUBLE_MINUS)
		;

pointersign
        : MUL_SIGN
        ;

log_op1
        : log_op2 (LOG_OR log_op2)*
		;

log_op2
        :log_op3 (LOG_AND log_op3)*
		;

log_op3
        : LOG_NOT log_op3
		| comp_expr
		;

var
	    : CHAR
        | INT
        | FLOAT
		| '(' log_op1 ')'
		| IDENTIFIER
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


SINGLE_COMMENT
        :  [/][/][ a-zA-Z0-9_/]*[\n]
        ;

MULTI_COMMENT
//        :  ['/*'][ -~]*['*/']
        : [ a-zA-Z0-9_/]*[\n]*[*][/]
//        | [\n]([ *][ a-zA-Z0-9_/]*[\n])*[*][/]
        ;


IDENTIFIER
        : [_a-zA-Z][_a-zA-Z0-9]*
        ;

WS
        : [ \n\t\r]+ -> skip
        ;
