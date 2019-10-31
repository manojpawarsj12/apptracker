''' 
This file gives the linux support for this repo
'''
import sys
import os
import subprocess
import re


def get_active_window_raw():
    '''
    returns the details about the window not just the title
    '''
    root = subprocess.Popen(
        ['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)
    stdout, stderr = root.communicate()

    m = re.search(b'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout)
    if m != None:
        window_id = m.group(1)
        window = subprocess.Popen(
            ['xprop', '-id', window_id, 'WM_NAME'], stdout=subprocess.PIPE)
        stdout, stderr = window.communicate()
    else:
        return None

    match = re.match(b"WM_NAME\(\w+\) = (?P<name>.+)$", stdout)
    if match != None:
        ret = match.group("name").strip(b'"')
        return ret
    return None


def get_chrome_url_x():
    ''' 
    instead of url the name of the website and the title of the page is returned seperated by '/' 
    '''
    detail_full = get_active_window_raw()
    detail_list = detail_full.split(' - ')
    detail_list.pop()
    detail_list = detail_list[::-1]
    _active_window_name = 'Google Chrome -> ' + " / ".join(detail_list)
    return _active_window_name


def get_active_window_x():
    full_detail = get_active_window_raw()
    detail_list = None if None else full_detail.split(" - ")
    new_window_name = detail_list[-1]
    return new_window_name
