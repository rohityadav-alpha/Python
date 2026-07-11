#Question 5: Given student dictionary, ask for a key. Print value if found otherwise Invalid Key.
student_dict={"name":"rohit",
              "age":23,
              "cource":"python"}
key=input("Enter keyword :")
if key in student_dict.keys():
    print(student_dict[key])
else:
    print("invalid")
