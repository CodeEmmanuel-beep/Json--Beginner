import math
import statistics
import os
import called
import json
from datetime import datetime

print(
    "                                    Sales Calculator: John's Electronics Superstore                                                        "
)
File_path = r"C:\Users\HP\Desktop\PythonBackend\WeekOne\Shaw.json"
if os.path.exists(File_path):
    with open(File_path, "r") as f:
        Shaw = json.load(f)
        if isinstance(Shaw, dict):
            Shaw = [Shaw]
else:
    Shaw = []
Count = int(input("Enter desired numbers of operation: "))
print(f"This Series Of Calculation will be carried out for {Count} number of time(s)")
for i in range(Count):
    print(f"Ruuning Calculations {i+1} of {Count}")
    choice = input("Do you want to see previous data? yes/no: ").strip().lower()
    if choice == "yes":
        if not Shaw:
            print(f"\nNo Previous Data")
        else:
            print(f"\nPrevious Result:")
            for index, value in enumerate(Shaw, start=1):
                print(
                    f"{index}. {value['timestamp']} {value['operation']} {value['result']}"
                )
                continue
    sales = input("Enter Sales or type 'exit': ").split()
    if sales[0].lower() == "exit":
        break
    sales = [float(s) for s in sales]
    print("Operations: \nadd \navg \nbest \nworst \nrange \nfreq \nbonus \nrate")
    operation = input("Choose Operation:")
    if operation == "rate":
        rate = float(input("Enter rate: "))
        result = called.tax(sales, rate, operation)
        print(result)
    else:
        result = called.analyze(sales, operation)
        print(result)
    Quit = input("Do you want to continue y/n?: ").strip().lower()
    if not isinstance(result, (str, int, float, list, dict)):
        result = str(result)
    result = str(result)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Shaw.append(
        {"operation": str(operation), "timestamp": timestamp, "result": str(result)}
    )
    print(f"saved {operation} = {result} ({timestamp})")
    if Quit == "n":
        break
with open(File_path, "w") as f:
    json.dump(Shaw, f, indent=2, ensure_ascii=False)
print("All Result Saved Bye")
