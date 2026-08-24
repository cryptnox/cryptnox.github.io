================================
Cryptnox Product Documentation
================================


Cryptnox Hardware Wallet
=========================

.. raw:: html

   <div class="card-icon">
     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
       <rect x="1" y="4" width="22" height="16" rx="2" ry="2"/>
       <line x1="1" y1="10" x2="23" y2="10"/>
     </svg>
   </div>

*Cryptnox Hardware Wallet* is a JavaCard Open Platform 3 smartcard with an EAL6+ Common Criteria
certified secure element. It provides hardware-secured private key storage and transaction signing
for cryptocurrency applications over NFC and contact (T=1) interfaces. The technical reference
covers lifecycle management, the secure channel, seed management, BIP32 key derivation, EC
signatures on secp256k1 and NIST P-256, and MuSig2 (BIP-327) multi-signature commands.

The same card also carries the FIDO Alliance certified FIDO2 and U2F applets (FIDO2 CTAP2.1,
Level 1), so the wallet card doubles as a FIDO2 security key for passkeys and strong
authentication alongside its wallet function.

* **Hardware Wallet Technical Reference v2.0** [`HTML <https://docs.cryptnox.com/cryptnox-hardware-wallet/v2.0/>`__] [`PDF <https://docs.cryptnox.com/cryptnox-hardware-wallet/v2.0/cryptnox-hardware-wallet-v2.0.pdf>`__]
* **Hardware Wallet Technical Reference v1.6** [`HTML <https://docs.cryptnox.com/cryptnox-hardware-wallet/v1.6/>`__] [`PDF <https://docs.cryptnox.com/cryptnox-hardware-wallet/v1.6/cryptnox-hardware-wallet-v1.6.pdf>`__]


-------------------------


Cryptnox CLI
=============

.. raw:: html

   <div class="card-icon">
     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
       <polyline points="4 17 10 11 4 5"/>
       <line x1="12" y1="19" x2="20" y2="19"/>
     </svg>
   </div>

*Cryptnox CLI* brings full smartcard control to the terminal, handling card initialization, secure
channel setup, PIN management, seed generation, key derivation, and transaction signing through a
single command interface.

* **Cryptnox CLI User Guide** [`HTML <https://docs.cryptnox.com/cryptnox-cli/>`__] [`PDF <https://docs.cryptnox.com/cryptnox-cli/cryptnox-cli.pdf>`__]


-------------------------


Cryptnox SDK for Python
=========================

.. raw:: html

   <div class="card-icon">
     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
       <polyline points="16 18 22 12 16 6"/>
       <polyline points="8 6 2 12 8 18"/>
     </svg>
   </div>

*Cryptnox SDK for Python* brings Cryptnox smartcard support to the Python ecosystem, surfacing
secure channel, APDU exchange, key derivation, and signing through a clean Python API. It integrates
directly into desktop wallets, backend services, and automation workflows, adding hardware-secured
keys to any Python application.

* **Cryptnox SDK for Python** [`HTML <https://docs.cryptnox.com/cryptnox-sdk-py/>`__] [`PDF <https://docs.cryptnox.com/cryptnox-sdk-py/cryptnox-sdk-py.pdf>`__]


-------------------------


Cryptnox SDK for ESP32
=========================

.. raw:: html

   <div class="card-icon">
     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
       <polyline points="16 18 22 12 16 6"/>
       <polyline points="8 6 2 12 8 18"/>
     </svg>
   </div>

*Cryptnox SDK for ESP32* brings Cryptnox smartcard support to the ESP-IDF ecosystem, wrapping secure
channel, APDU exchange, key derivation, and signing into a ready-to-use component for the ESP32's
Wi-Fi/Bluetooth SoCs. Connected firmware gains hardware-secured key storage without ever handling the
card protocol directly.

* **Cryptnox SDK for ESP32** [`HTML <https://docs.cryptnox.com/cryptnox-sdk-esp32/>`__] [`PDF <https://docs.cryptnox.com/cryptnox-sdk-esp32/cryptnox-sdk-esp32.pdf>`__]


-------------------------


Cryptnox SDK for Arduino
=========================

.. raw:: html

   <div class="card-icon">
     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
       <polyline points="16 18 22 12 16 6"/>
       <polyline points="8 6 2 12 8 18"/>
     </svg>
   </div>

*Cryptnox SDK for Arduino* packages Cryptnox smartcard support as an Arduino library, exposing secure
channel, APDU exchange, key derivation, and signing through a sketch-friendly API. Installable
directly through the Arduino IDE and Library Manager, it adds hardware-secured keys to any board in
just a few lines of code.

* **Cryptnox SDK for Arduino** [`HTML <https://docs.cryptnox.com/cryptnox-sdk-arduino/>`__] [`PDF <https://docs.cryptnox.com/cryptnox-sdk-arduino/cryptnox-sdk-arduino.pdf>`__]


-------------------------


Cryptnox SDK for C++
=========================

.. raw:: html

   <div class="card-icon">
     <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
       <polyline points="16 18 22 12 16 6"/>
       <polyline points="8 6 2 12 8 18"/>
     </svg>
   </div>

*Cryptnox SDK for C++* is the portable core at the heart of Cryptnox's embedded SDKs, implementing
secure channel, APDU exchange, key derivation, and signing in platform-neutral C++. It ships no
transport driver, crypto backend, or logging output, so porting Cryptnox support to a new native
platform means supplying those platform-specific pieces and building on top of the core.

* **Cryptnox SDK for C++** [`HTML <https://docs.cryptnox.com/cryptnox-sdk-cpp/>`__] [`PDF <https://docs.cryptnox.com/cryptnox-sdk-cpp/cryptnox-sdk-cpp.pdf>`__]


-------------------------


Smart Card Readers
==================

*Cryptnox USB smart card readers* connect contact (ISO 7816) and contactless (ISO 14443)
smart cards to Windows, macOS and Linux over USB-C. Both readers support extended APDU,
which is what national eID schemes and ICAO 9303 travel documents require for certificates
and signatures larger than the 255/256-byte short-APDU limit.

* **Smart Card Reader Compatibility by Country** [`HTML <https://docs.cryptnox.com/reader-compatibility.html>`__] — national eID and professional card compatibility per country, with the official government middleware required for each


-------------------------


Other resources
===============

* `Cryptnox Website <https://www.cryptnox.com>`_
* `Cryptnox on GitHub <https://github.com/cryptnox>`_
* `Hardware Wallet Card — product page <https://shop.cryptnox.com/product/hardware-wallet-smartcard-dual/>`_
* `FIDO2 & MIFARE DESFire Card — product page <https://shop.cryptnox.com/product/cryptnox-smartcard-fido2/>`_
* `FIDO2 Card Technical Specifications <https://cryptnox.com/cryptnox-fido2-card-technical-specifications/>`_
* `Contact Cryptnox <https://cryptnox.com/contact/>`_

|

-------------------------

..
