# Supported HTML for help center articles

Source: https://support.zendesk.com/hc/en-us/articles/6644509092378-Supported-HTML-for-help-center-articles

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

The
[source code editor](https://support.zendesk.com/hc/en-us/articles/4408824584602)
lets you edit the HTML source of articles and content blocks for the help center. This lets you customize and style help center content in ways that aren't possible using the standard WYSIWYG editor. To keep your help center secure and provide the best end-user experience, Zendesk limits the HTML you can use in articles and content blocks.

The following sections list the HTML elements, attributes, and content supported in articles and content blocks. In addition to the listed attributes, the HTML elements in this section also support the following global attributes:
`aria-*`, `class`, `data-*`,
`dir`, `id`, `lang`,
`tabindex`, `title`

All tags supports the following inline styles in addition to the inline styles listed in on the individual tags:
`aspect-ratio`, `background`,
`background-color`, `background-image`,
`border`, `border-bottom`,
`border-bottom-color`, `border-bottom-style`,
`border-bottom-width`, `border-collapse`,
`border-color`, `border-left`,
`border-left-color`, `border-left-style`,
`border-left-width`, `border-radius`,
`border-right`, `border-right-color`,
`border-right-style`, `border-right-width`,
`border-spacing`, `border-style`,
`border-top`, `border-top-color`,
`border-top-style`, `border-top-width`,
`border-width`, `box-sizing`,
`color`, `display`, `font`,
`font-family`, `font-size`,
`font-style`, `font-variant`,
`font-variant-caps`,
`font-variant-ligatures`, `font-weight`,
`height`, `letter-spacing`,
`line-height`, `max-height`,
`max-width`, `min-height`,
`min-width`, `orphans`,
`outline`, `padding`,
`padding-bottom`, `padding-left`,
`padding-right`, `padding-top`,
`text-align`, `text-decoration`,
`text-decoration-color`,
`text-decoration-line`,
`text-decoration-style`, `text-indent`,
`text-transform`, `vertical-align`,
`white-space`, `widows`,
`width`, `word-spacing`

In most cases, Zendesk recommends using CSS classes instead of inline styles to style help center content. See [Styling HTML in help articles](https://support.zendesk.com/hc/en-us/articles/4408824584602#topic_d2c_x4x_kxb).

## a

**Attributes**: `href`, `name`,
`rel`, `target`, `title`

**Allowed protocols for href**: `ftp`,
`http`, `https`, `mailto`,
`sftp`, `sms`, `tel`

**Allowed inline styles**: only global styles

**Content**: `@text`, `abbr`,
`address`, `aside`, `audio`,
`bdi`, `bdo`, `blockquote`,
`br`, `cite`, `code`,
`data`, `del`, `details`,
`dfn`, `div`, `dl`,
`em`, `figure`, `footer`,
`h1`, `h2`, `h3`,
`h4`, `h5`, `h6`,
`header`, `hr`, `img`,
`ins`, `kbd`, `mark`,
`noscript`, `ol`, `p`,
`pre`, `q`, `ruby`,
`s`, `samp`, `section`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`table`, `time`, `ul`,
`var`, `video`

## abbr

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## address

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## article

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## aside

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## audio

**Attributes**: `autoplay`, `controls`,
`disableremoteplayback`, `loop`,
`muted`, `preload`, `src`

**Allowed protocols for src**: `blob`,
`data`, `http`, `https`

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `bdi`, `bdo`,
`br`, `cite`, `code`,
`data`, `del`, `dfn`,
`em`, `iframe`, `img`,
`ins`, `kbd`, `mark`,
`noscript`, `q`, `ruby`,
`s`, `samp`, `small`,
`source`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `track`, `var`

## bdi

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## bdo

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## blockquote

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## br

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: void element

## caption

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## cite

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## code

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## col

**Attributes**: `span`

**Allowed inline styles**: only global styles

**Content**: void element

## colgroup

**Attributes**: `span`

**Allowed inline styles**: only global styles

**Content**: `col`

## data

**Attributes**: `value`

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## dd

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## del

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## details

**Attributes**: `open`

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## dfn

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`em`, `iframe`, `img`,
`ins`, `kbd`, `mark`,
`noscript`, `q`, `ruby`,
`s`, `samp`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `time`,
`var`, `video`

## div

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## dl

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `dd`, `dt`

## dt

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## em

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## figcaption

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## figure

**Attributes**: only global attributes

**Allowed inline styles**: `float`

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figcaption`,
`figure`, `footer`, `h1`,
`h2`, `h3`, `h4`,
`h5`, `h6`, `header`,
`hr`, `iframe`, `img`,
`ins`, `kbd`, `mark`,
`noscript`, `ol`, `p`,
`pre`, `q`, `ruby`,
`s`, `samp`, `section`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`table`, `time`, `ul`,
`var`, `video`

## footer

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`h1`, `h2`, `h3`,
`h4`, `h5`, `h6`,
`hr`, `iframe`, `img`,
`ins`, `kbd`, `mark`,
`noscript`, `ol`, `p`,
`pre`, `q`, `ruby`,
`s`, `samp`, `section`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`table`, `time`, `ul`,
`var`, `video`

## h1

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## h2

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## h3

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## h4

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## h5

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## h6

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## header

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`h1`, `h2`, `h3`,
`h4`, `h5`, `h6`,
`hr`, `iframe`, `img`,
`ins`, `kbd`, `mark`,
`noscript`, `ol`, `p`,
`pre`, `q`, `ruby`,
`s`, `samp`, `section`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`table`, `time`, `ul`,
`var`, `video`

## hr

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: void element

## iframe

**Attributes**: `allow`,
`allowfullscreen`, `frameborder`,
`height`, `mozallowfullscreen`,
`msallowfullscreen`, `name`,
`oallowfullscreen`, `src`,
`webkitallowfullscreen`, `width`

**Allowed protocols for src**: `blob`,
`data`, `http`, `https`

**Allowed domains for embeds**:
`https://content.jwplatform.com/`,
`https://fast.wistia.com/`,
`https://play.vidyard.com/`,
`https://player.vimeo.com/`,
`https://players.brightcove.net/`,
`https://web.microsoftstream.com/`,
`https://www.loom.com/`,
`https://www.microsoft.com/`,
`https://www.youtube-nocookie.com/`,
`https://www.youtube.com/`

**Allowed inline styles**: only global styles

**Content**: void element

## img

**Attributes**: `alt`, `height`,
`name`, `src`, `width`

**Allowed protocols for src**: `blob`,
`data`, `http`, `https`

**Allowed inline styles**: only global styles

**Content**: void element

## ins

**Attributes**: `cite`, `datetime`

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## kbd

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## li

**Attributes**: only global attributes

**Allowed inline styles**: `list-style`,
`list-style-image`, `list-style-position`,
`list-style-type`

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## mark

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## nav

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## noscript

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `q`, `ruby`,
`s`, `samp`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `time`,
`var`, `video`

## ol

**Attributes**: `reversed`, `start`,
`type`

**Allowed inline styles**: `list-style`,
`list-style-image`, `list-style-position`,
`list-style-type`

**Content**: `li`

## p

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## pre

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## q

**Attributes**: `cite`

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## rp

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`

## rt

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## ruby

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`rp`, `rt`, `ruby`,
`s`, `samp`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `time`,
`var`, `video`

## s

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## samp

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## section

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## small

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## source

**Attributes**: `src`, `type`

**Allowed protocols for src**: `blob`,
`data`, `http`, `https`

**Allowed inline styles**: only global styles

**Content**: void element

## span

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## strong

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## sub

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## summary

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `h1`,
`h2`, `h3`, `h4`,
`h5`, `h6`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## sup

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## table

**Attributes**: `border`, `cellpadding`,
`cellspacing`

**Allowed inline styles**: `margin`,
`margin-bottom`, `margin-left`,
`margin-right`, `margin-top`

**Content**: `caption`, `colgroup`,
`tbody`, `tfoot`, `thead`,
`tr`

## tbody

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `tr`

## td

**Attributes**: `colspan`, `rowspan`

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## tfoot

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `tr`

## th

**Attributes**: `colspan`, `rowspan`,
`scope`

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `address`, `aside`,
`audio`, `bdi`, `bdo`,
`blockquote`, `br`, `cite`,
`code`, `data`, `del`,
`details`, `dfn`, `div`,
`dl`, `em`, `figure`,
`footer`, `h1`, `h2`,
`h3`, `h4`, `h5`,
`h6`, `header`, `hr`,
`iframe`, `img`, `ins`,
`kbd`, `mark`, `noscript`,
`ol`, `p`, `pre`,
`q`, `ruby`, `s`,
`samp`, `section`, `small`,
`span`, `strong`, `sub`,
`summary`, `sup`, `table`,
`time`, `ul`, `var`,
`video`

## thead

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `tr`

## time

**Attributes**: `datetime`

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## tr

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `td`, `th`

## track

**Attributes**: `default`, `kind`,
`label`, `src`, `srclang`

**Allowed protocols for src**: `blob`,
`data`, `http`, `https`

**Allowed inline styles**: only global styles

**Content**: void element

## ul

**Attributes**: only global attributes

**Allowed inline styles**: `list-style`,
`list-style-image`, `list-style-position`,
`list-style-type`

**Content**: `li`

## var

**Attributes**: only global attributes

**Allowed inline styles**: only global styles

**Content**: `@text`, `a`,
`abbr`, `audio`, `bdi`,
`bdo`, `br`, `cite`,
`code`, `data`, `del`,
`dfn`, `em`, `iframe`,
`img`, `ins`, `kbd`,
`mark`, `noscript`, `q`,
`ruby`, `s`, `samp`,
`small`, `span`, `strong`,
`sub`, `summary`, `sup`,
`time`, `var`, `video`

## video

**Attributes**: `controls`, `height`,
`poster`, `preload`, `src`,
`width`

**Allowed protocols for src**: `blob`,
`data`, `http`, `https`

**Allowed inline styles**: only global styles

**Content**: `source`, `track`