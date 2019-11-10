#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This program shows the power up to a number


def main():

    green = 0
    red = 0
    blue = 0

    for red in range(256):
        for green in range(256):
            for blue in range(256):
                print("RGB({0},{1},{2})".format(red, green, blue))


if __name__ == "__main__":
    main()
