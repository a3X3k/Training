extern printf
extern scanf

section .data
	fmt: db "%d", 0
	output1: db "Addition is %d",10,0
	output2: db "Subtraction is %d",10,0
	output3: db "Multiplication is %d",10,0
	;output4: db "EAX is %d",10,0
	;output5: db "EBX is %d",10,0
	output6: db "Division -- Quotient is %d",10,0
	;output7: db "Division -- Remainder is %d",10,0

section .text
	global main

	main:
	push ebp
	mov ebp, esp
	sub esp, 0x10

	lea eax, [ebp-0x4]
	push eax
	push fmt
	call scanf

	lea edx, [ebp-0x8]
	push edx
	push fmt
	call scanf

	mov ebx, dword [ebp-0x4]
	mov eax, dword [ebp-0x8]
	mov dword [ebp-0x12],ebx
	mov dword [ebp-0x16],eax
	
	add eax, ebx
	mov dword [ebp-0x8], eax
	
	sub eax,ebx
	sub ebx,eax
	mov dword [ebp-0x4], ebx

	push dword [ebp-0x8]
	push output1
	call printf

	push dword [ebp-0x4]
	push output2
	call printf

	mov eax,dword [ebp-0x12]
	mov ebx,dword [ebp-0x16]
	mul ebx
	mov dword [ebp-0x4], eax

	push dword [ebp-0x4]
	push output3
	call printf

	;push dword [ebp-0x12]
	;push output4
	;call printf

	;push dword [ebp-0x16]
	;push output5
	;call printf

	mov eax,dword [ebp-0x12]
	mov ebx,dword [ebp-0x16]
	mov edx,0
	div ebx
	push eax

	push output6
	call printf

	leave
	ret

