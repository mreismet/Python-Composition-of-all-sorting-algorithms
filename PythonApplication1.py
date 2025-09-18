import csv
filename = "TextFile1.txt"
fields = []
rows = []
tempnumber = 0

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)
    for row in csvreader:
      rows.append(row)

print('Field names are: ' + ', '.join(fields))
for i in range(len(rows)):
    value = int(rows[i][4]) * 0.5
    rows[i][5] = ((int(rows[i][2]) + (value))) / (int(rows[i][3]) + int(rows[i][2]))

n = len(rows)
while(n > 0):
  for i in range(0,len(rows) - 1):
      if(float(rows[i][5]) > float(rows[i+1][5])):
          if(int(rows[i][0]) > int(rows[i+1][0])):
            tempnumber = rows[i+1][0]
            rows[i + 1][0] = rows[i][0]
            rows[i][0] = tempnumber
      elif(float(rows[i][5]) < float(rows[i+1][5])):
          if(int(rows[i][0]) > int(rows[i+1][0])):
            tempnumber = rows[i][0]
            rows[i][0] = rows[i + 1][0]
            rows[i + 1][0] = tempnumber
            rows.insert(i,rows.pop(i+1))
      elif(float(rows[i][5]) == float(rows[i+1][5])):
        if((int(rows[i][6]) - int(rows[i][7])) < (int(rows[i+1][6]) - int(rows[i+1][7]))):
            if(int(rows[i][0]) > int(rows[i+1][0])):
              tempnumber = rows[i][0]
              rows[i][0] = rows[i + 1][0]
              rows[i + 1][0] = tempnumber
            rows.insert(i - 1,rows.pop(i + 1))
        else:
          if(int(rows[i][0]) > int(rows[i+1][0])):
            tempnumber = rows[i][0]
            rows[i][0] = rows[i + 1][0]
            rows[i + 1][0] = tempnumber
  n = n - 1

for row in rows[:32]:
  for col in row:
      print(col, end =" ")
  print('\n')

