# Displaying subsections in your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408883063066-Displaying-subsections-in-your-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Enterprise |

You can [add subsections](https://support.zendesk.com/hc/en-us/articles/4408834687130) (sections in sections) to your help center knowledge base to create more levels of hierarchy, up to six levels deep.

By default, the standard Copenhagen theme's section page template displays a list of each section's subsections. You can [modify the theme's code](https://support.zendesk.com/hc/en-us/articles/4408839332250-) to display subsections using other page templates or to change the look of the subsections lists.

Note: This article is provided for instructional purposes only. Zendesk does not support or guarantee the code. Zendesk also can't provide support for third-party technologies such as JavaScript, jQuery, or CSS. Post any issues you have in the comments section or try searching for a solution online or from your favorite AI chat bot.

You can only show the direct subsections of a section. You cannot show multiple levels of subsections.

This article contains the following examples:

- [Showing subsections on category pages](#topic_ldx_5gs_jhb)
- [Showing sections and subsections as blocks](#topic_j3b_vgs_jhb)

## **Showing subsections on category pages**

You can update the template to display subsections below each section's articles.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/example_subsections_on_category_page.png)

**To customize the category page template**

In the category page template, insert the following block after `<section class="section">`:

```
{{#if sections}}
 <ul class="section-list">
    {{#each sections}}
      <li class="section-list-item">
        <a href="{{url}}">
          <span>{{name}}</span>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            focusable="false"
            viewBox="0 0 16 16"
            aria-hidden="true"
          >
            <path
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-width="2"
              d="M5 14.5l6.1-6.1c.2-.2.2-.5 0-.7L5 1.5"
            ></path>
          </svg>
        </a>
      </li>
    {{/each}}
 </ul>
{{/if}}
```

## **Showing sections and subsections as blocks**

You can customize the Copenhagen theme's category page template to display sections as blocks.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/example_section_blocks_io_category_page.png)

Similarly, you can customize the sections page template to display subsections as blocks.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/example_subsections_on_sections_page.png)

**To customize the category page template**

In the category page template, replace the `<div id="main-content" class="section-tree">` tag and its contents with the following snippet:

```
<section class="categories blocks">
 <ul class="blocks-list">
      {{#each sections}}
      <li class="blocks-item">
            <a href='{{url}}' class="blocks-item-link">
              <h4 class="blocks-item-title">{{name}}</h4>
              <p class="blocks-item-description">{{excerpt description}}</p>
            </a>
      </li>
      {{/each}}
 </ul>
</section>
```

**To customize the sections template**

In the sections page template, replace the `{{#if section.sections}}>` block and its contents with the following snippet:

```
{{#if section.sections}}
 <section class="sections blocks">
    <ul class="blocks-list">
      {{#each section.sections}}
        <li class="blocks-item">
          <a href="{{url}}" class="blocks-item-link">
            <h4 class="blocks-item-title">{{name}}</h4>
            <p class="blocks-item-description">{{excerpt description}}</p>
          </a>
        </li>
      {{/each}}
    </ul>
 </section>
{{/if}}
```