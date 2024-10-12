
num_years = int(input("Enter number of years:"))
total_inches_rainfall = 0
total_months = 0

for year in range(1, num_years + 1):
    for month in range(1, 13):
        total_inches_rainfall = total_inches_rainfall + float(input(f"Enter the inches of rainfall for year {year} month {month}: "))
        total_months = total_months + 1

print(f"Number of months: {total_months}")
print(f"Total inches of rainfall: {total_inches_rainfall:.2f}")
print(f"Average rainfall per month: {total_inches_rainfall:.2f}")