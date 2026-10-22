:description: First-time setup of a Cryptnox POS terminal, step by step with screenshots: admin code on the terminal, joining its Wi-Fi by QR code, authorising the phone's browser, reading the payout addresses off the merchant's Cryptnox card, accepting them on the terminal, and connecting to the shop Wi-Fi.
:orphan:

=====================================
Cryptnox POS: first-time setup
=====================================

*Last reviewed: 22 October 2026. Screens from firmware v1.0.0. Network names, browser numbers and
addresses differ on every terminal.*

Setup moves back and forth between the **terminal** and your **phone**. Everything that decides
where money goes is accepted on the terminal's own screen; the phone only proposes. Allow about
ten minutes. This page is part of the `Cryptnox POS guide <cryptnox-pos.html>`__.

Before you start
================

You need the terminal, a phone with a camera, the merchant's Cryptnox Hardware Wallet card with its
PIN, and the password of the Wi-Fi network the terminal will use.

.. list-table::
   :widths: 50 50

   * - .. figure:: _static/cryptnox-pos/setup-01-boot.png
          :alt: Terminal boot screen: the Cryptnox logo, cryptnox-pos, a spinner and the words Starting NFC reader
          :width: 240px

          Power the terminal on. It boots and starts its NFC reader.
     - .. figure:: _static/cryptnox-pos/setup-02-welcome.png
          :alt: Welcome screen: Thank you for choosing Cryptnox POS, let's configure your terminal, with a Start button
          :width: 240px

          On the welcome screen, tap **Start**.

Step 1: set the admin code (terminal)
=====================================

The admin code protects every change to the terminal. It is only ever typed on the terminal
itself, never on a phone.

.. list-table::
   :widths: 50 50

   * - .. figure:: _static/cryptnox-pos/setup-03-admin-code.png
          :alt: Set admin code screen with a numeric keypad, an eye icon and a tick
          :width: 240px

          Type a new admin code on the keypad. The eye icon shows or hides the digits. Tap ✓.
     - .. figure:: _static/cryptnox-pos/setup-04-confirm-code.png
          :alt: Confirm code screen with the keypad
          :width: 240px

          Type the same code again to confirm, then tap ✓.

.. important::

   Write the admin code down and keep it safe. You will need it to authorise any phone that
   configures the terminal later.

Step 2: connect your phone
==========================

The terminal opens its own temporary Wi-Fi network, just for setup.

.. list-table::
   :widths: 50 50

   * - .. figure:: _static/cryptnox-pos/setup-05-connect-phone-qr.png
          :alt: Connect your phone screen with a QR code, the network name Cryptnox-ABCD and its password
          :width: 240px

          **Terminal.** Scan the QR code with your phone's camera, or join manually with the
          network name and password shown on the screen. Each terminal has its own.
     - .. figure:: _static/cryptnox-pos/setup-06-phone-authorize.jpg
          :alt: Phone setup page: Authorize this browser, waiting for the admin code on the terminal screen, Browser 4189
          :width: 240px

          **Phone.** Your phone joins the terminal's network and opens the setup page by itself,
          as a "Sign in to network" page. If it does not, open ``192.168.4.1`` in the browser.

Step 3: authorise this browser
==============================

The setup page has to be approved on the terminal, which proves you are standing in front of it.

.. list-table::
   :widths: 50 50

   * - .. figure:: _static/cryptnox-pos/setup-07-browser-number.png
          :alt: Terminal screen showing Browser 4189 and the admin code keypad
          :width: 240px

          **Terminal.** The terminal shows the same browser number as the phone. Check that both
          numbers match, then enter the admin code and tap ✓.
     - If the terminal does not show the request, tap **Ask the terminal again** on the phone.

       If the numbers do not match, do not enter the code: another device is trying to connect.

Step 4: set the payout addresses
================================

Payout addresses are where takings are sent: the merchant's own addresses. The phone only proposes
them; nothing changes until they are accepted on the terminal.

.. list-table::
   :widths: 50 50

   * - .. figure:: _static/cryptnox-pos/setup-08-continue-on-phone.png
          :alt: Terminal screen: Step 4, Payout addresses, continue on your phone
          :width: 240px

          **Terminal.** The terminal tells you to continue on your phone.
     - .. figure:: _static/cryptnox-pos/setup-09-phone-payout-read-card.jpg
          :alt: Phone setup page, Payout addresses section, with a Read from a Cryptnox card button
          :width: 240px

          **Phone.** The easiest way: tap **Read from a Cryptnox card**. Whichever card is tapped,
          its own addresses are used, so use the merchant's card, never a customer's.
   * - .. figure:: _static/cryptnox-pos/setup-10-phone-payout-type.jpg
          :alt: Phone setup page, Or type an address, with Ethereum and Tron fields and Propose buttons
          :width: 240px

          **Phone, alternative.** Or type the addresses yourself: one Ethereum address (also used
          for Polygon) and/or one Tron address, then tap **Propose** for each. Tap **Continue** when
          you are done.
     - .. figure:: _static/cryptnox-pos/setup-11-card-pin.png
          :alt: Terminal screen asking for the Card PIN
          :width: 240px

          **Terminal.** If you chose to read a card, the terminal asks for that card's PIN. Enter it
          and tap ✓.
   * - .. figure:: _static/cryptnox-pos/setup-12-hold-card.png
          :alt: Terminal screen: Hold card to reader, reading your payout addresses
          :width: 240px

          Hold the merchant's Cryptnox Hardware Wallet against the reader until the addresses are
          read.
     - .. figure:: _static/cryptnox-pos/setup-13-accept-eth-address.png
          :alt: Terminal screen: Set payout address? Ethereum / Polygon payout address, with Accept and Reject buttons
          :width: 240px

          The terminal shows the Ethereum / Polygon address. Check it against your own records, then
          tap **Accept**. Tap **Reject** if anything looks wrong.
   * - .. figure:: _static/cryptnox-pos/setup-14-accept-tron-address.png
          :alt: Terminal screen: Set payout address? Tron payout address, with Accept and Reject buttons
          :width: 240px

          Do the same for the Tron address.
     - .. important::

          Always check the full address on the terminal's screen, not only on the phone. The
          terminal's screen is the one you can trust.

Step 5: connect to your Wi-Fi
=============================

The terminal has a single radio: when it joins your network, the setup network disappears. This is
the last step on the phone.

.. list-table::
   :widths: 50 50

   * - .. figure:: _static/cryptnox-pos/setup-15-wifi-handover.png
          :alt: Terminal screen: Wi-Fi network, scan with your phone, connected, the setup page is open in the browser
          :width: 240px

          **Terminal.** The terminal hands over to the phone for the Wi-Fi settings.
     - .. figure:: _static/cryptnox-pos/setup-16-phone-wifi.jpg
          :alt: Phone setup page, Wi-Fi section, with an SSID list, a password field and a Join this network button
          :width: 240px

          **Phone.** Pick your network from the list (tap **Scan again** if it is missing), enter its
          password, then tap **Join this network**.
   * - .. figure:: _static/cryptnox-pos/setup-17-phone-complete.jpg
          :alt: Phone setup page: Configuration complete, please follow the instructions on the terminal's screen
          :width: 240px

          The page shows **Configuration complete**. You can close it. If the terminal cannot join
          your network, it reopens the setup network and this page comes back by itself.
     - **Terminal.** Follow the last instructions on the terminal's screen. Setup is done.

Next
====

* `Take a USDC payment <cryptnox-pos-payment.html>`__: the sale, from choosing the coin to
  *Approved*.
* `Settings and the control panel <cryptnox-pos-settings.html>`__: brightness, Wi-Fi, fees,
  production or test networks, firmware updates.
* `Cryptnox POS guide <cryptnox-pos.html>`__: parts, wiring, flashing and what the dev kit is not.
