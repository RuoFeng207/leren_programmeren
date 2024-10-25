week = ("maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag")

print("Alledagen van de week zijn: ")
for a in (week):
    print(f"-{a}")
print("")
var ="de weekend dagen zijn: "
for b in range(5,7):
    var +=week [b]
    if b<6:
        var+= " & "
    if b>5:
        var+="."
print(var)

print("")
var ="de werk dagen zijn: "
for c in range(0,5):
    var +=week [c]
    if c<3:
        var+= " , "
    if c ==3:
        var+=" & "
    if c ==4:
        var+="."
print(var)
week_reversed =tuple(reversed(week))


print("")
var ="Alle dagen in omgekeerde vorgorde zijn: "
for d in range(0,7):
    var +=week_reversed [d]
    if d<6:
        var+= " -> "
    if d>5:
        var+="."
print(var)

print("")
var ="de werk dagen in omgekeerde volgode zijn: "
for e in range(2,7):
    if e>1:
        var+= "\n - "
    var +=week_reversed [e]
print("")
print(var)
week_reversed =tuple(reversed(week))

var ="de weekend dagen zijn: "
print("")
for f in range(0,2):
    if f >0:
        var+= " & "

    var +=week_reversed [f]
print("")
print(var)