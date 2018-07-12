import csv

# the output is pic/query name/fake desc
data_reader = csv.reader(open('out.csv'))
for row in data_reader:
    # this is eliminating the empty sets
    if not row:
        # print("List is empty")
        pass
    # this is eliminating the new lines
    elif "\n" in row:
        pass
    # this is printing the art's name
    elif "<br/>" in row:
        print(row[4][1:-1])
    # this works with the links for the pictures.
    elif "<img src=" in row[0]:
        print("https://www.thonky.com/animal-crossing-new-leaf/" + row[0][10:-3])
    # this prints the first item in the set. It's usually the information we need.
    else:
        print(row[0])
        print('\n')
    # print(row)
