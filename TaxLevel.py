import csv

class TaxLevel:

    INFINITE = 99999999999999

    def __init__(self, min_sum: int, max_sum: int, tax_percentage: float):
        self.min_sum = min_sum  # the minimum income taxed at this level
        self.max_sum = max_sum  # the maximum income taxed at this level
        self.tax_percentage = tax_percentage  # the sum's percentage taxed at this level

    @staticmethod
    def generate_israel_tax_levels() -> list:
        result = []

        # add the tax levels to the result list
        result.append(TaxLevel(0, 75480, 10.0))
        result.append(TaxLevel(75481, 108360, 14.0))
        result.append(TaxLevel(108361, 173880, 20.0))
        result.append(TaxLevel(173881, 241680, 31.0))
        result.append(TaxLevel(241681, 502920, 35.0))
        result.append(TaxLevel(502921, 647640, 47.0))
        result.append(TaxLevel(647641, TaxLevel.INFINITE, 50.0))

        return result

    @staticmethod
    def generate_tax_levels_from_csv(tax_levels_filename) -> list:
        result = []

        # open the csv file
        with open(tax_levels_filename, newline='') as source_file:
            reader = csv.reader(source_file, delimiter=',')


def calculate_tax(to_pay: int, tax_levels: list) -> float:
    tax = 0.0
    already_calculated = 0
    pay_sum = to_pay  # the total amount to pay

    for level in tax_levels:  # calculate the tax to be paid in each level
        if pay_sum < level.max_sum:  # check if the "last level" to pay was reached
            # print(str(float(to_pay)) + " * " + str(level.tax_percentage) + "% = " + str(float(to_pay) * (level.tax_percentage / 100.0)))
            tax += float(to_pay) * (level.tax_percentage / 100.0)
            break

        # print(str(level.max_sum - already_calculated) + " * " + str(level.tax_percentage) + "% = " + str(float(level.max_sum - already_calculated) * (level.tax_percentage / 100.0)))
        tax += float(level.max_sum - already_calculated) * (level.tax_percentage / 100.0)
        to_pay -= (level.max_sum - already_calculated)  # update the amount of money left to be taxed
        already_calculated += (level.max_sum - already_calculated)

    return tax

