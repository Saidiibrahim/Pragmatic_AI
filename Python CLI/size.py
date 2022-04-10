import os
import sys

def main(file):
    bytes_size = os.path.getsize(file)
    mb_size = int(bytes_size/1024**2)
    print(mb_size, "MB")


if __name__ == '__main__': # If this script is executed in terminal, then run lines below
    if len(sys.argv) == 1:
        print("""
        This is a CLI tool that calculates file sizes
        and it takes a single argument
        """)
        sys.exit(0) # So that the program terminates here
    file = sys.argv[-1]
    main(file)