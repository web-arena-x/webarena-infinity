# Applying ticket forms to tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408832861210-Applying-ticket-forms-to-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

A ticket form is a set of predefined ticket fields for a specific support
request. The ticket form that's applied to the ticket determines the fields
and data a ticket contains.

End users can select a ticket form when they submit a request, if [multiple ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858) are
available to them, and that ticket form will be applied to their ticket.
Agents can apply any available form to a ticket or change a ticket's
existing form.

**To apply or change a ticket form for a ticket**

- In a ticket that isn't closed, click the **Form** field in
  the ticket properties panel, then select a form from the
  drop-down list.

  Note: For multibrand users, the forms displayed in
  this list depend on the brand applied to the
  ticket. Depending on your settings, you may be
  able to access another brand's ticket forms by
  switching the brand from the Brand drop-down
  list.

  You can't change the ticket form for a closed
  ticket.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticketforms_agent_form_field.png)

  The ticket
  fields update for the ticket form you selected.
  Depending on how an admin configured the form, only
  certain, relevant ticket statuses may be available
  in the status picker (see [About the agent
  experience with form ticket
  statuses](https://support.zendesk.com/hc/en-us/articles/7755811560346#topic_vbd_gqx_vcc)).

  If you change forms while
  working on a ticket, any data entered in the
  previous form that is not shown in the new form will
  still be available until you submit the ticket.

  For example, consider that you enter data in
  the Platform field in a Software request form, then
  switch to a Hardware request that does not contain
  the Platform field. If you switch back to the
  Software form before you submit the ticket, your
  data will be saved in the Platform field. If,
  however, after switching to the Hardware form you
  submit the ticket, the Platform data from the
  Software form will not be retained in the
  ticket.

  Note that ticket field values can
  still be referenced by and acted on by triggers and
  automations, even if the ticket form is switched to
  another form that doesn't contain the ticket
  field.

Note: Keep in mind, that if an agent changes the brand of a ticket, and the
currently selected form is not associated with new brand, the form
doesn't change. This is to prevent loss of data entered in the
ticket fields.