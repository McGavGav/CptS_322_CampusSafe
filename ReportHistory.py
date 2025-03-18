import csv 

def viewReportHistory (filename = "reports.csv"):
    try:
        with open(filename, mode= 'r') as file:
            reader = csv.reader(file)
            next(reader)
            print("\n Campus Safety Report: ")
            for row in reader:
                title, description, location, date = row
                print(f"\nTitle: {title}\n Description: {description}\n Location: {location}\n Date Reported:{date}\n")

    except FileNotFoundError:
        print ("Error: file not found")


viewReportHistory() 