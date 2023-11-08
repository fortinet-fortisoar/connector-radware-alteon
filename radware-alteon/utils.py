import base64
import copy
import json
from urllib.parse import urlparse

import requests
from connectors.core.connector import ConnectorError, get_logger
from requests import exceptions as req_exceptions

logger = get_logger('radware-alteon')


class Radware_Alteon():
    def __init__(self, server_url, authentication_type, api_key, username, password, verify_ssl):
        self.server_url = server_url
        self.authentication_type = authentication_type
        self.username = username,
        self.password = password
        self.verify_ssl = verify_ssl
        self.connect_timeout = 10
        self.read_timeout = 10
        self.is_logged_in = False
        if authentication_type == 'Basic Authentication':
            usr_pass = username + ":" + password
            usr_pass = usr_pass.encode()
            api_token = base64.b64encode(usr_pass).decode("utf-8")
        else:
            api_token = api_key
        self.headers = {
            'Authorization': 'Basic {}'.format(api_token)
        }
        self.login()


    def __exit__(self):
        if self.is_logged_in:
            self.logout()

    def make_rest_call(self, endpoint, params={}, payload=None, headers=None, method='GET'):
        service_endpoint = '{0}{1}'.format(self.server_url, endpoint)
        logger.debug('API Service URL: {}'.format(service_endpoint))
        if headers:
            self.headers.update(headers)
        try:
            response = requests.request(method, service_endpoint, data=payload, params=params, headers=self.headers,
                                        verify=self.verify_ssl, timeout=(self.connect_timeout, self.read_timeout))
            logger.debug('API Status Code : {}'.format(response.status_code))
            logger.debug('Rest API Response : {}'.format(response.text))
            if response.ok:
                json_data = json.loads(response.content.decode('utf-8'))
                return json_data
            else:
                logger.error("Rest API Response: {0}".format(response.text))
                raise ConnectorError('Status Code: {0}, API Response: {1}'.format(response.status_code, response.text))
        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as err:
            logger.error(err)
            raise ConnectorError(str(err))

    def login(self) -> dict:
        # login logout got the input form in here
        # https://support.radware.com/app/answers/answer_view/a_id/16798/~/how-to-authenticate-the-alteon-rest-api
        # resp = sess.post(api_url, auth=HTTPBasicAuth(username, password))
        resp = self.make_rest_call('/config/login', method='POST')
        if resp:
            self.is_logged_in = True

    def logout(self) -> dict:
        resp = self.make_rest_call('/config/logout', method='POST')
        if resp:
            self.is_logged_in = False
        return resp

    def view_table(self) -> dict:
        return self.make_rest_call('/config/IpAclNewCfgTable', method='GET')

    def view_table_element(self, index: int) -> dict:
        return self.make_rest_call(f'/config/IpAclNewCfgTable/{index}', method='GET')

    def edit_table_element(self, index: int, ipaddr: str, mask: str) -> dict:
        payload = {
            'Ip': ipaddr,
            'Mask': mask
        }

        body_data = json.dumps(payload, separators=('', ' : '), indent=0)

        tmp_header = copy.deepcopy(self.headers)
        tmp_header['Context-Type'] = 'text/plain'
        tmp_header['Accept-Encoding'] = 'gzip, deflate, br'
        tmp_header['Content-Length'] = str(len(body_data))
        api_url = copy.deepcopy(self.server_url)
        parsed = urlparse(api_url)
        port = parsed.port
        if not port:
            port = 443 if api_url.startswith('https') else 80
        tmp_header['Host'] = f'{parsed.hostname}:{port}'
        return self.make_rest_call(f'/config/IpAclNewCfgTable/{index}', payload=body_data, headers=tmp_header,
                                   method='PUT')

    def add_table_element(self, index: int, ipaddr: str, mask: str) -> dict:
        payload = {
            'Ip': ipaddr,
            'Mask': mask
        }

        body_data = json.dumps(payload, separators=('', ' : '), indent=0)

        tmp_header = copy.deepcopy(self.headers)
        tmp_header['Context-Type'] = 'text/plain'
        tmp_header['Accept-Encoding'] = 'gzip, deflate, br'
        tmp_header['Content-Length'] = str(len(body_data))
        api_url = copy.deepcopy(self.server_url)
        parsed = urlparse(api_url)
        port = parsed.port
        if not port:
            port = 443 if api_url.startswith('https') else 80
        tmp_header['Host'] = f'{parsed.hostname}:{port}'

        if index == 0:
            ip_acl_new_ctg_table = self.view_table().get('IpAclNewCfgTable', [])
            if len(ip_acl_new_ctg_table) > 0:
                index = ip_acl_new_ctg_table[-1].get('Indx', 0) + 1

        return self.make_rest_call(f'/config/IpAclNewCfgTable/{index}', payload=body_data,
                                   headers=tmp_header, method='POST')

    def delete_table_element(self, index: int) -> dict:
        return self.make_rest_call(f'/config/IpAclNewCfgTable/{index}', method='DELETE')
