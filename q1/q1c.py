def fix_message_data(data: bytes) -> bytes:
    """
    Implement this function to return the "fixed" message content. This message
    should have minimal differences from the original message, but should pass
    the check of `msgcheck`.

    The fix in this file should be *different* than the fix in q1b.py.

    :param data: The source message data.
    :return: The fixed message data.
    """
    data = bytearray(data)
    count = data[0]
    total = data[1]
    
    for i in range(count):
        if (2+i)<len(data):
            total ^= data[2 + i]
    
    # Add a new byte that makes total == 120
    fix_byte = total ^ 120
    if (count<len(data)):
        data[count+2] = fix_byte
    else:
        data.append(fix_byte)  # byte to cancel the error
    data[0] = count + 1  # update count
    return bytes(data)


def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    fixed_data = fix_message_data(data)
    with open(path + '.fixed', 'wb') as writer:
        writer.write(fixed_data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    fix_message(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
