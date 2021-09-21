class TaxLevel:
    def __init__(self, min_sum: int, max_sum: int, tax_percentage: double):
        self.min_sum = min_sum  # the minimum income taxed at this level
        self.max_sum = max_sum  # the maximum income taxed at this level
        self.tax_percentage = tax_percentage  # the sum's percentage taxed at this level

    @staticmethod
    def generate_tax_levels() -> list[TaxLevel]:
        result = []

        result.append(TaxLevel(0, 75480, 10.0))
        result.append(TaxLevel(75481, 108360, 14.0))
        result.append(TaxLevel(108361, 173880, 20.0))
        result.append(TaxLevel(173881, 241680, 31.0))
        result.append(TaxLevel(241681, 502920, 35.0))
        result.append(TaxLevel(502921, 647640, 47.0))
        result.append(TaxLevel(647641, None, 50.0))

