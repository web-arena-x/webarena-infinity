# Understanding Embedded voice

Source: https://support.zendesk.com/hc/en-us/articles/4408830696090-Understanding-Embedded-voice

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Your mobile app or website might be full of useful information to help customers, but sometimes
they just want to talk to a real human being. Embedded voice enables you to add a
*digital line*, then embed a call button in your mobile app or Web Widget
(Classic), so your customers can call you immediately, and enjoy a seamless experience,
without leaving the app or widget. Digital lines can be added to the messaging Web
Widget using the Zendesk API. See [Voice API in messaging quick start](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/web/voice-messaging-qs/).

Adding a call button means customers don’t need to know your phone number but can still
access your contact center.

Embedded voice gives you these benefits:

- You don’t need to publish a phone number for your customers to call.
- You can expand your voice support footprint across countries without the
  need for phone numbers there.
- There is no monthly charge for a digital line. You are only charged when
  you use it. To find out more about the cost of digital lines, see [Zendesk number availability and pricing](https://support.zendesk.com/hc/en-us/articles/4408846483482).
- You control the integration and get to control who can call you. For
  example, you might choose to only add a call button for signed in customers, or your
  VIP customers.

This article contains the following sections:

- [Requirements for adding a call button](#topic_brt_jzw_gnb)
- [Setting up Embedded voice](#topic_qhh_kzw_gnb)
- [Understanding digital line limitations](#topic_myc_lzw_gnb)

## Requirements for adding a call button

You’ll need the following to add a call button to your app or Web Widget
(Classic):

- A digital line.
- A Zendesk phone number that’s enabled for outbound calling must be
  chosen to complete the setup of a digital line. You’ll need this for any
  features that involve making an outbound call to a PSTN like forwarding a call
  to an external number. This number is not published or used by your
  callers.
- If you're adding a call button to an app, the app must be enabled with
  a call button and associated with a digital line using the [Talk SDK](https://developer.zendesk.com/documentation/classic-web-widget-sdks/talk-sdk/ios/introduction/). The device on which the app
  is installed must support the WebRTC communication protocol.
- If you want customers to be able to call from Web Widget (Classic), you'll need
  an active Web Widget (Classic) in your account. For help, see [Web Widget (Classic) resources](https://support.zendesk.com/hc/en-us/articles/4408833907354).

Note: Unlike with phone numbers, you can add digital lines while you are on a Suite trial.

## Setting up Embedded voice

The high-level flow for setting up digital calling looks like this:

|  |  |  |  |  |
| [Step 1:](#topic_gkm_5zw_gnb) Configure a digital line |  | [Step 2:](#topic_gz1_vzw_gnb) Configure one of the following to connect your customers to a digital line:   - Configure your app with the Talk SDK and add a call button - Configure Web Widget (Classic) to display a call button |  | [Step 3:](#topic_dnd_vzw_gnb) Customers can now call you direct from your app or Web Widget (Classic) |

### Step 1: Adding and configuring a digital line

You add a digital line the same way you’d add a phone line, though some of the
settings might differ slightly from the phone number settings.

You’ll find all you need to get started in [Adding a digital line](https://support.zendesk.com/hc/en-us/articles/1260805715389).

### Step 2: Configuring your app or Web Widget (Classic)

After you've added a digital line, you can configure your app or Web Widget
(Classic). Use the information in the following two sections to get started.

#### Configuring your app with a call button

The Talk SDK gives you all the tools you need to integrate a call button into
your app and link it to one of your digital lines. To get started, see [Adding a call button to your mobile
app](https://support.zendesk.com/hc/en-us/articles/4408830559258).

#### Configuring the Web Widget (Classic) with a call button

You can configure a Web Widget (Classic) configuration that adds a call
button to your widget. To get started, see [Configuring voice options in Web
Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824310426).

### Step 3: Understanding the customer and agent calling experience

From the caller's point of view, a call from an app or through Web Widget
(Classic) works the same as any other type of call, except the caller does not
need to dial or know your number. After the caller clicks the Call button, they
are connected. The caller will hear any greetings you have configured and then
be placed in the queue along with calls from all of your other numbers.

From the agent's point of view, in-app calls are also similar to other calls. The
caller number will show on the console as "Caller unknown," but the line will
appear with a unique *nickname* that you gave to the digital line.

## Understanding digital line limitations

The following features are not currently available on a digital line:

- Interactive voice response (IVR)
- Caller recording consent (opt-in/opt-out)
- Priority lines
- Callback

To use these calling features, you’ll need to use a [Zendesk phone number](https://support.zendesk.com/hc/en-us/articles/4408824192026).