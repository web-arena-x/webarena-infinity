# Adding rich content to answers in bot builder (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/5133127616282-Adding-rich-content-to-answers-in-bot-builder-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This article describes functionality available only
to customers who had a drafted or published AI agent as of February 2, 2025. For
information about equivalent functionality in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see [Building dialogues for AI agents - Advanced](https://support.zendesk.com/hc/en-us/sections/8264324615322).

In
bot builder, you can add rich content elements to some of the steps in your AI agent’s
answers. Rich content elements appear to your customers in the Web Widget, mobile apps,
social apps, and third-party apps.

Rich content elements can be added when you are
[creating a new answer](https://support.zendesk.com/hc/en-us/articles/4422584657434),
[adding a new step to an existing answer](https://support.zendesk.com/hc/en-us/articles/6707589714458#topic_l32_tf2_k1c), or
updating an existing step.

This article describes the following rich content types:

- [Adding images and gifs](#topic_kh1_xsz_nvb)
- [Adding emoji](#topic_ct2_xsz_nvb)
- [Adding button links](#topic_ewh_2nm_nwb)

## Adding images and gifs

You can add an image or an animated gif to your answer flow, to provide an
engaging experience, add screenshots or other
visuals to illustrate answers, and present products and services in a way that best
represents your brand.

Images and gifs can be added to the following step types:

- [Send message](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-flow-step-types#topic_iqz_fwc_k4b)
- [Add carousel](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_il3_pmj_tvb)

To be included in an answer step, the image or gif must:

- Have a web address that can be accessed by your customers. Don't add image URLs from restricted
  help centers, as these won't be displayed in the answer.
- Be no larger than 10 MB
- Be one of the following image formats:
  - bmp
  - gif
  - heic
  - heif
  - jfif
  - jpg
  - jpeg
  - png
  - svg+xml
  - tiff
  - tif
  - webp

  **To add an image or gif to a step**

  1. With the new or existing answer open in bot builder, click the
     step type you want to add the image or gif to, or click the Add step
     icon (
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_step_icon_flowb.png)) and select the step type to
     create a new step.
  2. If you’re adding the image to a Send message step, click the
     **Insert image**
     icon (
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_image_icon.png)).
  3. Enter the image’s web address (required) and description
     (optional), then click
     **Done**.
  4. Finish configuring the step, then click
     **Done**
     at the top
     of bot builder.

     The image or gif appears in the step preview.

     The
     image, as well as any other updates, will not appear to the customer
     until you
     [publish the answer](https://support.zendesk.com/hc/en-us/articles/4422584657434-Building-a-bot-using-answers#topic_vcg_44p_qtb).

## Adding emoji

You can use the emoji picker to add emoji to your answer flows.

Emoji can be added to the following answer step types:

- [Send message](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-flow-step-types#topic_iqz_fwc_k4b)
- [Present options](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-flow-step-types#topic_mnf_gwc_k4b)
- [Show help center articles](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-flow-step-types#topic_grj_gwc_k4b)
- [Transfer to agent](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-flow-step-types#topic_zqr_gwc_k4b)

**To add an emoji to a step**

1. With the new or existing answer open in bot builder, click the
   message step you want to add the emoji to. Alternatively, click the
   **Add
   step** icon (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_step_icon_flowb.png)) and select the step type you want
   to create.
2. In the AI agent message box, enter or update any text as needed, and click the **Emoji** icon
   ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/emoji_picker.png)) to open the picker.
3. Scroll or search for the emoji you want, then click it to add to the AI agent message.
4. Finish configuring the step, then click
   **Done**
   at the top of
   bot builder.

The emoji appears in the step preview.

The emoji, as well as
any other updates, will not appear to the customer until you
[publish the answer](https://support.zendesk.com/hc/en-us/articles/4422584657434-Building-a-bot-using-answers#topic_vcg_44p_qtb).

## Adding button links

You can add buttons to steps in your answer flow. When a customer clicks a button,
they'll open an external link, such as a different knowledge base
or another page within the current website.

You can add button links to the following step types:

- [Send message](https://support.zendesk.com/hc/en-us/articles/4408836323738-Understanding-answer-flow-step-types#topic_iqz_fwc_k4b)
- [Add carousel](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_il3_pmj_tvb)

**To add a button link to a Send message step**

1. Open or create a new answer in bot builder, then click an existing
   **Send message** step or create a new one.
2. Click **Add button**.
3. Enter the button’s web address and text, then click **Add**.
4. Finish configuring the step, then click **Done** at the top of bot
   builder.

You can add up to 10 button links to each Send message step.

You can edit the button by clicking the **Options icon** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)).

The button, as well as any other updates,
will not appear to the customer until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250#topic_ads_n1n_3bc).

**To add a button link to an Add carousel step**

1. Open or create a new answer in bot builder, then click an existing
   **Add carousel** step or create a new one.
2. Click a carousel panel.
3. Click **Add button** and select **Open link** from the action
   dropdown menu.
4. Where requested, enter the button’s web address and text, then click
   **Done**.
5. Finish configuring the step, then click **Done** at the top of bot
   builder.

You can edit the button by clicking the carousel panel's **Options
icon** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)).

The button, as well as any other updates,
will not appear to the end user until you [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250#topic_ads_n1n_3bc).

## Saving responses

You can add a button to save a variable and its value when a customer clicks a
carousel panel button. The variable and value can then be used downstream in bot
builder.

A carousel panel can include a maximum of three buttons. These buttons can be a
mixture of buttons to save a response and buttons to open a link, but only one
button to save a response is allowed.

**To add a save response button**

1. Open or create a new answer in bot builder, then click an existing
   **Add
   carousel**
   step or create a new one.
2. Click a carousel panel.
3. Click
   **Add button**
   and select
   **Save response** from the action
   dropdown menu.
4. Enter a descriptive button text to display to the customer.
5. Enter a variable name and value to save. If you are using a dynamic
   carousel, you can click the plus button to select a value from the
   **Make
   API**
   call.

If, for example, you create a **Send message** step after the carousel, you can reference the
variable by clicking the plus button in **AI agent message**.