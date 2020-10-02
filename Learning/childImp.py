from Learning.OopsDemo import Calculator  # class import


class ChildImp(Calculator):  # inheritance
    num2 = 200

    def __init__(self):  # child constructor
        Calculator.__init__(self, 2, 9)  # parent constructor

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj = ChildImp()
print(obj.getCompleteData())
