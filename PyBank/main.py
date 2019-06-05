import os
import csv
csvpath = os.path.join('PyBank/budget_data.csv')

with open(csvpath, newline='') as csvfile:

    #split data into columns
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    header = next(csvreader)
    #print(f"CSV Header: {header}")

    # define list
    nets = []
    dates = []
   
    # Loop throgh rows and creat the list 'nets'
    for row in csvreader:  
        net = int(row[1])
        nets.append(net) 
        date = str(row[0])
        dates.append(date)

        change = [nets[i + 1] - nets[i] for i in range(len(nets)-1)] 
        
    # summary values
    count = len(nets)
    total = sum(nets)
    minimum = min(change)
    maximum = max(change)
    avg_change = round(sum(change)/(len(change)),2)
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total}")
    print(f"Average  Change: ${avg_change}")
    print(f"Greatest Decrease in Profits: $({maximum})")
    print(f"Greatest Increase in Profits: $({minimum})")
