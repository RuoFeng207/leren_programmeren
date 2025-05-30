tekst_snelheid = 0.0
totaal = []
# prijs 
prijs = {
    "prijs_bol":1.10,
    "prijs_bakje":0.75,
    "prijs_hoorntje":1.25,
    "tot_prijs":0
}
# aantal
smaken = {
    "aardbei": {
        "naam":"B.Aardbei",
        "aantal":0,
        "prijs":1.10
    },
    "chocolade": {
        "naam":"B.Chocolade",
        "aantal":0,
        "prijs":1.10
    },
    "mint": {
        "naam":"B.Mint",
        "aantal":0,
        "prijs":1.10
    },
    "vanile": {
        "naam":"B.Vanile",
        "aantal":0,
        "prijs":1.10
    }
}
houders = {
    "bakje": {
        "naam":"Bakje",
        "aantal":0,
        "prijs":0.75
    },
    "hoortje": {
        "naam":"Hoortje",
        "aantal":0,
        "prijs":1.25
    }
}
toppings = {
    "geen":{
        "naam":"geen",
        "aantal":0,
        "prijs":0
    },
    "slagroom":{
        "naam":"Slagroom",
        "aantal":0,
        "prijs":0.50
    },
    "sprinkels":{
        "naam":"Sprinkels",
        "aantal":0,
        "prijs":0.30
    },
    "caramel saus":{
        "naam":"Caramel saus",
        "aantal":0,
        "prijs":{
            "hoorntje":0.60,
            "bakje":0.90
        }
    }
}

keus = {
    "ja/nee":{
        "J":"ja",
        "N":"nee",
    },
    "smaak":{
        "A":"aardbei",
        "C":"chocolade",
        "M":"mint",
        "V":"vanile"
    },
    "houder":{
        "H":"hoortje",
        "B":"bakje"
    },
    "toppings":{
        "A":"geen",
        "B":"slagroom",
        "C":"sprinkels",
        "D":"caramel saus"
    }
}