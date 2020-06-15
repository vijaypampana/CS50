from bs4 import BeautifulSoup
import json
import namegenerator, os, random
from datetime import datetime
import requests as req


__name__ = "utilities"

global clientCodeStart, firstNameStart, ssnFlag, delimiter
clientCodeStart = "8888"
firstNameStart = "auto"
ssnFlag = True
delimiter = ","


def jsonBeautifierprocess(value):
    return json.dumps(json.loads(value), indent=2)


def xmlBeautifierprocess(value):
    return str.replace((BeautifulSoup(value, "lxml").prettify(encoding='UTF-8')).decode("UTF-8"), "\n", "\r\n")


def appendZero(param, val):
    value = str(param)
    ln = val - len(value)
    while (ln > 0):
        value = '0' + value
        ln = ln - 1
    return value


def generateRandomChar(val):
    return namegenerator.gen().replace("-", "")[:val]


def getRandomNumber(val):
    return appendZero(int(random.random() * (10 ** val)), val)


def createNormalUser(env, version, apikey, clientCode):
    now = datetime.now()
    firstName = firstNameStart + generateRandomChar(8)
    lastName = generateRandomChar(8)
    loginid = generateRandomChar(8)
    userCode = clientCodeStart + str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + str(now.microsecond)
    ssn = getRandomNumber(9)
    fileContent = ""
    endPoint = ""
    with open("static/files/soap/createUser.xml") as file:
        fileContent = file.read()
    fileContent = str.replace(fileContent, '${version}', version)
    fileContent = str.replace(fileContent, '${apikey}', apikey)
    fileContent = str.replace(fileContent, '${client_code}', clientCode)
    fileContent = str.replace(fileContent, '${firstName}', firstName)
    fileContent = str.replace(fileContent, '${lastName}', lastName)
    fileContent = str.replace(fileContent, '${ssn}', ssn)
    fileContent = str.replace(fileContent, '${loginid}', loginid)
    fileContent = str.replace(fileContent, '${user_code}', userCode)

    if(env == 'qa') :
        endPoint = "https://qa-api.regrpayverisbp.com/api/services/CustomerServices"
    elif(env == 'qa2'):
        endPoint = "https://qa-api.regrpayverisbp.com/api/services/CustomerServices"

    resp = req.post(endPoint, fileContent)

    if resp.status_code != req.codes.ok:
        return "Encounter a issue while creating a new User"
    else:
        print(userCode)
        return userCode
