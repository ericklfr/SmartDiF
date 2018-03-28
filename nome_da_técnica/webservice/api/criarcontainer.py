from __future__ import print_function
import sys
import json


def main():
    total = int(sys.argv[1]) + int(sys.argv[2])
    print(total, end='')

if __name__ == "__main__":
    main()
    sys.exit(0)