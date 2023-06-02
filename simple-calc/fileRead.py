#read file 'r'
#write to file 'w'
#append to file 'a'
#read and write to file 'r+'

try:
    country_fle = open("demo.txt", "r")
    print(country_fle.readable())
    # print(country_fle.readline())
    # print(country_fle.readline())
    #print(country_fle.readlines()[1:4])
    for lines in country_fle.readlines():
        print(lines)
        # if len(lines) <= 2:
        #     break
        # print(lines)

except ValueError:
    print("Something went wrong")

else: print("File is readable")
country_fle.close()