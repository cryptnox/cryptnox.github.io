:description: What a Cryptnox Blockchain Public Key / Address Control Attestation Certificate contains, what each field means, how a relying party verifies it, and what it deliberately does not certify.
:orphan:

============================================================
Blockchain Address Control Attestation
============================================================

*Last reviewed: 2 September 2026.*

This page is the technical reference for the certificate produced by Cryptnox Wallet
identity verification: what is in it, what each field means, how to verify one, and where
its scope ends.

A worked example is available as a
`sample attestation certificate (PDF)
<https://cryptnox.com/wp-content/uploads/2026/09/cryptnox-blockchain-address-control-attestation-certificate-sample.pdf>`__.
It uses a fictional specimen passport and a stand-in portrait.

What it attests
===============

A **Blockchain Public Key / Address Control Attestation Certificate** is a three-page PDF
issued and electronically sealed by Cryptnox SA. It records two facts, and only two:

1. A natural person completed Cryptnox SA's identity-verification process — a
   government-issued identity document check and a selfie/liveness check.
2. At the timestamp recorded, that person **demonstrated cryptographic control** of one
   named blockchain public key or address, by signing a Cryptnox challenge with the
   corresponding private key.

.. important::

   The attestation evidences **control**, not ownership. It is not evidence of legal
   ownership of the key, the address or any related asset, and not evidence of continuing
   control after the recorded moment. See `What it does not certify`_.

How the attestation is produced
===============================

The signature is created by a key held on a Cryptnox card. The private key is used inside
the card's EAL6+ certified secure element and is never exposed to the phone in readable
form.

1. **Document capture** — a passport or a supported national identity card is photographed
   and its data extracted.
2. **ePassport chip read (optional)** — the ISO/IEC 14443 chip is read over NFC and its
   document-authenticity and data-authenticity checks are evaluated. Not every document
   carries a readable chip, and the step can be skipped; skipping it produces a weaker
   attestation, because the data then comes from the printed page rather than from the
   chip.
3. **Selfie and active liveness check** — matched against the portrait from the document.
4. **Key selection** — the holder chooses which key on the card will sign. Bitcoin SegWit,
   Ethereum, TRON and XRP keys are supported. Selecting a key moves nothing: no
   transaction is created or broadcast.
5. **On-card signature** — the card signs a Cryptnox challenge bound to the
   identity-verification result and to the certificate metadata.
6. **Issue and seal** — Cryptnox SA issues the PDF and applies its electronic seal.

Certificate fields
==================

Page 1 carries the attestation. Pages 2 and 3 carry the Terms, Scope and Reliance Notice
and the electronic seal.

Identity
--------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Meaning
   * - ``Issue Date``
     - The date the certificate was issued and sealed. Everything attested is tied to this
       moment, not to any period after it.
   * - ``Name``, ``Date of Birth``
     - Read from the identity document, not entered by the holder.
   * - ``Passport Number``
     - The number of the document presented. If a supported national identity card was
       used instead of a passport, this is that card's number.
   * - ``Issuing Country``
     - The three-letter ICAO 9303 code of the issuing state — for example ``CHE`` for
       Switzerland. The sample certificate shows ``UTO``, the code of the fictional
       "Utopia" specimen document.
   * - ``Selfie Verification``
     - Result of matching the live selfie and liveness check against the portrait held in
       the document.
   * - ``ICAO NFC Chip``
     - Whether the document's contactless chip was read over NFC and verified. ``YES``
       means the identity data came from the chip itself, which is what allows the
       certificate to state that the data was retrieved from a government-issued
       *electronic* identity document.

Attested key or address
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Meaning
   * - ``Public Key / Address (Hex / Bech32 / Base58)``
     - The single public key or address the attestation covers, printed in full so that a
       relying party can compare it character by character with the one it asked about.
       The encoding follows the chain of the selected key — hexadecimal, Bech32 or
       Base58. **The attestation is limited to this one key or address** and says nothing
       about any other address the holder may control.

Signing card and key provenance
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Meaning
   * - ``Cryptnox Card Serial``
     - Serial number of the individual card that produced the signature. It binds the
       attestation to one physical card.
   * - ``Card Authenticity Check``
     - Result of the check that the card is a genuine Cryptnox card rather than a clone or
       a software emulator. Corresponds to the card ``Origin`` state exposed by the
       Cryptnox SDKs (``ORIGINAL`` / ``FAKE`` / ``UNKNOWN``).
   * - ``Key Origin``
     - Where the signing key came from. **Internal** means the key was generated by the
       card's own on-chip random number generator inside the secure element, rather than
       created elsewhere and loaded in. The qualifier records how the card was
       initialised — a key generated on a single card, a key generated through the paired
       dual-card ceremony, and a key imported from an external recovery phrase are
       recorded differently, so a relying party can tell them apart. Corresponds to the
       ``SeedSource`` state exposed by the Cryptnox SDKs.
   * - ``Private Key Exposure``
     - Confirms the private key was never available outside the secure element in readable
       form. The signature is produced on the card; the key does not leave it.

Issuer and seal
---------------

The issuer is **Cryptnox SA, Avenue Cardinal-Mermillod 36, 1227 Carouge GE, Switzerland**.

The document carries a Cryptnox SA electronic seal, with a certificate issued by SSL.com,
so a recipient can confirm in a standard PDF reader that the document originated from
Cryptnox SA and has not been altered since sealing.

.. note::

   The seal evidences the authenticity, integrity and origin of the document. It is **not**
   a qualified electronic signature, a qualified or regulated electronic seal, or a
   qualified electronic attestation of attributes, and it is **not** an electronic
   signature by the person identified in the document.

Verifying an attestation
========================

A relying party can check the following without contacting Cryptnox:

1. **Seal** — open the PDF in a reader that validates document signatures and confirm the
   seal resolves to Cryptnox SA and reports the document as unmodified.
2. **Key or address** — compare the printed public key or address, character by character,
   with the one you asked the holder about. They must match exactly.
3. **Identity fields** — check the name, date of birth and document number against the
   identity you are onboarding.
4. **Chip field** — if your process requires data taken from the document chip rather than
   its printed page, require ``ICAO NFC Chip: YES``.
5. **Timestamp** — read the issue date as the moment of the verification event, and decide
   whether an attestation of that age is acceptable for your purpose.
6. **Provenance fields** — if your process cares whether the key was generated on the card
   or imported from an external recovery phrase, read ``Key Origin``.

Regulatory context
==================

The European Banking Authority's Travel Rule Guidelines **EBA/GL/2024/11**, paragraph 83,
list five methods by which a crypto-asset service provider may verify that a self-hosted
address belongs to its customer. Two of them are relevant here:

* **Method (c)** — a transfer of a predefined small amount to and from the address (the
  "Satoshi test").
* **Method (d)** — having the customer **digitally sign a specific message** with the key
  corresponding to the address. This is what a Cryptnox attestation does.

Under Regulation (EU) 2023/1113, Article 14(5), such verification applies to transfers to
or from self-hosted addresses above EUR 1 000, from 30 December 2024.

Compared with a Satoshi test, a signed message moves no funds, pays no network fee, and
does not depend on the customer having a spendable balance. What a Cryptnox attestation
adds beyond a bare signed message is that the signature is bound, in one sealed document,
to a government-issued identity document check and a liveness check.

.. note::

   Whether a particular attestation satisfies a particular institution's process is that
   institution's decision. Cryptnox SA does not represent that use of this certificate
   makes any crypto-asset service provider compliant with any regulation.

What it does not certify
========================

The certificate states this explicitly, and the limits are part of the artifact. The
attestation does not certify, represent, warrant or imply that:

* the identified person **legally owns** the private key, public key, address or any
  related asset;
* the identified person **continues to control** the key or address after the recorded
  verification time;
* any associated asset is lawful, unencumbered, transferable, recoverable or available;
* the address has any particular balance, transaction history, source of funds, AML,
  sanctions, tax or risk status;
* the identified person has consented to, approved or entered into any contract,
  transaction or other legal act, beyond the technical signing of the Cryptnox challenge;
* Cryptnox SA has provided banking, custody, brokerage, exchange, payment, AML,
  sanctions-screening, travel-rule, tax, legal, accounting or financial-advisory services.

Control of a key can change or cease immediately after verification — through loss,
compromise, transfer, delegation, smart-contract logic or key rotation. The certificate is
evidence of the verification event recorded in it, and must not be treated as evidence of
continuing control.

Data handling
=============

Cryptnox SA does not retain copies of government identity documents, selfie or liveness
images, biometric templates, or raw verification material after the attestation process
completes, apart from transient processing and short-lived security, audit, error,
anti-abuse and email-delivery logs necessary to operate and secure the service.

The sealed certificate itself contains personal data, including the identity and the
blockchain public key or address. Once issued, storing, forwarding or publishing it is the
recipient's decision.

Related
=======

* `Generate a proof of address control <https://cryptnox.com/verify-your-identity-in-the-cryptnox-wallet/>`__
  — the step-by-step guide to the Cryptnox Wallet flow.
* `How blockchain-signed identity verification works <https://cryptnox.com/blockchain-signed-identity-verification/>`__
  — identity proof versus cryptographic proof of key control.
* **Hardware Wallet Technical Reference v2.0**
  [`HTML <https://docs.cryptnox.com/cryptnox-hardware-wallet/v2.0/>`__] — seed management,
  key derivation and EC signature commands underlying the signing operation.
