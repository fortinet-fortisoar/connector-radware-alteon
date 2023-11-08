from connectors.core.connector import get_logger, ConnectorError, Connector

from .operations import supported_operations, health_check

logger = get_logger('radware-alteon')


class ConnectorWrapper(Connector):

    def execute(self, config, operation, params, *args, **kwargs):
        try:
            return supported_operations.get(operation)(config, params)
        except Exception as Err:
            raise ConnectorError(Err)

    def check_health(self, config=None, *args, **kwargs):
        try:
            return health_check(config, *args, **kwargs)
        except Exception as Err:
            raise ConnectorError(Err)
