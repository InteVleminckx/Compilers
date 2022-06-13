.data
fl0:	.float	0.5

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-12
	sw $ra, 4($sp)

	li	$t0, 10
	sw	$t0,-4($sp)
	l.s	$f0, fl0
	swc1	$f0,-8($sp)
	li	$t0, '%'
	sw	$t0,-12($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	lwc1	$f0,-8($sp)		#load local variable or temp register from stack
	mov.s $f12, $f0
	li $v0, 2
	syscall

	lw	$t0,-12($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 11
	syscall


	lw $ra, 4($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
exit:
	li $v0, 10
	syscall