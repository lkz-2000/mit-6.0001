a=float(input("Enter the starting salary:"))
annual_salary=a
total_cost=1000000
semi_annual_raise=0.07
current_savings=0
part_down_payment=0.25*total_cost
months=0
r=0.04
st=0
end=10000
portion_saved=0
cont=0
while part_down_payment-current_savings>100 or current_savings-part_down_payment>100:
    cont+=1
    portion_saved=(st+end)//2
    current_savings=0
    annual_salary=a
    for months in range(36):
        current_savings=current_savings+current_savings*r/12
        current_savings=current_savings+(portion_saved/10000)*annual_salary/12
        months=months+1
        if months%6==0:
            annual_salary=annual_salary*(1+semi_annual_raise)
    if current_savings<part_down_payment:
        st=portion_saved
    else:
        end=portion_saved
    if st==9999:
        print("It is not possible to pay the down payment in three years.")
        break
    if part_down_payment-current_savings<=100 and current_savings-part_down_payment<=100:
        print("Best savings rate:","0."+str(portion_saved))
        print("Steps in bisection search:",cont)
        
    