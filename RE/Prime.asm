extern printf
extern scanf

section .data
	fmt: db "%d", 0
	output1 : db "Enter the N : ",0
	output2 : db "N is %d",10,0
	output3 : db "Neither Prime Nor Composite!",10,0
	output4 : db "Its a Prime",10,0
	output5 : db "Its Not Prime",10,0
	output6 : db "Its a Invalid Number",10,0

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

	mov ecx, dword[ebp-0x4]
    	dec ecx

	cmp dword [ebp-0x4],0
	jle INVALID

	cmp dword [ebp-0x4],1
	je EQUAL

	mov ebx, 2
    	mov eax, dword[ebp-0x4]
    	cmp eax, 2
    	jg CHECK
    	je PRIME

	CHECK:
	mov eax, dword[ebp-0x4]
   	mov edx, 0
   	div ebx
    	cmp edx, 0
    	je NOTPRIME

    	cmp ebx, ecx
    	je PRIME

    	inc ebx
   	jmp CHECK

	PRIME:
	push output4
	call printf
    	leave
    	ret

	NOTPRIME:
	push output5
	call printf
    	leave
    	ret

	INVALID:
	push output6
	call printf
    	leave
    	ret
	
	EQUAL:
	push output3
	call printf
    	leave
    	ret
	
	leave
	ret

