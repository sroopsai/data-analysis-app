import csv


def main():
    data = csv.DictReader(open("Emissions.csv"), "rt")
    for row in data:
        print(row)


if __name__ == "__main__":
    main()
