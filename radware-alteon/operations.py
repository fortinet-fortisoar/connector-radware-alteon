""""
Copyright start
MIT License
Copyright (c) 2023 Fortinet Inc
Copyright end
"""

from connectors.core.connector import get_logger, ConnectorError
from .utils import Radware_Alteon
logger = get_logger('radware-alteon')


def init_connector(config) -> Radware_Alteon:
    try:
        server_url = config.get('server_url')
        authentication_type = config.get('authentication_type')
        api_token = config.get('api_token')
        username = config.get('username')
        password = config.get('password')
        verify_ssl = config.get('verify_ssl', False)
        return Radware_Alteon(server_url, authentication_type, api_token, username, password, verify_ssl)
    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))


def view_table(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config)
        return alt.view_table()
    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))


def view_table_element(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config)
        index = params.get('index')
        return alt.view_table_element(index)

    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))


def edit_table_element(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config)
        index = params.get('index')
        ip_address = params.get('ip_address')
        mask = params.get('mask')
        return alt.edit_table_element(index, ip_address, mask)

    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))


def add_table_element(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config)
        index = params.get('index')
        ip_address = params.get('ip_address')
        mask = params.get('mask')
        return alt.add_table_element(index, ip_address, mask)

    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))


def delete_table_element(config, params, *args, **kwargs) -> dict:
    try:
        alt = init_connector(config)
        index = params.get('index')
        return alt.delete_table_element(index)

    except Exception as e:
        logger.exception(e)
        raise ConnectorError('Error: {0}'.format(str(e)))


def health_check(config=None, *args, **kwargs):
    try:
        alt = init_connector(config)
        if alt.is_logged_in:
            return True
    except Exception as e:
        logger.exception('Error in health_check')
        raise ConnectorError('Error: {0}'.format(str(e)))


supported_operations = {
    'view_table': view_table,
    'view_table_element': view_table_element,
    'edit_table_element': edit_table_element,
    'add_table_element': add_table_element,
    'delete_table_element': delete_table_element
}
