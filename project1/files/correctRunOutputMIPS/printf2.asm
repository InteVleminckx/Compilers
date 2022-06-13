.data
str3:	.asciiz	" "
str4:	.asciiz	"!\n"
str1:	.asciiz	"Hello"
str2:	.asciiz	"World"

.text
.globl main

main:
	sw	$fp, -4($sp)
	addi	$fp,$sp,0
	addi	$sp,$sp,-12
	sw $ra, 4($sp)

	la $a0, str1
	li $v0, 4
	syscall

	la $a0, str3
	li $v0, 4
	syscall

	la $a0, str2
	li $v0, 4
	syscall

	la $a0, str4
	li $v0, 4
	syscall


	lw $ra, 4($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
exit:
	li $v0, 10
	syscall