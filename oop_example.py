
DM = "root dm"
class MyAgent:
    DM = "agent DM"

    def __init__(self):
        print("agent init")
        self.DM ="modified agent dm"

    def init(self):
        print("agent init caller")
        self.DM ="outside initializer called"

    def output(self):
        print(DM)
        print(self.DM)

class Runner:
    def __init__(self, agent):
        self.agent = agent
        agent.init()

    def output(self):
        self.agent.output()

# agent = MyAgent()
# agent.output()

thingy = Runner(MyAgent())
thingy.output()
