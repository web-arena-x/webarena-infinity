# Troubleshooting Sell Voice problems

Source: https://support.zendesk.com/hc/en-us/articles/4408824413722-Troubleshooting-Sell-Voice-problems

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

All calls from Zendesk Sell are VOIP (Voice over IP) calls. Call quality can be dependent on internet connection, your microphone or headset, and general service load. 
  
To ensure the highest level calls, here are some actions you can take:

- Use a wired internet connection whenever possible.
- Use an Ethernet connection instead of WiFi.
- Avoid placing calls when connected to free/public WiFi as the connection can be unreliable.
- Use a headset with a noise-canceling microphone rather than your computer's microphone/speaker.
- Depending on the security requirements of your Sell data, if you're using a VPN, then see if your IT team can do VPN split tunnelling (so that information doesn't have to go through the VPN server). Alternatively, see if your IT team can prioritize VoIP traffic on their VPN server.
- Reduce bandwidth consumption from other applications or people (if possible).

For optimum voice quality, we recommend that you use Google Chrome as your browser on a high-speed, low latency Ethernet or Wireless connection.

This article covers the following topics:

- [Setting up the network for best results](#h_01F6JBM1PFSTRC9MP3TM9F0NQK)
- [Troubleshooting suggestions](#h_01F6JBMCHV1RSST2N0B2FB2QZE)
 - [Browser cannot establish a call](#h_01F8T1YQH6CMKEAK095WFQEN91)
 - [One-way audio](#h_01F8T1Z5B734EA03JDP3T3M4RR)
 - [Call audio is garbled](#h_01F8T1ZG2TECVCXNART14QPGJF)
 - [Audio drops out](#h_01F8T1ZT6SFZNEXG89YPBZKK1K)
 - [Calls not saving](#h_01F8T203EHHQMDSDR6SXMXD6VJ)

## Setting up the network for best results

Voice uses Twilio to provide our VOIP services. In order to provide Voice, your browser establishes a connection to Twilio on these addresses and ports:

| | | | | |
| --- | --- | --- | --- | --- |
| **Component** | **Address** | **Client-side port used** | **Server-side port used** | **Protocol** |
| Signaling | chunderw-gll.twilio.com | Any | 443 | TCP |
| Presence | matrix.twilio.com | Any | 443 | TCP |
| RTP | A dynamic IP pulled from Amazon’s public range | Any | 10,000 – 20,000 | UDP |

You can find Amazon's dynamic IP range on their [forums](https://forums.aws.amazon.com/ann.jspa?annID=1701).

For client-side ports, most machines select from the ephemeral range of ports 1,024 to 65,535.

If your router supports Quality of Service (QoS) settings, use these to prioritize port 443, along with the IP addresses of the computers you use to make Voice calls. If your router's QoS settings are fairly simple, use them to prioritize all SIP traffic in order to give Voice priority over most other things on your network.

## Troubleshooting suggestions

If you are still having problems, here are some potential solutions:

### Browser cannot establish a call

- Check that your browser is not restricting access to your microphone or headset. If you are using Chrome, you can check this from **Settings > Advanced > Content Settings > Microphone**. Make sure "app.futuresimple.com:443" is in the "**Allow**" list. If this option is listed as "**Block**", click the X to delete it from the list. Removing this entry will allow you to grant Zendesk Sell a new connection the next time you go to place a call.
- Check that the ports in your router and firewall allow for Voice traffic.
- Ensure you have enough credits on your account to place calls.

### One-way audio

- Confirm that your headset and microphone are correctly connected to your computer.
- Check that the correct output and input for audio are selected in your computer's system settings.
- Ensure that any hardware mute buttons are not enabled.

### Call audio is garbled

- This is usually a network issue, try checking your network connection and carrying out a [Pingtest.](http://www.ping-test.net/)
- Try using a headset with your computer instead of the default built-in microphone.
- Reduce ambient noise nearby.
- Ensure your computer has enough resources available to process a call - make sure that your RAM and CPU are not over utilized. Close any unneeded applications and tabs.

### Audio drops out

- Check your network speed and latency from [Pingtest.](http://www.ping-test.net/) The test will give your network a letter grade. Work with your network provider or IT team in order to bump your network quality to an "A" grade.
- Check that your microphone has been enabled on the browser. You should also check the quality of the headset.

### Calls not saving

- Ensure you know how to log a call.
- Ask your admin if they have enabled recording in your account.
- Ensure you are saving calls correctly (see [How to troubleshoot Sell Voice recordings](https://support.zendesk.com/hc/en-us/articles/4408830815514)).