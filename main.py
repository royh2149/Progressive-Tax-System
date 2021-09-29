from TaxLevel import *
from sys import exit

# levels = TaxLevel.generate_israel_tax_levels()

income = int(input("What was your annual income?\n"))  # get the user's income

# ask the user to select the tax levels
levels_source = int(input("What tax-levels to use?\n" + str(codes) + "\nYou may use 0 to use a file (csv, xlsx) as an input.\n"))

# determine how to generate the tax-levels table
if levels_source == 0:
    filename = input("Enter filename: ")  # get the csv  filename to use
    levels = TaxLevel.generate_tax_levels_from_csv(filename)  # generate the levels described in the csv file
elif levels_funcs.get(levels_source) is None:  # ensure the selected levels-system exists
    print("Invalid Tax Levels Source! Exiting...")
    exit(1)  # issue an error and exit
else:  # get the selected levels-system
    levels = levels_funcs.get(levels_source)

# calculate the tax the user has to pay and print it
print("The tax you need to pay, before bonuses, refunds, etc. is %.2f" % calculate_tax(income, levels))

    

