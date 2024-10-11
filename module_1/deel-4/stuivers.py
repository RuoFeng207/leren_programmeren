# invul = 76.61
# bedrag =round ((invul)*100/5)*5/100
# print(bedrag)
def afronden_5cent(bedrag):
    cent = 5
    return (round(bedrag*100/cent)*cent/100)