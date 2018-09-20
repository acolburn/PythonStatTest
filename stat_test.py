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
testList.append(aTest("one-way independent ANOVA", 0, 1, 1, 0, 0))
testList.append(aTest("Kruskall-Wallis test", 0, 1, 0, 0, 0))
testList.append(aTest("one-way repeated measures ANOVA", 0, 1, 1, 0, 1))
testList.append(aTest("Friedman's ANOVA", 0, 1, 0, 0, 1))
# testList.append(aTest("Chi squared test",0,0,0,0,0))...check on this
testList.append(aTest("ANCOVA", 0, 1, 1, 1, 0))

print("All the tests ...")
for test in testList:
    print(test.name)

print("All the parametric tests...")
for test in testList:
    if test.parametric == True:
        print(test.name)

print("Now, remove the nonparametric tests...")
for test in testList:
    if test.parametric == False:
        testList.remove(test)

print("...and print what's left")
for test in testList:
    print(test.name+", "+str(test.parametric))
