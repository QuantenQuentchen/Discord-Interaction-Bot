from Imports import *
import Command_Classes as CC

# Non-Violent-Non-NSFW-2-Person-Interactions
Hug = CC.Interaction("Hug", [], "//Author// hugs //Target//.", "hug", "You hug the mentioned User.", "hug", False, 1,
                     False,
                     False, True, "2P Int")
Kiss = CC.Interaction("Kiss", [], "//Author// kisses //Target//.", "kiss", "You kiss the mentioned User.", "kiss",
                      False,
                      1,
                      False, False, True, "2P Int")
Pat = CC.Interaction("Pat", [], "//Author// pats //Target//.", "pat", "You pat the mentioned User", "pat", False, 1,
                     False,
                     False, True, "2P Int")
Simp = CC.Interaction("Simp", [], "//Author// simps for //Target//.", "simp for", "You simp for the mentioned User",
                      "simp",
                      False, 1, False, False, False, "2P Int")
SmallTalk = CC.Interaction("Small_talk", ["sm", "smalltalk"], "//Author// has a pleasent conversation with //Target//.",
                           "engage in smalltalk with", "You engage in smalltalk with the mentioned User", "small_talk",
                           False, 1,
                           False, False, True, "2P Int")
TalkAboutFears = CC.Interaction("TalkAboutFears", ["TalkAboutMyFears", "taf"],
                                "//Author// talks about theire fears with //Target//.",
                                "talk about his fears with",
                                "You talk about your fears with the mentioned User", "talk_about_my_fears", False, 1,
                                False, False, True,
                                "2P Int")
Love = CC.Interaction("Love", [], "Author// starts loving //Target//", "love", "You love the mentioned User", "love",
                      False, 1,
                      False, False, False, "2P Int")
Cuddle = CC.Interaction("Cuddle", [], "//Author// cuddles with //Target//", "cuddle",
                        "You cuddle with the mentioned User",
                        "cuddle", False, 1, False, False, True, "2P Int")
HoldHands = CC.Interaction("HoldHands", ["Holdhands"], "//Author// hold Hands with //Target//", "hold hands with",
                           "You hold hands with the mentioned User", "hold_hands", False, 1, False, False, True,
                           "2P Int")
KissCheek = CC.Interaction("KissCheek", ["KiscCheek"], "//Author// kisses the cheek of //Target//", "kiss those cheeks",
                           "You kiss the cheek of the mentioned User", "kiss_cheek", False, 1, False, False, True,
                           "2P Int")
IceWith = CC.Interaction("IceWith", ["Icewith"], "//Author// eats ice together with //Target//", "eat ice with",
                         "You eat ice with the mentioned User", "ice_together", False, 1, False, False, True, "2P Int")
Call = CC.Interaction("Call", [], "//Author// calls //Target//.", "call", "You call the mentioned User.", "call", False,
                      1,
                      False,
                      False, True, "2P Int")
Cinema = CC.Interaction("Cinema", ["movie", "WatchMovie"], "//Author// goes to the Movies with //Target//.",
                        "go to the Cinema with", "You go to the Cinema with the mentioned User", "cinema", False, 1,
                        False,
                        False,
                        True, "2P Int")
Picnic = CC.Interaction("Picnic", [], "//Author// has a picnic with //Target//.", "have a picnic with",
                        "You have a picnic with "
                        "the mentioned User",
                        "picknick", False, 1, False, False, True, "2P Int")
ShareHeadphones = CC.Interaction("ShareHeadphones", ["ShareEarphones"],
                                 "//Author// shares theire Headphones with //Target//.", "share "
                                                                                         "headphones with",
                                 "You share you Headphones with the mentioned User.", "share_headphones", False, 1,
                                 False,
                                 False, True,
                                 "2P Int")

# Non-Violent-Non-NSFW-1-Person-Interactions
Smirk = CC.Interaction("Smirk", [], "//Author// smirks.", "smirk", "You smirk", "smirk", True, 0, False, False, False,
                       "Solo Int")
Wink = CC.Interaction("Wink", [], "//Author// winks.", "wink", "You wink", "wink", True, 0, False, False, False,
                      "Solo Int")
PrettyEyes = CC.Interaction("PrettyEyes", ["Pretty_Eyes"], "//Author// makes pretty eyes.", "Nope",
                            "You make pretty eyes",
                            "pretty_eyes"
                            , True, 0, False, False, False, "Solo Int")
Smile = CC.Interaction("Smile", [], "//Author// smiles", "Nope", "You smile", "smile", True, 0, False, False, False,
                       "Solo Int")
EvilGrin = CC.Interaction("EvilGrin", ["Evil_Grin"], "//Author// grins maniacally.", "Nope", "You grin, but eeeeevil.",
                          "grin", True,
                          0, False, False, False, "Solo Int")
Laugh = CC.Interaction("Laugh", [], "//Author// starts laughing", "Nope", "You start laughing", "laugh", True, 0, False,
                       False,
                       False, "Solo Int")
PlayWithHair = CC.Interaction("PlaywithHair", ["PlayWithHair", "Play_with_Hair"], "//Author// plays with their Hair",
                              "play with Hair",
                              "You play with your Hair", "play_with_hair", True, 0, False, False, False, "Solo Int")
Eva = CC.Interaction("Eva", ["Evangelion"], "Depressions strike again.", "eva", "Baka shinji", "eva", True, 0, False,
                     False,
                     False, "Solo Int")
CreepyLaugh = CC.Interaction("CreepyLaugh", ["Creepy_Laugh", "creepy_laugh"], "//Author// starts to laugh creepy.",
                             "laugh creepy",
                             "You start to laugh crepily.", "creepy_laugh", False, 1, False, False, True, "2P Int")
Blush = CC.Interaction("Blush", [], "//Author// blushes.", "blush", "You start to blush.", "blush", True, 0, False,
                       False,
                       False,
                       "Solo Int")
Dance = CC.Interaction("Dance", [], "//Author// starts to dance.", "dance", "You dance.", "dance", True, 0, False,
                       False,
                       False,
                       "Solo Int")

# Violent-Non-NSFW-2-Person-Interactions
Kill = CC.Interaction("Kill", ["Murder"], "//Author// kills //Target//.", "kills", "You kill the mentioned User",
                      "kill",
                      False,
                      1, False, False, False, "Fight")
Punch = CC.Interaction("Punch", [], "//Author// punches //Target//.", "punch", "You punch the mentioned User", "punch",
                       False, 1,
                       False, False, False, "Fight")
Stomp = CC.Interaction("Stomp", [], "//Author// stomps //Target//.", "stomps", "You stomp the mentioned User", "stomp",
                       False, 1,
                       False, False, False, "Fight")
Roundhouse = CC.Interaction("Roundhouse", [], "//Author// roundhouse kicks //Target//.", "roundhous kicks",
                            "You kick the mentioned User with your Feet. But EPIC!!!", "roundhouse", False, 1, False,
                            False, False,
                            "Fight")
Slap = CC.Interaction("Slap", [], "//Author// slaps //Target//.", "slaps", "You slap the mentioned User", "slap", False,
                      1,
                      False,
                      False, False, "Fight")
Scream = CC.Interaction("Scream", [], "//Author// screams at //Target//.", "scream", "You scream at the mentioned User",
                        "scream",
                        False, 1, False, False, False, "Fight")
Insult = CC.Interaction("Insult", [], "//Author// insults //Target//.", "insult", "You insult the mentioned User",
                        "insult", False,
                        1, False, False, False, "Fight")
Uppercut = CC.Interaction("Uppercut", [], "//Author// attacks //Target// with an uppercut.", "uppercut",
                          "You punch the User with an Uppercut", "uppercut", False, 1, False, False, False, "Fight")
Bite = CC.Interaction("Bite", [], "//Author// bites //Target//.", "bite", "You bite the mentioned User", "bite", False,
                      1,
                      False,
                      False, False, "Fight")
Choke = CC.Interaction("Choke", [], "//Author// chockes //Target//.", "choke", "You choke the mentioned User", "choke",
                       False, 1,
                       False, False, False, "Fight")
VampireBite = CC.Interaction("VampireBite", ["VampBite"], "//Author// bites //Target// with their fangs.",
                             "vampire bite",
                             "You bite the "
                             "mentioned "
                             "User with "
                             "your "
                             "fangs.",
                             "vampire_bite", False, 1, False, False, False, "Fight")


def Init(Object):
    Object.Command()
    Object.Kommand()
    return True


def InitAll():
    for Int in CC.ActList:
        Init(Int)
