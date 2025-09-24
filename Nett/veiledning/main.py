from pathlib import Path
import csv

# Read file:
path = Path("bokutlån.csv")
with open("bokutlån.csv", "r", encoding="utf-8") as csv_file:
    line = path.read_text().splitlines()

    reader = csv.reader(line)
    header_row = next(reader)
    print(header_row)

    print("\n")

    for index, clumn_header in enumerate(header_row):
        print(index, clumn_header)

    try:
        if index == 0:
            pass

        loan_periods = []
        extended_days = []

        for row in reader:
            loan = int(row[5])
            loan_periods.append(loan)
            extend_day = int(row[6])
            extended_days.append(extend_day)
    except ValueError:
        pass
    except Exception as e:
        pass
    # print(loan_periods)
    # print(extended_days)

    loan_periods_total = sum(loan_periods)
    extended_days_total = sum(extended_days)

    total_amount_of_days = sum(loan_periods + extended_days)
    total_days_int = int(total_amount_of_days)
    print(
        f"\nThe total amount of days books have been loaned out is:\n{total_amount_of_days}.")

    print("The average amount of days book have been loaned out:")
    print(total_days_int / 2)


__name__ == "__main__"
list = read_file()
sortByDate(list)
