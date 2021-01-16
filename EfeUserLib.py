import os
import sys
import random

NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def Bool(string):
    if string.lower() == "true":
        return True
    else:
        return False

def RemoveFromList(List, String):
    newlist = []
    for i in range(len(List)):
        if List[i] != String:
            newlist.append(List[i])

    return newlist

def GenerateID():
    if 'UsedIDs.txt' in os.listdir('.'):
        with open('UsedIDs.txt', 'r') as f:
            UsedIDs = f.read()
    else:
        with open('UsedIDs.txt', 'x') as f:
            pass
        with open('UsedIDs.txt', 'r') as f:
            UsedIDs = f.read()

    usedids = []
    for i in range(len(UsedIDs.split('\n'))-1):
        usedids.append(UsedIDs.split('\n')[i])
    GeneratedID = ""
    while True:
        while len(GeneratedID) < 16:
            GeneratedID = GeneratedID + NUMS[random.randint(len(NUMS)-len(NUMS), len(NUMS)-1)]
        if GeneratedID not in usedids:
            with open('UsedIDs.txt', 'a') as f:
                f.write('\n'+GeneratedID)
            return GeneratedID
            break

def SetAttrib(User, Attrib, Value):
    if Attrib.upper() + '.txt' in RemoveFromList(os.listdir("USERS/"+User.replace('\n', '').replace(' ', '_')+"/"), 'PERMISSIONS') + os.listdir("USERS/"+User.replace('\n', '').replace(' ', '_')+"/PERMISSIONS/"):
        if Attrib.upper() + '.txt' in os.listdir("USERS/"+User.replace('\n', '').replace(' ', '_')+"/PERMISSIONS/"):
            filewrite = open("USERS/"+User.replace('\n', '').replace(' ', '_')+"/PERMISSIONS/"+Attrib.upper()+".txt", 'w+')
            fileread = open("USERS/"+User.replace('\n', '').replace(' ', '_')+"/PERMISSIONS/"+Attrib.upper()+".txt", 'r+')
            filewrite.write(str(Value))
            filewrite.close()
            fileread.close()
            return True
        else:
            if Attrib.upper() + '.txt' in RemoveFromList(os.listdir("USERS/"+User.replace('\n', '').replace(' ', '_')+"/"), 'PERMISSIONS'):
                filewrite = open("USERS/"+User.replace('\n', '').replace(' ', '_')+"/"+Attrib.upper()+".txt", 'w+')
                filewrite.write(str(Value))
                filewrite.close()
            else:
                return False
    else:
        return False

def CreateAttrib(User, Attrib, Loc=1):
    if Attrib in RemoveFromList(os.listdir('USERS/'+User.replace('\n', '').replace(' ', '_')+'/'), 'PERMISSIONS') + os.listdir('USERS/'+User.replace('\n', '').replace(' ', '_')+'/PERMISSIONS/'):
        return False
    else:
        if Loc == 1:
            if Attrib.upper()+'.txt' not in RemoveFromList(os.listdir('USERS/'+User.replace('\n', '').replace(' ', '_')+'/'), 'PERMISSIONS'):
                filecreate = open('USERS/'+User.replace('\n', '').replace(' ', '_')+'/'+Attrib.upper()+'.txt', 'x')
                filecreate.close()
                return True
            else:
                return False
        elif Loc == 2:
            if Attrib.upper()+'.txt' not in os.listdir('USERS/'+User.replace('\n', '').replace(' ', '_')+'/PERMISSIONS/'):
                filecreate = open('USERS/'+User.replace('\n', '').replace(' ', '_')+'/PERMISSIONS/'+Attrib.upper()+'.txt', 'x')
                filecreate.close()
                return True
            else:
                return False
        else:
            return False


def GetAttrib(User, Attrib, Loc=1):
    if Loc == 1:
        fileread = open('USERS/'+User.replace('\n', '').replace(' ', '_')+'/'+Attrib.upper()+'.txt')
        filecontents = fileread.read()
        fileread.close()
        return filecontents
    elif Loc == 2:
        fileread = open('USERS/'+User.replace('\n', '').replace(' ', '_')+'/PERMISSIONS/'+Attrib.upper()+'.txt')
        filecontents = fileread.read()
        fileread.close()
        return filecontents
    else:
        return False

def ListUsers():
    users = []
    for user in os.listdir('USERS/'):
        users.append(user)
    return users


def InspectUser(User, Loc=None):
    mydict = {'ID': None, 'MONEY': None, 'USERNAME': None, 'ISADMIN': None, 'ISBANNED': None}
    for Attrib in RemoveFromList(os.listdir("USERS/"+User.replace(' ', '_')+'/'), 'PERMISSIONS'):
        fileread = open("USERS/"+User.replace(' ', '_')+"/"+Attrib, 'r')
        mydict[Attrib.upper().replace('.TXT', '')] = fileread.read()
        fileread.close()

    for Attrib in os.listdir("USERS/"+User.replace(' ', '_')+"/PERMISSIONS/"):
        fileread = open("USERS/"+User.replace(' ', '_')+"/PERMISSIONS/"+Attrib, 'r')
        mydict[Attrib.upper().replace('.TXT', '')] = fileread.read()
        fileread.close()

    return mydict


def Login(User, Pass):
    loginok = False
    usernamefileread = open("USERS/"+User.replace('\n', '').replace(' ', '_')+"/USERNAME.txt", 'r')
    passwordfileread = open("USERS/"+User.replace('\n', '').replace(' ', '_')+"/PASSWORD.txt", 'r')
    if User.replace('\n', '').replace(' ', '_') == usernamefileread.read().replace("\n", "").replace(' ', '_') and Pass.replace('\n', '') == passwordfileread.read().replace("\n", ""):
        bannedfileread = open("USERS/"+User.replace(' ', '_')+"/PERMISSIONS/ISBANNED.txt", 'r')
        adminfileread = open("USERS/"+User.replace(' ', '_')+"/PERMISSIONS/ISADMIN.txt", 'r')
        hesbanned = Bool(bannedfileread.read())
        hesadmin = Bool(adminfileread.read())
        if not hesadmin and not hesbanned:
            loginok = True
        elif hesadmin and not hesbanned:
            loginok = True
        else:
            loginok = False

    if loginok:
        return True
    else:
        return False

def _reg(Username, Password):
    if Username.replace('\n', '').replace(' ', '_') not in os.listdir('USERS/'):
        os.mkdir('USERS/'+Username.replace('\n', '').replace(' ', '_'))
        with open('USERS/'+Username.replace('\n', '').replace(' ', '_')+'/USERNAME.txt', 'w+') as f:
            f.write(Username.replace('\n', ''))
        with open('USERS/'+Username.replace('\n', '').replace(' ', '_')+'/PASSWORD.txt', 'w+') as f:
            f.write(Password.replace('\n', ''))
        with open('USERS/'+Username.replace('\n', '').replace(' ', '_')+'/ID.txt', 'w+') as f:
            f.write(GenerateID())
        os.mkdir('USERS/'+Username.replace('\n', '').replace(' ', '_')+'/PERMISSIONS')
        with open('USERS/'+Username.replace('\n', '').replace(' ', '_')+'/PERMISSIONS/ISADMIN.txt', 'w+') as f:
            f.write('False')
        with open('USERS/'+Username.replace('\n', '').replace(' ', '_')+'/PERMISSIONS/ISBANNED.txt', 'w+') as f:
            f.write('False')
        return True
    else:
        return False

def Register(Username, Password):
    if 'USERS' in os.listdir('.'):
        _reg(Username, Password)
    else:
        os.mkdir('USERS')
        _reg(Username, Password)
