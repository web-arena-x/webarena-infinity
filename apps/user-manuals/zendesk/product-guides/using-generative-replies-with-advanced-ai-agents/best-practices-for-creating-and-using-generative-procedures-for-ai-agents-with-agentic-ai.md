# Best practices for creating and using generative procedures for AI agents with agentic AI

Source: https://support.zendesk.com/hc/en-us/articles/9424547622298-Best-practices-for-creating-and-using-generative-procedures-for-AI-agents-with-agentic-AI

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Generative procedures are AI-generated procedures that help power the decision-making capabilities of [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066). Instead of building scripted conversation flows in the dialogue builder, you can enter your business policies and let the AI agent generate a procedure to map out the best path to resolution.

This article provides best practices about when to use generative procedures, as well as how to write and optimize them.

This article contains the following topics:

- [When to use a generative procedure or a dialogue](#topic_rml_mq2_wfc)
- [Tips for writing generative procedures](#topic_z4k_nq2_wfc)

Related articles:

- [Examples of generative procedures for AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/9424547984026)
- [Creating generative procedures for AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8979864563610)

## When to use a generative procedure or a dialogue

When determining whether to use a generative procedure or a dialogue to guide your AI agent’s conversation flow, consider the following guidance. Then see [Configure whether a use case uses a dialogue or generative procedure](https://support.zendesk.com/hc/en-us/articles/9041911005850#topic_elk_mcf_52c).

| **Use a generative procedure when…** | **Use a dialogue when…** |
| --- | --- |
| - A process is easy to break into clear and logical   steps. - Your API use cases are straightforward and don’t require   multiple conditions. - You want to use generative AI reasoning on top of a   response from your APIs. - You want the AI agent to answer based on information   already contained in your knowledge source. | - A process is long and complex, with multiple branching   scenarios. - You need to include multiple APIs calls and complex   conditions. - You want to include rich-message formatting, such as   buttons, cards, and carousels. - You don’t want the AI agent to deviate from a script,   especially for legal or financial use cases. |

## Tips for writing generative procedures

When [creating a generative procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610), keep the following tips in mind. Adhering to these guidelines helps you write more effective procedures.

- [Use clear, specific language](#topic_zkl_kw2_wfc)
- [Break down complex tasks](#topic_gz4_lw2_wfc)
- [Present steps in logical, sequential order](#topic_clh_mw2_wfc)
- [Define clear conditions and actions](#topic_l2w_mw2_wfc)
- [Maintain consistent terminology](#topic_g4m_nw2_wfc)
- [Avoid combining multiple actions in one step](#topic_sgb_4w2_wfc)
- [Include requests for feedback before executing conditional steps](#topic_ubh_nxg_zfc)
- [Provide examples when helpful](#topic_v2s_4w2_wfc)
- [Anticipate and handle errors](#topic_or2_qw2_wfc)
- [Highlight critical steps](#topic_u2b_rw2_wfc)
- [Use an imperative, direct writing style](#topic_b2v_rw2_wfc)
- [Test, iterate, and update regularly](#topic_jw4_sw2_wfc)

### Use clear, specific language

Write each step using simple, direct words. Avoid vague terms, jargon, and complex sentences to ensure the AI interprets instructions correctly. Specify exactly what information is needed to avoid misunderstandings.

Additionally, writing in English helps optimize flows. However, performance is still the same in all major languages.

- **Good**: "Ask the customer to provide their 10-digit account number."
- **Bad**: "Request account info from the user." (It’s ambiguous what “account info” means without more context.)

### Break down complex tasks

Divide complicated processes into smaller, focused steps. Each step should represent a single, manageable action, improving clarity and execution.

- **Good**:
 1. “Verify customer identity.
 2. Check account balance.
 3. Process payment.”
- **Bad**: "Verify identity and check balance and process payment in one step."

### Present steps in logical, sequential order

Arrange instructions in the order the AI should execute them, reflecting the actual workflow. Use numbered or clearly structured lists.

- **Good**: Steps follow the natural flow: Greet → Verify → Diagnose → Resolve/Escalate
- **Bad**: "Verify identity after escalating the issue."

### Define clear conditions and actions

Use explicit “If… then…” statements with precise instructions for each condition and the resulting action or next step. This reduces ambiguity and guides decision-making.

- **Good**: “If the payment can’t be processed, then tell the user there was a problem with the payment and ask them for a different payment method.”
- **Bad**: "If there’s a problem with payment, handle it accordingly."

### Maintain consistent terminology

Always use the exact same names for entities (for example, plans, policies, or billing types) throughout the procedure to prevent confusion or misinterpretation. Consistent naming prevents the AI from mixing terms. To see the already-created entities, type a forward slash (/) or click the plus icon (+) in the [procedure editor](https://support.zendesk.com/hc/en-us/articles/8979864563610#topic_ult_rs2_52c).

- **Good**: Always refer to "Premium Plan" when discussing that service level.
- **Bad**: Alternate between "Premium Plan," "Gold Plan," and "top-tier subscription."

### Avoid combining multiple actions in one step

If a step involves more than one major task, split it into separate steps to keep instructions clear and unambiguous. This prevents skipping or misunderstanding tasks.

- **Good**:
 - Step 1: Confirm the issue reported by the customer.
 - Step 2: Provide troubleshooting steps based on issue type.
- **Bad**: "Confirm the customer’s issue and then provide troubleshooting and escalate if unresolved."

### Include requests for feedback before executing conditional steps

Whenever you include a conditional step in your procedure, the AI agent should first ask the customer a clarifying question to ensure that the conditional is ready to be evaluated. This helps prevent the AI agent from sending the same reply twice.

In other words: Tell → Ask → Conditional, instead of Tell → Conditional.

- **Good**: “Here’s the policy. Do you need anything else?” Or, "Did that answer your question?" Or, "Let me know if you have any questions about this."

 The conditional branch then triggers only after the user’s reply, eliminating a potential duplicate response.
- **Bad**:
 - Step 1: The AI agent tells the user something, but doesn’t ask a clarifying question.
 - Step 2: A conditional branch that should run only if the user later asks a very specific follow-up.

    Because the AI agent isn’t told to wait between step 1 and step 2, it immediately evaluates the vague condition, finds nothing to match, and resends the last message.

### Provide examples when helpful

Include contextual examples for common scenarios to clarify expected outcomes and reduce ambiguity. Examples guide the AI’s tone and content.

- **Good**: "If the customer says ‘My bill is too high,’ respond with: ‘I see your charges include extra data usage this month.’"
- **Bad**: No example given, leaving the AI unsure how to respond.

### Anticipate and handle errors

Include instructions for error handling, such as what to do if data is missing, incomplete, or contradictory, to ensure robustness and reliability.

- **Good**: "If API returns 'timeout', retry up to 2 times. If still failing, escalate the request."
- **Bad**: "If the API call fails, try again." (No retry limit or fallback.)

### Highlight critical steps

Use capital letters or other formatting techniques to emphasize important or mandatory steps within the procedure, reducing the risk of compliance or operational errors.

- **Good**: "VERIFY CUSTOMER IDENTITY BEFORE DISCLOSING ACCOUNT INFORMATION."
- **Bad**: No emphasis on identity verification step.

### Use an imperative, direct writing style

Write steps as commands or instructions (for example, “Check if…”, “Ask the customer…”, or “Escalate the request if…”) to avoid uncertainty and vagueness.

- **Good**: "Ask for the customer’s last payment date."
- **Bad**: "You might want to ask when they last paid."

### Test, iterate, and update regularly

Continuously test the procedure with real interactions, gather feedback, and revise the steps as policies or customer needs evolve to maintain accuracy and customer satisfaction.

- **Good**: Review procedures monthly and adjust steps based on customer feedback or policy changes.
- **Bad**: Write once and never revise.