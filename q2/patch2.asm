JMP 109 # jump to 0x804863A (the jmp opcode is relative to the position)

cmp byte ptr [eax], '#'       # Check if first char is '#'
jne print_line
cmp byte ptr [eax + 1], '!'   # Check if second char is '!'
jne print_line

add eax, 2                    # Skip "#!"
push eax                      # system(line + 2)
call -365                     # system call (jump to 0x08048460)
add esp, 4                    # Clean stack
jmp 146                       # jump to 0x0804865F

print_line:
jmp 109                       # jump to 0x0804863A  


