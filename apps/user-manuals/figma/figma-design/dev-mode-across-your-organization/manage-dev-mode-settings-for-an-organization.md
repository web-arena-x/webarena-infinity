# Manage Dev Mode settings for an organization

Source: https://help.figma.com/hc/en-us/articles/22927410880535-Manage-Dev-Mode-settings-for-an-organization

---

Who can use this feature

Available on the [Enterprise plan](https://help.figma.com/hc/en-us/articles/360040328273)

**Organization admins only.**

Organization admins can manage Dev Mode settings for the entire organization, including:

- [Pin Dev Mode plugins](#h_01HX7WRTJJRSF08WYVQB4Z0RT0) for every member of an organization
- Update the [default code language for Dev Mode code snippets](#h_01HX7WZYS0ZVPTSZ472B38CS7A)
- [Set a plugin to auto-run](#h_01HX7X3W9ZGSN655DPYKTHMQRX) for members when they open a file

**Tip:** You can check who has a Dev seat under the **People** tab in **Admin**.

[Learn more about managing Dev Mode seats as an admin →](https://help.figma.com/hc/en-us/articles/19813618057623-Dev-Mode-is-out-of-beta-what-admins-need-to-know#h_01HKN1D11HX25FYBJXCVR1FR75)

**Note:** These settings apply to all files in an organization, excluding drafts.

## Pin and unpin plugins

Pinning a plugin in Dev Mode automatically adds it to the Inspect panel for all users. If you prefer that all users have the same tools for managing tasks, inspecting designs, or generating code, pinning plugins can help your users find them more easily.

When you pin a plugin in Dev Mode in the organization, Figma will:

- Automatically display the plugin in the Inspect panel in Dev Mode. It's not possible to pin plugins for a specific team or group of members.
- Add the plugin to the approved list, if enabled. **[Learn more about approved plugins →](https://help.figma.com/hc/en-us/articles/4404228724759)**

### Pin a plugin

To pin a Dev Mode plugin for the entire organization:

1. Go to the listing for the plugin that you want to pin.
2. Click **Copy link** in the **Share** section to add the plugin URL to your clipboard.
3. From the file browser, click **Admin** in the left sidebar.
4. Select the **Settings** tab, then click **Dev Mode settings** in the **Extensions** section.
5. If **Pinned plugins** is not enabled, enable the setting. You should only need to do this once per organization.
6. Click **+**.
7. Paste the plugin link in the field provided and click **Add** to confirm.
8. Click **Save** to apply your changes.

### Unpin plugins for the organization

Organization admins can remove pinned Dev Mode plugins at any time. Unpinning a plugin doesn’t prevent people from using the plugin, and people can still pin the plugin to their files if they wish. To prevent organization members from using a plugin, use the [Approve plugins setting](https://help.figma.com/hc/en-us/articles/4404228724759).

To unpin Dev Mode plugins:

1. From the file browser, click **Admin** in the left sidebar.
2. Select the **Settings** tab, then click **Dev Mode settings** in the **Extensions** section.
3. Next to the pinned plugin that you want to remove, click **Remove**.
4. Click **Save** to apply your changes.

## Set a default language for code snippets

You can set a default language for code snippets in Dev Mode to match the language and properties used by developers when implementing designs. This helps developers save time and avoid language mix-ups.

You can set a default [language for code snippets in Dev Mode](../turn-designs-to-code/use-code-snippets-in-dev-mode.md#01H8CZ5SQRTZDA7BYCA12K0KS6) for the entire organization. When you set a default language for code snippets, the code snippets that appear in Dev Mode’s Inspect panel will use the language you set. Additionally, specific properties may be available based on the language you set as default. For example, some languages let you also set a default unit of measure.

You can also add plugins to provide additional languages for code snippets, such as any codegen plugins that are used internally by your developers.

Setting a default language does not prevent members of your organization from manually selecting a different option when they’re inspecting a design in Dev Mode.

To set a default language for code snippets in Dev Mode:

1. From the file browser, click **Admin** in the left sidebar.
2. Select the **Settings** tab, then click **Dev Mode settings** in the **Extensions** section.
3. If **Default code language** is not yet enabled, click the toggle to enable the setting.
4. In the **Language** dropdown menu, select the language you want to set as default or click **Add plugin.**
5. If you want to use a plugin to provide a default language:
   1. Go to the listing for the plugin that you want to use to generate code snippets.
   2. Click **Copy link** in the **Share** section to add the plugin URL to your clipboard.
   3. Paste the plugin link in the field provided and click **Add** to confirm. Figma will add the plugin as an option for default language.
6. If required, configure any additional properties for the default language, such as the unit of measure.
7. Click **Save** to apply your changes.

## Set a plugin to auto-run

Setting a Dev Mode plugin to auto-run when a file opens is a great way to implement organizational standards for all of your Dev Mode users. For example, if your teams consistently use an internal Figma plugin for development support, you can set that plugin to run automatically, ensuring all Dev Mode users have the same experience.

You can set a specific Dev Mode plugin to run automatically when a Figma file opens. The auto-run setting cannot be used for codegen plugins that provide code snippets to the inspect panel — see [Set default language for code snippets](#h_01HX7WZYS0ZVPTSZ472B38CS7A) for those plugins.

Only one plugin can be set to auto-run per organization.

To set a plugin to auto-run for the entire organization:

1. Go to the listing for the plugin that you want to auto-run.
2. Click **Copy link** in the **Share** section to add the plugin URL to your clipboard.
3. From the file browser, click **Admin** in the left sidebar.
4. Select the **Settings** tab, then click **Dev Mode settings** in the **Extensions** section.
5. If **Auto-run plugin** is not enabled, enable the setting. You should only need to do this once per organization.
6. Paste the plugin link in the field provided and click **Set** to confirm.
7. Click **Save** to apply your changes.