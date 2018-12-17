import requests
import datetime
APIKEY="RGAPI-89fa49ce-0100-4f03-9a57-5eea749f0a26"
#CAPS="https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/g2ps?api_key=" + APIKEY
#CAPSRANKED="https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/g2ps?api_key=" + APIKEY
#FAKER="https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/Hide%20on%20bush"
BJERGID="dr5Hw9W8cqvr8y2nD2h9ttTKTkNDZ80d87OwvS78VbY4MRo"
BJERGRANKED="https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/tsm%20bjergsen?api_key=" + APIKEY

matchList = []
matchIdList = []
dateList = []
finalList = []
patchList = []
champList = []
primary = ""
secondary = ""
keystone = ""
rune1 = ""
rune2 = ""
rune3 = ""
rune4 = ""
rune5 = ""

teamList = []
opponentList = []
championDictionary= {
                     "266":"Aatrox",
                     "103":"Ahri",
                     "84":"Akali",
                     "12":"Alistar",
                     "32":"Amumu",
                     "34":"Anivia",
                     "1":"Annie",
                     "22":"Ashe",
                     "136":"AurelionSol",
                     "268":"Azir",
                     "432":"Bard",
                     "53":"Blitzcrank",
                     "63":"Brand",
                     "201":"Braum",
                     "51":"Caitlyn",
                     "164":"Camille",
                     "69":"Cassiopeia",
                     "31":"Cho'Gath",
                     "42":"Corki",
                     "122":"Darius",
                     "131":"Diana",
                     "36":"DrMundo",
                     "119":"Draven",
                     "245":"Ekko",
                     "60":"Elise",
                     "28":"Evelynn",
                     "81":"Ezreal",
                     "9":"Fiddlesticks",
                     "114":"Fiora",
                     "105":"Fizz",
                     "3":"Galio",
                     "41":"Gangplank",
                     "86":"Garen",
                     "150":"Gnar",
                     "79":"Gragas",
                     "104":"Graves",
                     "120":"Hecarim",
                     "74":"Heimerdinger",
                     "420":"Illaoi",
                     "39":"Irelia",
                     "427":"Ivern",
                     "40":"Janna",
                     "59":"Jarvan IV",
                     "24":"Jax",
                     "126":"Jayce",
                     "202":"Jhin",
                     "222":"Jinx",
                     "145":"Kaisa",
                     "429":"Kalista",
                     "43":"Karma",
                     "2":"Olaf",
                     "30":"Karthus",
                     "38":"Kassadin",
                     "55":"Katarina",
                     "10":"Kayle",
                     "141":"Kayn",
                     "85":"Kennen",
                     "121":"KhaZix",
                     "203":"Kindred",
                     "240":"Kled",
                     "96":"KogMaw",
                     "7":"LeBlanc",
                     "64":"Lee Sin",
                     "89":"Leona",
                     "127":"Lissandra",
                     "236":"Lucian",
                     "117":"Lulu",
                     "99":"Lux",
                     "54":"Malphite",
                     "90":"Malzahar",
                     "57":"Maokai",
                     "11":"Master Yi",
                     "21":"Miss Fortune",
                     "82":"Mordekaiser",
                     "25":"Morgana",
                     "267":"Nami",
                     "75":"Nasus",
                     "111":"Nautilus",
                     "518":"Neeko",
                     "76":"Nidalee",
                     "56":"Nocturne",
                     "20":"Nunu",
                     "61":"Orianna",
                     "516":"Ornn",
                     "80":"Pantheon",
                     "78":"Poppy",
                     "555":"Pyke",
                     "133":"Quinn",
                     "497":"Rakan",
                     "33":"Rammus",
                     "421":"RekSai",
                     "58":"Renekton",
                     "107":"Rengar",
                     "92":"Riven",
                     "68":"Rumble",
                     "13":"Ryze",
                     "113":"Sejuani",
                     "35":"Shaco",
                     "98":"Shen",
                     "102":"Shyvana",
                     "27":"Singed",
                     "14":"Sion",
                     "15":"Sivir",
                     "72":"Skarner",
                     "37":"Sona",
                     "16":"Soraka",
                     "50":"Swain",
                     "134":"Syndra",
                     "223":"TahmKench",
                     "163":"Taliyah",
                     "91":"Talon", 
                     "44":"Taric",
                     "17":"Teemo",
                     "412":"Thresh",
                     "18":"Tristana",
                     "48":"Trundle",
                     "23":"Tryndamere",
                     "4":"Twisted Fate",
                     "29":"Twitch",
                     "77":"Udyr",
                     "6":"Urgot",
                     "110":"Varus",
                     "67":"Vayne",  
                     "45":"Veigar",
                     "161":"Vel'Koz", 
                     "254":"Vi", 
                     "112":"Viktor",
                     "8":"Vladimir",
                     "106":"Volibear",
                     "19":"Warwick",
                     "62":"Wukong",
                     "498":"Xayah",
                     "101":"Xerath",
                     "5":"Xin Zhao",
                     "157":"Yasuo",
                     "83":"Yorick",
                     "154":"Zac",
                     "238":"Zed",
                     "115":"Ziggs",
                     "26":"Zilean",                 
                     "142":"Zoe",
                     "143":"Zyra",      
                     }

masteryDictionary = {"8000":"Precision",
                     "8005":"Press The Attack",
                     "8008":"Lethal Tempo",
                     "8021":"Fleet Footwork",
                     "8010":"Conquerer",
                     "9101":"Overheal",
                     "9111":"Triumph",
                     "8009":"Presence Of Mind",
                     "9104":"Legend: Alacrity",
                     "9105":"Legend: Tenacity",
                     "9103":"Legend: Bloodline",
                     "8014":"Coup De Grace",
                     "8017":"Cut Down",                   
                     "8299":"Last Stand",    
                     "8100":"Domination",
                     "8112":"Electrocute",
                     "8124":"Predator",
                     "8128":"Dark Harvest",
                     "9923":"Hail of Blades",
                     "8126":"Cheap Shot",
                     "8139":"Taste of Blood",
                     "8143":"Sudden Impact",
                     "8136":"Zombie Ward",
                     "8120":"Ghost Poro",
                     "8138":"Eyeball Collection",
                     "8135":"Ravenous Hunter",
                     "8134":"Ingenious Hunter",
                     "8105":"Relentless Hunter",
                     "8106":"Ultimate Hunter",
                     "8214":"Summon Aery",
                     "8229":"Arcane Comet",
                     "8230":"Phase Rush",
                     "8224":"Nullifying Orb",
                     "8226":"Manaflow Band",
                     "8275":"Nimbus Cloak",
                     "8210":"Transcendence",
                     "8234":"Celerity",
                     "8233":"Absolute Focus",
                     "8237":"Scorch",
                     "8232":"Waterwalking",
                     "8236":"Gathering Storm",
                     "8437":"Grasp of the Undying",
                     "8439":"Aftershock",
                     "8465":"Guardian",
                     "8446":"Demolish",
                     "8463":"Font of Life",
                     "8401":"Shield Bash",
                     "8429":"Conditioning",
                     "8444":"Second Wind",
                     "8473":"Bone Plating",
                     "8451":"Overgrowth",
                     "8453":"Revitalize",
                     "8242":"Unflinching",
                     "8351":"Glacial Augment",
                     "8359":"Kleptomancy",
                     "8360":"Unsealed Spellbook",
                     "8306":"Hextech Flashtraption",
                     "8304":"Magical Footwear",
                     "8313":"Perfect Timing",
                     "8321":"Future's Market",
                     "8316":"Minion Dematerializer",
                     "8345":"Biscuit Delivery",
                     "8347":"Cosmic Insight",
                     "8410":"Approach Velocity",
                     "8352":"Time Warp Tonic"
                     
                    }

#class Match:
#    def __init__(self,player,champ,patch,date,vs,enemyTeam,ownTeam,primary,keystone,r1,r2,r3,secondary,r4,r5):
#        self.player = player
#        self.champ = champ
#        self.patch = patch
#        self.date = date
#        self.vs = vs
#        self.enemyteam = enemyTeam
#        self.ownTeam = ownTeam
#   
#    
#    def toCsv(): 
        
        
    
#def requestRankedData(id):
#    NARANKED = "https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/" + id + "?api_key=" + APIKEY
#    response = requests.get(NARANKED)
#    return response.json()

#send request to API 
def sendRequest(URL):
    response = requests.get(URL)
    return response.json()

#get match information from API
def requestMatchInfo(accID,matchID):
    #if bjergsen
    if(accID == BJERGID):
        requestURL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + str(matchID) + "?api_key=" + APIKEY
        return sendRequest(requestURL)
    
#get the champions that were played in the game and convert from player to champion    
def getChampsPlayed(matchID):
    matchInfo = getMatch(str(matchID))
    champsPlayed = matchInfo['participants']
    identities = matchInfo['participantIdentities']
    champsDict = {}
    playersDict = {}
    print opponentList
    print teamList
    for x in champsPlayed:
        champsDict[x['participantId']] = x['championId']
        
    for x in identities:
        playersDict[x['participantId']] = x['player']['summonerName']           
#    print teamList[0][1]
    createTeamsToChampionsDict(champsDict,playersDict,identities)


#creates a dictionary key = players, value = champions
def createTeamsToChampionsDict(cD,pD,identity):
    transDict = {}
    for x in range(1,11):
        transDict[pD[x]] = championDictionary[str(cD[x])] 
#    print transDict  
    convertPlayersToChamps(transDict)
    
def convertPlayersToChamps(tD):
    #gets keys of transDict in list form
    for i in teamList:
        for x in i:
            i[i.index(x)] = tD[x]
    for i in opponentList:
        for x in i:
            i[i.index(x)] = tD[x]
    
def getMatch(matchID):
    requestURL = "https://na1.api.riotgames.com/lol/match/v4/matches/" + matchID + "?api_key=" + APIKEY
    return sendRequest(requestURL)

def getMatchHistory(accID):
    #if bjergsen
    if(accID == "dr5Hw9W8cqvr8y2nD2h9ttTKTkNDZ80d87OwvS78VbY4MRo"):
        requestURL = "https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + accID + "?endIndex=1&beginIndex=0&api_key=" + APIKEY
        return sendRequest(requestURL)

def getMatchIdList(matchlist):
    for x in matchList:
        matchIdList.append(x['gameId'])
    
def getMatchParticipants(matchID):
    tempTeamList = []
    tempOpponentList = []
    participantList = []
#    print matchIdList.index(matchID)
    matchInfo = getMatch(str(matchID))
    identities = matchInfo['participantIdentities']
    for x in identities:
#        print x['player']['summonerName']
        participantList.append(x['player']['summonerName'])
  
#    print participantList
    if participantList.index('TSM Bjergsen') > 4:
       for x in range(0,5):
           tempOpponentList.append(participantList[x])
       for x in range(5,10):
           tempTeamList.append(participantList[x])
    else:
       for x in range(0,5):
           tempTeamList.append(participantList[x])
       for x in range(5,10):
           tempOpponentList.append(participantList[x])
    
    opponentList.append(tempOpponentList)  
    teamList.append(tempTeamList)
    tempTeamList[:]
    tempOpponentList[:]
    participantList[:]

def getPatchList(accountID):
    for x in matchIdList:
        match = requestMatchInfo(accountID,x)
        temp = str(match['gameVersion'])
        patchList.append(temp[0:4])
        
def getDateList(accountID):
    for i in range(len(matchList)):
        temp = matchList[i]['timestamp']
        date = datetime.datetime.fromtimestamp(temp/1e3)
#        print date
        datestring = str(date.month) + "/" + str(date.day)
        dateList.append(datestring)


#def parseList(accID):
#    finalList.append("Choose player:")
    #if bjergsen
#    if(accID == "dr5Hw9W8cqvr8y2nD2h9ttTKTkNDZ80d87OwvS78VbY4MRo"):
#        for i in range(len(matchList)):
#            player = Match("Tsm Bjergsen",patchList[i],dateList[i])
#            tempFinalList.append("Tsm Bjergsen")
#            tempFinalList.append(patchList[i])
#            tempFinalList.append(dateList[i])
            
#            finalList.append(','.join(tempFinalList) )
#            print finalList
            
#            tempFinalList.pop()
#            tempFinalList.pop()
#            tempFinalList.pop()
            

listR = getMatchHistory(BJERGID)   
matchList = listR['matches']
#print matchList
getMatchIdList(matchList)

#print matchList
for x in matchIdList:
    getMatchParticipants(x)
    getChampsPlayed(x)
#    
#    print str(x['gameId'])

print opponentList
print teamList
#print parts[0]['player']['summonerName']
getPatchList(BJERGID)
getDateList(BJERGID)
#parseList(BJERGID)
#print finalList




