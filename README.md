# IT-Networking

Networking scripts, device configurations, automation tools and IT notes.

## 📁 Repository Structure
```
IT-Networking/
├── scripts/
│   ├── python/        # Python automation (ping sweep, port scan, backups)
│   ├── bash/          # Linux shell scripts
│   └── powershell/    # Windows scripts
├── configs/
│   ├── cisco/         # Cisco router/switch configs
│   └── mikrotik/      # MikroTik configs
├── notes/             # Subnetting, VLANs, routing, troubleshooting notes
├── .github/workflows/ # CI checks
└── requirements.txt   # Python dependencies
```

## 🚀 Getting Started
```bash
git clone https://github.com/irfaniqbal-IT/IT-Networking.git
cd IT-Networking
pip install -r requirements.txt
python scripts/python/ping_sweep.py 192.168.1.0/24
```

## ⚠️ Security
- **Never** commit real passwords, SNMP communities, API keys or public IPs of production devices.
- Replace secrets with placeholders like `<PASSWORD>` before pushing configs.
- Only scan networks you own or have permission to test.

## 📄 License
MIT — see [LICENSE](LICENSE).
