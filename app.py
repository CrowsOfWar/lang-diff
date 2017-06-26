
from diff import gen_diff
import urllib.request
import json

base_url = 'https://api.github.com/repos/CrowsOfWar/AvatarMod/'

branches_json = urllib.request.urlopen(base_url + 'branches').read()
branches = json.loads(branches_json)
print(branches)
