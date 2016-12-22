
import json
import sys
import os

class setting:
    def __init__(self,name,setup):
        self.name = name
        self.setup = setup
        self.dict={}
        self.path = "setting.json"

    def savesetting(self):
        with open(self.path, 'w') as f:
            self.dict[self.name]= self.setup
            buf = json.dumps(self.dict)
            f.write(buf)

    def load_settings(self):
        with open(self.path) as f:
                c = f.read()
                d1 = json.loads(c)
                settings = d1[self.name]

        return settings



def main():
    text = setting("text",1)
    text.savesetting()
    a = text.load_settings()
    print a

main()