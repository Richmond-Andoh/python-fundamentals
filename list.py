names = ["Richmond", "Osborn", "John", "Sakai"]
schools = list(("Saviour", "Baptist", "Christ Academy", "Corsa"))
schools[2] = "Future Leaders"
hobby = "Football"
print(names[0][3])
print(schools[3:4])
print(type(hobby))
print(schools)
print(len(schools))
print(names[-2])


my_list = ["Richmond", "John", "Andy", "Osborn", "Sakai"]
if "Sakai" and "John" in my_list:
    print("Yes they are included")
else:
    print("They are out the group")

