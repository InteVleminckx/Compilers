.data
str1:	.asciiz	"Enter the number of prime numbers required\n"
str4:	.asciiz	"First "
str5:	.asciiz	" prime numbers are :\n"
str7:	.asciiz	"2\n"
str9:	.asciiz	"\n"
str2:	.asciiz	"%d"

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-32
	sw $ra, 24($sp)

	li	$t0, 3
	sw	$t0,8($sp)
	la $a0, str1
	li $v0, 4
	syscall

	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-4($sp)
	li $v0, 5
	syscall
	move $t0, $v0
	sw	$t0,4($sp)
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-8($sp)
	li	$t0, 1
	sw	$t0,-12($sp)
	lw	$t0,-8($sp)		#load local variable or temp register from stack
	lw	$t1,-12($sp)		#load local variable or temp register from stack
	sge	$t0, $t0, $t1
	sw	$t0,-8($sp)
	lw	$t0,-8($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __IF_0__
	beq	$t0, 0, __END_IF_1__

__IF_0__:
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-12($sp)
	la $a0, str4
	li $v0, 4
	syscall

	lw	$t0,-12($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str5
	li $v0, 4
	syscall

	la $a0, str7
	li $v0, 4
	syscall

	b __END_IF_1__

__END_IF_1__:
	li	$t0, 2
	sw	$t0,12($sp)
	b __WHILE_CONDITION_0__

__WHILE_CONDITION_0__:
	lw	$t0,12($sp)		#load local variable or temp register from stack
	sw	$t0,-16($sp)
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-20($sp)
	lw	$t0,-16($sp)		#load local variable or temp register from stack
	lw	$t1,-20($sp)		#load local variable or temp register from stack
	sle	$t0, $t0, $t1
	sw	$t0,-16($sp)
	lw	$t0,-16($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __WHILE_1__
	beq	$t0, 0, __END_WHILE_5__

__WHILE_1__:
	li	$t0, 2
	sw	$t0,20($sp)
	b __WHILE_CONDITION_2__

__WHILE_CONDITION_2__:
	lw	$t0,20($sp)		#load local variable or temp register from stack
	sw	$t0,-20($sp)
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-24($sp)
	li	$t0, 1
	sw	$t0,-28($sp)
	lw	$t0,-24($sp)		#load local variable or temp register from stack
	lw	$t1,-28($sp)		#load local variable or temp register from stack
	sub	$t0	,$t0,$t1
	sw	$t0,-24($sp)
	lw	$t0,-20($sp)		#load local variable or temp register from stack
	lw	$t1,-24($sp)		#load local variable or temp register from stack
	sle	$t0, $t0, $t1
	sw	$t0,-20($sp)
	lw	$t0,-20($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __WHILE_3__
	beq	$t0, 0, __END_WHILE_4__

__WHILE_3__:
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-24($sp)
	lw	$t0,20($sp)		#load local variable or temp register from stack
	sw	$t0,-28($sp)
	lw	$t0,-24($sp)		#load local variable or temp register from stack
	lw	$t1,-28($sp)		#load local variable or temp register from stack
	div	$t0,$t1 	#mod
	mfhi	 $t6  	# temp for the mod
	sw	$t6,-24($sp)
	li	$t0, 0
	sw	$t0,-28($sp)
	lw	$t0,-24($sp)		#load local variable or temp register from stack
	lw	$t1,-28($sp)		#load local variable or temp register from stack
	seq	$t0, $t0, $t1
	sw	$t0,-24($sp)
	lw	$t0,-24($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __IF_2__
	beq	$t0, 0, __END_IF_3__

__IF_2__:
	b __END_WHILE_4__

__END_IF_3__:
	lw	$t0,20($sp)		#load local variable or temp register from stack
	add	$t0	,$t0,1
	sw	$t0,20($sp)
	b __WHILE_CONDITION_2__

__END_WHILE_4__:
	lw	$t0,20($sp)		#load local variable or temp register from stack
	sw	$t0,-28($sp)
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-32($sp)
	lw	$t0,-28($sp)		#load local variable or temp register from stack
	lw	$t1,-32($sp)		#load local variable or temp register from stack
	seq	$t0, $t0, $t1
	sw	$t0,-28($sp)
	lw	$t0,-28($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __IF_4__
	beq	$t0, 0, __END_IF_5__

__IF_4__:
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-32($sp)
	lw	$t0,-32($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str9
	li $v0, 4
	syscall

	lw	$t0,12($sp)		#load local variable or temp register from stack
	add	$t0	,$t0,1
	sw	$t0,12($sp)
	b __END_IF_5__

__END_IF_5__:
	lw	$t0,8($sp)		#load local variable or temp register from stack
	add	$t0	,$t0,1
	sw	$t0,8($sp)
	b __WHILE_CONDITION_0__

__END_WHILE_5__:
	li	$t0, 0
	sw	$t0,-36($sp)
	lw	$t0,-36($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 24($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)

exit:
	li $v0, 10
	syscall