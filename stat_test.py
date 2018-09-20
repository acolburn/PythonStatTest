class aTest:
    name = ""
    twoGroups = -1
    continuous = -1
    parametric = -1
    covariates = -1
    paired = -1

    def __init__(self, name, twoGroups, continuous, parametric, covariates, paired):
        self.name = name
        self.twoGroups = twoGroups
        self.continuous = continuous
        self.parametric = parametric
        self.covariates = covariates
        self.paired = paired


testList = []
testList.append(aTest("independent samples t-test", 1, 1, 1, 0, 0))
testList.append(aTest("dependent samples t-test", 1, 1, 1, 0, 1))
testList.append(aTest("Mann-Whitney U-test", 1, 1, 0, 0, 0))
testList.append(aTest("Wilcoxson matched pairs test", 1, 1, 0, 0, 1))

for test in testList:
    if test.paired == False:
        print(test.name+" is unpaired.")
    if test.parametric == True:
        print(test.name + " is parametric.")
