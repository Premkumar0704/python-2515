car_name="Mahindra Scorpio"
car_varient="Z2 E"
on_road_price= 1726297
down_payment = 200000
interest=10
p = loan_amount = on_road_price - down_payment
r = monthly_interest = ((interest/12)/100)
n = number_of_months =5
emi=(p*r*(1+r)**n /((1+r)**n)-1)
print(f"car name={"car_name"},varient={"car_varient"}")
print(f"price={"on_road_price"}")
print(down_payment)
print(interest)
print(emi)