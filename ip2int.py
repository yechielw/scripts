#!/bin/python
print(int(''.join(format(int(octet), '08b') for octet in __import__('sys').argv[1].split('.')), 2))
