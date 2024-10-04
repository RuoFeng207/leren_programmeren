month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    month_discount_brands.split()
    if brand in month_discount_brands:
        korting =price*MONTH_DISCOUNT_PERC/100
        round(korting,2)
        print(korting)
calc_discount(1000, "Vespa", month_discount_brands)