def patch_program_data(program: bytes) -> bytes:
    """
    Implement this function to return the patched program. This program should
    return 0 for all input files.

    :param data: The bytes of the source program.
    :return: The bytes of the patched program.
    """
    program = bytearray(program)
    for i in range(len(program) - 5):
        if (program[i] == 0x3A and program[i+1] == 0x45 and
            program[i+3] == 0x0F and program[i+4] == 0x94 and program[i+5] == 0xC0):

            # Replace with: mov al, 1 = B0 01, and pad with NOPs
            program[i] = 0xB0  # mov al, imm8
            program[i+1] = 0x01
            program[i+2] = 0x90  # nop
            program[i+3] = 0x90  # nop
            program[i+4] = 0x90  # nop
            program[i+5] = 0x90  # nop

            return bytes(program)


def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    patched = patch_program_data(data)
    with open(path + '.patched', 'wb') as writer:
        writer.write(patched)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msgcheck-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
