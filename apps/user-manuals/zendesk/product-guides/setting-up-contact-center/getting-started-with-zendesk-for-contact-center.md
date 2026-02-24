# Getting started with Zendesk for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9824150119450-Getting-started-with-Zendesk-for-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

This article helps you get up and running with Zendesk for Contact Center. Some of the processes mentioned below might need to be carried out by the Zendesk Professional Services team.

This article contains the following topics:

- [Understanding Contact Center components](#topic_lhf_szt_ygc)
- [Setting up Amazon Connect](#topic_lqz_5zt_ygc)
- [Linking Connect and Contact Center with a CloudFormation stack](#topic_xwl_vzt_ygc)
- [Setting up users and access](#topic_lhm_vzt_ygc)
- [Configuring Contact Center to send call recordings to Zendesk](#topic_jjn_vzt_ygc)
- [Configuring allowed domains in Connect](#topic_tb4_vzt_ygc)
- [Installing and configuring the Zendesk for Contact Center app](#topic_xk4_vzt_ygc)
- [Next steps](#topic_us4_vzt_ygc)

A PDF version of this guide is attached at the end of the article.

## Understanding Contact Center components

Before you start, it’s important to know the key building blocks of Contact Center and how they interact. Contact Center runs on Amazon Connect, a cloud contact center that manages calls, chats, queues, and contact flows. There are several terms you'll need to be familiar with before you get started.

See [Understanding Contact Center components](https://support.zendesk.com/hc/en-us/articles/9829206009242).

## Setting up Amazon Connect

Connect is the cloud service that powers Contact Center. It manages calls, chats, queues, and contact flows. Each Contact Center customer must run a Connect instance in their own AWS account, and a Contact Center account can link to only one Connect instance.

You can automatically set up Connect, or manually set it up yourself.

See [Setting up Amazon Connect for Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121369370).

## Linking Connect and Contact Center

To link Connect and Contact Center, use a CloudFormation stack provided by Zendesk. The stack is a pre-defined set of AWS resources and configurations that sets up everything you need.

See [Linking Connect and Contact Center with a CloudFormation stack](https://support.zendesk.com/hc/en-us/articles/9543543231258).

## Setting up users and access

Users (agents or admins) need to sign into Contact Center, and Connect must allow the connection. Contact Center uses Amazon Cognito for agent authentication, including single sign-on (SSO).

See [Setting up Contact Center users and access](https://support.zendesk.com/hc/en-us/articles/9459000058010).

## Configuring allowed domains in Connect

Because Contact Center is a separate web app that links to Connect through a browser, you must whitelist the Contact Center domain in the Connect instance settings. This ensures that when an agent uses Contact Center, Connect recognizes it and permits the connection.

See [Configuring allowed domains for Contact Center](https://support.zendesk.com/hc/en-us/articles/9829256194330).

## Configuring Contact Center to send call recordings to Zendesk

Contact Center can send call recordings to Zendesk, where they can be accessed in a ticket. This action is known as *writeback*. To allow Contact Center to send call recordings back to Zendesk after a call, turn on the Voice Post Call Lambda in AWS.

See [Configuring Contact Center to send call recordings to Zendesk](https://support.zendesk.com/hc/en-us/articles/9696142065306).

## Installing and configuring the Zendesk for Contact Center app

The Contact Center app from the Zendesk Marketplace is the interface you'll use to control your contact center. Before you can use Contact Center, you must install the app and configure various settings.

See [Installing and configuring the Zendesk for Contact Center app](https://support.zendesk.com/hc/en-us/articles/9459088830874).

## Testing your Contact Center installation

After completing the previous steps, you're ready to test Contact Center to make sure everything is working correctly. If you have any problems, see [Troubleshooting Contact Center](https://support.zendesk.com/hc/en-us/articles/9696137463066).

See [Testing Contact Center](https://support.zendesk.com/hc/en-us/articles/9832930064026).

## Next steps

Now that you've completed the installation, here are some useful resources to help you get started using Contact Center.

- [Accessing workflows in Contact Center](../contact-center-basics/accessing-workflows-in-contact-center.md)
- [Contact Center general integration settings](contact-center-general-integration-settings.md)
- [Mapping and displaying Contact Attributes](https://docs.google.com/document/d/1IdcwY_ArKErKbV8tfANDLdrndmoVIGsd95n6KVyrmxY/edit?usp=sharing)
- [Manually associating Contact Center calls to tickets](../using-contact-center/manually-associating-contact-center-calls-to-tickets.md)
- [Accessing call recording and transcription settings in Contact Center](../using-contact-center/accessing-call-recording-and-transcription-settings-in-contact-center.md)