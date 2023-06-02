try:
    country_file = open("demo.txt", "w")
    #print(country_file.writable())
    # country_file.write("South Africa")

    country_file.write("Canada")
    print(country_file)
except ValueError:
    print("something went wrong")
finally:
    print("File has been written to successfuly")

# create a new file and write to it
try:
    my_new_country_file = open("newDemo.txt", "w")
    my_new_country_file.write("This is my new demo text file")
except ValueError:
    print("something went wrong")
finally: print("File was created and written to successfuly")

#append new value to new file created
try:
    appendNew = open("newDemo.txt", "+a")
    appendNew.write("\nThis is a new value added to the file")
except ValueError: print("Something went wrong so couldn't append")
finally: print("Append successfuly")
