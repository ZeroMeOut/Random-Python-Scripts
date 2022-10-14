test2_file = open("test2.txt", "a")  # "a" makes the file appendable
test3_file = open("test3.txt", "w")  # "w" overrides the file

test2_file.write("That is cap\n")  # Appends existing file
test3_file.write("That is op")  # Overrides/Creates file

test2_file.close()
test3_file.close()