#!/usr/bin/env python3

import asyncio
import ast
from connectrum.client import StratumClient
from connectrum.svr_info import ServerInfo
from connectrum import ElectrumErrorResponse
from prompt_toolkit.shortcuts import prompt_async
from prompt_toolkit.contrib.completers import WordCompleter


STRATUM_COMPLETER = WordCompleter([
    "server.version",
    "server.banner",
    "server.donation_address",
    "server.peers.subscribe",
    "blockchain.numblocks.subscribe",
    "blockchain.headers.subscribe",
    "blockchain.address.subscribe",
    "blockchain.address.get_history",
    "blockchain.address.get_mempool",
    "blockchain.address.get_balance",
    "blockchain.address.get_proof",
    "blockchain.address.listunspent",
    "blockchain.utxo.get_address",
    "blockchain.block.get_header",
    "blockchain.block.get_chunk",
    "blockchain.transaction.broadcast",
    "blockchain.transaction.get_merkle",
    "blockchain.transaction.get",
    "blockchain.estimatefee",
])


async def interact(conn, svr, connector):
    try:
        await connector
    except Exception as e:
        print("Unable to connect to server: %s" % e)
        return -1

    print("\nConnected to: %s\n" % svr)

    try:
        rv = await conn.RPC("server.banner", [])
        print(rv)
    except ElectrumErrorResponse as e:
        print(e)

    while True:
        try:
            result = await prompt_async(">>> ",
                                        completer=STRATUM_COMPLETER,
                                        patch_stdout=True)
        except KeyboardInterrupt:
            continue
        except EOFError:
            break

        result = result.strip()

        if result == "":
            continue

        if " " not in result:
            result += " []"

        command, args = result.split(" ", 1)
        args = ast.literal_eval("%s" % args)
        rv = await conn.RPC(command, args)
        print(repr(rv))

    conn.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Interact with an electrum server")
    parser.add_argument("args", nargs="*", default=[],
                        help="Arguments for method")
    parser.add_argument("--server", default="cluelessperson.com",
                        help="Hostname of Electrum server to use")
    parser.add_argument("--protocol", default="s",
                        help="Protocol code: t=TCP Cleartext, s=SSL, etc")
    parser.add_argument("--port", default=None,
                        help="Port number to override default for protocol")
    parser.add_argument("--tor", default=False, action="store_true",
                        help="Use local Tor proxy to connect")

    args = parser.parse_args()

    svr = ServerInfo(args.server, args.server,
                     ports=("%s%s" % (args.protocol, args.port)
                            if args.port else args.protocol))

    loop = asyncio.get_event_loop()

    conn = StratumClient()
    connector = conn.connect(svr, args.protocol,
                             use_tor=svr.is_onion,
                             disable_cert_verify=True)

    loop.run_until_complete(interact(conn, svr, connector))
    loop.close()


if __name__ == '__main__':
    main()
