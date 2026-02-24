# Creating accessible help center content

Source: https://support.zendesk.com/hc/en-us/articles/5275654678554-Creating-accessible-help-center-content

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Creating help center content that is accessible and easy to use by everyone, including those who rely on assistive technology, ensures that anyone accessing Zendesk has a successful and positive experience.

Note: To achieve optimum accessibility for your help center, ensure that not only your content is accessible, but also your help center theme. See [Making your help center accessible](https://support.zendesk.com/hc/en-us/articles/5318477060250).

This article contains the following sections:

- [Content accessibility guidelines](#topic_ox5_nlb_fwb)
- [Content accessibility resources](#topic_gjf_q5b_fwb)

## Content accessibility guidelines

The following table contains guidelines for making your help center articles accessible and easy to use by everyone.

Note: For a more detailed description of all web content accessibility guidelines, see the [Web Content Accessibility Guidelines (WCAG) 2.1 standard](https://www.w3.org/TR/WCAG21/).

| Article element | Guideline | Example |
| --- | --- | --- |
| Body content | To create content that is easily understandable by everyone, use:  - Clear and simple language - Shorter paragraphs - Headings and organization - Bullets or numbered lists | **Not accessible** “If you want to assemble the widget, begin by inspecting the box. If the box is damaged, meaning that it has dents or is broken, be sure to report it to us. Next you can begin to perform the following tasks: Insert the screws into the unit and tighten them. Turn on the unit.”  **Accessible**  To assemble the widget   1. Inspect the box for damage. If it is damaged, [report it to customer service](https://support.zendesk.com/hc/en-us/articles/5275654678554). 2. Insert the screws into the widget and tighten. 3. Press the ON button. |
| Headings | Use headings hierarchically, with <h1> being the most important heading and subheadings organized as <h2>, <h3>, and so on. Increase or decrease headings by one level at a time when ordering them on the page. For example, use a <h4> after an <h3>, rather than a <h5> or <h6>. Try to have only one <h1>, with the most important text in it (such as the page’s title).  Organizing web pages by headings makes them visually distinguishable for users with cognitive disabilities and is easier for screen reader users to navigate. | **Not accessible (no subheadings)**  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque volutpat turpis ac ultrices pulvinar. Nullam pharetra neque ac eros fermentum, sed tempor lorem tristique. Aenean ut malesuada diam.  **Not accessible (skipped subheading levels)**  Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Heading 1  Quisque tempor semper metus eu venenatis.  Heading 4  Etiam et vehicula ipsum.  **Not accessible (more than one <h1>**  Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Heading 1  Quisque tempor semper metus eu venenatis.  Heading 1  Etiam et vehicula ipsum.  **Accessible**  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Heading 1 Quisque tempor semper metus eu venenatis. Integer vehicula interdum velit, sit amet rutrum nisi sollicitudin ac.  Heading 2 Etiam et vehicula ipsum. Aenean placerat semper leo et bibendum. |
| Images | Provide clear and concise alternate (alt) text for purposeful images that describe what the image is about. Alt text is read aloud by screen reader software.  If you are using   - In content blocks, use the [ALT function on the content block editor toolbar](inserting-images-in-articles-and-content-blocks.md#topic_fsy_nz1_3vb) to enter alternative text. - In articles, use the source code editor to add <img> alt attribute to the image.  Hide decorative images by using a null alt text (`alt=""`) so they can be ignored by assistive technologies such as screen readers. | **Not accessible**  `<img src="/guide-media/screenshot">`  **Accessible**  `<img src="/guide-media/screenshot" alt="Screenshot of the Create content block page">` |
| Link color and style | Use a link color that contrasts with the page and surrounding text and includes a non-color indicator (such as underline or icon). This makes your links accessible for users who have difficulty differentiating text with low contrast or who are colorblind.  Avoid using images as links. If necessary, use an image that includes alternative text that describes the location and purpose of the link. | **Not accessible**   - See *Creating accessible help center content* - See   **Accessible** See [Creating accessible help center content](https://support.zendesk.com/hc/en-us/articles/5275654678554) |
| Link text | Create link text that makes sense without the surrounding content. For example, avoid ambiguous link text such as “click here,” or “learn more”. Screen readers can’t interpret where the link will lead when it's not stated in the text.  Don't use the raw URL for the link text. Screen readers will read the entire URL to users, regardless of length. | **Not accessible**  [Click here](https://support.zendesk.com/hc/en-us/articles/5275654678554) See [www.website.com/linkedpage.html](https://support.zendesk.com/hc/en-us/articles/5275654678554) **Accessible**  [View a list of accessibility resources](https://support.zendesk.com/hc/en-us/articles/5275654678554) |
| Titles | Use page titles that describe the topic or purpose. | **Not accessible**  “Accessibility details”  **Accessible**  “Creating accessible help center content” |
| Video | Select a video provider who supports closed captions. Closed captions make videos more accessible to people who are deaf or hard of hearing. Provide a transcript and audio description for the video. | **Accessible** |

## Content accessibility resources

Familiarize yourself with the following resources to learn more about how to create accessible help center content:

- [Making Zendesk products accessible](https://support.zendesk.com/hc/en-us/articles/4408838287514)
- [Zendesk Product Accessibility](https://www.zendesk.com/company/agreements-and-terms/accessibility/)
- [Web Content Accessibility Guidelines (WCAG) 2.1](https://www.w3.org/TR/WCAG21/)
- [Making your help center accessible](https://support.zendesk.com/hc/en-us/articles/5318477060250)