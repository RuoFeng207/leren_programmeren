import time,math
from termcolor import colored
from data import JOURNEY_IN_DAYS,COST_FOOD_HUMAN_COPPER_PER_DAY,COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_HORSE_SILVER_PER_DAY,COST_TENT_GOLD_PER_WEEK
from data import COST_INN_HUMAN_SILVER_PER_NIGHT,COST_INN_HORSE_COPPER_PER_NIGHT

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
    human_food = copper2gold(COST_FOOD_HUMAN_COPPER_PER_DAY) 
    horse_food = copper2gold(COST_FOOD_HORSE_COPPER_PER_DAY)    
    som = ((human_food*people)+(horse_food*horses))*JOURNEY_IN_DAYS
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
    
    horse = (people*1)/2
    horse = math.ceil(horse)
    return horse
def getNumberOfTentsNeeded(people:int) -> int:
    tent = (people*1)/3
    tent = math.ceil(tent)
    return tent


def getTotalRentalCost(horses:int, tents:int) -> float:
    silver_horses =horses*JOURNEY_IN_DAYS #paarden 
    cost_horse =COST_HORSE_SILVER_PER_DAY*silver_horses
    to_gold = silver2gold(cost_horse)
    week =JOURNEY_IN_DAYS/7
    weeks= math.ceil(week)
    tot_tenst = tents*weeks
    tent_gold = tot_tenst*COST_TENT_GOLD_PER_WEEK
    tot_gold = tent_gold+to_gold
    return tot_gold

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    lijst = []
    for new_item in items:
        bootschappen = (f"{new_item['amount']}{new_item['unit']} {new_item['name']}")
        lijst.append(bootschappen)

    if len(lijst) > 1:
        return ', '.join(lijst[:-1]) + ' & ' + lijst[-1]
    elif lijst:
        return lijst[0]


def getItemsValueInGold(items: list) -> list:
    # gold_values = []
    som = 0
    for item in items:
        if item['price']['type'] == "copper":
            gold = copper2gold(item['price']['amount'])
        elif item['price']['type'] == "silver":
            gold = silver2gold(item['price']['amount'])
        elif item['price']['type'] == "platinum":
            gold = platinum2gold(item['price']['amount'])
        elif item['price']['type'] == "gold":
            gold = item['price']['amount']
        else:
            gold = 0
        
        som +=gold* item['amount']
    
    return float(som)
##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    gold = 0
    for dictionary in people:
        lijst = dictionary["cash"]
        for cash in lijst:
            if cash == "copper":
                gold += copper2gold(dictionary["cash"]["copper"])
            if cash == "silver":
                gold+= silver2gold(dictionary["cash"]["silver"])
            if cash =="platinum":
                gold+= platinum2gold(dictionary["cash"]["platinum"])
            if cash == "gold":
                gold+= dictionary["cash"]["gold"]
    return float(gold)

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    intresting_investors = []
    for investor in investors:
        if "profitReturn" in investor:
            if investor["profitReturn"]<=10:
                intresting_investors.append(investor)
            
    return intresting_investors
             
            
def getAdventuringInvestors(investors:list) -> list:
    interested_investors =  getInterestingInvestors(investors)
    adventuring_investors = []
    for adventure in interested_investors:
        if "adventuring" in adventure:
            if adventure["adventuring"] == True:
                adventuring_investors.append(adventure)
    return adventuring_investors

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total = 0
    int_investors =getInterestingInvestors(investors)
    advent_investors =getAdventuringInvestors(int_investors)
    for inventor in advent_investors:
        print(inventor)
        rent_cost = getTotalRentalCost(1,1)
        gear_cost = getItemsValueInGold(gear)
        food_cost = getJourneyFoodCostsInGold(1,1)
        total+= rent_cost + gear_cost+food_cost
    
    return float(total)

##################### O11 # ####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    night_cost_in_gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    stable_cost_in_gold= copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    cost_people = night_cost_in_gold*people
    cost_horses = stable_cost_in_gold*horses
    cost_night= round(cost_people+cost_horses,2)

    if cost_night>leftoverGold:
        night_amount= 0
    else:
        night_amount = int(leftoverGold/cost_night)
    return night_amount

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    night_cost_in_gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    stable_cost_in_gold= copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    cost_people = night_cost_in_gold*people
    cost_horses = stable_cost_in_gold*horses
    tot_cost_horses=nightsInInn*cost_horses
    tot_cost_people=nightsInInn*cost_people
    total_cost = round(tot_cost_horses+tot_cost_people,2)
    return total_cost

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