class aTest:
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

print("Now, remove the nonparametric tests...")
# can't just iterate through list and remove certain items
# when you delete one item, the other indexes change too
# so we iterate through a copy of the list and remove
# from the original list--without moving from item to item
# in the original
for test in list(testList):
    if test.parametric == False:
        testList.remove(test)

print("...and print what's left")
for test in testList:
    print(test.name)

print("Next, remove test requiring two groups...")
for test in list(testList):
    if test.twoGroups == True:
        testList.remove(test)

print("...and print what's left")
for test in testList:
    print(test.name)
