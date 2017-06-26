
from diff import gen_diff
import urllib.request
import json
import dateutil.parser
import datetime

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def find_dev_branch(branches):
    develop_branch = ''
    develop_version = 0

    for i in range(0, len(branches)):
        branch = branches[i]
        branch_name = branch['name']
        if branch_name.startswith(('a', 'b', 'i')) and isFloat(branch_name[1:]):

            branch_version = float(branch_name[1:])
            if (branch_name.startswith('b')):
                branch_version += 100

            if branch_version > develop_version:
                develop_branch = branch_name
                develop_version = branch_version

    return develop_branch

def get_cache():
    try:
        file = open('_date_cache.txt', 'r')
    except:
        file = open('_date_cache.txt', 'w')

    return dateutil.parser.parse(file.read())

# date is a datetime.datetime object
def write_cache(date):
    format = '%Y-%m-%dT%H%M%S%z'
    date_str = date.strftime(format)
    print('Date string: ' + date_str)

    back = dateutil.parser.parse(date_str)
    print('Back into an object: ' + back + ' ; is same? ' + (back == date))

get_cache()

base_url = 'https://api.github.com/repos/CrowsOfWar/AvatarMod/'

branches_json = urllib.request.urlopen(base_url + 'branches').read()
branches = json.loads(branches_json)
dev_branch_name = find_dev_branch(branches)

dev_branch_json = urllib.request.urlopen(base_url + 'branches/' + dev_branch_name).read()
dev_branch = json.loads(dev_branch_json)

dev_branch_date_str = dev_branch['commit']['commit']['author']['date']
dev_branch_date = dateutil.parser.parse(dev_branch_date_str)

write_cache(dev_branch_date)

#print(str(dev_branch_date) + ' ' + datetime.datetime.strptime(str(dev_branch_date)))
