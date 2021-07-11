import csv
from os import listdir
from os.path import isfile, join

# Not going to read the file using csv since space is a valid character. Can do
# by counting indices instead.


def _read_file(filename):
    lines = []
    with open(filename) as f:
        line = f.readline().rstrip()
        while line != "":
            lines.append(line)
            line = f.readline()
    return lines


def transform_spaced_page(filename):
    """ Takes in a txt file containing pattern symbols where each is
        separated by space.

        Params:
            filename: the filename (without any types).
    """
    lines = _read_file(f"{filename}.txt")

    with_commas = [[char for count, char in enumerate(line) if count % 2 == 0]
                   for line in lines]

    with open(f"{filename}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(with_commas)


def convert_all_pages(folder):
    """ Converts all the pages found inside the specified folder. """
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    filenames = [f'{folder}{name.replace(".txt", "")}' for name in onlyfiles]
    for filename in filenames:
        transform_spaced_page(filename)


if __name__ == "__main__":
    convert_all_pages("pages/Hyacinth_Hippo/")
