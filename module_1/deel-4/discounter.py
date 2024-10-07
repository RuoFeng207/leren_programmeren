month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if brand in month_discount_brands:
        return round(price/100*MONTH_DISCOUNT_PERC,2)
    else:
        return 0

    
print(calc_discount(100, "Vespa", month_discount_brands))
print(calc_discount(100, "Nokia", month_discount_brands))