:description: Cryptnox POS is open-source firmware that turns an ESP32 "Cheap Yellow Display" and a PN532 NFC module into a crypto payment terminal paid by tapping a Cryptnox Hardware Wallet card. Parts, wiring, flashing, first-time setup, the payment flow, supported assets, the secure build and what the dev kit is not.
:orphan:

=================================================================
Cryptnox POS: Open-Source Crypto Payment Terminal (ESP32 Dev Kit)
=================================================================

*Last reviewed: 22 October 2026. Covers* ``cryptnox-pos`` *v1.0.0.*

``cryptnox-pos`` is open-source firmware that turns a low-cost ESP32 touchscreen board, the
ESP32-2432S028 "Cheap Yellow Display" (CYD), plus a PN532 NFC module into a tap-to-pay crypto
payment terminal. The customer taps a **Cryptnox Hardware Wallet** card, the card signs the
transfer inside its secure element, the terminal broadcasts it to the chain and shows
**Approved** only once the transaction is mined.

It is also the reference project for the `Cryptnox SDK for ESP32
<https://docs.cryptnox.com/cryptnox-sdk-esp32/>`__: a complete end-user product built on the SDK,
with the UI, the chain code and the operator setup around it.

* **Source code and releases:** https://github.com/cryptnox/cryptnox-pos
* **API reference (Doxygen):** https://docs.cryptnox.com/cryptnox-pos/
* **Licence:** LGPL-3.0, or a commercial licence for proprietary use

Step-by-step pages with screenshots: `first-time setup <cryptnox-pos-setup.html>`__ ·
`take a USDC payment <cryptnox-pos-payment.html>`__ · `settings and the control panel
<cryptnox-pos-settings.html>`__.

.. figure:: _static/cryptnox-pos/payment-10-approved.png
   :alt: Terminal screen showing Approved, 1.00 USDC, a shortened transaction hash and a New sale button
   :width: 240px

   The end of a sale: *Approved* appears only once the transaction is mined.

What it is, and what it is not
==============================

.. important::

   **Reference and educational dev kit, not a tamper-resistant payment terminal.**
   The ESP32 is not a secure microcontroller and has no protected RAM. The optional
   `secure build`_ protects secrets at rest and locks the boot chain, but at run time the
   card PIN (typed on the screen, never stored) and the Wi-Fi password sit in plaintext RAM.
   What keeps the money safe is the card: **private keys never leave the Cryptnox Hardware
   Wallet**, so a compromised terminal still cannot sign a payment the cardholder did not
   tap for.

It is **not** the C-WaaS terminal. Cryptnox's `C-WaaS blockchain card scheme
<https://cryptnox.com/card-wallet-as-a-service-cwaas/>`__ runs issuer-managed cards through
terminals with a Secure Access Module and issuer co-signing, for banks and card programmes.
``cryptnox-pos`` is the self-custody counterpart: anyone with a Cryptnox Hardware Wallet card
can pay, there is no issuer in the loop, and the merchant receives the funds directly at an
address they configured. How the C-WaaS terminal differs is described in `How the C-WaaS POS
terminal works <https://cryptnox.com/cwaas-pos-terminal-registration-and-payment-flow/>`__.

What you need
=============

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Part
     - Notes
   * - ESP32-2432S028 "Cheap Yellow Display"
     - ESP32-WROOM-32, 2.8" ILI9341 240×320 display used in portrait, XPT2046 resistive touch,
       4 MB flash. Sold under many names; the `CYD community repository
       <https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display>`__ lists the variants.
   * - PN532 NFC module
     - The common red breakout board, used over **I²C**. Its two mode switches must be set to
       I²C.
   * - Cryptnox Hardware Wallet card
     - Firmware **v1.6.0 or later** (the `Dual Card Set
       <https://shop.cryptnox.com/product/hardware-wallet-smartcard-dual/>`__ ships v1.6.1).
       The card must be initialised with a seed; see `Preparing the card`_.
   * - Four jumper wires and a USB cable
     - Female-to-female Dupont wires between the CYD's CN1 header and the PN532; a data USB
       cable to flash and power the board.
   * - A computer
     - For the prebuilt firmware: any machine with Chrome or Edge, or Python and ``esptool``.
       To build from source: `ESP-IDF v5.5
       <https://docs.espressif.com/projects/esp-idf/en/v5.5/esp32/get-started/index.html>`__.

Wiring
======

The CYD exposes its free GPIOs on the **CN1** header. The firmware talks to the PN532 over I²C
on two of them.

.. list-table::
   :header-rows: 1
   :widths: 25 40 35

   * - PN532 pin
     - CYD pin (CN1)
     - Wire colour in the diagram
   * - GND
     - GND
     - black
   * - VCC
     - 3.3V
     - red
   * - SDA
     - GPIO 27
     - yellow
   * - SCL
     - GPIO 22
     - blue

.. note::

   Set the PN532 mode switches to **I²C = ``1 0``** as printed on the board: switch 1 ON,
   switch 2 OFF (``0 1`` is SPI). The PN532 reads the switches only at its own power-up and
   its reset pin is not wired, so after changing them **unplug and replug the USB cable**; an
   ESP32 reset is not enough. Double-check the wiring before powering the board.

A wiring diagram is in the repository at ``hardware/schematics/cyd_esp32_pn532_i2c_bb.png``.
The display, touch panel and backlight are wired internally on the CYD and need nothing.

Flashing the firmware
=====================

Prebuilt image (no toolchain)
-----------------------------

Each `release <https://github.com/cryptnox/cryptnox-pos/releases>`__ ships two files:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - File
     - Use
   * - ``cryptnox-pos-<version>-full.bin``
     - Fresh install over USB, written at flash offset ``0x0``
   * - ``cryptnox-pos-<version>-app.bin``
     - Update of an already installed terminal, over Wi-Fi (see `Updating over Wi-Fi`_)

Over USB, with ``esptool`` (``pip install esptool``), on the port the board enumerates as
(``COM3``, ``/dev/ttyUSB0``, …):

.. code-block:: text

   python -m esptool --chip esp32 --port COM3 -b 460800 write_flash 0x0 cryptnox-pos-v1.0.0-full.bin

Without installing anything, Espressif's `web flasher <https://espressif.github.io/esptool-js/>`__
in Chrome or Edge does the same with flash address ``0x0``. The board restarts into first-time
setup.

Building from source
--------------------

1. Install `ESP-IDF v5.5
   <https://docs.espressif.com/projects/esp-idf/en/v5.5/esp32/get-started/index.html>`__ and
   open its environment (``export.sh`` on macOS and Linux, the ESP-IDF PowerShell on
   Windows).
2. Clone the repository **with submodules**; the Cryptnox SDK, TFT_eSPI and
   XPT2046_Touchscreen are submodules, and LVGL and arduino-esp32 are fetched from the IDF
   component registry on the first build:

   .. code-block:: text

      git clone --recursive https://github.com/cryptnox/cryptnox-pos.git
      cd cryptnox-pos

3. Copy the configuration template and fill it in (``main/config.h`` is gitignored):

   .. code-block:: text

      cp config.template.h main/config.h

4. Set the target, build, flash and watch the log:

   .. code-block:: text

      idf.py set-target esp32
      idf.py -p PORT build flash monitor

The first build is long: it downloads and compiles LVGL and the Arduino runtime.

.. warning::

   Never use plain ``idf.py flash`` on a board that has already been provisioned with the
   `secure build`_: it would write plaintext that the chip then mis-decrypts. Use the
   repository's ``tools/secure_flash.py`` instead.

What goes in ``config.h`` and what does not
-------------------------------------------

``config.h`` holds what is fixed per build: the JSON-RPC endpoints for each network (PublicNode
by default), chain IDs, the token contract addresses for the production and test deployments,
EIP-1559 gas defaults, optional TLS certificate pins, and **fallback** payout addresses. Every
address must be in EIP-55 mixed-case form; the firmware checks the checksum at boot and refuses
to start on a mismatch. ``tests/units/test_networks.cpp`` checks that each configured address
parses, but only a block explorer can confirm that a contract is the right one before the
terminal takes real money.

Four things are deliberately **not** in the firmware and are set on the device instead:

* **Wi-Fi** network and password, chosen during setup from the terminal's own scan;
* **payout addresses** and token contracts, typed in a browser or read off the operator's
  own Cryptnox card, and accepted on the panel;
* the **card PIN**, entered on the touchscreen for each sale and wiped from RAM after
  signing;
* the **amount**, entered on the keypad per sale.

Preparing the card
==================

The card that pays must hold a seed, with the Ethereum derivation path
``m/44'/60'/0'/0/0`` (and ``m/44'/195'/0'/0/0`` for Tron) available. A new card is initialised
once with the `Cryptnox CLI <https://docs.cryptnox.com/cryptnox-cli/>`__:

.. code-block:: text

   cryptnox initialize
   cryptnox seed generate

The same card can also be set up in the Cryptnox Wallet app on a phone. A card that was never
set up is reported as such by the terminal, rather than as a wrong PIN.

First-time setup: the config portal
===================================

Setup is a short browser flow on the terminal's **own Wi-Fi access point**. Nothing is typed
on the 2.8" panel except the admin code, and nothing that decides where the money goes is
accepted anywhere except on the panel.

.. list-table::
   :header-rows: 1
   :widths: 6 20 14 60

   * - Step
     - What
     - Where
     - Detail
   * - 1
     - Admin code
     - panel
     - A six-digit code, typed on the terminal. It never crosses a network. Wrong attempts
       earn an escalating lockout that survives a power cycle.
   * - 2
     - QR code
     - panel
     - The panel shows a QR code for its own WPA2 access point. Scanning it with a phone
       camera joins the network, and the captive portal opens the setup page by itself.
   * - 3
     - Authorise
     - both
     - The page shows a four-digit browser number and the terminal shows the same one. If they
       match, the operator enters the admin code on the panel. The session then carries a random
       128-bit token. If they do not match, another device is trying to connect.
   * - 4
     - Addresses
     - browser
     - Payout addresses are typed, or **read off a Cryptnox card** with one tap after its PIN:
       whichever card is tapped, its own addresses are used, so it must be the merchant's card.
       Each address is displayed on the panel and must be accepted there. Ethereum and Polygon
       share one address; Tron has its own.
   * - 5
     - Wi-Fi
     - browser
     - The venue network is picked from the terminal's own scan and the password entered.
       WPA2 only.
   * - 6
     - Finish
     - panel
     - The terminal restarts, which is what applies the configuration.

Consequences worth knowing before deploying one:

* **There is no remote administration.** The access point is the radio's only interface while
  the portal is open, so an operator is in front of the terminal or nowhere. The terminal is
  off the venue network, and not taking payments, while the page is open (15-minute window,
  or until **Done**).
* **A terminal whose saved network has gone** opens the portal by itself with only the Wi-Fi
  step, and asks for no admin code, because that step cannot move money.
* **An asset with no payout address of its own is not offered** on the amount screen, and the
  panel says in red when the recipient shown is the firmware's built-in fallback.
* The same page, reached later from the control panel (swipe the grey bar at the bottom of the
  sale screen upwards, enter the admin code; tabs **Screen**, **Wi-Fi**, **Tx**, **About**),
  changes everything else: gas fees, production or test networks, token contracts, the clock's
  time zone, firmware updates. The terminal's own tabs report and do not edit; brightness and
  touch calibration are the exceptions. Details: `settings and the control panel
  <cryptnox-pos-settings.html>`__.

Taking a payment
================

1. **Amount.** The operator picks the network and the coin, types the amount on the keypad (two
   decimals, up to 9999.99) and taps **Charge**.
2. **Review.** The screen shows the amount, the destination address, the maximum network fee and
   the token contract in full; **Confirm** or **Cancel**.
3. **PIN.** The cardholder enters the card PIN on the on-screen keypad. It is verified before
   signing and wiped from RAM afterwards.
4. **Tap.** The cardholder holds the card on the PN532. The terminal opens the secure channel
   (*Processing*), the card signs the transaction hash (*Signing*), the terminal works out the
   signature's recovery bit against the card's own public key, RLP-encodes the EIP-1559
   transaction and broadcasts it (*Authorizing*), then polls for the receipt (*Confirming*).
5. **Approved or Declined.** *Approved* appears only on a mined receipt with status ``0x1``,
   for that transaction hash, to the expected contract, with a transfer to the payee for
   exactly that amount; the screen shows the amount, the coin and a shortened transaction hash.
   **New sale** starts the next one. Screens: `take a USDC payment <cryptnox-pos-payment.html>`__.

How long step 4 takes is the chain's block time plus the RPC provider's latency, not the
terminal's. A terminal with no network time refuses to sign rather than guess: SNTP is
corroborated against the HTTPS ``Date`` header, and a clock skew beyond the limit declines the
sale.

Supported assets and networks
=============================

.. list-table::
   :header-rows: 1
   :widths: 22 30 24 24

   * - Chain
     - Assets
     - Production network
     - Test network
   * - Ethereum
     - ETH, USDC, USDT
     - Ethereum mainnet
     - Sepolia
   * - Polygon
     - POL, USDC, USDT
     - Polygon
     - Amoy
   * - Tron
     - TRX, USDT (USDC on test network only)
     - Tron mainnet
     - Nile

The **Network** setting switches all three chains together between production and test
deployments; a mixed configuration is deliberately impossible. A terminal that has never been
told otherwise is on **production**, and switching restarts it. Token contracts are stored per
network; payout addresses are shared, since a card's address is the same account on either
deployment. USDC on Tron is a test-network-only selection: Circle wound it down in 2024–25.

Updating over Wi-Fi
===================

The terminal never contacts GitHub or any update server. A browser carries the bytes:

1. Download the release's ``-app.bin`` on a phone or laptop **before** joining the terminal's
   access point.
2. On the terminal: Settings → About → **Update** (or Wi-Fi → **Configure**). Scan the QR
   code, enter the admin code on the panel.
3. **Browse** and pick the file. The terminal verifies the image and asks on its own screen;
   nothing reboots until somebody accepts it there. A version older than the running one is
   called out in red.
4. The first boot after an update is on probation: a reset before the panel, the card reader
   and the wallet layer have all come up returns to the previous firmware.

Updates wipe the settings, so the terminal runs first-time setup again. A unit flashed with
the old single-slot partition table cannot update over the air and needs one serial reflash
first. With the secure build, an image that is not signed with the project's key is refused
before it can ever become bootable.

Secure build
============

By default the firmware and its settings storage are **unencrypted and unsigned**, which is
right for a bench. The optional secure build adds:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Feature
     - Effect
   * - Flash Encryption
     - A flash dump is ciphertext without the key.
   * - Encrypted NVS (``nvs_keys`` partition)
     - The Wi-Fi password, payout addresses and gas settings are encrypted at rest.
   * - Secure Boot v2 (RSA-3072)
     - Only firmware signed with your key boots, and only such firmware installs over Wi-Fi.

.. warning::

   These burn **eFuses, which is irreversible**. Validate on a sacrificial board first; a
   misconfigured burn bricks the unit. On the classic ESP32, Secure Boot v2 supports **a single
   key with no revocation or rotation**: a leaked key cannot be revoked, and a lost key means
   no unit in the field can ever be updated again. Keep both keys offline, in several copies,
   and out of every repository.

The repository provides two configuration overlays (``sdkconfig.defaults.flash_encryption`` for
development, which stays reflashable, and ``sdkconfig.defaults.release`` for a locked
production unit), a one-shot provisioning script (``tools/secure_provision.py``) and a routine
reflash script (``tools/secure_flash.py``) that pre-encrypts images on the host. A unit built
with the development overlay still reports *Flash encryption mode is DEVELOPMENT (not secure)*
at boot, and its flash can be read out over the cable: the repository's own security analysis
lists shipping such a unit as the first thing to prevent. The full procedure is in the
repository README.

Security notes
==============

What the design defends, in the repository's own words (``docs/security-analysis.md``):

* **No private key on the terminal, ever.** The card signs; the terminal never holds a key
  and never sees a seed.
* **Every change that can redirect money is confirmed on the panel**, by a person in front
  of the terminal, never in the browser alone.
* **Payout addresses are stored in duplicate** and cross-checked, so one corrupted settings
  entry cannot silently redirect funds.
* **The node is not trusted for what gets signed.** The transaction is built and hashed on
  the device; a receipt counts only when it matches that hash, contract, payee and amount.
* **Firmware updates are signed** and verified against a key compiled into the running
  firmware.

What it does **not** defend:

* The ESP32 has no protected RAM: the card PIN and the Wi-Fi password are readable by anyone
  who can reach live memory.
* The setup page is plain HTTP, on the terminal's own WPA2 access point rather than the venue
  network. The session token and, during setup, the venue Wi-Fi password travel over that
  link.
* Nothing about a completed payment is recorded on the device: no receipt, no log. The chain
  is the record.
* The RPC provider is trusted for chain state. It cannot make the card sign a different
  transfer, but it could report a receipt that never landed; the chain, not the terminal's
  screen, is authoritative for settlement.
* No penetration test, side-channel or fault-injection analysis has been performed. The card
  applet is out of scope of that analysis.

Troubleshooting
===============

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Symptom
     - What to check
   * - ``No ACK from PN532`` at boot, or *Card not found*
     - The PN532 mode switches (``1 0`` for I²C, then unplug and replug USB), SDA on GPIO 27
       and SCL on GPIO 22, and the card centred on the antenna.
   * - Inverted colours or banding on gradients
     - Already handled in the firmware for the common panel. A blank or scrambled screen means
       the other ILI9341 variant: set ``CONFIG_TFT_ILI9341_DRIVER=y`` instead of ``_2`` and
       rebuild.
   * - Touch targets are offset
     - Calibrate: menu → admin code → **Screen** → **Touch**. An unconfirmed calibration
       reverts after 20 seconds, so a bad one cannot lock you out.
   * - Wi-Fi will not connect
     - Only WPA2 is supported. Check the network name and password.
   * - ``Signature check failed``
     - The card's signature did not verify under the public key it exported for the same
       path. Retry with the card held still; if it repeats, the card needs looking at.
   * - *Update* says there is no second firmware slot
     - The unit still has the old single-slot partition table. Reflash once over USB.
   * - Build says the app partition is full
     - The table has two 1.94 MB slots on 4 MB flash. The image assets and the panel fonts
       are the largest items; ``idf.py size-components`` shows where the space goes.

Frequently asked questions
==========================

**Can I use it to take payments in a shop?**
   Technically yes, and that is what it does. It is published as a reference dev kit with its
   limits stated plainly: no tamper resistance, secrets in RAM at run time, no payment record
   on the device. For a merchant programme with issued cards, terminals with a Secure Access
   Module and issuer controls, see `C-WaaS
   <https://cryptnox.com/card-wallet-as-a-service-cwaas/>`__.

**Which card pays?**
   Any Cryptnox Hardware Wallet card with firmware v1.6.0 or later that holds a seed. The
   cardholder's own self-custody card, not a card issued by the merchant.

**Does the terminal hold any keys?**
   No. The card signs inside its EAL6+ certified secure element after PIN verification. The
   terminal builds the transaction, asks the card for a signature and broadcasts the result.

**Does it need an internet connection?**
   Yes, over Wi-Fi (WPA2): to reach the JSON-RPC endpoint, broadcast the transaction and wait
   for the receipt. Without network time it refuses to sign.

**Which chains and assets does it accept?**
   ETH, USDC and USDT on Ethereum; POL, USDC and USDT on Polygon; TRX and USDT on Tron, each
   on the production network or its test network. The asset is picked on the device for each
   sale.

**Is this the same as the C-WaaS terminal?**
   No. The C-WaaS terminal is part of an issuer-run card scheme and uses a Secure Access Module
   and issuer co-signing. ``cryptnox-pos`` has no issuer: the cardholder's own card signs and
   the merchant's configured address receives the funds.

**Can I change the user interface or ship it in my own product?**
   Yes. The firmware is LGPL-3.0; a commercial licence is available for proprietary use
   without LGPL obligations. Ask through the `contact form <https://cryptnox.com/contact/>`__.

Related
=======

* `First-time setup <cryptnox-pos-setup.html>`__, `take a USDC payment
  <cryptnox-pos-payment.html>`__ and `settings and the control panel
  <cryptnox-pos-settings.html>`__: step-by-step pages with screenshots.
* `cryptnox-pos on GitHub <https://github.com/cryptnox/cryptnox-pos>`__: source code,
  releases, wiring diagram, the config-portal, over-the-air update and security-analysis
  documents.
* `cryptnox-pos API reference <https://docs.cryptnox.com/cryptnox-pos/>`__: the generated
  documentation for the firmware.
* **Cryptnox SDK for ESP32** [`HTML <https://docs.cryptnox.com/cryptnox-sdk-esp32/>`__]: the
  secure channel, PN532 transport and signing component the terminal is built on.
* **Cryptnox CLI** [`HTML <https://docs.cryptnox.com/cryptnox-cli/>`__]: initialising a card
  and generating its seed.
* **Hardware Wallet Technical Reference v2.0**
  [`HTML <https://docs.cryptnox.com/cryptnox-hardware-wallet/v2.0/>`__]: key derivation and
  signature commands used by the terminal.
* `Cryptnox Hardware Wallet Dual Card Set
  <https://shop.cryptnox.com/product/hardware-wallet-smartcard-dual/>`__: the card that pays.
