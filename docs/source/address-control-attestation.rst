:description: What a Cryptnox Blockchain Public Key / Address Control Attestation Certificate contains, what each field means, what the card actually signs, how the PDF is sealed, how a relying party verifies it, and what it deliberately does not certify.
:orphan:

============================================================
Blockchain Address Control Attestation
============================================================

*Last reviewed: 4 September 2026.*

This page is the technical reference for the certificate produced by Cryptnox Wallet
identity verification: what is in it, what each field means, what the card signs, how to
verify one, and where its scope ends.

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
5. **On-card signature** — the card signs a Cryptnox challenge: a canonical record of the
   verification event carrying the identity fields, hashes of the document photograph and
   the selfie, the selected chain, the public key and a single-use nonce. See
   `What the card signs`_.
6. **Issue and seal** — Cryptnox SA issues the PDF and applies its electronic seal.

Technical details
=================

This section describes the cryptographic objects behind the certificate, so that an
integrator, an auditor or an automated verifier can reason about exactly what was signed,
by which key, and what Cryptnox checked before issuing.

Three separate signatures by three different keys are involved. Telling them apart is the
key to reading the document correctly — only the first is made by the holder.

.. list-table::
   :header-rows: 1
   :widths: 24 24 52

   * - Object
     - Signed by
     - Covers
   * - Verification record (the "Cryptnox challenge")
     - The holder's Cryptnox card
     - Identity fields, image hashes, chain, public key, nonce and timestamp. ECDSA on
       secp256k1 over SHA-256, DER, canonical low-S.
   * - Manufacturer certificate
     - Cryptnox DLT Cards CA, at manufacture
     - The card's static public key and serial number. X.509.
   * - Document Security Object
     - The issuing state's Document Signer — ePassport chip only
     - The hashes of the chip's data groups. CMS SignedData, RSA or ECDSA.
   * - The certificate PDF
     - Cryptnox SA, at issue
     - The complete three-page document. PAdES-B-T, RSA-2048 with SHA-256 and an RFC 3161
       timestamp.

What the card signs
-------------------

The "Cryptnox challenge" is not a bare random nonce. It is a deterministic text record of
the verification event — sixteen newline-separated lines, in a fixed order, carrying:

* the signing timestamp, in UTC to the millisecond;
* the identity fields read from the document — given name, surname, date of birth,
  document number, document type, e-mail, gender, expiry date, nationality and issuing
  country;
* the SHA-512 hashes of the document photograph and of the selfie;
* the selected blockchain;
* the public key being attested;
* a single-use random nonce.

The wallet hashes that record with SHA-256, and the card signs the resulting 32-byte
digest. The record is built identically on iOS, Android and the server, so the server can
rebuild it from the submission and check the signature against it.

The signature is ECDSA on secp256k1, produced inside the card's secure element with a key
derived on-card at the standard derivation path for the selected chain — BIP-84 for Bitcoin
SegWit, BIP-44 for Ethereum, TRON and XRP. It is returned in DER form in canonical low-S
encoding, with a fresh random nonce for every signature. All four supported chains use the
same curve; the chain only selects the derivation path, and the exported public key is what
the certificate prints.

Because the public key and the nonce are inside the signed record, the signature is bound
to this one verification event and cannot be transplanted onto another identity, another
key or another submission. Because the image hashes are inside it, the photographs Cryptnox
face-matches are provably the ones the holder saw when they tapped the card.

Command-level detail for the signing operation is in the
`Hardware Wallet Technical Reference
<https://docs.cryptnox.com/cryptnox-hardware-wallet/v2.0/>`__.

How the card proves it is genuine
---------------------------------

Every Cryptnox card carries an X.509 manufacturer certificate over its static public key
and serial number, issued by the Cryptnox DLT Cards CA and chaining through a Cryptnox
intermediate to a Cryptnox root. The wallet checks the card when it connects, and Cryptnox
re-validates the whole chain server-side before accepting a submission.

The card serial printed on the certificate is read from that manufacturer certificate. It
is not supplied by the wallet.

The key-origin fields are taken from the card's own record of how its seed was created:
generated on a single card, generated through the paired dual-card ceremony, or imported
from an external recovery phrase.

What Cryptnox verifies before issuing
-------------------------------------

Every check is fail-closed and runs before anything is stored. A submission that fails any
applicable check is rejected and no certificate is rendered.

* **The card signature** — the signed record is rebuilt from the submission, hashed, and
  the ECDSA signature is verified against the submitted public key.
* **The card** — the manufacturer certificate is within its validity window and chains to a
  Cryptnox root.
* **Uniqueness** — each signed nonce is accepted once, so a submission cannot be replayed.
* **The person** — the selfie is compared with the photograph of the identity document,
  and with the chip portrait when the chip was read, at a similarity threshold of 80 or
  higher.
* **The chip**, when one was read — ICAO 9303 Passive Authentication: every data group must
  hash to the value recorded in the Document Security Object, and that object's CMS
  signature must verify from the issuing state's Document Signer Certificate up to a
  Country Signing CA in the ICAO and BSI master lists.

Cryptnox does not query any blockchain. No balance, transaction history, sanctions or
ownership lookup is performed, and no chain address is derived server-side: the public key
is verified and printed as submitted.

Trust anchors
-------------

Three independent roots of trust are involved, none of them the holder's.

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Purpose
     - Anchor
   * - The card is genuine
     - Cryptnox Root → Cryptnox Intermediate → Cryptnox DLT Cards CA, published by
       Cryptnox.
   * - The ePassport chip is authentic
     - Country Signing CA certificates from the ICAO 9303 Part 12 CSCA master lists and
       the BSI master list.
   * - The document seal is genuine
     - SSL.com Root Certification Authority RSA, a member of the Adobe Approved Trust
       List; DigiCert Trusted Root G4 for the timestamp. Both are in the reader's own
       trust store.

How the certificate is sealed
-----------------------------

The three-page PDF carries a PAdES signature (``ETSI.CAdES.detached``) computed over the
entire file with SHA-256 and RSA-2048. The signing certificate is issued to Cryptnox SA by
SSL.com, a member of the Adobe Approved Trust List, and the signature carries an RFC 3161
timestamp from DigiCert. The document therefore validates in standard PDF readers with no
Cryptnox-specific software and no call to Cryptnox.

The seal evidences the origin and integrity of the document. It is **not** a qualified
electronic signature or seal, not an electronic attestation of attributes, and not a
signature by the person identified in the document.

Verifying the seal yourself
---------------------------

Open the PDF in Adobe Acrobat or Reader: the Signature Panel must report *"Signed and all
signatures are valid"*, with signer **Cryptnox SA**.

Automated pipelines can validate the embedded CMS against the SSL.com root instead. With
`pyHanko <https://pyhanko.readthedocs.io/>`__:

.. code-block:: bash

   pip install pyHanko
   pyhanko sign validate --pretty-print --trust ssl-com-root-rsa.pem \
       cryptnox-attestation-signed.pdf

Or with OpenSSL, after extracting the CMS blob and the byte range it covers:

.. code-block:: bash

   python3 -c "
   import re, sys
   d = open(sys.argv[1], 'rb').read()
   br = [int(x) for x in re.search(rb'/ByteRange\s*\[([^\]]+)\]', d).group(1).split()]
   open('signed.bin', 'wb').write(d[br[0]:br[0]+br[1]] + d[br[2]:br[2]+br[3]])
   open('sig.der', 'wb').write(
       bytes.fromhex(re.search(rb'/Contents\s*<([0-9A-Fa-f]+)>', d).group(1).decode())
       .rstrip(b'\x00'))
   " cryptnox-attestation-signed.pdf

   openssl cms -verify -inform DER -in sig.der -content signed.bin -binary \
       -CAfile ssl-com-root-rsa.pem -out /dev/null
   openssl pkcs7 -inform DER -in sig.der -print_certs -noout   # expect CN=Cryptnox SA

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
     - The date the certificate was rendered and sealed, to day precision. The card
       signature carries its own UTC timestamp to the millisecond inside the signed
       record; the two normally fall on the same day, but can differ if a submission is
       retried or queued.
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
       the document. The similarity score behind it is retained in the verification
       record but is not printed.
   * - ``ICAO NFC Chip``
     - Whether the document's contactless chip was read over NFC and verified. ``YES``
       means the chip was read and passed both the data-integrity and the
       document-authenticity checks described in
       `What Cryptnox verifies before issuing`_, so the identity data came from the chip
       itself rather than from the printed page. A chip read that fails either check
       causes the whole submission to be rejected, so ``YES`` on an issued certificate
       always implies both passed.

Attested key or address
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Meaning
   * - ``Public Key / Address (Hex / Bech32 / Base58)``
     - The single public key the attestation covers. In certificates issued today this is
       always the **uncompressed secp256k1 public key in hexadecimal** — 130 characters,
       beginning ``04`` — whichever of the four chains was selected; the chain address is
       derived from this key but is not itself printed. The field label names the three
       encodings the certificate format allows. The value is printed in full so that a
       relying party can compare it against the key it asked about, deriving the chain
       address from it where an address is what needs comparing.
       **The attestation is limited to this one key** and says nothing about any other key
       or address the holder may control.

Signing card and key provenance
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Meaning
   * - ``Cryptnox Card Serial``
     - Serial number of the individual card that produced the signature, read server-side
       from the card's manufacturer certificate. It binds the attestation to one physical
       card.
   * - ``Card Authenticity Check``
     - ``OK`` means the card's manufacturer certificate was validated against the Cryptnox
       certificate authorities at the moment the attestation was issued. It is not a
       status reported by the card: a submission whose manufacturer certificate does not
       chain to a Cryptnox root is rejected before any certificate is rendered, so an
       issued certificate always reads ``OK``.
   * - ``Key Origin``
     - Where the signing key came from, as recorded by the card. Three states are printed:
       ``Internal — generated on card (single)``, meaning the key was generated by the
       card's own on-chip random number generator inside the secure element;
       ``Internal — generated on card (dual)``, meaning it was generated through the
       paired dual-card ceremony; and ``External — generated off card (mnemonic)``,
       meaning it was imported from an external recovery phrase. Any other card state
       prints ``-``. Unlike the card signature and the manufacturer chain, this value is
       reported by the card rather than independently re-derived by Cryptnox.
   * - ``Private Key Exposure``
     - Follows from ``Key Origin``. For a key generated on the card it reads
       ``Never in the clear``: the key was created and is used inside the secure element,
       the signature is produced on the card, and the key never leaves it. For a key
       imported from a recovery phrase it reads ``Exposed during import``, because the
       seed existed outside the card before it was loaded.

Issuer and seal
---------------

The issuer is **Cryptnox SA, Avenue Cardinal-Mermillod 36, 1227 Carouge GE, Switzerland**.

The document carries a Cryptnox SA electronic seal, with a certificate issued by SSL.com,
so a recipient can confirm in a standard PDF reader that the document originated from
Cryptnox SA and has not been altered since sealing. See `How the certificate is sealed`_
for the format and `Verifying the seal yourself`_ for how to check it.

.. note::

   The seal evidences the authenticity, integrity and origin of the document. It is **not**
   a qualified electronic signature, a qualified or regulated electronic seal, or a
   qualified electronic attestation of attributes, and it is **not** an electronic
   signature by the person identified in the document.

Verifying an attestation
========================

A relying party can check the following without contacting Cryptnox:

1. **Seal** — open the PDF in a reader that validates document signatures and confirm the
   seal resolves to Cryptnox SA and reports the document as unmodified. For automated
   checks, see `Verifying the seal yourself`_.
2. **Key or address** — compare the printed public key with the key you asked the holder
   about, character by character. Where you hold an address rather than a key, derive the
   address for the relevant chain from the printed key and compare that. They must match
   exactly.
3. **Identity fields** — check the name, date of birth and document number against the
   identity you are onboarding.
4. **Chip field** — if your process requires data taken from the document chip rather than
   its printed page, require ``ICAO NFC Chip: YES``.
5. **Timestamp** — read the issue date as the day of the verification event, and decide
   whether an attestation of that age is acceptable for your purpose.
6. **Provenance fields** — if your process cares whether the key was generated on the card
   or imported from an external recovery phrase, read ``Key Origin`` and
   ``Private Key Exposure``.

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
