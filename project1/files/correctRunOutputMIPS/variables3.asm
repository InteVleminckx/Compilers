.data
str1:	.asciiz	"; "

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-24
	sw $ra, 16($sp)

	la	 $t3, 12($sp) #loading array
	li	$t0, 10
	sw	$t0, 0($t3)
	la	 $t3, 12($sp) #loading array
	li	$t0, 20
	sw	$t0, -4($t3)
	la	 $t3, 12($sp) #loading array
	li	$t0, 30
	sw	$t0, -8($t3)
	lw	$t0,12($sp)		#load local variable or temp register from stack
	sw	$t0,-4($sp)
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-8($sp)
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-12($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	lw	$t0,-8($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	lw	$t0,-12($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall


	lw $ra, 16($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
exit:
	li $v0, 10
	syscall