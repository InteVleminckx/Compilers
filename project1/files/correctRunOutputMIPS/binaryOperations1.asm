.data
str1:	.asciiz	"; "
fl0:	.float	10.0

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-12
	sw $ra, 4($sp)

	li	$t0, 10
	sw	$t0,-4($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	l.s	$f0, fl0
	swc1	$f0,-8($sp)
	lwc1	$f0,-8($sp)		#load local variable or temp register from stack
	mov.s $f12, $f0
	li $v0, 2
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	li	$t0, 10
	sw	$t0,-12($sp)
	lw	$t0,-12($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	l.s	$f0, fl0
	swc1	$f0,-16($sp)
	lwc1	$f0,-16($sp)		#load local variable or temp register from stack
	mov.s $f12, $f0
	li $v0, 2
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	li	$t0, 10
	sw	$t0,-20($sp)
	lw	$t0,-20($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	l.s	$f0, fl0
	swc1	$f0,-24($sp)
	lwc1	$f0,-24($sp)		#load local variable or temp register from stack
	mov.s $f12, $f0
	li $v0, 2
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	li	$t0, 10
	sw	$t0,-28($sp)
	lw	$t0,-28($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	l.s	$f0, fl0
	swc1	$f0,-32($sp)
	lwc1	$f0,-32($sp)		#load local variable or temp register from stack
	mov.s $f12, $f0
	li $v0, 2
	syscall

	la $a0, str1
	li $v0, 4
	syscall

	li	$t0, 1
	sw	$t0,-36($sp)
	lw	$t0,-36($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 4($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)

exit:
	li $v0, 10
	syscall