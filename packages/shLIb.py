import json
class shCom:

    def exit(self):
        quit()

    def executeScript(self, target):
        comReg = None
        with open("./packages/shReg.json", "r") as regFile:
            regData = json.load(regFile)
            comReg = regData["com"]
        pass