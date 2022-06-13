.data

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-20
	sw $ra, 12($sp)

	li	$t0, 10
	sw	$t0,4($sp)
	la	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,8($sp)
	lw	$t0,8($sp)		#load local variable or temp register from stack #p=1
	lw	$t0,0($t0) #p=1
	sw	$t0,-4($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall


	lw $ra, 12($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
exit:
	li $v0, 10
	syscall