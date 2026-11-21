#!/usr/bin/env bash
# network_info.sh - quick Linux network diagnostics
# Usage: bash network_info.sh [target-host]
set -euo pipefail

TARGET="${1:-8.8.8.8}"

echo "===== Hostname ====="; hostname
echo; echo "===== IP Addresses ====="; ip -brief addr
echo; echo "===== Routing Table ====="; ip route
echo; echo "===== DNS Servers ====="; grep nameserver /etc/resolv.conf || true
echo; echo "===== Listening Ports ====="; ss -tuln
echo; echo "===== Ping ${TARGET} ====="; ping -c 4 "${TARGET}" || echo "Ping failed"
echo; echo "===== Traceroute ${TARGET} ====="
if command -v traceroute >/dev/null; then traceroute -m 15 "${TARGET}"; else echo "traceroute not installed"; fi
