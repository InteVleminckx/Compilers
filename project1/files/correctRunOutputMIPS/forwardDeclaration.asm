.data
str1:	.asciiz	"Hello "
str3:	.asciiz	"World\n"

.text
.globl main

f:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-12
	sw $ra, 4($sp)

	la $a0, str1
	li $v0, 4
	syscall

	lw $ra, 4($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
	jr	$ra


g:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-12
	sw $ra, 4($sp)

	la $a0, str3
	li $v0, 4
	syscall

	jal	f
	lw	$t0, 0($sp)		#load return value from the stack
	sw	$t0,-4($sp)
	la $a0, str3
	li $v0, 4
	syscall


	lw $ra, 4($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
	jr	$ra

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-12
	sw $ra, 4($sp)

	jal	f
	lw	$t0, 0($sp)		#load return value from the stack
	sw	$t0,-8($sp)
	jal	g
	lw	$t0, 0($sp)		#load return value from the stack
	sw	$t0,-12($sp)
	li	$t0, 1
	sw	$t0,-16($sp)
	lw	$t0,-16($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 4($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)


	lw $ra, 4($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
exit:
	li $v0, 10
	syscall