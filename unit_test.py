from stat_test import *

s = '''
o - I want to start over.
2 - I am comparing two groups
3 - I am comparing three or more groups
i - My groups are independent
m - My groups are matched or dependent
p - My data is parametric
n - My data is nonparametric
c - My data includes a covariate
v - My data does not include a covariate
Your selection: '''


def processSelection(selection):
    if (selection == 'o'):
        makeList()
    elif (selection == '2'):
        isTwoGroups()
    elif (selection == '3'):
        isNotTwoGroups()
    elif (selection == 'i'):
        isNotPaired()
    elif (selection == 'm'):
        isPaired()
    elif (selection == 'p'):
        isParametric()
    elif (selection == 'n'):
        isNotParametric()
    elif (selection == 'c'):
        hasCovariate()
    elif (selection == 'v'):
        hasNoCovariate()


makeList()
selection = ''
while (selection != 'q'):
    selection = input(s)
    processSelection(selection)
    printList()
    selection = input("Enter q to quit, ENTER to continue: ")
