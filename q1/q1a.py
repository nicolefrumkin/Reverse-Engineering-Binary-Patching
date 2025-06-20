def validate(input_bytes: bytes) -> bool:
    count = input_bytes[0]       # var_4
    total = input_bytes[1]       # var_9 is initialized to this

    for i in range(count):       # var_8 is the index
        if i+2 < len(input_bytes):  # Prevent out-of-bounds
            byte_to_xor = input_bytes[i+2]
            total ^= byte_to_xor

    return total == 0x78         

    
def check_message(path: str) -> bool:
    """
    Return True if `msgcheck` would return 0 for the file at the specified path,
    return False otherwise.
    :param path: The file path.
    :return: True or False.
    """
    with open(path, 'rb') as reader:
        # Read data from the file, do whatever magic you need
        data = reader.read()
        return validate(data)

def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
