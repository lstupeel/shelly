import json

class ShellyMain:
    comReg = None
    usrReg = None
    sysReg = None

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
        self.initLibs()

        while True:
            self.waitForCommand()

    def initLibs(self):
        libs = self.sysReg["include"]
        for lib in libs:
            exec(f"from {lib} import *")

    def readReg(self):
        with open("./packages/shReg.json", "r") as regFile:
            regData = json.load(regFile)
            self.comReg = regData["com"]
            self.usrReg = regData["usr"]
            self.sysReg = regData["sys"]

    def addReg(self, reg , dest, data):
        regFile = open("./packages/shReg.json", "r")
        regData = json.load(regFile)
        if dest in regData[reg]:
            i = None

            while i not in ["y", "n", "no", "yes", ""]:
                print(dest, "in registry", reg, "equals", regData[reg][dest])
                i = input("Do you want to rewrite it?(y or n):")

            if i == "yes" or "y" or "":
                regData[reg][dest] = data
                regFile.close()
                regFile = open("./packages/shReg.json", "w")
                json.dump(regData, regFile)
                regFile.close()

            elif i == "n" or "no":
                pass
        else:
            regData[reg][dest] = data
            regFile.close()
            regFile = open("./packages/shReg.json", "w")
            json.dump(regData, regFile)
            regFile.close()
        self.readReg()
                
    def executeScript(self, target):
        pass
    
    def waitForCommand(self):
        comLine = input(self.usrReg["username"] + "@~>")
        self.executeCommand(comLine.split(" "))
        pass

    def executeCommand(self, comLine):
        if comLine[0] in self.comReg:
            eval(self.comReg[comLine[0]])
        else:
            print(comLine[0],  ":is wrong command") 

if __name__ == '__main__':
    shell = ShellyMain()
    shell.initialize()
