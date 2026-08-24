:description: Which national eID and smart cards work with Cryptnox USB smart card readers, country by country, with the official government middleware required for each.
:orphan:

.. meta::
   :description: Which national eID and smart cards work with Cryptnox USB smart card readers, country by country, with the official government middleware required for each.

==================================================
Smart Card Reader Compatibility by Country
==================================================

*Last reviewed: 24 August 2026.*

This page answers one question, country by country: **will a Cryptnox USB smart card
reader read my national ID or professional card, and what software do I also need?**

Two rules govern every row on this page.

**1. The reader is necessary but not sufficient.**
Every national card scheme listed here also requires its own government middleware. A
reader that meets the published specification will still do nothing until that software
is installed. Where a scheme provides no freely installable software, this page says so.

**2. Contact and contactless are different cards, not different modes.**
A card with gold pads on the surface is a *contact* card and needs the contact reader. A
card read by holding it near the device is *contactless* and needs the contactless reader.
Some cards have both interfaces; many have only one. Getting this wrong is the single most
common cause of a reader "not working".

.. contents:: Countries on this page
   :local:
   :depth: 1


The two readers
===============

.. list-table::
   :header-rows: 1
   :widths: 22 39 39

   * - 
     - Contact reader
     - Contactless reader
   * - Interface
     - ISO/IEC 7816, Class A/B/C (5 V / 3 V / 1.8 V)
     - ISO/IEC 14443 Type A **and** Type B, 13.56 MHz
   * - Protocols
     - T=0 and T=1
     - 106 / 212 / 424 / 848 kbps
   * - Extended APDU
     - Yes
     - Yes
   * - Stack
     - PC/SC 2.0, USB-IF CCID, Microsoft WHQL
     - PC/SC, USB 2.0 CCID
   * - Card power
     - up to 500 mA
     - not applicable
   * - Operating systems
     - Windows, macOS, Linux — no driver installation
     - Windows, macOS, Linux, Android via USB OTG
   * - Connector
     - USB-C, with a USB-A adapter supplied
     - USB-C, with a USB-A adapter supplied

**Extended APDU support is the specification that decides most of this page.** Certificates
and signatures on modern national cards routinely exceed the 255/256-byte short-APDU limit;
readers without extended APDU fail precisely there, and the failure looks like a broken
card rather than a broken reader. Both Cryptnox readers support it.


How to read the verdicts
========================

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Verdict
     - Meaning
   * - **Works**
     - Confirmed from the scheme's own published reader requirements *and* from users
       reporting generic PC/SC readers in service.
   * - **Likely**
     - The interface and specification match, but community confirmation is thin or the
       scheme itself warns that some readers fail. Test before deploying at scale.
   * - **No**
     - Interface mismatch, a mandatory homologation we do not hold, or the middleware
       does not support this class of reader.


Europe
======

Belgium — Belgian eID
---------------------

**Works with the contact reader.** The Belgian eID is a contact card. Belgian users report
that generic budget readers of any age drive it, and readers well over a decade old remain
in service. The card also carries a contactless interface, but the desktop software path
is the contact one.

*Middleware:* the free, open-source `eID Middleware and eID Viewer <https://eid.belgium.be/en>`_.

Also covers the Kids-ID and the foreigner's card.

Czechia — eObčanka
------------------

**Works with the contact reader.** The Czech Ministry of the Interior publishes a
standards-based specification rather than an approved-model list: ISO 7816, CCID, PC/SC,
with Microsoft WHQL and plug-and-play operation recommended for Windows. The Cryptnox
contact reader meets all of them.

*Middleware:* `eObčanka klient <https://info.identitaobcana.cz/Download/>`_ — the card
manager and identification tools.

Estonia — ID-kaart
------------------

**Works with the contact reader.** Estonia's ID-card runs on the standard USB CCID driver.
The national ID authority notes that any reader capable of retrieving data from the card
can be used, while cautioning that it has only tested certain models itself.

*Middleware:* `DigiDoc4 and the ID-software suite <https://www.id.ee/en/>`_.

Germany — Fahrerkarte and Personalausweis
-----------------------------------------

These are two different cards with two different readers, and confusing them is the most
common German support case.

.. list-table::
   :header-rows: 1
   :widths: 26 12 12 25 25

   * - Card
     - Contact
     - NFC
     - Middleware
     - Verdict
   * - **Fahrerkarte** (digital tachograph driver card)
     - Yes
     - No
     - tachograph/DVR software, varies by vendor
     - **Works** — contact reader
   * - **Personalausweis** (nPA, eID function)
     - No
     - Yes
     - `AusweisApp <https://www.ausweisapp.bund.de/en/download>`_
     - **Works** — contactless reader
   * - elektronische Gesundheitskarte (eGK)
     - Yes
     - partial
     - gematik TI stack
     - **No** — a gematik-approved terminal is mandatory

The Personalausweis eID function requires **extended length** APDU support: its
certificates exceed 400 bytes and many inexpensive NFC readers cap at 261. AusweisApp
states that a reader may work even if it is not on the tested list.

Hungary, Latvia, Romania, Slovakia
----------------------------------

All four issue contact eID cards that work with the contact reader:

* Hungary — eSzemélyi · `eSzemélyi Kliens <https://eszemelyi.hu/letoltesek/>`_
* Latvia — eID · `eParaksts <https://www.eparaksts.lv/en/Downloads>`_
* Romania — CEI · `CEI app <https://hub.mai.gov.ro/aplicatie-cei>`_
* Slovakia — eID karta · `eID klient <https://www.slovensko.sk/sk/na-stiahnutie>`_

Italy — TS-CNS and CIE
----------------------

**TS-CNS works with the contact reader.** The health/services card carries a contact chip
and is driven by a per-card driver plus a smart card manager from the official list.

**CIE 3.0 is contactless only** — it has no contact pads. Italian sources caution that not
every contactless reader drives it reliably, so this is a *Likely*, not a *Works*.

*Middleware:* `CIE Software <https://www.cartaidentita.interno.gov.it/en/useful-info-for-citizens/cie-software/>`_.

Luxembourg — eID
----------------

**Contactless reader only.** The Luxembourg government's own guidance specifies a
contactless reader for the national eID.

*Middleware:* `LuxTrust Middleware <https://www.luxtrust.com/en/middleware>`_.

Netherlands — UZI-pas and ZORG-ID
---------------------------------

**Contact reader, with an important limit.** The Cryptnox contact reader meets the UZI
register's published reader specification — PC/SC, extended APDU support, and more than
60 mA of card power.

.. warning::

   **UZI passes using 4096-bit RSA keys are a separate case.** SafeSign, the UZI
   middleware, keys its maximum APDU size to a list of reader names and applies a
   255/256-byte default to any reader not on that list. A 4096-bit RSA signature is 512
   bytes and cannot be returned under that default. Cryptnox readers are **not currently
   on that list**, so a UZI pass carrying a 4096-bit key will not complete a signature
   until they are added. This is a software list, not a hardware limit — the reader
   itself supports extended APDU. Check the UZI register's approved-reader list and your
   own software's supported-reader list before ordering.

*Middleware:* `SafeSign <https://www.uziregister.nl/uzi-pas/activeer-en-installeer-uw-uzi-pas/overzicht-safesign-software>`_.

The Netherlands has no citizen contact card — DigiD is a phone and app scheme. The Belgian
eID is widely used on Dutch desktops and is covered above.

Poland — e-dowód
----------------

**Contactless reader.** The Polish e-dowód's electronic layer is contactless; there is no
contact chip to read. The reader meets the MSWiA technical requirements: ISO 14443 Type A
and B, extended APDU, PC/SC.

*Middleware:* the free e-dowód software or the eDO App.

Poland's tachograph driver card is a contact card and **works with the contact reader**.

Portugal — Cartão de Cidadão
----------------------------

**Works with the contact reader.** Generic readers drive the card; note that some public
service applications are reported to be fussy — that is the application, not the reader.
The contactless interface is restricted to authorities.

*Middleware:* `Autenticação.gov <https://www.autenticacao.gov.pt/cc-aplicacao>`_.

Spain — DNIe
------------

**Works with the contact reader.**

**Not with a desktop contactless reader.** The DNIe chip is dual-interface, but the desktop
software path is not: OpenSC's DNIe driver recognises the contact ATRs only and does not
work over a contactless reader, and the official NFC route (DNIeRemote / DNIeSmartConnect)
uses a *mobile phone* as the reader rather than a USB one.

*Middleware:* `DNIe software <https://www.dnielectronico.es/PortalDNIe/PRF1_Cons02.action?pag=REF_1100>`_.

Sweden — SITHS
--------------

**Contact reader, employer-supplied software.** On the hardware side the requirement is
simply PC/SC compatibility, which the contact reader meets.

.. note::

   SITHS middleware is **not a free public download**. Net iD requires a commercial
   licence, and Inera replaced it with SITHS eID in 2024. In practice the software reaches
   the user through their employer. Do not plan on installing it independently.

Finland's FINeID is a contact card and works with the contact reader, using
`mPollux DigiSign <https://dvv.fi/en/download-card-reader-software>`_ from DVV — note that
DVV has stated this client is available only until the end of 2026.

United Kingdom and Ireland
--------------------------

Neither country issues a national eID card. The **digital tachograph driver card** is a
contact card and **works with the contact reader**, as does the **NHS Smartcard** in the UK,
which is a contact smart card issued to health service staff and driven through the
employer's identity agent software.

Countries where a desktop reader is the wrong tool
--------------------------------------------------

Published here because knowing what *not* to buy saves more time than another compatible
row:

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Country
     - Why a USB reader is not the route
   * - Austria
     - The Bürgerkarte was decommissioned in December 2023. ID Austria replaced it and
       authenticates by phone or FIDO2 token — no card reader is involved.
   * - Bulgaria, Cyprus, Slovenia
     - The national schemes are mobile-first by design and steer citizens to a phone app.
   * - France
     - Carte Vitale and CPS require homologated terminals, which is a certification we do
       not hold. The tachograph card is unaffected and works.
   * - Greece
     - The Greek ID chip is contactless RFID, not a contact chip.


Outside Europe
==============

United States and Canada — CAC and PIV
--------------------------------------

**Works with the contact reader.** DoD CAC and federal PIV cards are contact cards for
logical access, and the contact reader drives them.

.. warning::

   **A contactless reader cannot be used to log in with a PIV or CAC card.** Under
   NIST SP 800-73, the card's PIN cannot be verified over the plain contactless interface
   — only over the contact interface or a Virtual Contact Interface, and establishing a
   VCI requires secure-messaging key establishment plus a pairing code. Without a PIN
   there is no authentication. The contactless interface exposes the card's physical
   access control credential only. Any product advertising contactless CAC login is
   describing its *contact* slot.

United Arab Emirates — Emirates ID
----------------------------------

**Works with either reader.** The Emirates identity authority's own developer
documentation states that any PC/SC reader, contact or contactless, may be used. Note that
the practical audience is organisational — registration desks, telecoms, banks, healthcare
— because the consumer route is the UAEICP phone app.

*Middleware:* `EIDA SDK Toolkit <https://icp.gov.ae/en/id-card-benefits/sdk-toolkit/>`_.


Travel documents — ICAO 9303
============================

EU Regulation 2019/1157 requires member state ID cards to follow **ICAO Doc 9303**, the
same specification as passports. The contactless reader reads ICAO 9303 electronic
machine-readable travel document chips over ISO 14443 Type A and B, with extended APDU —
which matters, because ePassport data groups routinely exceed the short-APDU limit and
readers without extended APDU fail on them.

What that does **not** mean:

* The chip is password-protected. Access keys are derived from the **MRZ** (document
  number, date of birth, expiry date) or from the **CAN** printed on the document.
* It requires **MRTD reading software**, which Cryptnox does not supply.
* It yields document data and the facial image only. **Fingerprints are protected by
  Extended Access Control and are available to authorities only.**
* It is not the eID authentication or signature function, which is a different applet.


What these readers cannot do
============================

* **125 kHz cards** — EM4100, HID Prox and similar low-frequency badges. The contactless
  reader is 13.56 MHz only.
* **iPhone and iPad** — neither reader works with them.
* **Contact and contactless at the same time** — these are two separate products.
* **PIN entry on the reader** — neither has a keypad, so schemes that mandate on-device
  PIN entry are out of scope.
* **Guarantee the government's software.** We can state that the reader meets a scheme's
  published requirements. We cannot promise how a given public-service application behaves.


Common questions
================

**What kind of card reader do I need for the Belgian eID?**
A contact smart card reader with PC/SC support, plus the free eID Middleware from
eid.belgium.be. Generic readers work; there is no approved-model requirement.

**Which USB card readers work with the Czech eObčanka?**
Any reader meeting the Ministry of the Interior's published specification — ISO 7816,
CCID, PC/SC, ideally WHQL-certified and plug-and-play. There is no approved-model list.

**Why does my reader work in one country but not another?**
Three things have to line up: the card's interface (contact or contactless), the reader's
specification (PC/SC, extended APDU, voltage class), and the national middleware. In
practice the middleware is the most common blocker — it may support only one interface, be
restricted to an approved list of reader names, or not be publicly downloadable at all.

**Do I need extended APDU support?**
For the German Personalausweis, ICAO 9303 travel documents, and any scheme using 3072- or
4096-bit RSA keys, yes. Certificates and signatures at those sizes exceed the 255/256-byte
short-APDU limit, and a reader without extended APDU fails on them.

**Does one reader cover several countries?**
For contact cards, largely yes — Belgium, Czechia, Estonia, Slovakia, Hungary, Latvia,
Romania, Portugal, Spain, Finland and the UK/Irish tachograph card all run on a
standards-compliant PC/SC contact reader. The middleware differs per country; the hardware
does not.


Sources
=======

Every verdict on this page is drawn from the scheme's own published reader requirements
and, where available, from user reports of generic readers in service. Government
middleware pages are linked inline above. Standards referenced: ISO/IEC 7816, ISO/IEC
14443, ICAO Doc 9303, NIST SP 800-73, EU Regulation 2019/1157.


.. raw:: html

   <script type="application/ld+json">
   {
    "@context": "https://schema.org",
    "@graph": [
     {
      "@type": "TechArticle",
      "@id": "https://docs.cryptnox.com/reader-compatibility.html#article",
      "headline": "Smart Card Reader Compatibility by Country",
      "description": "Which national eID and smart cards work with Cryptnox USB smart card readers, country by country, with the official government middleware required for each.",
      "url": "https://docs.cryptnox.com/reader-compatibility.html",
      "inLanguage": "en",
      "dateModified": "2026-08-24",
      "datePublished": "2026-08-24",
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
       "@id": "https://docs.cryptnox.com/reader-compatibility.html"
      },
      "about": [
       {
        "@type": "Thing",
        "name": "Smart card reader"
       },
       {
        "@type": "Thing",
        "name": "National electronic identity card"
       },
       {
        "@type": "Thing",
        "name": "ISO/IEC 7816"
       },
       {
        "@type": "Thing",
        "name": "ISO/IEC 14443"
       },
       {
        "@type": "Thing",
        "name": "PC/SC"
       },
       {
        "@type": "Thing",
        "name": "Extended APDU"
       },
       {
        "@type": "Thing",
        "name": "ICAO 9303"
       },
       {
        "@type": "Thing",
        "name": "Belgian eID"
       },
       {
        "@type": "Thing",
        "name": "Czech eObčanka"
       },
       {
        "@type": "Thing",
        "name": "Estonian ID-kaart"
       },
       {
        "@type": "Thing",
        "name": "German Personalausweis"
       },
       {
        "@type": "Thing",
        "name": "Polish e-dowód"
       },
       {
        "@type": "Thing",
        "name": "Dutch UZI-pas"
       },
       {
        "@type": "Thing",
        "name": "Spanish DNIe"
       },
       {
        "@type": "Thing",
        "name": "NHS Smartcard"
       }
      ]
     },
     {
      "@type": "FAQPage",
      "@id": "https://docs.cryptnox.com/reader-compatibility.html#faq",
      "mainEntity": [
       {
        "@type": "Question",
        "name": "What kind of card reader do I need for the Belgian eID?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "A contact smart card reader with PC/SC support, plus the free eID Middleware from eid.belgium.be. Generic readers work; there is no approved-model requirement."
        }
       },
       {
        "@type": "Question",
        "name": "Which USB card readers work with the Czech eObčanka?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "Any reader meeting the Ministry of the Interior's published specification — ISO 7816, CCID, PC/SC, ideally WHQL-certified and plug-and-play. There is no approved-model list."
        }
       },
       {
        "@type": "Question",
        "name": "Why does my reader work in one country but not another?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "Three things have to line up: the card's interface (contact or contactless), the reader's specification (PC/SC, extended APDU, voltage class), and the national middleware. In practice the middleware is the most common blocker — it may support only one interface, be restricted to an approved list of reader names, or not be publicly downloadable at all."
        }
       },
       {
        "@type": "Question",
        "name": "Do I need extended APDU support?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "For the German Personalausweis, ICAO 9303 travel documents, and any scheme using 3072- or 4096-bit RSA keys, yes. Certificates and signatures at those sizes exceed the 255/256-byte short-APDU limit, and a reader without extended APDU fails on them."
        }
       },
       {
        "@type": "Question",
        "name": "Does one reader cover several countries?",
        "acceptedAnswer": {
         "@type": "Answer",
         "text": "For contact cards, largely yes — Belgium, Czechia, Estonia, Slovakia, Hungary, Latvia, Romania, Portugal, Spain, Finland and the UK/Irish tachograph card all run on a standards-compliant PC/SC contact reader. The middleware differs per country; the hardware does not."
        }
       }
      ]
     }
    ]
   }
   </script>
