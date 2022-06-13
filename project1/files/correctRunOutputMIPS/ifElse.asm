.data
str1:	.asciiz	"Hello world!\n"
str4:	.asciiz	"Something went wrong"

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-16
	sw $ra, 8($sp)

	li	$t0, 5
	sw	$t0,4($sp)
	la $a0, str1
	li $v0, 4
	syscall

	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-4($sp)
	li	$t0, 5
	sw	$t0,-8($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	lw	$t1,-8($sp)		#load local variable or temp register from stack
	seq	$t0, $t0, $t1
	sw	$t0,-4($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __IF_0__
	beq	$t0, 0, __ELSE_1__

__IF_0__:
	la $a0, str1
	li $v0, 4
	syscall

	b __END_IF_ELSE_2__

__ELSE_1__:
	la $a0, str4
	li $v0, 4
	syscall

	b __END_IF_ELSE_2__

__END_IF_ELSE_2__:
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