import matplotlib 
import math
import os
import argparse


def print_colored_text(text, color_code=37):
    '''
    Color Codes:
    30 - Black
    31 - Red
    32 - Green
    33 - Yellow
    34 - Blue
    35 - Magenta
    36 - Cyan
    37 - White
    '''
    print(f"\033[{color_code}m{text}\033[0m")

def square_generator():

def main():


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processing selected arguments ...")
    parser.add_argument("-square_nums", "-i" , required=False, help="Input square's number")
    parser.add_argument("-size" , "-z" , required=False , help="Input picture size")
    parser.add_argument("-save" , "-s" , required=False , help="Do you want to save the generated picture or not?")


square_nums = 