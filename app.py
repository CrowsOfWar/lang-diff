
from diff import gen_diff
import urllib.request
import json
import dateutil.parser
import datetime
import os.path

cache_location = '_date_cache.txt'

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

    if not os.path.isfile(cache_location):
        open(cache_location, 'x')

    try:
        return dateutil.parser.parse(open(cache_location, 'r').read())
    except ValueError:
        return datetime.datetime(datetime.MINYEAR, 1, 1)

# date is a datetime.datetime object
def write_cache(date):
    format = '%Y-%m-%dT%H%M%S%z'
    date_str = date.strftime(format)

    open(cache_location, 'w').write(date_str)

base_url = 'https://api.github.com/repos/CrowsOfWar/AvatarMod/'

branches_json = urllib.request.urlopen(base_url + 'branches').read()
branches = json.loads(branches_json)
dev_branch_name = find_dev_branch(branches)

dev_branch_json = urllib.request.urlopen(base_url + 'branches/' + dev_branch_name).read()
dev_branch = json.loads(dev_branch_json)

dev_branch_date_str = dev_branch['commit']['commit']['author']['date']
dev_branch_date = dateutil.parser.parse(dev_branch_date_str)

old_date = get_cache()

if dev_branch_date > old_date:
    print('Found new dev branch commit!')
else:
    print('No new dev branch commit, skipping')

write_cache(dev_branch_date)

#print(str(dev_branch_date) + ' ' + datetime.datetime.strptime(str(dev_branch_date)))
