<p align="center">
  <img src="https://github.com/user-attachments/assets/6ce54a27-8fb6-48e6-9d1f-da144f43425a"/>
</p>
<h3 align="center">cryptnox.github.io</h3>
<p align="center">Central hub for Cryptnox technical documentation</p>
<br/>

[![Documentation status](https://img.shields.io/badge/docs-latest-blue)](https://cryptnox.github.io)
[![License: GPLv3](https://img.shields.io/badge/License-LGPLv3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

This repository serves as the root of the Cryptnox documentation portal, available at [docs.cryptnox.com](https://docs.cryptnox.com).

---

## Documentation

| Project | Description |
|--------|-------------|
| [**cryptnox-hardware-wallet**](https://docs.cryptnox.com/cryptnox-hardware-wallet/) | Technical reference for Cryptnox Hardware Wallet smart cards |
| [**cryptnox-cli**](https://docs.cryptnox.com/cryptnox-cli/) | Command-line interface for managing smart card wallets |
| [**cryptnox-sdk-py**](https://docs.cryptnox.com/cryptnox-sdk-py/) | Python SDK for managing smart card wallets via secure communication |

---

## How it works

Each documentation site is maintained in its own repository and automatically served as a sub-path via **GitHub Pages**:

```
docs.cryptnox.com/                              → cryptnox/cryptnox.github.io
docs.cryptnox.com/cryptnox-hardware-wallet/     → cryptnox/cryptnox-hardware-wallet
docs.cryptnox.com/cryptnox-cli/                 → cryptnox/cryptnox-cli
docs.cryptnox.com/cryptnox-sdk-py/              → cryptnox/cryptnox-sdk-py
```

---

## Related repositories

- [cryptnox/cryptnox-hardware-wallet](https://github.com/cryptnox/cryptnox-hardware-wallet)
- [cryptnox/cryptnox-cli](https://github.com/cryptnox/cryptnox-cli)
- [cryptnox/cryptnox-sdk-py](https://github.com/cryptnox/cryptnox-sdk-py)

---

## Versioning

Documentation is versioned per card firmware using [sphinx-multiversion](https://holzhaus.github.io/sphinx-multiversion/).
Each firmware version has a corresponding Git branch named `v{major}.{minor}.{patch}`.
The `main` branch always reflects the latest development docs.

### URL structure

```
docs.cryptnox.com/          → redirects to the latest released version
docs.cryptnox.com/v1.6.1/   → docs for firmware 1.6.1
docs.cryptnox.com/main/     → latest/development docs
```

### Adding a new version

```bash
git checkout main
git pull
git checkout -b v1.6.2
# make any firmware-specific changes to the docs
git push origin v1.6.2
```

The CI/CD pipeline automatically builds and deploys the new version alongside all existing versions.

### Updating an existing version

```bash
git checkout v1.6.1
# edit docs
git push origin v1.6.1
```

### Version selector

Users see a version dropdown at the bottom of the RTD theme sidebar to switch between available versions.

---

## Get your hardware

Cryptnox smart cards and compatible readers are available at [shop.cryptnox.com](https://shop.cryptnox.com).
