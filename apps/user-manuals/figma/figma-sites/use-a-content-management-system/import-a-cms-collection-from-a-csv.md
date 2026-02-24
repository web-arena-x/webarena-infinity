# Import a CMS collection from a CSV

Source: https://help.figma.com/hc/en-us/articles/35691883305879-Import-a-CMS-collection-from-a-CSV

---

Who can use this feature

Available on all plans

Requires edit access to the site file

Import your existing content into the Figma Sites CMS by uploading a comma-separated values (CSV) file to create a new collection. There are two steps to this process:

1. [Prepare your CSV for import](#h_01KAD1GYSW1C0HXH4JAET13S1H)
2. [Import your CSV and map the fields](#h_01KAD1GYSWWPMM9T3PSNZGES4C)

## 1. Prepare your CSV for import

Each column in your CSV becomes a field, and each row becomes an item. Use this checklist to make sure your CSV file imports successfully:

- Export the file as **CSV (UTF‑8)**.
- Include a single header row with no empty or duplicate column names.
- Two of these columns must be called **Title** and **Slug**.
- Make sure every value in the **Slug** column is unique. This could be a numeric ID like`12345` or a version of the title like `welcome-post`.
- Images must be available in **JPEG**, **GIF** or **PNG** formats from publicly accessible HTTPS URLs. Make sure you link directly to the image file, not to a webpage that contains it.
- The CSV file must under **2 MB**.
- There is a maximum of **200 items** (rows of content). Each collection in CMS is currently limited to 200 items while in beta.
- Use the [supported fields](#h_01KAD1GYSWRG7V7SEZF15VNJR1) guide below to make sure your content is correctly formatted for import.

**Tip:** You don’t need to import every column in your CSV. Only the columns you choose to import will be created in the CMS collection.

### Supported fields

Content in your CSV should match these field types:

| CMS field types | How to format the CSV column | Example |
| --- | --- | --- |
| **Title** (required) | Plain text | `Welcome post` |
| **Slug** (required) | Lowercase letters, numbers, and hyphens only; no spaces | `welcome-post` |
| **Plain text** | Plain text | `Landing page` |
| **Rich text** | Plain text, HTML, or Markdown | `<p>Welcome to <strong>Sites</strong></p>` |
| **Link** | Full URL beginning with `https://` | `https://example.com` |
| **Image** | Public, direct URL to an image file; supports **JPEG**, **PNG**, and **GIF** formats | `https://images.example.com/hero.jpg` |
| **Date** | Any [ISO-8601 date](https://www.w3.org/TR/NOTE-datetime) that includes a year, month, and day; date won't be valid if it doesn't have all three | `2024-01-31` or `2024-01-31T14:42:00Z` |

### Example data to test

Below is a mock dataset you can use to test importing.

| Title | Slug | Artist | ID | Album description | Publish date |
| --- | --- | --- | --- | --- | --- |
| Sgt. Pepper's Lonely Hearts Club Band | sgt-peppers-lonely-hearts-club-band | The Beatles | 1001 | <p><strong>Landmark pop album</strong> blending rock, psychedelia, and studio experimentation.</p> | 1967-06-01 |
| Pet Sounds | pet-sounds | The Beach Boys | 1002 | <p><em>Orchestral pop masterpiece</em> whose harmonies and production redefined studio music.</p> | 1966-05-16 |
| Kind of Blue | kind-of-blue | Miles Davis | 1003 | <p>Modal jazz cornerstone celebrated for <strong>spacious improvisation</strong> and tone.</p> | 1959-08-17 |
| Nevermind | nevermind | Nirvana | 1004 | <p><strong>Grunge breakthrough</strong> that brought alternative rock to the mainstream.</p> | 1991-09-24 |
| Abbey Road | abbey-road | The Beatles | 1005 | <p>Polished Beatles classic famous for its <em>side-two medley</em> and iconic cover.</p> | 1969-09-26 |

[Download the CSV file](https://help.figma.com/hc/article_attachments/36433956575255)

## 2. Import your CSV and map the fields

![CSV import window showing field mapping options for sample data set, including Title, Slug, Artist, ID, Album description, and Publish date.](https://help.figma.com/hc/article_attachments/36433993698455)

Follow these steps to upload your CSV, map the fields, troubleshoot issues, and create your new collection. A collection can currently have a maximum of **100 fields**.

1. From a Figma Sites file, click  **CMS** in the left navigation bar.
2. Click  **Add collection** and choose **Import CSV**.
3. Click **Upload from computer** and select your CSV file.
4. **Map columns to fields.** For each column, choose a field type from the dropdown. You can rename fields as needed.
5. Click **Import**. Your collection and items are added to the CMS.

**Note:** If your images aren’t showing up after import, we recommend double-checking they are mapped to an **Image** field rather than a **Link** field.

**Tip:** You can adjust the schema and data after importing. For example, for the **Album** collection, we could consider adding a cover image using a new **Image** field.

## Troubleshooting

Quick fixes for the most common problems:

| **Issue** | **How to fix** |
| --- | --- |
| **Parsing or encoding errors** | Re-export as **CSV (UTF-8)** and remove non-printing characters or smart quotes. |
| **Missing header row** | Re-export the file and include a single header row. |
| **Wrong file type** | Upload a `.csv` file, not `.xlsx` or other file type |
| **Data mismatch** | Change the field type from the column dropdown or fix the values in your CSV (e.g., non-date strings in a **Date** column). |
| **Image not appearing** | Confirm the image URL is public and references the actual image file. Replace the URL or upload the image directly to the item after import. |
| **Invalid URLs** | Ensure **Link** and **Image** columns contain valid, publicly accessible `https://` URLs. |
| **Duplicate slugs** | **Slug** values must be unique. Edit the CSV to de-duplicate, then try again. |
| **Dates import incorrectly** | Use ISO 8601 (`YYYY-MM-DD`) or a full timestamp (`YYYY-MM-DDThh:mm:ssZ`). |
| **Missing Title or Slug field** | Make sure your CSV contains two columns named **Title** and **Slug**. |