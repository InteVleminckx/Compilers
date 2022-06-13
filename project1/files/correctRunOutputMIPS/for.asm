.data
str1:	.asciiz	"\n"

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-16
	sw $ra, 8($sp)

	li	$t0, 0
	sw	$t0,4($sp)
	b __WHILE_CONDITION_0__

__WHILE_CONDITION_0__:
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-4($sp)
	li	$t0, 10
	sw	$t0,-8($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	lw	$t1,-8($sp)		#load local variable or temp register from stack
	slt	$t0, $t0, $t1
	sw	$t0,-4($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __WHILE_1__
	beq	$t0, 0, __END_WHILE_2__

__WHILE_1__:
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-8($sp)
	lw	$t0,-8($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	lw	$t0,4($sp)		#load local variable or temp register from stack
	add	$t0	,$t0,1
	sw	$t0,4($sp)
	b __WHILE_CONDITION_0__

__END_WHILE_2__:
	li	$t0, 0
	sw	$t0,-12($sp)
	lw	$t0,-12($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 8($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)

exit:
	li $v0, 10
	syscall