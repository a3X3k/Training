extern printf
extern scanf

section .data
	fmt: db "%d", 0
	output1 : db "Enter the N : ",0
	output2 : db "N is %d",10,0
	output3 : db "Fibonacci is %d",10,0

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

	mov ecx,2
	mov eax,0
	mov ebx,1 

	add dword [ebp-0x4],1

	L1:
	
	add eax,ebx
	mov edx,eax

	mov eax,ebx
	mov ebx,edx

	add ecx,1
	cmp ecx,dword [ebp-0x4]
	
	jl L1

	push edx
	push output3
	call printf

	leave
	ret
