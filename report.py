import json
import os

def new_report():
    report = {}
    report["name"] = input("Enter your name: ")
    report["id"] = input("Enter WSU ID: ")
    report["location"] = input("Enter location of incident: ")
    report["description"] = input("Enter description of incident: ")
    report["time"] = input("Enter time of incident: ")

    file_path = "campus_safe_reports.json"
    
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as file:
            reports = json.load(file)
    else:
        reports = []

    reports.append(report)

    with open(file_path, "w") as file:
        json.dump(reports, file, indent=2)

if __name__ == "__main__":
    new_report()