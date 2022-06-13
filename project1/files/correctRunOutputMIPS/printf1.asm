.data
str1:	.asciiz	"Hello World!\n"

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


	lw $ra, 4($sp)
	addi	$sp,$fp,0
	lw	$fp, -4($sp)
exit:
	li $v0, 10
	syscall