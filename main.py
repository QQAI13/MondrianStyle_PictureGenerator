import argparse
import generator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processing selected arguments ...")
    parser.add_argument("-square_nums", "-i" , required=False, help="Input square's number")
    parser.add_argument("-height" , "-H" , required=False , help="Input picture's height")
    parser.add_argument("-width" , "-W" , required=False , help="Input picture's width")
    parser.add_argument("-save" , "-s" , required=False , help="Do you want to save the generated picture or not?")
    args = parser.parse_args()
    generator.window_generator()