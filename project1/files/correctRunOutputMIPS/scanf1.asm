.data
str1:	.asciiz	"Enter two numbers:"
str4:	.asciiz	"; "
str2:	.asciiz	"%d%d"

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-20
	sw $ra, 12($sp)

	la $a0, str1
	li $v0, 4
	syscall

	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-4($sp)
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-8($sp)
	li $v0, 5
	syscall
	move $t0, $v0
	sw	$t0,4($sp)
	li $v0, 5
	syscall
	move $t0, $v0
	sw	$t0,8($sp)
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-12($sp)
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-16($sp)
	lw	$t0,-12($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str4
	li $v0, 4
	syscall

	lw	$t0,-16($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	li	$t0, 1
	sw	$t0,-20($sp)
	lw	$t0,-20($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 12($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)

exit:
	li $v0, 10
	syscall