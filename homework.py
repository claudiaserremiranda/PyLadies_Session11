import argparse

parser = argparse.ArgumentParser(description='argparse add line numbers on text')
parser.add_argument("input_file", default=None, help=("Input file to read"))
parser.add_argument("-n", "--number", help="number on first line", required=True, type=int)
parser.add_argument("--space", action="store_true", help=("adds an extra line between each line")) #boolean flag and optional

args = parser.parse_args()

def addlines(input_file, number, space=False):
    with open('output_file.txt', mode='a', encoding='utf-8') as output_file:
        source = open(input_file, encoding='utf-8')
        content = source.readlines()
        for line in content:
            if space:
                output_file.writelines(f"{number} {line}\n")
            else:
                output_file.writelines(f"{number} {line}")
            number = number + 1
        source.close()  

addlines(args.input_file, args.number, args.space)

