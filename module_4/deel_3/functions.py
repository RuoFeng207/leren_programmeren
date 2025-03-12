import time
from termcolor import colored
from data import JOURNEY_IN_DAYS,COST_FOOD_HUMAN_COPPER_PER_DAY,COST_FOOD_HORSE_COPPER_PER_DAY

##################### O03 #####################
munt = 50
def copper2silver(amount:int) -> float:
    copper_silver = amount/10
    return copper_silver
# print(f"{munt} koper munt(en) is gelijk aan {copper2silver(munt)} zilver (munt)")

def silver2gold(amount:int) -> float:
    silver_gold = amount/5
    return silver_gold
# print(f"{munt} zilver munt(en) is gelijk aan {silver2gold(munt)} goud munt(en)")

def copper2gold(amount:int) -> float:
    copper_gold = amount/50
    return copper_gold
# print(f"{munt} koper munt(en) is gelijk aan {copper2gold(munt)} goud munt(en)")

def platinum2gold(amount:int) -> float:
    platinum_gold = amount*25
    return platinum_gold
# print(f"{munt} platinum munt(en) is gelijk aan {platinum2gold(munt)} goud munt(en)")

def getPersonCashInGold(personCash:dict) -> float:
    gold = 0
    for cash in personCash:
        if cash == "copper":
            gold+= copper2gold(personCash[cash])
        if cash =="silver":
            gold+= silver2gold(personCash[cash])
        if cash == "platinum":
            gold+= platinum2gold(personCash[cash])
        if cash == "gold": 
            gold += personCash[cash]

    return gold


##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    COST_FOOD_HUMAN_COPPER_PER_DAY = 0.08
    COST_FOOD_HORSE_COPPER_PER_DAY = 0.06
    
    som = ((COST_FOOD_HUMAN_COPPER_PER_DAY*people)+(COST_FOOD_HORSE_COPPER_PER_DAY*horses))*JOURNEY_IN_DAYS
    total=round(som,2)
    return total
##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    result = []
    for item in list: 
        if key in item:
            if item[key]== value:
                result.append(item)
            
            else:
                print("error value bestaat niet")
        else:
            print("key not found")
    return result

def getAdventuringPeople(people:list) -> list:
    lijst = []
    for x in people:
        if "adventuring" in x:
            if x["adventuring"] == True:
                return people

    return lijst
def getShareWithFriends(friends:list) -> list:
    lijst = []
    for x in friends:
        if "shareWith" in x:
            if x["shareWith"] == True:
                return friends
    return lijst

def getAdventuringFriends(friends:list) -> list:
    lijst = []
    for x in friends:
        if "adventuring" in x and "shareWith" in x:
            if x["adventuring"] == True and x["shareWith"] == True:
                return friends
            
    return lijst

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    horse = 4.4
    pass
def getNumberOfTentsNeeded(people:int) -> int:
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    pass

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()