#!/usr/bin/python

# Markdown Table Of Content (TOC) Generator

import sys

def generate_TOC():
    print(md_toc.build_toc(sys.argv[1]), end='')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Bad CLI args (Require md file).")
        exit(1)
    generate_TOC()
