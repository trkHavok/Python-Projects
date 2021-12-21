def calc_total_inches(num_feet, num_inches):
    num_inches = num_inches + (num_feet * 12)
    return(num_inches)

feet = int(input("How many Feets?"))
inches = int(input("How many Inches?"))
print('Total inches:', calc_total_inches(feet, inches))