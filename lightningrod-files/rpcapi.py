from oslo.config import cfg
import oslo.messaging as messaging
from oslo_log import log

LOG = log.getLogger(__name__)


class RPCagent(object):
    def __init__(self):
        transport = messaging.get_transport(cfg.CONF)

        cfg.CONF.set_override('rabbit_host', 'arancino')
        cfg.CONF.set_override('rabbit_port', 5672)
        cfg.CONF.set_override('rabbit_userid', 'openstack')
        cfg.CONF.set_override('rabbit_password', 'RABBIT_PASS')
        cfg.CONF.set_override('rabbit_login_method', 'AMQPLAIN')
        cfg.CONF.set_override('rabbit_virtual_host', '/')
        cfg.CONF.set_override('rpc_backend', 'rabbit')
        target = messaging.Target(topic='cyborg-agent')
        client = messaging.RPCClient(transport, target)
        return client
    
