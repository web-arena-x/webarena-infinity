# Preparing to offer voice support

Source: https://support.zendesk.com/hc/en-us/articles/4408827987482-Preparing-to-offer-voice-support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Use this article to understand some of the factors you need to consider to ensure that your equipment works correctly for voice support, and provides high quality calls. Each section contains tips that can help you improve both connection and audio quality.

This article covers the following topics:

- [Preparing and optimizing your network](#topic_ihs_f2s_vgb)
- [Choosing the right headset](#topic_gvj_32s_vgb)
- [Configuring your web browser](#topic_gp4_j2s_vgb)

## Preparing and optimizing your network

A good internet connection is crucial. Although a Wi-Fi connection works, a hardwired connection to your network with Wi-Fi disabled on agents computers works best.

For best results, set up a dedicated network for your calls with at least 500kbps network bandwidth. This will remove the impact of other applications and services using a shared network.

Zendesk uses network ports to send and receive information using the UDP and TCP protocols.
Ports are like doors. If the doors are closed, the data cannot pass through, leading to issues with call quality. Allowing these ports to be opened for outbound traffic lets data through. By default, many routers block this traffic in an effort to protect your computer.
Additionally, Mac and Windows operating systems might have system firewalls enabled that block the required ports.

Because you configure these settings for a specific network, when you work from a different network (like your home network), you must open the required ports on that network also.

Finally, if your network bandwidth is limited, consider implementing DSCP tags in your network. These tags let your network know how to prioritize traffic.

For detailed information about opening the required ports and implementimg DSCP, see [Network requirements for voice support](https://support.zendesk.com/hc/en-us/articles/4408831417498).

## Choosing the right headset

Use the following information to help choose the headset that's right for your agents:

- **Analog headset:** These plug into the 3.5mm headphone socket on a computer and generally give the best call quality. We recommend a dedicated headset for agents. A headset from a cell phone, for example, might not give optimum audio and microphone quality.
- **Digital headset:** These usually connect to a computer USB port or digital audio port and also provide a good experience for agents.
- **Wireless headset:** Typically, Bluetooth or mobile phone headsets. These will work but might be susceptible to poor quality audio and connection problems.

If agents are having call quality issues, a good troubleshooting tip is to always try using a different headset first. Additionally, ensure that neither of the call participants have muted their headsets.

## Configuring your web browser

Zendesk uses [WebRTC (Web Real-Time Communication)](https://webrtc.org/), a browser-based communication protocol to make calls.
Ensure that your browser is compatible with WebRTC (for example, Google Chrome, and Firefox). Some older browsers do not support WebRTC.

You should turn off automatic updates for your agents browsers, except for security updates. This enables you to manage changes to your browser and test them out with a small number of agents first.

If a headset is not recognized by your web browser, you might need to edit your browser settings to not use the built-in microphone.

For more information, see [Setting up your browser to take calls](https://support.zendesk.com/hc/en-us/articles/4408823796890).