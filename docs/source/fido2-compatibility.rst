:description: Which services and operating systems work with a Cryptnox FIDO2 NFC card, as second-factor or passwordless sign-in, and where extra software is needed.

:orphan:

=================================================
FIDO2 Card Compatibility — Services and Platforms
=================================================

*Last reviewed: 26 August 2026.*

This page answers: **will a Cryptnox FIDO2 card sign me in to a given service, on the
device I actually use?**

The answer is never a single yes or no, because FIDO2 compatibility has two independent
halves. Read your **platform** row, read your **service** row, and take the intersection.

.. contents:: On this page
   :local:
   :depth: 1


Table A — platform and transport
================================

This decides **which protocol is available at all**. It is a property of the operating
system and the connection, not of the service.

.. list-table::
   :header-rows: 1
   :widths: 16 20 22 42

   * - Platform
     - Transport
     - Protocol available
     - Notes
   * - **Windows 10/11**
     - NFC reader or contact reader
     - full FIDO2 / CTAP2
     - Broadest support. Works across all major browsers.
   * - **iOS**
     - NFC (hold card to top of phone)
     - FIDO2 / CTAP2
     - iPhone 7 and later, iOS 13.3+.
   * - **Android**
     - NFC
     - **CTAP1 / U2F only**
     - Android does **not** support CTAP2 over external NFC security keys. Most services
       keep U2F backward compatibility, so second-factor sign-in works — but see the
       worked example below.
   * - **macOS**
     - NFC reader or contact reader
     - varies
     - Support differs by macOS version and browser. Test before relying on it.
   * - **Linux**
     - contact reader
     - FIDO2 **via a bridge**
     - Browsers expect a HID interface; CCID smart card readers do not present one.
       Requires the open-source `Cryptnox FIDO2 HID bridge
       <https://github.com/cryptnox/cryptnox-fido2-bridge>`_, a small daemon that presents
       the card to the browser as an HID-FIDO device. **This applies to every FIDO2 use on
       Linux** — second factor, passwordless, everything.

Table B — services
==================

This decides **what the service accepts**. Nearly every service that supports security
keys uses them as a **second factor**; passwordless is a smaller, explicitly enabled set.

.. list-table::
   :header-rows: 1
   :widths: 22 16 18 44

   * - Service
     - Second factor
     - Passwordless
     - Setup guide
   * - **Microsoft** (Entra ID / Account)
     - yes
     - **yes** (Entra ID)
     - `guide <https://cryptnox.com/setup-guide-cryptnox-fido2-card-for-microsoft-account/>`__ · `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-microsoft/>`__
   * - **Google**
     - yes
     - **yes** (Advanced Protection)
     - `guide <https://cryptnox.com/configure-fido2-card-to-google-account-complete-guide/>`__ · `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-google/>`__
   * - **AGOV** (Switzerland)
     - yes
     - **yes**
     - `registration guide <https://cryptnox.com/collections/how-to-register-on-agov-using-cryptnox-fido2-card/>`__
   * - **SwissID** (Switzerland)
     - yes
     - —
     - `registration guide <https://cryptnox.com/collections/how-to-register-on-swissid-using-cryptnox-fido2-card/>`__
   * - **login.gov** (United States)
     - yes
     - **no**
     - Always requires a password in addition to MFA — the key is a second factor, never
       the only one. `overview <https://cryptnox.com/best-fido2-security-key-cards-login-gov/>`__
   * - **Apple**
     - yes
     - —
     - `overview <https://cryptnox.com/best-fido2-security-key-cards-for-apple/>`__
   * - **GitLab**
     - yes
     - —
     - `guide <https://cryptnox.com/securely-setup-fido2-card-for-gitlab-account-cryptnox/>`__
   * - **Facebook**
     - yes
     - —
     - `guide <https://cryptnox.com/setup-guide-for-fido2-card-to-facebook-account/>`__
   * - **X / Twitter**
     - yes
     - —
     - `guide <https://cryptnox.com/how-to-set-x-account-passkey-guide/>`__
   * - **Cloudflare**
     - yes
     - —
     - `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-cloudflare/>`__
   * - **Shopify**
     - yes
     - —
     - `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-shopify/>`__
   * - **Binance**
     - yes
     - —
     - `overview <https://cryptnox.com/best-fido2-security-key-cards-binance/>`__
   * - **Coinbase**
     - yes
     - —
     - `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-coinbase/>`__
   * - **Bitfinex**
     - yes
     - —
     - `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-bitfinex/>`__
   * - **Bank of America**
     - yes
     - —
     - `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-bank-of-america/>`__
   * - **Dropbox**
     - yes
     - —
     - `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-dropbox/>`__
   * - **NordVPN**
     - yes
     - —
     - `overview <https://cryptnox.com/best-fido2-security-key-cards-nordvpn/>`__
   * - **Fastmail**
     - yes
     - —
     - `overview <https://cryptnox.com/best-fido2-security-key-cards-fastmail/>`__
   * - **GoDaddy**
     - yes
     - —
     - `overview <https://cryptnox.com/collections/best-fido2-security-key-cards-for-godaddy/>`__
   * - **SSH**
     - yes
     - —
     - `guide <https://cryptnox.com/ssh-with-the-fido2/>`__

A dash under *Passwordless* means the service has not enabled FIDO2-only sign-in, or we
have not confirmed that it has — not that it is impossible. Test before relying on it.


The composition rule
====================

**Your answer is the intersection of your platform row and your service row.** Both must
allow what you are trying to do.

The worked example is **Microsoft on Android**:

* the card is CTAP2-capable ✅
* Microsoft Entra ID is CTAP2-capable ✅
* **the combination still fails** ❌

Android speaks only CTAP1/U2F over an external NFC key, and Microsoft requires CTAP2 with
user verification on every attempt — it does not accept U2F credentials. Use a reader on
Windows, or NFC on iPhone.

That single case teaches the whole model: **capability is not the same as a usable path.**
A component being able to do something says nothing about whether the platform in front of
it will ask.

Two related consequences worth stating plainly:

* **One card can appear twice in an account.** Registering the same card over CTAP1 on
  Android and CTAP2 on desktop creates two separate credentials. That is expected.
* **Cryptnox FIDO2 is listed by Microsoft** for Entra ID attestation (AAGUIDs
  ``9c835346-796b-4c27-8898-d6032f515cc5`` and
  ``1d1b4e33-76a1-47fb-97a0-14b10d0933f1``, both NFC). Attestation eligibility is not the
  same as passwordless support, and individual server implementations of CTAP1 vary.


What these cards cannot do
==========================

* **Passwordless everywhere.** These are **MFA-first**: a hardware second factor on top of
  a password. Passwordless works only where a service has explicitly enabled FIDO2-only
  sign-in. login.gov is the clearest counter-example — it always requires a password.
* **CTAP2 over Android NFC.** Second-factor U2F works on most services; Microsoft does not.
* **Linux without the bridge.** A CCID reader alone will not satisfy a browser.
* **Fingerprint on the card.** FIDO2 user verification on these cards is **PIN-based**.
* **Migrate credentials between cards.** Each card holds its own keys. A replacement card
  must be registered with each service again.
* **Act as a USB device.** These are NFC and contact smart cards, not USB tokens.


Common questions
================

**Does a FIDO2 security key card work with Android over NFC?**
Yes for second-factor sign-in on most services, because Android supports CTAP1/U2F over
external NFC keys and most services keep U2F backward compatibility. It does not work with
Microsoft, which requires CTAP2 with user verification.

**Which services support passwordless sign-in with an external NFC card?**
A small set that has explicitly enabled FIDO2-only login — Microsoft Entra ID, Google
Advanced Protection and AGOV among them. Most services accept the key only as a second
factor on top of a password, and login.gov always requires one.

**Why does my security key appear twice in my account settings?**
Because CTAP1 and CTAP2 registrations create separate credentials. Registering the same
card on an Android phone and on a desktop produces two entries. Both work.

**What decides whether a given service and device combination works?**
Three things: the card's capability, the platform's protocol support, and what the service
accepts. In practice the platform is the usual blocker — most notably Android, which
speaks only CTAP1 over external NFC keys.

**Do I need extra software?**
On Linux, yes — the open-source Cryptnox FIDO2 HID bridge, for every FIDO2 use. On Windows,
macOS and iOS, no. Setting or changing the card PIN uses the Cryptnox app.


Related
=======

* `FIDO2 card technical specifications <https://cryptnox.com/cryptnox-fido2-card-technical-specifications/>`__
* `Using the card with Android <https://cryptnox.com/cryptnox-nfc-fido-card-android/>`__
* `Windows setup guide <https://cryptnox.com/fido2-card-for-windows-setup-guide/>`__
* `Setting the card PIN <https://cryptnox.com/how-to-set-pin-for-the-fido2-card/>`__
* `Managing credentials on the card <https://cryptnox.com/how-to-manage-credential-of-fido2-card-security-key/>`__
* :doc:`Smart card reader compatibility by country <reader-compatibility>`


.. raw:: html

   <script type="application/ld+json">
   {
    "@context": "https://schema.org",
    "@graph": [
     {
      "@type": "TechArticle",
      "@id": "https://docs.cryptnox.com/fido2-compatibility.html#article",
      "headline": "FIDO2 Card Compatibility — Services and Platforms",
      "description": "Which services and operating systems work with a Cryptnox FIDO2 NFC card, as second-factor or passwordless sign-in, and where extra software is needed.",
      "url": "https://docs.cryptnox.com/fido2-compatibility.html",
      "inLanguage": "en",
      "dateModified": "2026-08-26",
      "datePublished": "2026-08-26",
      "author": {
       "@type": "Organization",
       "name": "Cryptnox SA",
       "url": "https://cryptnox.com/"
      },
      "publisher": {
       "@id": "https://cryptnox.com/#organization"
      },
      "mainEntityOfPage": {
       "@type": "WebPage",
       "@id": "https://docs.cryptnox.com/fido2-compatibility.html"
      },
      "about": [
       {
        "@type": "Thing",
        "name": "FIDO2"
       },
       {
        "@type": "Thing",
        "name": "WebAuthn"
       },
       {
        "@type": "Thing",
        "name": "CTAP2"
       },
       {
        "@type": "Thing",
        "name": "CTAP1"
       },
       {
        "@type": "Thing",
        "name": "U2F"
       },
       {
        "@type": "Thing",
        "name": "NFC security key"
       },
       {
        "@type": "Thing",
        "name": "Passwordless authentication"
       },
       {
        "@type": "Thing",
        "name": "Multi-factor authentication"
       },
       {
        "@type": "Thing",
        "name": "Microsoft Entra ID"
       },
       {
        "@type": "Thing",
        "name": "Google Advanced Protection"
       },
       {
        "@type": "Thing",
        "name": "AGOV"
       },
       {
        "@type": "Thing",
        "name": "SwissID"
       },
       {
        "@type": "Thing",
        "name": "login.gov"
       },
       {
        "@type": "Thing",
        "name": "Android NFC"
       },
       {
        "@type": "Thing",
        "name": "Linux FIDO2 bridge"
       }
      ]
     },
     {
      "@type": "FAQPage",
      "@id": "https://docs.cryptnox.com/fido2-compatibility.html#faq",
      "mainEntity": [
       {
        "@type": "Question",
        "name": "Does a FIDO2 security key card work with Android over NFC?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "Yes for second-factor sign-in on most services, because Android supports CTAP1/U2F over external NFC keys and most services keep U2F backward compatibility. It does not work with Microsoft, which requires CTAP2 with user verification."
        }
       },
       {
        "@type": "Question",
        "name": "Which services support passwordless sign-in with an external NFC card?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "A small set that has explicitly enabled FIDO2-only login — Microsoft Entra ID, Google Advanced Protection and AGOV among them. Most services accept the key only as a second factor on top of a password, and login.gov always requires one."
        }
       },
       {
        "@type": "Question",
        "name": "Why does my security key appear twice in my account settings?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "Because CTAP1 and CTAP2 registrations create separate credentials. Registering the same card on an Android phone and on a desktop produces two entries. Both work."
        }
       },
       {
        "@type": "Question",
        "name": "What decides whether a given service and device combination works?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "Three things: the card's capability, the platform's protocol support, and what the service accepts. In practice the platform is the usual blocker — most notably Android, which speaks only CTAP1 over external NFC keys."
        }
       },
       {
        "@type": "Question",
        "name": "Do I need extra software?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "On Linux, yes — the open-source Cryptnox FIDO2 HID bridge, for every FIDO2 use. On Windows, macOS and iOS, no. Setting or changing the card PIN uses the Cryptnox app."
        }
       }
      ]
     }
    ]
   }
   </script>
