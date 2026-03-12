================================
Cryptnox Product Documentation
================================

.. toctree::
   :maxdepth: 3
   :caption: CONTENTS
   :hidden:

   copyright


Cryptnox Hardware Wallet
=========================

.. raw:: html

   <div class="card-icon">
     <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75">
       <rect x="2" y="5" width="20" height="14" rx="2" stroke="currentColor" stroke-width="1.75" fill="none"/>
       <path stroke-linecap="round" stroke-linejoin="round" d="M2 10h20"/>
       <path stroke-linecap="round" stroke-linejoin="round" d="M6 15h4"/>
     </svg>
   </div>

*Cryptnox Hardware Wallet* is a JavaCard Open Platform 3 smartcard with an EAL6+ Common Criteria
certified secure element. It provides hardware-secured private key storage and transaction signing
for cryptocurrency applications over NFC and contact (T=1) interfaces.

All communication is protected by a secure channel based on GlobalPlatform SCP03, ensuring
confidentiality, authentication, and integrity. The card supports SECP256k1 and SECP256r1 curves
with ECDSA and BIP340 Schnorr signing, BIP32/SLIP10 hierarchical key derivation, and multiple
authentication methods including PIN, user key challenge-response, and FIDO.

* **Hardware Wallet Technical Reference** [`View Docs <https://embarquech.github.io/hardware-wallet-doc/introduction.html>`__]


-------------------------


Cryptnox CLI
=============

.. raw:: html

   <div class="card-icon">
     <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75">
       <path stroke-linecap="round" stroke-linejoin="round"
             d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
     </svg>
   </div>

*Cryptnox CLI* is a command-line tool for interacting with Cryptnox smartcards from the terminal.
It handles card initialization, secure channel establishment, PIN management, seed generation,
key derivation, and transaction signing through a straightforward command interface.

* **Cryptnox CLI User Guide** [`View Docs <https://cryptnox.github.io/cryptnox-cli/>`__]


-------------------------


Cryptnox SDK for Python
=========================

.. raw:: html

   <div class="card-icon">
     <svg fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.75">
       <path stroke-linecap="round" stroke-linejoin="round"
             d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/>
     </svg>
   </div>

*Cryptnox SDK for Python* is a library that enables developers to integrate Cryptnox smartcard
functionality into their own applications. It provides programmatic access to secure channel
establishment, APDU communication, key derivation, and signing operations, allowing custom
wallet software and automation workflows to leverage the card's hardware security.

* **Cryptnox SDK for Python** [`View Docs <https://cryptnox.github.io/cryptnox-sdk-py/>`__]


-------------------------


Other resources
===============

* `Cryptnox Website <https://www.cryptnox.com>`_
* `Cryptnox on GitHub <https://github.com/cryptnox>`_
