
import plotly.graph_objects as go
import time
import json
b = []
d = []
with open('activities.json', 'r') as jsonfile:
    a = json.load(jsonfile)
e = a['activities']
for i in e:
    b.append(i['name'])
tot = 0
for i in e:
    sed = 0
    for j in i["time_entries"]:
        sed = sed + int(j["minutes"])*60 + \
            int(j["seconds"])+int(j["hours"])*3600
        tot = tot+sed
    d.append(sed)
kek = time.strftime("%d,%H:%M:%S", time.gmtime(tot))
kek = "TotalTime used :"+kek
fig = go.Figure(data=[go.Pie(labels=b, values=d, hole=.4)])
fig.update_traces(hoverinfo='percent+name', textinfo='label', textfont_size=20,
                  marker=dict(line=dict(color='#000000', width=2)))
fig.update_layout(
    title_text="Your Usage Activitiy",
    annotations=[dict(text=kek, x=0.9, y=0.9, font_size=12, showarrow=False)])
fig.show()
