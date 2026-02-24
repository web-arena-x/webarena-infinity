# Understanding tags and ticket fields

Source: https://support.zendesk.com/hc/en-us/articles/4408881943194-Understanding-tags-and-ticket-fields

---

You might have noticed that drop-down fields and checkbox fields have [associate tags attached](https://support.zendesk.com/hc/en-us/articles/4408883152794-Adding-and-using-custom-ticket-fields#topic_ext_est_kc) to their options. Knowing how these interact will give you a greater understanding of the platform and a better idea of how to set up your workflows. For more information on tags see, [Using tags](https://support.zendesk.com/hc/en-us/articles/4408888664474-Using-tags).

This tip covers the following sections:

- [Understanding tag and ticket field interactions](#topic_itw_qlh_1v)
- [Changing the field option tag](#topic_q4v_qlh_1v)

## Understanding tag and ticket field interactions

There are two ways field values and tags interact:

1. When you select a field option, the associated tag will automatically be added to the ticket.
2. If you add a tag, the associated field option will be selected as well.

Basically, when Zendesk Support tries to populate fields, it looks for tags on the ticket first and then selects the associated field options for those tags. This is why you cannot have duplicate tags associated; the system won't know which field option to use. To prevent this, you will receive an error when you try to use the same associated tag.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tagsticketfields.png)

This tag and field option relationship causes the following results:

- If you add a tag that is associated with a different field option, the new option will be selected and the original field option's tag will be deleted automatically.
- If you rename a field option, all tickets with the associated tag, including closed tickets, will be updated with the new name.
- Deleting a field option will change the ticket field to 'null' in all tickets with the field option. If you re-add the option, along with the same associated tag, then the ticket field will be selected again automatically.

Note: If you add a tag that is associated with a field value, the corresponding ticket field value will be filled even if the ticket field isn't currently active on the ticket form. The ticket field value and the corresponding tag will appear in the [ticket events](https://support.zendesk.com/hc/en-us/articles/4408829602970) log.

## Changing the field option tag

If you change a field option tag, there will be different repercussions than when changing a field option. For example, you can change the field option title with little repercussions (aside from reporting), but you cannot change the field option tag with the same results. Since the tag is the backbone, if you change the tag, you will create a new field option.

Changing the tag will result in the following behavior:

- Changing a field option's tag will automatically deselect that option from all tickets with the field selected.
- If you change the field option tag to a tag that does not exist on a ticket, the field will revert to a 'null' value.
- If you change the field option tag to tag that does exist on a ticket, the field will revert to a 'null' value until an update occurs. After an update, Zendesk Support re-reads the tags and will select the correct field option.
- Since you need an update to populate the updated field option, you cannot change field option tags to edit closed tickets.

  Note: The only exception to this rule is if your field option was deleted and then re-added into the same field (as discussed above). You cannot create the same field option in a different field and expect the results to populate historical tickets.

As you might imagine, this can become especially messy when you delete field options or disable/delete entire fields. Remember, data is important. Once it's gone, you'll never be able to get it back.