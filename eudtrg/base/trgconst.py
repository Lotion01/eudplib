from eudtrg import LICENSE #@UnusedImport
from .trgstrconst import AIScriptDict
from .utils import binio

# Long list of known constants
class All: pass
class Enemy: pass
class Ally: pass
class AlliedVictory: pass
class AtLeast: pass
class AtMost: pass
class Exactly: pass
class SetTo: pass
class Add: pass
class Subtract: pass
class Move: pass
class Patrol: pass
class Attack: pass
class Player1: pass
class Player2: pass
class Player3: pass
class Player4: pass
class Player5: pass
class Player6: pass
class Player7: pass
class Player8: pass
class Player9: pass
class Player10: pass
class Player11: pass
class Player12: pass
class CurrentPlayer: pass
class Foes: pass
class Allies: pass
class NeutralPlayers: pass
class AllPlayers: pass
class Force1: pass
class Force2: pass
class Force3: pass
class Force4: pass
class NonAlliedVictoryPlayers: pass
class Enable: pass
class Disable: pass
class Toggle: pass
class Ore: pass
class Gas: pass
class OreAndGas: pass
class Total: pass
class Units: pass
class Buildings: pass
class UnitsAndBuildings: pass
class Kills: pass
class Razings: pass
class KillsAndRazings: pass
class Custom: pass
class Set: pass
class Clear: pass
class Random: pass
class Cleared: pass


AllyStatusDict = {
    Enemy:0,
    Ally:1,
    AlliedVictory:2,
}

ComparisonDict = {
    AtLeast:0,
    AtMost:1,
    Exactly:10,
}

ModifierDict = {
    SetTo:7,
    Add:8,
    Subtract:9,
}

OrderDict = {
    Move:0,
    Patrol:1,
    Attack:2,
}

PlayerDict = {
    Player1:0,
    Player2:1,
    Player3:2,
    Player4:3,
    Player5:4,
    Player6:5,
    Player7:6,
    Player8:7,
    Player9:8,
    Player10:9,
    Player11:10,
    Player12:11,
    CurrentPlayer:13,
    Foes:14,
    Allies:15,
    NeutralPlayers:16,
    AllPlayers:17,
    Force1:18,
    Force2:19,
    Force3:20,
    Force4:21,
    NonAlliedVictoryPlayers:26,
}

PropStateDict = {
    Enable:4,
    Disable:5,
    Toggle:6,
}

ResourceDict = {
    Ore:0,
    Gas:1,
    OreAndGas:2,
}

ScoreDict = {
    Total:0,
    Units:1,
    Buildings:2,
    UnitsAndBuildings:3,
    Kills:4,
    Razings:5,
    KillsAndRazings:6,
    Custom:7,
}

SwitchActionDict = {
    Set:4,
    Clear:5,
    Toggle:6,
    Random:11,
}

SwitchStateDict = {
    Set:2,
    Cleared:3,
}

def ParseConst(d, s):
    return d.get(s, s)

def ParseAllyStatus(s): return ParseConst(AllyStatusDict, s)
def ParseComparison(s): return ParseConst(ComparisonDict, s)
def ParseModifier(s): return ParseConst(ModifierDict, s)
def ParseOrder(s): return ParseConst(OrderDict, s)
def ParsePlayer(s): return ParseConst(PlayerDict, s)
def ParsePropState(s): return ParseConst(PropStateDict, s)
def ParseResource(s): return ParseConst(ResourceDict, s)
def ParseScore(s): return ParseConst(ScoreDict, s)
def ParseSwitchAction(s): return ParseConst(SwitchActionDict, s)
def ParseSwitchState(s): return ParseConst(SwitchStateDict, s)
def ParseAIScript(s):
    return binio.b2i4(ParseConst(AIScriptDict, s))

def ParseCount(s):
    if s is All: return 0
    else: return s
