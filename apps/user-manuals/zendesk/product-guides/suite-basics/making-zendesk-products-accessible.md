# Making Zendesk products accessible

Source: https://support.zendesk.com/hc/en-us/articles/4408838287514-Making-Zendesk-products-accessible

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

At Zendesk, it’s important to make our products accessible and easy for everyone to use, including people who rely on assistive technology.

As our products continue to evolve, accessibility is a priority. Our goal is not only to meet the industry standard ([WCAG 2.1 AA](https://www.w3.org/TR/WCAG21/)), but also to go beyond it wherever possible.

This article describes some of the most notable accessibility features in Zendesk products. For additional information, including our compliance audits, refer to [Zendesk Product Accessibility](https://www.zendesk.com/company/agreements-and-terms/accessibility/).

This article includes the following sections:

- [Accessibility features in Zendesk products](#topic_pky_zs2_dfb)
- [Accessibility Recommendations for users](#topic_azb_z52_dfb)

## Accessibility features in Zendesk products

Zendesk products include these accessibility features:

| Feature | Description |
| --- | --- |
| Navigation, page titles, and headings | Zendesk products use consistent navigation methods. Page titles, headings, and labels describe the topic or purpose. Content is presented in the correct reading sequence. |
| Style sheet flexibility | To help improve visibility, many users prefer to configure their own style sheets. Zendesk does not specifically block user style sheets or use inline style sheets (with the exception of some reporting features). |
| Keyboard shortcuts | As an alternative to point and click, Zendesk supports a number of keyboard shortcuts to enable the primary functionality of the application. The Zendesk team is working to improve ticket fields within the Support interface and standardize keyboard interactions. Some drop-down components in Support allowed for the selection of menu items through the use of the Tab key, but others didn't. To fix this inconsistency, the Product team follows [WAI-ARIA](https://www.w3.org/TR/wai-aria-practices/#menu) guidance in reserving the Tab key for navigation and the Enter and Space keys for selection. Autocomplete drop-down components only allow for selection through the Enter key. |
| Image tagging, text alternatives | Many images are textually tagged or otherwise available to assistive technology. |
| Image consistency | Zendesk is actively working on bringing consistency to all icons to make sure the meaning assigned to those images is consistent throughout our products. |
| Image maps | Zendesk does not use server-side or client-side image maps that can obscure or hide application controls from screen readers. |
| Background images | Zendesk uses background images presented via cascading style sheets (CSS). In many cases, these background images are used for cosmetic purposes and do not restrict control. |
| Links | Zendesk products contain links which indicate their purpose, in context. |
| Communications channels | Zendesk supports multiple communications channels, including email, talk, and chat, that give users communication options. |
| Speech and hearing alternatives | Zendesk products do not contain any features that require user speech or hearing, unless the voice channel is activated. |
| Animations | Some animations are included, but they are not used in conjunction with basic product functionality. |
| Color recognition | To help users with color recognition issues, color coding is not the only means of conveying information to indicate an action, prompt a response, or distinguish a visual element. Other design elements are included. All information conveyed with color is also available without color, for example from context or markup. |
| Display attributes | Zendesk products do not override user-selected contrast and color selections and other individual display attributes. |
| Flashing and blinking | No features of Zendesk use flashing or blinking greater than 2 Hz or lower than 55Hz. |
| Tables | To aid screen reader technology, row and column headings are identified in tables. |
| Application plug-ins | No additional plug-ins are necessary to view or interact with content on Zendesk products. |
| Forms | Zendesk pays careful attention to standards when marking up forms. In a few cases, labels may not have relevant “for” properties to associate them with their relevant input. |
| Time limits | Users can take as long as they need to complete tasks. There are no time-limited features or items of functionality in Zendesk products. |
| Product support documentation | End users with disabilities can request product support documentation in alternate formats. Admins can modify the look of the [Zendesk Help Center.](https://support.zendesk.com/hc/en-us/articles/4408842914714-Help-Center-CSS-cookbook-Guide-Professional-and-Enterprise-) |

## Accessibility Recommendations for users

For best results, Zendesk recommends that users do the following:

- Become familiar with Zendesk keyboard shortcuts. For more information, see [Viewing and disabling keyboard shortcuts](https://support.zendesk.com/hc/en-us/articles/4408832849946-Viewing-and-disabling-keyboard-shortcuts).
- Take advantage of [personal style sheets](http://www.lostsaloon.com/technology/using-a-custom-stylesheet-in-a-web-browser/) or adjust browser settings to meet your accessibility needs.
- Get familiar with features that allow you to customize the Support ticket interface, including [using dark mode](https://support.zendesk.com/hc/en-us/articles/9011095783322), [changing text color](https://support.zendesk.com/hc/en-us/articles/4408831849882#topic_vpl_wfh_1qb), and [creating customized layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138).
- If you have a help center, familiarize yourself with guidelines for making your help center and its content more accessible. See [Making your help center accessible](https://support.zendesk.com/hc/en-us/articles/5318477060250) and [Creating accessible help center content](https://support.zendesk.com/hc/en-us/articles/5275654678554)
- To report accessibility issues that you find with our products, email us at [product-accessibility@zendesk.com](mailto:product-accessibility@zendesk.com). Your feedback is important to us.