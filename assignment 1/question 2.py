Gross_income = int(input("enter your gross income : "))
Standard_deduction = 10000
Number_of_dependents = int(input("enter number of dependents"))
Additional_deduction =  Number_of_dependents*3000
Taxable_income = Gross_income - Standard_deduction - Additional_deduction
print("Taxablei ncome : ",str(Taxable_income))
Tax_rate = 0.20
Tax = Taxable_income*Tax_rate
print("Tax :", str(Tax))
