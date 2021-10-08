from packages.shLIb import *
import json
class ShellyMain:
    comReg = None
    def initialize(self):
        print("                 _____ _          _ _       \n" +
              "                /  ___| |        | | |      \n" +
              "                \ `--.| |__   ___| | |_   _ \n" +
              "                 `--. \ '_ \ / _ \ | | | | |\n" +
              "                /\__/ / | | |  __/ | | |_| |\n" +
              "                \____/|_| |_|\___|_|_|\__, |\n" +
              "                          testing ver. __/ |\n" +
              "                                      |___/ ")
        self.readReg()
        print(self.comReg)
        while True:
            self.waitForCommand()

    def readReg(self):
        with open("./packages/shReg.json", "r") as regFile:
            regData = json.load(regFile)
            self.comReg = regData["com"]

    def addReg(self, reg , dest, data):
        with open("./packages/shReg.json", "r+") as regFile:
            regData = json.load(regFile)
            if dest in regData[reg]:
                i = None
                while i != "yes" or "y" or "n" or "no" or "":
                    print(dest, "in registry", reg, "equals", regData["reg"]["dest"])
                    i = input("Do you want to rewrite it?(y or n):")
                if i == "yes" or "y" or "":
                    regData[reg][dest] = data
                    print(regData)
                    json.dump(regData, regFile)
                    regFile.close()
                elif i == "n" or "no":
                    pass
            else:
                regData[reg][dest] = data
                print(regData)
                json.dump(regData, regFile)
                regFile.close()

    def waitForCommand(self):
        comLine = input("~>")
        self.executeCommand(comLine.split(" "))
        pass

    def executeCommand(self, comLine):
        if comLine[0] in self.comReg:
            eval(self.comReg[comLine[0]])
            # ShellyMain.addReg(self, comLine[1], comLine[2], comLine[3]) ЭТА ХУЙНЯ НИЧЕГО НЕ ДЕЛАЕТ!!! КОММЕНТАРИЙ НЕ УБИРАТЬ.
        else:
            print(comLine[0],  ":is wrong command")


if __name__ == '__main__':
    shell = ShellyMain()
    shell.initialize()
