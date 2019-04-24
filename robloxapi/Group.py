from .request import Request
from bs4 import BeautifulSoup
import requests
from .xcsrf import get_xcsrf
import json
class Group:
     
    def __init__(self, cookie=str(), id=str()):
        if cookie is None:
            self.cookie = False
            self.id = False
        self.cookie = cookie
        self.id = id
        self.xcsrf = get_xcsrf()
    
    def groupSearch(self, groupName, show):
        url = f'https://www.roblox.com/search/groups/list-json?keyword={groupName}&maxRows={str(show)}&startRow=0'
        r = requests.get(url)
        r = json.loads(r.text)
        results = r['GroupSearchResults']        
        return results

    def getGroup(self, id, login=False):
        url = f'https://groups.roblox.com/v1/groups/{id}'
        r = requests.get(url)
        if r.status_code is not 200:
            print(r.status_code)
            return {'found': False}
        else:
            groupinfo = json.loads(r.text)
            groupinfo['found'] = True
            return groupinfo
    
    def getGroupRoles(self, id, login=False):
        url = f'https://groups.roblox.com/v1/groups/{id}/roles'
        if login is True and self.cookie is not False:
            cookies = {
                '.ROBLOSECURITY': self.cookie
            }
        else:
            cookies = {}
        r = requests.get(url, cookies=cookies)
        if r.status_code is not 200:
            return {'found': False}
        else:
            data = json.loads(r.text)
            data['found'] = True
            del data['groupId']
            return data
        

