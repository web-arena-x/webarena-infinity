# Translating themes

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/language/translate-theme

---

# Translating themes

You can activate multiple languages from your Shopify admin so that customers all over the world can view content in their native language.

For themes that are compatible with selling in multiple languages, you can [change the default theme language](https://help.shopify.com/en/manual/international/localization-and-translation#change-the-default-language-of-your-online-store), and [add other languages](https://help.shopify.com/en/manual/international/localization-and-translation#add-new-language) so that customers can select their preferred language. If your theme doesn't have the language that you want, or if you want to edit the default translations, then you can [create the translations yourself](translate-theme.md#create-a-translation-for-your-theme).

## On this page

* [Create a translation for your theme](translate-theme.md#create-a-translation-for-your-theme)
* [Types of content that can be translated](translate-theme.md#types-of-content-that-can-be-translated)

## Create a translation for your theme

You can [translate and localize your store](https://help.shopify.com/en/manual/international/localization-and-translation#exporting-importing-translations) to change the language of your theme. You can add your own translations by installing Shopify's [Translate & Adapt app](https://help.shopify.com/en/manual/international/localization-and-translation#requirements), using CSV export/import, or by using a third-party app.

## Types of content that can be translated

There are three basic types of content that you might want to translate:

* [Plain text](translate-theme.md#translate-plain-text)
* [HTML](translate-theme.md#text-blocks-that-contain-html)
* [Liquid](translate-theme.md#text-blocks-that-contain-liquid)

You can translate each piece of text by entering translations into the text fields.

You don't have to translate every field in your theme. Your changes are saved automatically and you can stop at any time. You can access any existing translation if you want to make changes.

If you leave a field without a translation, then the default language for the theme is used.

You can translate plain text directly, but you'll need to take extra care when translating text blocks containing HTML or Liquid.

### Translate plain text

For most of the text on your online store, you don't need to use HTML or Liquid. When you enter a translation of a plain text block, all you have to do is replace the text with its equivalent in the other language.

### Text blocks that contain HTML

If a text block contains HTML, then you'll see pairs of angled brackets ( `<` `>` ) surrounding words or phrases.

You need to understand how the HTML is being used in the block that you're translating. Although you'll need to leave most of the content in the original English, there might be some English words outside of the angled brackets that you'll want to translate.

Text blocks that contain HTML are typically used for the following reasons:

* [creating links to another part of your online store or to a different website](translate-theme.md#translate-html-link-names)
* [adding formatting to text](translate-theme.md#translate-text-styled-with-html)

### Translate HTML link names

An HTML link is surrounded in tags that start with `<a href=` and end with `</a>`.

You must translate only the *name* of the link, and not its other components. The link name is the only part of the link that your customers will see.

```
Continue browsing <a href="/collections/all">here</a>.
```

In this example, you'd replace the words **Continue**, **browsing**, and **here**, with a suitable translation.

Never translate the destination address (also known as the target) in a link. The destination address is where a customer goes when they click the link. It's always shown in quotation marks and points to a specific web address. In the example link, the destination address is `/collections/all`.

### Translate text styled with HTML

HTML is sometimes used to give emphasis or additional styling to words or phrases, or to display symbols. You must translate only the words that are being styled by the HTML, and not the codes or tags themselves. Take a look at the [examples](translate-theme.md#html-styling-examples) to make sure that you understand what to translate and what you should leave unchanged.

#### HTML styling examples

In the following example, the `<strong>` tags are used to display text in bold:

```
<strong>On Sale</strong>
```

In this case, you'd translate only the words **On Sale**.

In the following example, HTML codes `&larr;` and `&rarr;` are used to generate left and right arrow symbols:

```
&larr; Previous Product
```

```
Next Product &rarr;
```

Here, you'd translate only the phrases **Previous Product** and **Next Product**.

In the following example, HTML `<strong>` tags are used to display the file name **collection-sidebar.liquid** in bold.

```
Add a type to your products for this list to build itself. All lists are created
in <strong>collection-sidebar.liquid</strong>
```

The file name here is a [Liquid template file](https://shopify.dev/api/liquid/objects/template). You should translate the file name only if it's necessary to match the name of the file itself. For example, if you have created your own files, then you might need to change the file name in the HTML.

Never translate HTML tags or symbol codes. These are used by your browser, and aren't seen by your customers.

### Text blocks that contain Liquid

Never translate [Liquid](https://shopify.dev/api/liquid) tags, objects, or filters.

Liquid is the templating language that controls the appearance of your website in different contexts. Liquid content is always wrapped in one of the following sets of symbols:

* `{{` and `}}`
* `{%` and `%}`
* `{%-` and `-%}`

For example:

```
Posted on {{ date }}
```

In this example, you would translate only the text around the Liquid, and not `{{ date }}`.

Here's an example of a text field that uses a combination of plain text, HTML, and Liquid:

```
<strong>{{ author }}</strong> on {{ date }}
```

Although this example might look complex, the only part that you'd need to translate is the word **on**.