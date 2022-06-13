.data
str1:	.asciiz	"\n"

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-16
	sw $ra, 8($sp)

	li	$t0, 1
	sw	$t0,4($sp)
	li	$t0, 1
	sw	$t0,-4($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	li	$t0, 1
	sw	$t0,-8($sp)
	lw	$t0,-8($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 8($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)

exit:
	li $v0, 10
	syscall