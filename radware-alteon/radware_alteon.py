# %%
import requests
import json
import copy
from urllib.parse import urlparse
from requests.auth import HTTPBasicAuth
from base64 import b64encode, b64decode

class Radware_Alteon():
    def __init__(
            self, 
            api_url: str, 
            b64EncodedAuth: str=None,
            username: str=None, 
            password: str=None, 
            userpass_encoding: str='utf-8', 
            verify_ssl: bool=False,
            connect_timeout: int=10,
            read_timeout: int=10
        ) -> None:
        self.api_url = api_url
        self.verify_ssl = verify_ssl
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout
        self.last_resp = None
        self.sess = requests.session()
        
        if not b64EncodedAuth:
            b64encoded_user_pass = b64encode(f'{username}:{password}'.encode(userpass_encoding))
            b64EncodedAuth = b64encoded_user_pass.decode(userpass_encoding)
            self.login(api_url, b64EncodedAuth, username, password, userpass_encoding)

        self.headers = {
            'Authorization': f'Basic {b64EncodedAuth}'
        } 


    def __exit__(self):
        if self.is_logged_in():
            self.logout()

    # ---------------------------- login logout start ---------------------------- 

    def login(self) -> None:
        # login logout got the input form in here
        # https://support.radware.com/app/answers/answer_view/a_id/16798/~/how-to-authenticate-the-alteon-rest-api
        # resp = sess.post(api_url, auth=HTTPBasicAuth(username, password))
        self.last_resp = self.sess.post(self.api_url, headers=self.headers, verify=self.verify_ssl, timeout=(self.connect_timeout, self.read_timeout))


    def is_logged_in(self) -> tuple:
        if self.last_resp.status_code == 200:
            return (True, self.last_resp.content)
        return (False, self.last_resp.content)


    def logout(self) -> None:
        self.last_resp = self.sess.post(f'{self.api_url}/config/logout', headers=self.headers, verify=self.verify_ssl, timeout=(self.connect_timeout, self.read_timeout))

    # ---------------------------- login log out end ---------------------------- 


    # ---------------------------- ipAclNewCfgTable.html start ---------------------------- 

    def view_table(self) -> dict:
        self.last_resp = self.sess.get(f'{self.api_url}/config/IpAclNewCfgTable', headers=self.headers, verify=self.verify_ssl, timeout=(self.connect_timeout, self.read_timeout))
        return self.last_resp.json()


    def view_table_element(self, indx: int) -> dict:
        self.last_resp = self.sess.get(f'{self.api_url}/config/IpAclNewCfgTable/{indx}', headers=self.headers, verify=self.verify_ssl, timeout=(self.connect_timeout, self.read_timeout))
        return self.last_resp.json()


    def edit_table_element(self, indx: int, ipaddr: str, action: str, mask: str) -> dict:
        # action { 1=other 2=delete 2147483647=unsupported }
        action_int = 2147483647 # unsupported
        if action.lower() == 'other (add)':
            action_int = 1 # other
        elif action.lower() == 'delete':
            action_int = 2 # delete

        payload = {
            'Ip': ipaddr,
            'Mask': mask
        }

        body_data = json.dumps(payload, separators=('', ' : '), indent=0)

        tmp_header = copy.deepcopy(self.headers)
        tmp_header['Context-Type'] = 'text/plain'
        tmp_header['Accept-Encoding'] = 'gzip, deflate, br'
        tmp_header['Content-Length'] = str(len(body_data))
        api_url = copy.deepcopy(self.api_url)
        parsed = urlparse(api_url)
        port = parsed.port
        if not port:
            port = 443 if api_url.startswith('https') else 80
        tmp_header['Host'] = f'{parsed.hostname}:{port}'

        self.last_resp = self.sess.put(f'{self.api_url}/config/IpAclNewCfgTable/{indx}', data=body_data, headers=tmp_header, verify=self.verify_ssl, timeout=(self.connect_timeout, self.read_timeout))
        return self.last_resp.json()


    def add_table_element(self, indx: int, ipaddr: str, action: str, mask: str) -> dict:
        # action { 1=other 2=delete 2147483647=unsupported }
        action_int = 2147483647 # unsupported
        if action.lower() == 'other (add)':
            action_int = 1 # other
        elif action.lower() == 'delete':
            action_int = 2 # delete

        payload = {
            'Ip': ipaddr,
            'Mask': mask
        }

        body_data = json.dumps(payload, separators=('', ' : '), indent=0)

        tmp_header = copy.deepcopy(self.headers)
        tmp_header['Context-Type'] = 'text/plain'
        tmp_header['Accept-Encoding'] = 'gzip, deflate, br'
        tmp_header['Content-Length'] = str(len(body_data))
        api_url = copy.deepcopy(self.api_url)
        parsed = urlparse(api_url)
        port = parsed.port
        if not port:
            port = 443 if api_url.startswith('https') else 80
        tmp_header['Host'] = f'{parsed.hostname}:{port}'

        if indx == 0:
            ipAclNewCfgTable = self.view_table().get('IpAclNewCfgTable', [])
            if len(ipAclNewCfgTable) > 0:
                indx = ipAclNewCfgTable[-1].get('Indx', 0) + 1

        self.last_resp = self.sess.post(f'{self.api_url}/config/IpAclNewCfgTable/{indx}', data=body_data, headers=tmp_header, verify=self.verify_ssl, timeout=(self.connect_timeout, self.read_timeout))
        return self.last_resp.json()
    
    
    def delete_table_element(self, indx: int) -> dict:
        self.last_resp = self.sess.delete(f'{self.api_url}/config/IpAclNewCfgTable/{indx}', headers=self.headers, verify=self.verify_ssl, timeout=(self.connect_timeout, self.read_timeout))
        return self.last_resp.json()
    
    # ---------------------------- ipAclNewCfgTable.html end ---------------------------- 



# %%
if __name__ == '__main__':
    alt = Radware_Alteon('https://google.com', 'user', 'pass')  
    if alt.is_logged_in():
        table = alt.view_table()
        print(f'table: {json.dumps(table, indent=4)}')

        # # todo change values to see if this works!
        # alt.view_table_element(table[0])
        # alt.edit_table_element(table[0])
        # alt.add_table_element(table[0])
        # alt.delete_table_element(table[0])
        # # end of todo

        print('user is successfully logged in')
        alt.logout()