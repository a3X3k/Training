extern printf
extern scanf

section .data
	fmt: db "%d", 0
	output1 : db "Enter the N : ",0
	output2 : db "N is %d",10,0
	output3 : db "Factorial is %d",10,0

section .text
	global main

	main:
	push ebp
	mov ebp, esp
	sub esp, 0x10

	push output1
	call printf
	
	lea eax, [ebp-0x4]
	push eax
	push fmt
	call scanf

	push dword [ebp-0x4]
	push output2
	call printf

	add dword [ebp-0x4],1
	mov ecx,1
	mov ebx,1
	
	L1:
	imul ebx,ecx
	add ecx,1
	
	cmp ecx,dword [ebp-0x4]
	jl L1

	push ebx
	push output3
	call printf

	leave
	ret
