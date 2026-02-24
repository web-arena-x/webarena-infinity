# Creating procedures for auto assist

Source: https://support.zendesk.com/hc/en-us/articles/7924047699738-Creating-procedures-for-auto-assist

---

Auto assistis an AI-powered assistant that understands the contents of submitted tickets and makes suggestions to your agents on how to solve them.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Auto assist is an AI tool that helps agents by suggesting solutions based on ticket content. To create effective procedures, write clear, step-by-step instructions as if guiding a new agent. Test procedures to ensure they provide accurate suggestions. Follow best practices like using consistent terminology, including feedback steps, and integrating actions or macros for improved assistance.

[Auto assist](https://support.zendesk.com/hc/en-us/articles/9945148867866) is an AI-powered assistant that understands the contents of submitted tickets and makes suggestions to your agents on how to solve them.

Procedures are the sets of written steps that auto assist should follow when making suggestions. You can think of defining procedures as similar to explaining to a new agent how a specific problem should be solved within your company.

This article describes how to write procedures for auto assist so that it makes the right suggestions to agents in a ticket. You can write procedures in all [Zendesk Support languages](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01H8Y4XESK886V2SA6E12WAZZ7).

This article contains the following topics:

- [Creating a procedure](#topic_vs3_j44_xcc)
- [Testing a procedure](#topic_y2w_j44_xcc)
- [Best practices for creating effective procedures](#topic_o3y_l44_xcc)
- [Example procedure](#topic_j4t_m44_xcc)

Related articles:

- [Turning on and configuring auto assist](https://support.zendesk.com/hc/en-us/articles/8013454025114)
- [Viewing and managing procedures for auto assist](https://support.zendesk.com/hc/en-us/articles/9012170900890)

## Creating a procedure

Procedures should be written as though you’re telling an agent how to perform an internal process. Format your procedure as a simple step-by-step breakdown of how to solve the customer’s request. Be specific and use consistent terminology throughout your procedure. To learn more, see [Understanding procedures for auto assist](https://support.zendesk.com/hc/en-us/articles/9945148867866#topic_rkr_344_xcc).

Tip: If you already have internal documentation that explains how your agents should solve certain customer requests, use that content as a starting point for auto assist procedures.

Alternatively, you can write a procedure as though you’re engineering a prompt to be used with a large language model (LLM) chatbot, such as ChatGPT. See [OpenAI’s best practices on prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering).

**To create a new procedure**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Manage articles** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_manage_articles.png)) in the sidebar, then select **Procedures**.
2. Click **Create procedure**.

   Alternatively, click the drop-down arrow next to **Create procedure** and select **Use example**. This populates the procedure **Name** and content fields with text that you can update as needed.
3. In the **Name** field, enter a descriptive name for the procedure.

   This name is used by auto assist to help connect the customer’s conversation to the right procedure. The procedure name appears only in Knowledge admin, not in the Agent Workspace for the agent.
4. To associate the procedure with specific brands, open the right-hand **Settings** panel, click **Selected brands**, then choose the brands you want to associate the procedure with.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_procedure_create_select_brand.png)

   By default, your procedure is automatically associated with all of your brands.
5. Click below the name field and enter the content for your procedure.

   You can do the following:
   - To add specific custom actions or action flows to your procedure, click **Insert action** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_add.png)) in the toolbar.

     Alternatively, enter a forward slash (**/**).

     In the menu, select a standard action, a custom action, or an action flow.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_procedure_insert_action.png)

     If you insert a standard action, you must specify the value you want auto assist to update the ticket or field to. See [Standard actions for auto assist](https://support.zendesk.com/hc/en-us/articles/9174548349978#topic_ubt_qyr_k2c) to learn more.

     If no actions or action flows exist, click **Manage actions** to [create an action](https://support.zendesk.com/hc/en-us/articles/8013439366810) or [action flow](https://support.zendesk.com/hc/en-us/articles/8855601898266#topic_fpt_1jg_t2c).

     The action or action flow is inserted into the procedure. You can hover to view what tasks it will perform.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_procedure_hover_action.png)
   - To add a macro to your procedure, type a forward slash (**/**)
     and select **Macros** from the menu.

     Click a macro to insert it into the procedure. Macros must be active and available to all agents to be inserted into a procedure.

     If no active macros exist, you can click **Manage macros** to [create or update a macro](https://support.zendesk.com/hc/en-us/articles/4408844187034#topic_zh2_4nw_4y).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_procedure_insert_macro.png)

     The macro is inserted into the procedure. You can hover over it to preview it.
   - To add steps for agents to follow manually, click the **Insert agent instructions** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_procedures_instructions_icon.png)) icon.

     In the **Instructions for agent** text block, enter the steps the agent should follow.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_procedures_agent_instructions_text_box.png)

     See [Creating instructions for agents in auto assist procedures](https://support.zendesk.com/hc/en-us/articles/9422234636698).
   - To add a help center article or another procedure, type a forward slash (**/**) and select **Help center content** from the menu.

     Select an article from the **Published articles list**, or click the **Published procedures tab** and select a procedure.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_procedures_insert_help_content.png)

     Click **Insert** to add the published procedure or article.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_procedures_insert_procedure_content.png)

     See [About help center content in procedures](https://support.zendesk.com/hc/en-us/articles/9945148867866#topic_trn_d23_b3c).
6. (Optional) Use the editing toolbar at the top of the page to add headings, bold and italic text, and bulleted and numbered lists. Currently, you can’t include images in procedures.
7. To publish your procedure, click the drop-down arrow next to **Save** draft and select **Publish**.
8. In the window that appears, click **Publish**.

   Published procedures are automatically available for auto assist to use.

## Testing a procedure

You should always test your procedure before letting auto assist suggest replies or actions in a real-world setting.

**To test a procedure**

1. [Limit the agents who can interact with auto assist](https://support.zendesk.com/hc/en-us/articles/8013454025114) to only those groups or agents who are performing the testing.
2. [Create a messaging or email ticket](https://support.zendesk.com/hc/en-us/articles/8013454025114)
   with the *agent\_copilot\_enabled* tag. Email tickets must be created from an email that's not associated with any agents in your Zendesk account, as auto assist doesn't respond to agent comments.
3. [Try to solve the ticket with auto assist’s help.](https://support.zendesk.com/hc/en-us/articles/7051314237466)
   - If you’re testing an [integration between auto assist and Shopify](https://support.zendesk.com/hc/en-us/articles/7719560079642), you can [place test orders on your Shopify store](https://help.shopify.com/en/manual/checkout-settings/test-orders).
4. If auto assist isn’t offering the suggestions you want, update the procedure to be clearer and more concrete.
5. Repeat steps 1–4 as needed until auto assist is offering the suggestions you want. Creating good procedures is an iterative process and might take a few rewrites.

## Best practices for creating effective procedures

When creating procedures, follow these best practices:

- **Write short, easy-to-follow steps.** Phrase your steps as straightforward commands that an agent would take. For example: "Ask the customer to watch this video: <link>" Avoid prompts such as "Find the item the customer asked for and share the link with the customer" (auto assist can’t autonomously search your help center or website).
- **Address the agent perspective.** Procedures should be written as if you’re talking to an agent. If you copy existing content from customer-facing help center articles, update them to reflect agent-focused considerations and actions.
- **Include feedback steps.** Help auto assist gather necessary customer input to move on to the next step. For example: "Ask the customer if <an action> worked."
- **Include actions where possible**. Add a standard or custom action that auto assist can execute if the agent approves. For example: "Add book to cart."
- **Include existing macros**. Add macros that are available to all agents so that auto assist can suggest macros. You can add one macro per procedure step.
 Avoid adding other actions in the same step as a macro.
- **Be consistent with terminology.** Always use the same terms for your products and services. That is, avoid using different words to refer to a single product or service.
- **Include conditions if necessary.** If you have different procedures based on some condition (for example, subscribers vs. non-subscribers), include that information in the procedure. For example: “Greet the customer, ask if they’re a subscriber, and wait for their answer before proceeding.”
- **Test and learn.** If auto assist isn’t offering the suggestions you want, update the procedure to be clearer and more concrete. See [Testing a procedure](#topic_y2w_j44_xcc).

## Example procedure

The example procedure below tells agent copilot how to help a customer select the right car for them.

### Title

Advising customer how to select a car

### Content

**Step 1: Understand the customer's needs**

Begin by asking questions to understand the customer's requirements:

- What is the primary use for the car (commuting, family vehicle, off-roading, etc.)?
- What is their budget for purchasing a car?
- Do they have any brand or model preferences?

**Step 2: Present suitable options from the list below**

Based on the information gathered, present a selection of cars that match their criteria and are on the list below. If the desired car is not here, you don’t have it. Never list cars that are not on the list below.

For commuters:

- Commuter car A: Known for its reliability, fuel efficiency, and advanced safety features. <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>
- Commuter car B: Celebrated for its great fuel economy, comfortable interior, and durability. <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>
- Commuter car C: Offers a balance of comfort, efficiency, and technology features. <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>

For families:

- Family car A: A family favorite due to its spacious interior, high safety ratings, and good fuel economy. <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>
- Family car B: Known for its third-row seating, robust safety features, and comfortable ride. <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>
- Family car C: A larger SUV that offers ample space, towing capacity, and advanced tech options. <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>

For off-road enthusiasts:

- Off-road car A: Renowned for its off-road capabilities and ruggedness.
 <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>
- Off-road car B: A reliable pickup with strong off-road credentials.
 <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>
- Off-road car C: Versatile and powerful, suitable for both work and play.
 <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>

For luxury seekers:

- Luxury car A: Combines luxury with performance and advanced technology.
 <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>
- Luxury car B: Offers a plush interior, smooth ride, and cutting-edge features. <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>
- Luxury car C: Known for its elegant design, all-wheel-drive system, and high-quality cabin. <Include real pricing, fuel efficiency, insurance costs, engine type, and any other important details.>

**Step 3: Discuss financing options**

After the customer has selected a car, ask the customer if they would rather pay in cash or credit.

**Step 4: Close the deal or offer a test drive**

If the customer is ready to close the deal:

- Thank them, ask for their name and phone number, and inform them that they will be contacted by another agent in 2 hours.

If the customer is not ready to make a choice:

- Encourage the customer to take a test drive in the cars they are most interested in. If they agree, ask them for their name and phone number. Then tell them that someone will reach out within 1 hour to confirm whether the timing they suggested is available.

Extra information that you know of:

Our dealership offers a 7-day return policy, flexible financing options (pay in monthly or semesterly installments), and a complimentary loaner vehicle during service appointments. For every other question regarding financing or promotions, you cannot help.