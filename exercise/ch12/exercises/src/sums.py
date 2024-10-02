# add the numbers in `data.txt`
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    "--input-file",
    default="data.txt",
    dest="input_file"
)


def main(args):
    sum = 0.0
    with open(args.input_file, "r") as file:
        for line in file:
            number = float(line)
            sum += number
    print(f"{sum:.2f}")


if __name__ == "__main__":
    main(parser.parse_args())
