.data
str1:	.asciiz	"Enter a number:"
str4:	.asciiz	"fib("
str5:	.asciiz	")\t= "
str6:	.asciiz	";\n"
str2:	.asciiz	"%d"

.text
.globl main

f:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-16
	sw $ra, 8($sp)

	lw	$t0,4($fp)		#load function argument from stack
	sw	$t0,4($sp)
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-4($sp)
	li	$t0, 2
	sw	$t0,-8($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	lw	$t1,-8($sp)		#load local variable or temp register from stack
	slt	$t0, $t0, $t1
	sw	$t0,-4($sp)
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __IF_0__
	beq	$t0, 0, __ELSE_1__

__IF_0__:
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-8($sp)
	lw	$t0,-8($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 8($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
	jr	$ra


	b __END_IF_ELSE_2__

__ELSE_1__:
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-12($sp)
	li	$t0, 1
	sw	$t0,-16($sp)
	lw	$t0,-12($sp)		#load local variable or temp register from stack
	lw	$t1,-16($sp)		#load local variable or temp register from stack
	sub	$t0	,$t0,$t1
	sw	$t0,-12($sp)
	addi	$sp, $sp, -8
	lw	$t0,-4($sp)		#load local variable or temp register from stack
	sw	$t0,4($sp)		#add function argument to the stack  
	jal	f
	lw	$t0, 0($sp)		#load return value from the stack
	addi	$sp, $sp, 8
	sw	$t0,-16($sp)
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-20($sp)
	li	$t0, 2
	sw	$t0,-24($sp)
	lw	$t0,-20($sp)		#load local variable or temp register from stack
	lw	$t1,-24($sp)		#load local variable or temp register from stack
	sub	$t0	,$t0,$t1
	sw	$t0,-20($sp)
	addi	$sp, $sp, -8
	lw	$t0,-12($sp)		#load local variable or temp register from stack
	sw	$t0,4($sp)		#add function argument to the stack  
	jal	f
	lw	$t0, 0($sp)		#load return value from the stack
	addi	$sp, $sp, 8
	sw	$t0,-24($sp)
	lw	$t0,-16($sp)		#load local variable or temp register from stack
	lw	$t1,-24($sp)		#load local variable or temp register from stack
	add	$t0	,$t0,$t1
	sw	$t0,-20($sp)
	lw	$t0,-20($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 8($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
	jr	$ra


	b __END_IF_ELSE_2__

__END_IF_ELSE_2__:

	lw $ra, 8($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
	jr	$ra

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-20
	sw $ra, 12($sp)

	la $a0, str1
	li $v0, 4
	syscall

	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-24($sp)
	li $v0, 5
	syscall
	move $t0, $v0
	sw	$t0,4($sp)
	li	$t0, 1
	sw	$t0,8($sp)
	b __WHILE_CONDITION_0__

__WHILE_CONDITION_0__:
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-28($sp)
	lw	$t0,-28($sp)		#load local variable or temp register from stack
	add	$t0	,$t0,1
	sw	$t0,8($sp)
	lw	$t0,4($sp)		#load local variable or temp register from stack
	sw	$t0,-32($sp)
	lw	$t0,-28($sp)		#load local variable or temp register from stack
	lw	$t1,-32($sp)		#load local variable or temp register from stack
	sle	$t0, $t0, $t1
	sw	$t0,-28($sp)
	lw	$t0,-28($sp)		#load local variable or temp register from stack
	beq	$t0, 1, __WHILE_1__
	beq	$t0, 0, __END_WHILE_2__

__WHILE_1__:
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-32($sp)
	lw	$t0,8($sp)		#load local variable or temp register from stack
	sw	$t0,-36($sp)
	addi	$sp, $sp, -8
	lw	$t0,-28($sp)		#load local variable or temp register from stack
	sw	$t0,4($sp)		#add function argument to the stack  
	jal	f
	lw	$t0, 0($sp)		#load return value from the stack
	addi	$sp, $sp, 8
	sw	$t0,-40($sp)
	la $a0, str4
	li $v0, 4
	syscall

	lw	$t0,-32($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str5
	li $v0, 4
	syscall

	lw	$t0,-40($sp)		#load local variable or temp register from stack
	la $a0, ($t0)
	li $v0, 1
	syscall

	la $a0, str6
	li $v0, 4
	syscall

	b __WHILE_CONDITION_0__

__END_WHILE_2__:
	li	$t0, 0
	sw	$t0,-44($sp)
	lw	$t0,-44($sp)		#load local variable or temp register from stack

	sw	$t0, 0($fp)		#add return value on the stack
	lw $ra, 12($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)


	lw $ra, 12($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
exit:
	li $v0, 10
	syscall