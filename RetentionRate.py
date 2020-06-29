from plotly import graph_objects as go

import sys

def compare(time, registered, days):
    newTime = [int(i) for i in time.split('.')]
    newReg = [int(i) for i in registered.split('.')]
    if(newTime[2] == newReg[2] and newTime[1] == newReg[1] and newTime[0] - days == newReg[0]):
        return True

def RetentionRate():
    file = open('Trainee Analyst Test DataSet - RetentionRate.csv', 'r')
    y = []
    IDs = list()
    x = [str(a) for a in file.read().split()]
    for k in range(1, len(x), 1):
        y.append([str(a) for a in x[k].split(',')])
    for i in range(0, len(y), 1):
        if(IDs.__contains__(y[i][0])):
            continue
        else:
            IDs.append(y[i][0])
    retentionDay = [int(0)for k in range(0, len(IDs), 1)]
    day = [int(k) for k in range(6)]
    amountOfRetention = [int(0)for k in range(0, 6, 1)]
    results = []
    for k in range(1,len(day), 1):
        for i in range(0, len(y), 1):
            if(compare(y[i][1], y[i][2], day[k])):
                ind = IDs.index(y[i][0])
                if(retentionDay[ind] == 0):
                    retentionDay[ind] = 1
        amountOfRetention[k] = 0
        for i in range(0, len(IDs), 1):
            if(retentionDay[i] == 1):
                amountOfRetention[k] = amountOfRetention[k] + 1
        results.append(amountOfRetention[k]/len(IDs)*100)
        print(results[k-1])

        retentionDay = [int(0) for k in range(0, len(IDs), 1)]
    fig = go.Figure(go.Bar(
        x=[int(num) for num in range(1, len(day), 1)],
        y=results))
    fig.show()

if __name__ == '__main__':
        sys.exit(RetentionRate())