import json
import csv
#json files are for dictionaries specificially
txt_data = "I like ice cream." 
#employees = ["Eugene", "patrick", "squiffart"]
file_path = "student_data.csv"
'''employee2 = {
    "name": "david",
    "age" : "30",
    'JOB' : "FRYCOOK"

}'''

employee3 = [
['Name', 'age', 'job'],
['Spngebobby', '32', 'cheif frycook'],
['Squidbooby', '23', 'register'],
['Patrick', '43', 'customer specialist'],
['David', '54', 'manager']
]





with open(file_path, "w", newline="") as file:
    #for employee in employees:
       # f.write("\n" + employee)
    #json.dump(employee2,file, indent=" ")
    #f.write("\n" + txt_data)
    writer = csv.writer(file)
    for row in employee3:
        writer.writerow(row)
    print(f"Data written to {file_path}")