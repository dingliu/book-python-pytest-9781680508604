# add the numbers in `data.txt`
from argparse import ArgumentParser, Namespace

parser = ArgumentParser()

parser.add_argument(
    "files",
    nargs="*",
    default=["data.txt"],
)


def main(args: Namespace):
    sum = 0.0
    for file_path in args.files:
        with open(file_path, "r") as file:
            for line in file:
                number = float(line)
                sum += number

    print(f"{sum:.2f}")


if __name__ == "__main__":
    main(parser.parse_args())
