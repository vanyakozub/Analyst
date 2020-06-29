from plotly import graph_objects as go

import sys

def firstEnter():
    y =[]
    file = open('Trainee Analyst Test DataSet - FirstEnter.csv', 'r')
    x = [str(a) for a in file.read().split()]
    for k in range(2,len(x), 1):
        y.append( [str(a) for a in x[k].split(',')])
    stages = [int(0) for num in range(0, 9, 1)]
    for z in range(0, len(y), 1):
        stages[int(y[z][1])] = stages[int(y[z][1])] + 1
    for i in range(0, 8, 1):
        for l in range(i+1, 9, 1):
            stages[i] = stages[i] + stages[l]
    config = {
        'displaylogo': False,
        'toImageButtonOptions': {
            'format': 'png',  # one of png, svg, jpeg, webp
            'filename': 'FirstEnter',
            'height': 800,
            'width': 1200,
            'scale': 1  # Multiply title/legend/axis/canvas sizes by this factor
        }
    }
    file.close()
    fig = go.Figure(go.Funnel(
        y=[int(num) for num in range(0, 9, 1)],
        x=stages))
    fig.show(config = config)

if __name__ == '__main__':
    sys.exit(firstEnter())
