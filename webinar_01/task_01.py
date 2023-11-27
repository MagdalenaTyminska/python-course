# working time calculation
from csv import DictReader
from datetime import datetime

employee_report = {}

# a - append , w - delete & write
with open('logs.txt', 'r', encoding='utf8') as file:
    reader = DictReader(file)
    for row in reader:
        # parse string to time
        start_date = datetime.strptime(row['Start Date'], '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(row['End Date'], '%Y-%m-%d %H:%M:%S')
        employee = row['Employee']
        customer = row['Client Name']
        time_delta = end_date - start_date

        if employee in employee_report:
            employee_report[employee] += time_delta
        else:
            employee_report[employee] = time_delta

for employee, duration in employee_report.items():
    # divmod - modulo
    hours, remainder = divmod(duration.total_seconds(), 3600)
    #_ not needed value
    minutes, _ = divmod(remainder, 60)
    print('Working time', employee, int(hours), 'hours', int(minutes), 'minutes')