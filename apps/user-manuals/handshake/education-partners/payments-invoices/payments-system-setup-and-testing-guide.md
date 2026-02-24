# Payments System Setup and Testing Guide

Source: https://support.joinhandshake.com/hc/en-us/articles/360007568934-Payments-System-Setup-and-Testing-Guide

---

Payments are integrated into Handshake with events, career fairs and on-campus interviews. This checklist and testing guide will take you from choosing a payment vendor, integrating vendor with Handshake, and testing to ensure payments are working correctly!

![](https://support.joinhandshake.com/hc/article_attachments/360009593014/mceclip2.png)**Step 1: Choose payment vendor**

- Stripe (Most common)
- TouchNet: You can have multiple site IDs setup for each of your career centers in Handshake. This can be a great option for distributed campuses.
- CASHNet: You can have multiple item codes set up with CASHNet in Handshake, one for each career center.
- Manual Payments: Any payment outside of these vendors, cash, check, or external payment method like PayPal

**![](https://support.joinhandshake.com/hc/article_attachments/360009593014/mceclip2.png)****Step 2: Integrate vendor with Handshake**

***Important: Make sure to closely follow integration instructions below!***

- Stripe: Click **[here](how-to-setup-a-stripe-account.md)** to set up Stripe and **[here](https://support.joinhandshake.com/hc/en-us/articles/219133537)** for more information
- TouchNet: **[Follow these steps to integrate](https://support.joinhandshake.com/hc/en-us/articles/115009782928)**
- CASHNet: **[Follow these steps to integrate](https://support.joinhandshake.com/hc/en-us/articles/115009783288)**
- Manual Payments: **[Follow these steps to enter manual payments for career fairs](https://support.joinhandshake.com/hc/en-us/articles/218693038)**

**![](https://support.joinhandshake.com/hc/article_attachments/360009593014/mceclip2.png)****Step 3: Test Your Payment Setup**

**Test your payment configuration with a career fair:**

- To test your payment integration you must create a career fair, sign-up as your on-campus employer, and pay for that fair.  You can delete the registration after testing. You will want to make a payment of $2 or more to make sure the payment went through.  Check in your system (Stripe, TouchNet or CASHNet) that the payment went through.

**Reconcile your payments:**

- Download your invoice report from Handshake by navigating to "Analytics" > "Invoices", or use the bulk download by clicking **Payment History** on the career fair's registration page.
- Verify the payments from these reports by matching the Session ID in Handshake to payments in your vendor's system

***Best Practice**: Use Vlookup to assist you in this matching*

**Additional Resources:**

- [**Payments and Invoices Help Center**](https://support.joinhandshake.com/hc/en-us/sections/115002677688-Payments-Invoices)
- [**Handshake Community - Payments**](https://support.joinhandshake.com/hc/en-us/community/topics/115000550467-Career-Fairs-Kiosks-Payments)