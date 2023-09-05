import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .radware_alteon import Radware_Alteon


logger = get_logger(LOGGER_NAME)


def init_connector(config, params) -> Radware_Alteon:
    try:
        url = config.get('uRL')
        b64EncodedAuth = config.get('b64EncodedAuth', None)
        username = config.get('username', None)
        password = config.get('password', None)
        usernamePasswordEncoding = config.get('userPassEncoding', 'utf-8')
        verify_ssl = config.get('verify_ssl', False)

        return Radware_Alteon(url, b64EncodedAuth, username, password, usernamePasswordEncoding, verify_ssl)
    
    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))


def view_table(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config, params)
        return alt.view_table()
    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))

    

def view_table_element(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config, params)
        indx = params.get('indx')

        return alt.view_table_element(indx)

    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))
   
    
def edit_table_element(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config, params)
        indx = params.get('indx')
        ip = params.get('ip')
        action = params.get('action', '')
        mask = params.get('mask')

        return alt.edit_table_element(indx, ip, action, mask)

    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))
    

def add_table_element(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config, params)
        indx = params.get('indx')
        ip = params.get('ip')
        action = params.get('action', '')
        mask = params.get('mask')

        return alt.add_table_element(indx, ip, action, mask)

    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))
    

def delete_table_element(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config, params)
        indx = params.get('indx')

        return alt.delete_table_element(indx)

    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))
    