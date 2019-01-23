import random

## 1 user selects starting path
## 2 load lists for paths
## 3 use random to select and pop off element description and add to output list
## 3b add stat changes to output list
## 4 check element for table change
## 5 if table change is needed change active table
## 6 repeat until 12 items in output list

base_stat_value = 10

#todo setup the selection input with proper error handling or move the front end of this to a Django site or use a CLI frontend tool?

# active_table = input("1. Academic Path \n 2. Life Experience Path \n 3. Military Path \n Choose your life path:")
active_table = "AC"

#todo make this table populated from import from csv files
master_tables = {
    "AC": [["Caught with banned books. Expelled. Move to Life Experience Table.", [0,0,0,0,0,0], "NONE"],
    ["Developed a drug habit.", [0,0,-1,0,1,0], "NONE"],
    ["Joined scientific expedition for month.", [1,0,0,0,0,0], "NONE"]],
    "LE": [],
    "ML": []
}


active_path = master_tables[active_table]
output_list = []

while len(output_list) != 2:

    #Takes path table, shuffles, and grabs a random element
    random.shuffle(active_path)
    new_item = active_path.pop()

    #adds newelement to growing list
    output_list.append(new_item)

    #changes table selection if needed
    if new_item[2] != "NONE":
        #master dictonary with tables
        active_table = new_item[2]
        active_path = master_tables[active_table]

print(output_list)


#tallies stat point changes
base_stats = [base_stat_value] * 6
for item in output_list:
    base_stats[0] += item[1][0]
    base_stats[1] += item[1][1]
    base_stats[2] += item[1][2]
    base_stats[3] += item[1][3]
    base_stats[4] += item[1][4]
    base_stats[5] += item[1][5]
print(base_stats)

#todo encapsulate things into functions/classes?