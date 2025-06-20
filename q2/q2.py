from infosec.core import assemble


def patch_program_data(program: bytes) -> bytes:
    """
    Implement this function to return the patched program. This program should
    execute lines starting with #!, and print all other lines as-is.
    
    WARNING! THIS FUNCTION MUST WORK EVEN IF THE SOURCE PROGRAM IS PLACED IN A DIFFERENT PATH!
    Use the provided path to the source program, and avoid hard-coding the path in
    the exercise directory!

    Use the `assemble` module to translate assembly to bytes. For help, in the
    command line run:

        ipython3 -c 'from infosec.core import assemble; help(assemble)'

    :param data: The bytes of the source program.
    :return: The bytes of the patched program.
    """
    # Assemble our patches
    patch1 = assemble.assemble_file('patch1.asm')
    patch2 = assemble.assemble_file('patch2.asm')

    patch1_offset = 0x8048634 - 0x8048000
    patch2_offset = 0x80485CD - 0x8048000
    
    # Create a mutable copy of the program
    patched = bytearray(program)

    # Apply the patches
    patched[patch1_offset:patch1_offset + len(patch1)] = patch1
    patched[patch2_offset:patch2_offset + len(patch2)] = patch2 
    return bytes(patched)


def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    patched = patch_program_data(data)

    with open(path + '.patched', 'wb') as writer:
        writer.write(patched)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
