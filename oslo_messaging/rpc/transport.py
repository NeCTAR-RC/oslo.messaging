__all__ = [
    'get_rpc_transport'
]

from oslo_messaging import transport as msg_transport


def get_rpc_transport(conf, url=None,
                      allowed_remote_exmods=None):
    """A factory method for Transport objects for RPCs.

    This method should be used to ensure the correct messaging functionality
    for RPCs. RPCs and Notifications may use separate messaging systems
    that utilize different drivers, different access permissions,
    message delivery, etc.

    Presently, this function works exactly the same as get_transport. It's
    use is recommended as disambiguates the intended use for the transport
    and may in the future extend functionality related to the separation of
    messaging backends.

    :param conf: the user configuration
    :type conf: cfg.ConfigOpts
    :param url: a transport URL, see :py:class:`transport.TransportURL`
    :type url: str or TransportURL
    :param allowed_remote_exmods: a list of modules which a client using this
                                  transport will deserialize remote exceptions
                                  from
    :type allowed_remote_exmods: list
    """
    return msg_transport._get_transport(conf, url,
                                        allowed_remote_exmods)
