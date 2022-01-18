annual_salary=float(input("Enter your annual alary:"))
portion_saved=float('0'+input("Enter the percent of your salary to save,as a decimal:"))
total_cost=float(input("Enter the cost of your dream home:"))
semi_annual_raise=float('0'+input("Enter the sami_annual raise,as a decimal:"))
current_savings=0
part_down_payment=0.25*total_cost
months=0
r=0.04
while current_savings<part_down_payment:
    current_savings=current_savings+current_savings*r/12
    current_savings=current_savings+portion_saved*annual_salary/12
    months=months+1
    if months%6==0:
        annual_salary=annual_salary*(1+semi_annual_raise)
print("Number of months:",months)
    
