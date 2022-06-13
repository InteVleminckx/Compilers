.data
x:	.word 10
str1:	.asciiz	";"

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-20
	sw $ra, 12($sp)

	lw	$t0,4
	sw	$t0,-4($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	li	$t0, 20
	sw	$t0,4($sp)
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-8($sp)
	lw	$t0,-8($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	li	$t0, 30
	sw	$t0,4($sp)
	li	$t0, 1
	sw	$t0,-12($sp)
	lw	$t0,-12($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __IF_0__
	beq	$t0, 0, __END_IF_1__

__IF_0__:
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-16($sp)
	lw	$t0,-16($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	li	$t0, 40
	sw	$t0,8($sp)
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-20($sp)
	lw	$t0,-20($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	b __END_IF_1__

__END_IF_1__:
	li	$t0, 1
	sw	$t0,-24($sp)
	lw	$t0,-24($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 12($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)

exit:
	li $v0, 10
	syscall