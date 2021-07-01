import re
import csv
import sys


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python tournament.py CSVFILENAME TEXTFILENAME")

    # Open csv
    with open(sys.argv[1], "r") as database:
        # Find STRs
        columns = csv.reader(database)
        STRs = next(columns)[1:]

        # Look for STRs counts in sequences
        counts = {}
        with open(sys.argv[2], "r") as sequence:
            reader = sequence.read()
            for STR in STRs:
                # Find consecutive sequences with REGEX
                pat = "(?:{seq})+".format(seq=STR)
                find = re.findall(pat, reader)
                if find:
                    count = max(find, key=len)
                    counts[STR] = str(len(count) // len(STR))

    # Find match -> if all(item in person.items() for item in counts.items()):
    match = "No match"
    with open(sys.argv[1], "r") as database:
        reader = csv.DictReader(database)
        for person in reader:
            name = person.pop("name")
            if counts == person:
                match = name

    print(match)


if __name__ == "__main__":
    main()
