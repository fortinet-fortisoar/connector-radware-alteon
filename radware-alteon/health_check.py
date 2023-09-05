from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
from .radware_alteon_wrapper_ipAclNewCfgTable import init_connector


logger = get_logger(LOGGER_NAME)


def health_check(config=None, *args, **kwargs):
    url = config.get('uRL')
    b64EncodedAuth = config.get('b64EncodedAuth', None)
    username = config.get('username', None)
    password = config.get('password', None)
    usernamePasswordEncoding = config.get('userPassEncoding', 'utf-8')
    verify_ssl = config.get('verify_ssl', False)

    if not b64EncodedAuth and (not username or not password):
        raise ConnectorError('Missing required parameters')
    
    alt = None
    try:
        alt = init_connector(config, None)
        alt.login()
        status, content = alt.is_logged_in()
        if status:
            return f'Connector is Available return value:\n{str(content)}'
        else:
            logger.error(f'Connector error:\n{str(content)}')
            raise ConnectorError(f'Connector error:\n{str(content)}')

    except Exception as e:
        logger.exception('Error invoking endpoint: {0}'.format(alt))
        raise ConnectorError('Error: {0}'.format(str(e)))
    
