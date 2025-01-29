import logging


log = logging.getLogger(__name__)

def bar() -> str:
    log.debug("bar")
    return "bar"
