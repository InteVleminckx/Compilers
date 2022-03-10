grammar mathGrammer;

math
        : log_op1 ';' math
        | extern_decl
        | extern_decl math
        | EOF
        ;

extern_decl
        : function_def
        | declaration
        ;

function_def
        : ';' // nog niet geïmplementeerd
        ;

declaration
        : decl_spec ';'
        | decl_spec init_decl_list ';'
        ;

decl_spec
        :
        | type
        | CONST
        | CONST decl_spec
        ;


init_decl_list
        : init_declarator
        | init_decl_list ',' init_declarator
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

IDENTIFIER
        : [_a-zA-Z][_a-zA-Z0-9]*
        ;

EQ_OP_S
        : '='
        ;

type        : CHAR_KEY
            | INT_KEY
            | FLOAT_KEY
            ;

CHAR_KEY
        : 'char ' // raar
        ;

INT_KEY
        : 'int '
        ;

FLOAT_KEY
        : 'float '
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


CONST       : 'const'
            ;

pointer     : pointersign
	        | pointersign type_qualifier_list
	        | pointersign pointer
	        | pointersign type_qualifier_list pointer
	        ;

AMPERSAND
        : '&'
        ;

type_qualifier_list : CONST
	                | type_qualifier_list CONST
	                ;

comp_expr	: comp_expr1 EQ_OP comp_expr
            | comp_expr1
			;
comp_expr1 	: expr COMP_OP expr
            | expr
			;

expr		: expr (PLUS | MIN) factor
			| factor
			;
factor		: factor bin_op2 term
			| term
			;
term		: (PLUS | MIN | pointersign | AMPERSAND)* var
            | (DOUBLE_PLUS | DOUBLE_MINUS) var
            | var (DOUBLE_PLUS | DOUBLE_MINUS)
			;

MUL_SIGN
        : '*'
        ;

pointersign
        : MUL_SIGN
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

log_op1 	: log_op2 (LOG_OR log_op2)*
			;
log_op2		: log_op3 (LOG_AND log_op3)*
			;
log_op3		: LOG_NOT log_op3
			| comp_expr
			;

var			: CHAR
            | INT
            | FLOAT
			| '(' log_op1 ')'
			| IDENTIFIER
			;

bin_op2 	: MUL_SIGN
			| DIV_SIGN
			| MOD_SIGN
			;

PLUS	    : '+';
MIN	        : '-';

LOG_OR      : '||'
            ;

LOG_AND     : '&&'
            ;

LOG_NOT     : '!'
            ;


COMP_OP 	: '>'
			| '<'
			| '<='
			| '>='
			;
EQ_OP		: '=='
			| '!='
			;

WS          : [ \n\t\r]+ -> skip
            ;
