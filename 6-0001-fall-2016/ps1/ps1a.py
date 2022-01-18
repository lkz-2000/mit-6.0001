annual_salary=float(input("Enter your annual alary:"))
portion_saved=float('0'+input("Enter the percent of your salary to save,as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))
current_savings=0
part_down_payment=0.25*total_cost
months=0
r=0.04
while current_savings<part_down_payment:
    current_savings=current_savings+current_savings*r/12
    current_savings=current_savings+portion_saved*annual_salary/12
    months=months+1
print("Number of months:",months)
    
