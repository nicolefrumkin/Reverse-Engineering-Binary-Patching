def patch_program_data(program: bytes) -> bytes:
    """
    Implement this function to return the patched program. This program should
    return 0 for all input files.

    The fix in this file should be *different* than the fix in q1d.py.

    :param data: The bytes of the source program.
    :return: The bytes of the patched program.
    """
    data = bytearray(program)

    # Search for 'mov eax, 1' and replace it with 'mov eax, 0'
    for i in range(len(program) - 4):
        if (data[i] == 0xB8 and data[i+1] == 0x01 and data[i+2] == 0x00 and data[i+3] == 0x00 and data[i+4] == 0x00):
            data[i+1:i+5] = b'\x00\x00\x00\x00'
            return bytes(data)


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
