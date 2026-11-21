#!/usr/bin/env python3
"""Ping sweep: find live hosts in a subnet.

Usage: python ping_sweep.py 192.168.1.0/24
"""
import ipaddress
import platform
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor


def ping(host: str) -> bool:
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(
        ["ping", flag, "1", "-W", "1", host] if flag == "-c" else ["ping", flag, "1", "-w", "1000", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    network = ipaddress.ip_network(sys.argv[1], strict=False)
    hosts = [str(h) for h in network.hosts()]
    print(f"Scanning {len(hosts)} hosts in {network} ...")
    with ThreadPoolExecutor(max_workers=64) as pool:
        for host, alive in zip(hosts, pool.map(ping, hosts)):
            if alive:
                print(f"[UP] {host}")


if __name__ == "__main__":
    main()
