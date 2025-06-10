tekst_snelheid = 0.0
totaal = []

prijs = {
    "prijs_bol": 1.10,
    "prijs_bakje": 0.75,
    "prijs_hoorntje": 1.25,
    "tot_prijs": 0
}

smaken = {
    "aardbei": {
        "naam": "B.Aardbei",
        "aantal": 0,
        "prijs": {"klant":1.10,
                  "bedrijf":9.80}
    },
    "chocolade": {
        "naam": "B.Chocolade",
        "aantal": 0,
        "prijs": {"klant":1.10,
                  "bedrijf":9.80}
    },
    "mint": {
        "naam": "B.Mint",
        "aantal": 0,
        "prijs": {"klant":1.10,
                  "bedrijf":9.80}
    },
    "vanile": {
        "naam": "B.Vanile",
        "aantal": 0,
        "prijs": {"klant":1.10,
                  "bedrijf":9.80}
    }
}

houders = {
    "bakje": {
        "naam": "Bakje",
        "aantal": 0,
        "prijs": 0.75
    },
    "hoorntje": {
        "naam": "Hoorntje",
        "aantal": 0,
        "prijs": 1.25
    }
}

toppings = {
    "geen": {
        "naam": "geen",
        "aantal": 0,
        "prijs": 0
    },
    "slagroom": {
        "naam": "Slagroom",
        "aantal": 0,
        "prijs": 0.50
    },
    "sprinkels": {
        "naam": "Sprinkels",
        "aantal": 0,
        "prijs": 0.30
    },
    "caramel saus": {
        "naam": "Caramel saus",
        "aantal": {
            "hoorntje": 0,
            "bakje": 0
        },
        "prijs": {
            "hoorntje": 0.60,
            "bakje": 0.90
        }
    }
}


keus = {
    "klant": {
        "1": "particuliere klant",
        "2": "zakelijke klant"
    },
    "smaak": {
        "A": "aardbei",
        "C": "chocolade",
        "M": "mint",
        "V": "vanile"
    },
    "houder": {
        "H": "hoorntje",
        "B": "bakje"
    },
    "toppings": {
        "A": "geen",
        "B": "slagroom",
        "C": "sprinkels",
        "D": "caramel saus"
    }
}
