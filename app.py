
from diff import gen_diff
import urllib.request
import json
import dateutil.parser
import datetime
import os.path
import dateutil.tz;

cache_location = '_commitcache.txt'

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

    return open(cache_location, 'r').read()

def write_cache(sha):
    open(cache_location, 'w').write(sha)

def get_commit_date(sha):
    if not sha:
        return datetime.datetime(datetime.MINYEAR, 1, 1, 0, 0, 0, 0, dateutil.tz.tzutc())

    commit_json = urllib.request.urlopen(base_url + 'commits/' + sha).read()
    commit = json.loads(commit_json)
    date_str = commit['commit']['author']['date']
    return dateutil.parser.parse(date_str)

def get_file(sha, path):
    url = 'https://raw.githubusercontent.com/CrowsOfWar/AvatarMod/' + sha + '/' + path
    try:
        return urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        print('Error reaching url ' + url)
        return ''

base_url = 'https://api.github.com/repos/CrowsOfWar/AvatarMod/'

branches_json = urllib.request.urlopen(base_url + 'branches').read()
branches = json.loads(branches_json)
dev_branch_name = find_dev_branch(branches)

dev_branch_json = urllib.request.urlopen(base_url + 'branches/' + dev_branch_name).read()
dev_branch = json.loads(dev_branch_json)

new_sha = dev_branch['commit']['sha']
old_sha = get_cache()

new_date = get_commit_date(new_sha)
old_date = get_commit_date(old_sha)

print('Comparing new_date ' + str(new_date) + ' vs old_date ' + str(old_date))
if new_date > old_date:
    print('Found new dev branch commit!')

    diff = ''
    if new_sha:
        new_lang = get_file(new_sha, 'src/main/resources/assets/avatarmod/lang/en_US.lang')
        old_lang = get_file(old_sha, 'src/main/resources/assets/avatarmod/lang/en_US.lang')
    else:
        diff = get_file(new_sha, 'src/main/resources/assets/avatarmod/lang/en_US.lang')

    print('\nDiff:\n' + diff)

else:
    print('No new dev branch commit, skipping')

#write_cache(dev_branch_date)

#print(str(dev_branch_date) + ' ' + datetime.datetime.strptime(str(dev_branch_date)))
