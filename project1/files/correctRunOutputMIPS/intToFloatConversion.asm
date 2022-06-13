.data
fl0:	.float	5
fl1:	.float	1.5

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-24
	sw $ra, 16($sp)

	li	$t0, 5
	sw	$t0,4($sp)
	l.s	$f0, fl0
	swc1	$f0,8($sp)
	l.s	$f0, fl1
	swc1	$f0,12($sp)
	li	$t0, 1
	sw	$t0,-4($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 16($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)

exit:
	li $v0, 10
	syscall