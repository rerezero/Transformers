#!/usr/bin/env python3
import argparse, sys
from pathlib import Path
from .model import Summarizer
from .utils import read_text

def parse_args(argv=None):
    ap = argparse.ArgumentParser(
        prog="mini-transformer",
        description="Текстийг богино дүгнэлт болгон хувиргах CLI хэрэгсэл"
    )
    ap.add_argument("-i", "--input",
                    help="Оролтын файл (заавал биш). Хоосон бол stdin ашиглана.")
    ap.add_argument("-o", "--output",
                    help="Дүгнэлтийг хадгалах файл (заавал биш).")
    return ap.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)
    text = read_text(args.input)
    summarizer = Summarizer()
    summary = summarizer(text)

    if args.output:
        Summarizer.save(summary, Path(args.output))
    print("=== SUMMARY ===")
    print(summary)

if __name__ == "__main__":
    sys.exit(main())

