# Using carousels in conversation flows for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749513370-Using-carousels-in-conversation-flows-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

A carousel is a rich messaging block type within a dialogue for an advanced AI agent. It
displays up to 10 options, each with a visual element called a card. Carousels provide a
visually pleasing way for customers to make a selection from options presented to them by the
AI agent.

This article contains the following topics:

- [About the carousel block](#topic_ezr_bkq_xfc)
- [CRM-specific requirements and
  limitations](#topic_yh2_glq_xfc)
- [Populating carousel cards via an API
  integration](#topic_bzz_fmq_xfc)

## About the carousel block

When you add a carousel block in a dialogue, two child blocks appear for configuration:

- **Card block**: Represents the first card in the carousel. It includes fields for
  image URL, card title, and description.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_carousel_card.png)
- **Card button block**: Represents a button element on the associated card. Each
  button can be one of two types: a standard button, or a button with an external link.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_carousel_card_button.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_carousel_card_button_link.png)

You can add more buttons to each card (though some CRMs have limits on the number of
buttons), and up to 10 cards total within a carousel.

You can add a fallback for users who don't interact with the carousel using the Fallback
toggle in the Details pane. A fallback block appears in the dialogue and can be configured
as an alternate branch.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_carousel_fallback.png)

Carousel blocks are available only for messaging AI agents, and only with certain CRMs.
CRMs may have specific requirements and limitations for carousels.

## CRM-specific requirements and limitations

If you’re adding carousels to a CRM integration, special requirements and limitations apply
in the following instances:

- [Using carousels with Sunshine
  Conversations](#topic_fpl_llq_xfc)
- [Using carousels with Zendesk Chat](#id_bhb_nlq_xfc)

### Using carousels with Sunshine Conversations

Sunshine Conversations has the following requirements and limitations in its support of
rich format messaging.

| Block type | Component | Sunshine Conversations limitations |
| --- | --- | --- |
| Card | All fields | - All fields mandatory unless otherwise specified |
|  | Card count | - Maximum 10 cards per carousel |
|  | Images | - URL maximum 2048 characters - URL must be valid http/https |
|  | Card title | - Maximum 128 characters |
|  | Description | - Maximum 128 characters - No line breaks allowed |
| Card button | Button count | - Maximum three buttons per card |
|  | Button text | - Mandatory - Maximum 35 characters |
|  | Button with external link | - URL maximum 2048 characters - URL must be valid http/https - Dialogue must end here |

### Using carousels with Zendesk Chat

Zendesk Chat has the following requirements and limitations in its support of rich format
messaging.

| Block type | Component | Zendesk Chat limitations |
| --- | --- | --- |
| Card | All fields | - All fields mandatory - Must contain at least one character (spaces don’t count) |
|  | Card count | - Maximum 10 cards per carousel |
|  | Images | - PNG, JPEG or GIF - Maximum 20MB - Render rectangularly (horizontal side being longest) - Automatically cropped from center to 2:1 ratio (width:height) - URL maximum 2000 characters - URL must be valid http/https |
|  | Card title | - Maximum 150 characters - Quotation marks (") not allowed |
|  | Description | - Maximum 150 characters - No line breaks - Quotation marks (") not allowed |
| Card button | Button count | - Maximum three buttons per card |
|  | Button text | - Mandatory - Maximum 20 characters |
|  | Button with external link | - Dialogue must end here - URL maximum 2000 characters - URL must be valid http/https |

## Populating carousel cards via an API integration

A carousel is static by default, but can be converted to a dynamic carousel in order to use
content fetched from an existing [custom API integration](https://support.zendesk.com/hc/en-us/articles/8357756844442). In a dynamic carousel, the card and card
button blocks are templates that contain the dynamic content.

**To add a carousel with dynamic content to a dialogue**

1. [In the dialogue builder](https://support.zendesk.com/hc/en-us/articles/9066753203738), click the plus (+) icon to add a
   carousel block.

   The dynamic carousel block appears along with the first template card
   block, a fallback block, and a Details pane.
2. To remove the fallback (optional), deselect **Fallback** on the Details pane.

   Otherwise, it can be configured as an alternate branch.
3. In the Details pane, click **Convert to dynamic carousel** and enter
   `dataSources` as the array type parameter.
4. In the template card block, enter text or parameters such as
   `%imageurl`, `%title`, and `%description`
   in the respective fields.
5. In the template card button block, enter text or a parameter such as
   `%buttontext`.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_carousel_2.png)