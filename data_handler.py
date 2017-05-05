import csv

# This module is for import only!


def write_csv(file, data):
    """Writes the data parameter into the file parameter."""

    with open(file, "w", newline="") as text:
        spamwriter = csv.writer(text)
        for story in data:
            spamwriter.writerow(story)


def read_csv(file):
    """Reads the .csv from file."""

    with open(file, "r") as text:
        spamreader = csv.reader(text)
        requested_data = list(spamreader)
    return requested_data


def append_csv(file, content):
    """Appends the content to the file parameter."""

    with open(file, "a", newline="") as text:
        spamwriter = csv.writer(text)
        spamwriter.writerow(content)
