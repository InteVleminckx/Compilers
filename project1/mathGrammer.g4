grammar mathGrammer;

math		: log_op1 ';' math
            | EOF
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
factor		: factor BIN_OP2 term
			| term
			;
term		: (PLUS | MIN)* var
			;

log_op1 	: log_op2 (LOG_OR log_op2)*
			;
log_op2		: log_op3 (LOG_AND log_op3)*
			;
log_op3		: LOG_NOT log_op3
			| comp_expr
			;

var			: INT
			| '(' log_op1 ')'
			;

BIN_OP2 	: '*'
			| '/'
			| '%'
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

INT			: [0-9]+
			;

WS          : [ \n\t\r]+ -> skip
            ;
