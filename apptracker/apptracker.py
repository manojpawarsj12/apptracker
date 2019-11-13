from __future__ import print_function
import time
from activity import *
import json
import datetime
import sys
import plotly.graph_objects as go
import argparse

if sys.platform in ['Windows', 'win32', 'cygwin']:
    import win32gui
    import uiautomation as auto
elif sys.platform in ['linux', 'linux2']:
    import linux as l

b=list()
def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]


def get_active_window():
    _active_window_name = None
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        window = win32gui.GetForegroundWindow()
        _active_window_name = win32gui.GetWindowText(window)
    else:
        print("sys.platform={platform} is not supported."
              .format(platform=sys.platform))
        print(sys.version)
    return _active_window_name


def get_chrome_url():
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        window = win32gui.GetForegroundWindow()
        chromeControl = auto.ControlFromHandle(window)
        edit = chromeControl.EditControl()
        return 'https://' + edit.GetValuePattern().Value
    else:
        print("sys.platform={platform} is not supported."
              .format(platform=sys.platform))
        print(sys.version)
    return _active_window_name


def show_activity():

    b = list()
    d = list()
    try:
        with open('activities.json', 'r') as jsonfile:
            a = json.load(jsonfile)
            e = a['activities']
    except Exception:
        print("no json data")
        pass

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
    kek = "Time used :"+kek

    fig = go.Figure(data=[go.Pie(labels=b, values=d, hole=.4)])
    fig.update_traces(hoverinfo='label+percent+name', textinfo='value', textfont_size=20,
                      marker=dict(line=dict(color='#000000', width=2)))
    fig.update_layout(
        title_text="Your Usage Activitiy",
        annotations=[dict(text=kek, x=0.18, y=0.5, font_size=20, showarrow=False)])
    fig.show()
    return b,  kek


def record(active_window_name, activity_name, start_time, activeList, first_time):
    print("CTRL+C to Quit:")
    try:
        activeList.initialize_me()
    except Exception:
        print('No json')

    try:
        while True:
            previous_site = ""
            if sys.platform not in ['linux', 'linux2']:
                new_window_name = get_active_window()
                if 'Google Chrome' in new_window_name:
                    new_window_name = url_to_name(get_chrome_url())
            if sys.platform in ['linux', 'linux2']:
                new_window_name = l.get_active_window_x()
                if 'Google Chrome' in new_window_name:
                    new_window_name = l.get_chrome_url_x()

            if active_window_name != new_window_name:
                print(active_window_name)
                activity_name = active_window_name

                if not first_time:
                    end_time = datetime.datetime.now()
                    time_entry = TimeEntry(start_time, end_time, 0, 0, 0, 0)
                    time_entry._get_specific_times()

                    exists = False
                    for activity in activeList.activities:
                        if activity.name == activity_name:
                            exists = True
                            activity.time_entries.append(time_entry)

                    if not exists:
                        activity = Activity(activity_name, [time_entry])
                        activeList.activities.append(activity)
                    with open('activities.json', 'w') as json_file:
                        json.dump(activeList.serialize(), json_file,
                                  indent=4, sort_keys=True)
                        start_time = datetime.datetime.now()
                first_time = False
                active_window_name = new_window_name

            time.sleep(1)

    except KeyboardInterrupt:
        with open('activities.json', 'w') as json_file:
            json.dump(activeList.serialize(), json_file,
                      indent=4, sort_keys=True)
def main():
    active_window_name = str()
    activity_name = ""
    start_time = datetime.datetime.now()
    activeList = AcitivyList([])
    first_time = True
    parser = argparse.ArgumentParser()
    parser.add_argument('-start',
                        help='start recording your usage activity')
    parser.add_argument("-show", help='show your usgae in pie chart')
    args = parser.parse_args()
    if args.start:
        record(active_window_name, activity_name,
             start_time, activeList, first_time)
    elif args.show:
        b,  tot = show_activity()
        print(tot," i.e day/hours/minutes/seconds format")
        print("*******APPS**********")
        j=1
        for i in b:
            print("{} : {}".format(j,i))   
            j+=1

if __name__ == "__main__":
    main()
