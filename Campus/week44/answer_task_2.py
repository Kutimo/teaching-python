import csv


def analyze_grades(input_csv, output_file):
    """
    Analyze student grades from CSV and create a report.
    CSV format: Name,Math,Science,English
    """
    student_averages = []

    try:
        # Read CSV
        with open(input_csv, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    name = row.get("Name", "Unknown")
                    math = float(row.get("Math", 0))
                    science = float(row.get("Science", 0))
                    english = float(row.get("English", 0))

                    avg = (math + science + english) / 3
                    student_averages.append((name, avg))

                except ValueError:
                    # Handles non-numeric values or missing data
                    continue

        # Find highest and lowest
        if not student_averages:
            raise Exception("No valid student data found.")

        highest = max(student_averages, key=lambda x: x[1])
        lowest = min(student_averages, key=lambda x: x[1])

        # Write report
        with open(output_file, "w") as report:
            report.write("Grade Report\n")
            report.write("============\n")
            for name, avg in student_averages:
                report.write(f"{name}: Average = {avg:.2f}\n")
            report.write("\n")
            report.write(f"Highest Average: {highest[0]} ({highest[1]:.2f})\n")
            report.write(f"Lowest Average: {lowest[0]} ({lowest[1]:.2f})\n")

    except FileNotFoundError:
        print(f"Error: File '{input_csv}' not found.")
    except csv.Error as e:
        print(f"CSV error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Test the function
if __name__ == "__main__":
    analyze_grades('grades.csv', 'grade_report.txt')
    print("Report generated")
