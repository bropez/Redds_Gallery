import csv

data_reader = csv.reader(open('out.csv'))
no_empties = []
# this is stripping the empty sets and new lines I created
for set in data_reader:
    if set != [] and '\n' not in set:
        no_empties.append(set)

# this deletes the ad that I didn't know about but caused havoc
for i, set in enumerate(no_empties):
    if "<script" in set[0]:
        del(no_empties[i])


# this strips everything and formats them into strings for whatever reason
for i, set in enumerate(no_empties):
    if len(set) is 5:
         no_empties[i] = set[4]
    elif ".jpg" in set[0]:
        no_empties[i] = "https://www.thonky.com/animal-crossing-new-leaf/" + set[0][10:-3]
    else:
        no_empties[i] = set[0]


# this is taking out all the quotation marks
for i, set in enumerate(no_empties):
    if '"' in set[0]:
        no_empties[i] = no_empties[i].strip('"')


def chunk_it(l, n):
    """
    A method to chunk out the current list into smaller sublists
    Thanks to Chris Albon for the code
    https://chrisalbon.com/python/data_wrangling/break_list_into_chunks_of_equal_size/
    :param l: the list to chunk from
    :param n: the number of items you'd like in each chunk
    :return: no return, just yield the chunks
    """
    for i in range(0, len(l), n):
        yield l[i:i+n]


chunks = list(chunk_it(no_empties, 3))

for chunk in chunks:
    print(chunk)

# now we put the chunks into a csv file
with open("out2.csv", "w") as f:
    wr = csv.writer(f)
    for line in chunks:
        wr.writerow(line)