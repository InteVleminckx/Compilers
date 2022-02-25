grammar mathGrammer;

math		: log_op1 ';' math
			;

comp_expr	: comp_expr1 EQ_OP comp_expr1
			;
comp_expr1 	: expr COMP_OP expr
			;


expr		: expr BIN_OP1 factor
			| factor
			;
factor		: factor BIN_OP2 term
			| term
			;
term		: UN_OP term 
			| var		 
			;


BIN_OP1 	: '+'
			| '-'
			;
BIN_OP2 	: '*'
			| '/'
			| '%'
			;
		
		
COMP_OP 	: '>'
			| '<'
			| '<='
			| '>='
			;
EQ_OP		: '=='
			| '!='
			;
		
		
log_op1 	: log_op2 ('||' log_op2)*
			;
log_op2		: log_op3 ('&&' log_op3)*
			;
log_op3		: '!' log_op3
			| comp_expr
			;
		
UN_OP		: '+'
			| '-'
			;
		
var			: INT
			| '(' expr ')'
			;
			
			
INT			: [0-9]+
			;

WS          : [ \n\t\r]+ -> skip
            ;