#!/usr/bin/env python3

from checksumdir import dirhash
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        directory = sys.argv[1]
        md5hash = dirhash(directory, "md5")
        print(md5hash)
