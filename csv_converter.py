import csv

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

    with open("{filename}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(with_commas)


def convert_all_pages(folder):
    """ Converts all the pages found inside the specified folder. """
    pass


if __name__ == "__main__":
    pass
#    fix_newlines("pages/Hyacinth_Hippo/page168.txt")


"""
def fix_newlines(filename):
    contents = _read_file(filename)

    contents_all = "".join(contents)
    contents_str = contents_all.replace("\n", " ")
    print(contents_str)

    desired_line_length = 55  # TODO: get from config
    # Go through them all
    with_commas = []
    current_line = []
    for count, char in enumerate(contents_str):
        print(f"{count}: {char}")
        if (count % 2 == 0):
            current_line.append(char)
            # Need to split if I've hit 55
            value = count // 2 + 1
            if value % desired_line_length == 0:
                with_commas.append(current_line)
                current_line = []

        # if count == 250:
        #     break

    with open("testing.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(with_commas)
"""
