#!/usr/bin/env python

import sys
import logging
import optparse
import warnings

sys.dont_write_bytecode = True

# Import necessary modules
from lib.core.common import setPaths
from lib.core.data import logger
from lib.core.patch import dirtyPatches, resolveCrossReferences
from lib.core.settings import RESTAPI_DEFAULT_ADAPTER, RESTAPI_DEFAULT_ADDRESS, RESTAPI_DEFAULT_PORT
from lib.utils.api import client, server

def main():
    dirtyPatches()
    resolveCrossReferences()

    logger.setLevel(logging.DEBUG)
    setPaths(modulePath())

    parser = optparse.OptionParser()
    parser.add_option("-s", "--server", help="Run as a REST-JSON API server", default=False, action="store_true")
    parser.add_option("-c", "--client", help="Run as a REST-JSON API client", default=False, action="store_true")
    parser.add_option("-H", "--host", help=f"Host of the REST-JSON API server (default \"{RESTAPI_DEFAULT_ADDRESS}\")", default=RESTAPI_DEFAULT_ADDRESS)
    parser.add_option("-p", "--port", help=f"Port of the REST-JSON API server (default {RESTAPI_DEFAULT_PORT})", default=RESTAPI_DEFAULT_PORT, type="int")
    parser.add_option("--adapter", help=f"Server (bottle) adapter to use (default \"{RESTAPI_DEFAULT_ADAPTER}\")", default=RESTAPI_DEFAULT_ADAPTER)
    parser.add_option("--username", help="Basic authentication username (optional)")
    parser.add_option("--password", help="Basic authentication password (optional)")

    options, _ = parser.parse_args()

    if options.server:
        server(options.host, options.port, adapter=options.adapter, username=options.username, password=options.password)
    elif options.client:
        client(options.host, options.port, username=options.username, password=options.password)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
