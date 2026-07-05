import pandas as pd

print("\nChoose File Type: ")
print("1. CSV File")
print("2. Excel File")

file_type = input("\nEnter Your Choice (1-2): ")

try:
    if file_type == "1":
        file_name = input("\nEnter CSV File Name (with .csv extension): ")
        df = pd.read_csv(file_name)

    elif file_type == "2":
        file_name = input("\nEnter Excel File Name (with .xlsx extension): ")
        df = pd.read_excel(file_name)

    else:
        print("Invalid File Type! Exiting...")
        exit()
    print("\nFile Loaded Successfully!")

except FileNotFoundError:
    print("\nError: File Not Found!")
    exit()

except Exception as e:
    print("\nError:", e)
    exit()


def preview_data():

    print("\n========== DATA PREVIEW ==========")

    rows, columns = df.shape

    print("\nTotal Rows :", rows)
    print("Total Columns :", columns)

    print("\nColumn Names:")
    for col in df.columns:
        print(col)

    print("\nFirst 5 Rows:")
    print(df.head())


def analyze_column():

    numeric_columns = df.select_dtypes(include="number").columns

    print("\nAvailable Numeric Columns:")
    for col in numeric_columns:
        print(col)

    column = input("\nEnter Column Name: ")

    if column not in numeric_columns:
        print("Invalid Column Name!")
        return

    print("\nChoose Operation")
    print("1. Total (Sum)")
    print("2. Average (Mean)")
    print("3. Minimum")
    print("4. Maximum")
    print("5. Count")

    operation = input("Enter Choice (1-5): ")

    if operation == "1":
        print("Total =", df[column].sum())

    elif operation == "2":
        print("Average =", df[column].mean())

    elif operation == "3":
        print("Minimum =", df[column].min())

    elif operation == "4":
        print("Maximum =", df[column].max())

    elif operation == "5":
        print("Count =", df[column].count())

    else:
        print("Invalid Operation!")


def check_missing_values():

    print("\nAvailable Columns:")

    for col in df.columns:
        print(col)

    column = input("\nEnter Column Name: ")

    if column in df.columns:

        missing = df[column].isnull().sum()

        print("\nMissing Values in", column, "=", missing)

    else:
        print("Invalid Column Name!")


while True:
    print(" \nData Analytics Tool: ")
  
    print("1. Preview Data")
    print("2. Analyze Numeric Column")
    print("3. Check Missing Values")
    print("4. Exit")

    choice = input("\nEnter Your Choice (1-4): ")

    if choice == "1":
        preview_data()

    elif choice == "2":
        analyze_column()

    elif choice == "3":
        check_missing_values()

    elif choice == "4":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")