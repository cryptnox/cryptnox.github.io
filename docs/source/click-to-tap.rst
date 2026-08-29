:description: What the Cryptnox Click-to-Tap button does, why FIDO2 sign-in on a desktop contact reader needs it, what it requires, and how to troubleshoot it.
:orphan:

.. meta::
   :description: What the Cryptnox Click-to-Tap button does, why FIDO2 sign-in on a desktop contact reader needs it, what it requires, and how to troubleshoot it.

============================================================
Click-to-Tap: FIDO2 User Presence on a Desktop Reader
============================================================

*Last reviewed: 29 August 2026.*

This page explains one button: what it is for, what it requires, and what it does not do.

The problem it solves
=====================

FIDO2 and WebAuthn require a **user-presence check** on every authentication. The
authenticator must prove that a human, and not software running unattended in the
background, approved the sign-in. It is a deliberate part of the standard, not an
implementation detail.

A USB security key satisfies that check with a metal touch button. A smart card does not
have one. When the card sits in an ordinary contact reader, the only gesture left that the
host recognises as "a person did something" is **removing the card from the slot and
inserting it again** — once per sign-in.

That is slow, it wears the card contacts and the reader connector, and the card is out of
the reader at exactly the moment the user is trying to work.

How Click-to-Tap works
======================

Pressing the button drives the smart-card interface through a controlled
**extraction-and-reinsertion sequence at the protocol level**. There is no mechanical
movement: the card is never physically ejected. The host sees the card leave and return,
which is the event it was waiting for, and the card stays seated in the slot.

The effect is the contactless "tap" gesture, delivered on a contact-mode card.

Requirements
============

.. list-table::
   :header-rows: 1
   :widths: 26 74

   * - Requirement
     - Detail
   * - Card
     - **Cryptnox FIDO2 smart cards only.** The button drives a Cryptnox-specific
       signalling sequence; it is not a generic CCID feature.
   * - Operating system
     - **Windows.** The button has no effect on macOS or Linux.
   * - Reader
     - The Cryptnox Click-to-Tap USB-C contact reader. The contactless reader has no
       button and does not apply.
   * - Software
     - None for the button itself. The reader is a standard USB CCID / PC-SC device and
       uses the smart-card stack already present in Windows.

With any other card, or on any other operating system, the device remains a fully
functional standard CCID / PC-SC contact reader — you simply do not get the tap
simulation.

Using it
========

1. Plug the reader into a USB port. The indicator confirms it has power.
2. Insert the Cryptnox FIDO2 card into the full-size slot, chip contacts down.
3. Sign in to a FIDO2 / WebAuthn service as usual and choose the security key.
4. When the prompt asks you to **tap your security key**, press the button on the reader.
5. The sign-in completes. Leave the card in the slot for the next one.

Troubleshooting
===============

**The button does nothing.**
Check the three requirements above in order: it must be a Cryptnox FIDO2 card, on Windows,
in the Click-to-Tap reader. Any one of the three missing produces exactly this symptom,
with no error message.

**The service never asks me to tap.**
Then there is nothing for the button to answer. Some services complete without a
user-presence prompt, and some browsers prompt only on first registration. The button is
only meaningful while a prompt is waiting.

**The card is not detected at all.**
That is a reader or middleware question, not a Click-to-Tap question. Confirm the card is
seated with the contacts facing down and fully inserted. On Linux, install ``pcscd``,
``libccid`` and ``pcsc-tools``, then check that ``pcsc_scan`` sees the reader.

**FIDO2 sign-in does not work on Linux.**
Browsers on Linux expect an HID FIDO interface, which a CCID reader does not present by
itself. Install the open-source `Cryptnox FIDO2 HID bridge
<https://github.com/cryptnox/cryptnox-fido2-bridge>`__. Note that this enables FIDO2
sign-in on Linux — it does not enable the Click-to-Tap button, which remains Windows-only.

**I want to use the button with my eID, PIV or CAC card.**
Not possible, and not a defect. Click-to-Tap answers a FIDO2 prompt. Government cards
authenticate through their own middleware and are unaffected by it. See
:doc:`reader-compatibility` for what those cards need.

What Click-to-Tap is not
========================

* **Not a replacement for the PIN.** User presence and user verification are different
  checks. The card's PIN policy is unchanged.
* **Not a security boundary.** The button is a convenience for a gesture the standard
  requires; it neither adds nor removes cryptographic protection.
* **Not a secure element.** The reader holds no keys, stores nothing and signs nothing.
  Every cryptographic operation happens on the card.
* **Not applicable to contactless cards**, which already tap physically.

Provenance
==========

The Click-to-Tap virtual-button signalling is Cryptnox-engineered firmware layered on the
standard USB CCID interface; the underlying reader hardware is a commodity component. The
button is protected by registered Austrian utility model **GM 55114/2025**, registered
German utility model **No. 202025108028.1**, and United States patent application
**No. 19/534.472** (pending).
