#!/usr/bin/python3
import os
import argparse

parser = argparse.ArgumentParser(description="Update verion number...")

parser.add_argument("-u", action="store", dest="ver")


def main():
    args = parser.parse_args()
    filename = args.ver
    parts = filename.split(".")
    ext = parts[-1]
    subver = parts[-2]
    wo_ext = parts[0]
    wo_ext2 = wo_ext.split("_")
    version = wo_ext2.pop()
    new_name = "_".join(wo_ext2)
    new_subver = int(subver)
    new_subver += 1
    new_filename = f"{new_name}_{version}.{new_subver}.{ext}"
    os.rename(filename, new_filename)


if __name__ == "__main__":
    main()
    # test()
