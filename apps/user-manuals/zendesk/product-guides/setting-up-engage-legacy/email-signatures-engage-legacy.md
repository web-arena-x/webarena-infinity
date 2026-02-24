# Email Signatures (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731498765466-Email-Signatures-Engage-Legacy

---

The Engage Email Signature functionality enables you to control signatures added to the end of emails sent from an Agent.

Email Signatures are configured based on Workflows, and as a result can be Queue based.

Email Signatures can be configured so that they are either editable or not for Agents.

## How to configure Email Signatures

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731462285466)

1. Navigate to **Workflows** (Settings -> Workflows)
2. Find the relevant Workflow and click the **Edit workflow** button
3. Scroll down to the **Email Signature Settings** section
4. Set **Email signatures** to Enabled
5. Set the value for **Editable signatures**
6. Enabled - allows Agents to edit the configured signature
7. Disabled - Agents will not be able to edit the configured signature
8. Add your company signature into the text editor
9. Note that you can use Personalisation Tokens to dynamically change signatures
10. As an example, use {{user.full\_name}} to add the Agents name into the signature

[Click here](https://support.zendesk.com/hc/en-us/articles/9696137593626) for a list of Personalisation Tokens

### Setting up Email Signatures using HTML

We recommend using the HTML editor when your signature includes images.

Note that Email Signatures that are configured using HTML cannot be edited by Agents.

1. Within the **Email Signature Settings** click the **Edit HTML** button (on the bottom right)
2. This will open the HTML editor
3. Add the HTML code for your signature
4. Click the **Rich Text** button to preview your signature

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731466346394)

## How to use Email Signatures

When an Agent is on an Email Contact, the Email Signature will be added to their reply as per the configuration (i.e. whether it is enabled or not).

![](https://support.zendesk.com/hc/article_attachments/9731437983002)

If the **Editable Signatures** setting is **Enabled**, the agent will be able to edit any part of the signature, including removing it entirely.

‍