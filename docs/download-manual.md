Task: Download and Structure GUI User Manuals

1. Input Source
   - The list of entry-point URLs is provided in `urls.txt`.
   - Use these URLs as starting points.
   - You may crawl additional relevant pages as needed to ensure completeness.

2. Scope Limitation (Important)
   - Only download documentation related to the GUI (Graphical User Interface).
   - Skip any documentation related to:
     - APIs
     - SDKs
     - Developer guides
     - CLI tools
     - Integration or backend configuration unless strictly GUI-related.
   - Use judgment to exclude non-GUI technical or developer-focused content.

3. Scope of Work
   - Download the full GUI user manuals starting from each entry point.
   - Determine which linked pages belong to the same manual.
   - Exclude unrelated content such as marketing pages, blog posts, release notes (unless GUI usage), or external resources.

4. Output Format
   - Convert all content into Markdown format. You can feel free to use any library you like.

5. Link Handling
   - Convert all internal links to relative links so the documentation works locally.
   - Ensure inter-page links function correctly within the downloaded structure.
   - External links may remain absolute.

6. Assets (Optional but Preferred)
   - Download images locally if reasonably feasible.
   - Update image references to use relative paths.
   - If downloading images is too complex, it is acceptable to skip.

7. Storage Location
   - Store all processed documentation under:
     `apps/user-manuals/`
   - Follow the folder structure and conventions used in:
     `apps/user-manuals/gitlab`
   - Maintain consistent naming and hierarchy.

8. Quality Requirements
   - Remove scripts, navigation bars, headers, footers, and UI clutter.
   - Keep only meaningful documentation content.
   - Ensure clean, readable Markdown output.
   - Maintain consistent formatting across all manuals.

9. Markdown Formatting Rules

   These rules prevent common scraping artifacts that are difficult to fix after the fact. Every output file must conform to them.

   9.1 One paragraph = one line (no hard wrapping)
   - Each paragraph must be a single unwrapped line, no matter how long.
   - Do NOT hard-wrap text at 80 characters or any other column width.
   - Many source sites and PDF extractors produce 80-char wrapped paragraphs. Libraries like `markdownify` and tools like `PyMuPDF` often preserve the original column wrapping. You must detect and undo this.
   - Bad:
     ```
     The Console Mobile Application provides
     mobile-relevant tasks that are a good companion
     to the full web experience.
     ```
   - Good:
     ```
     The Console Mobile Application provides mobile-relevant tasks that are a good companion to the full web experience.
     ```
   - **Why:** Wrapped lines are valid markdown and render identically, but they make raw files harder to read and harder for LLMs to process. They also create false diffs when content is later edited.

   9.2 List items: one item = one line
   - The content of each list item (bullet or numbered) must be on a single line, including the marker.
   - If a list item has a continuation paragraph (indented under the item), that paragraph must also be a single unwrapped line at the correct indent level.
   - Bad:
     ```
     - [Setting up notification routing for live
       chat](https://example.com/article)
     ```
   - Good:
     ```
     - [Setting up notification routing for live chat](https://example.com/article)
     ```

   9.3 Preserve structural blank lines
   - Separate headings, paragraphs, list blocks, code blocks, and tables with exactly one blank line.
   - Do NOT collapse blank lines between different structural elements.
   - Do NOT insert extra blank lines within a single list or table.

   9.4 No Private Use Area (PUA) characters
   - PDF extraction commonly produces Unicode Private Use Area characters (U+E000–U+F8FF) as bullet points or symbols. These render as invisible or garbled text.
   - Strip all PUA characters. Replace PUA bullet markers with standard markdown list syntax (`- `).
   - Run a check: if any character `c` satisfies `0xE000 <= ord(c) <= 0xF8FF`, it must be removed or replaced.

   9.5 Code blocks must be fenced
   - All code samples must be inside fenced code blocks (``` ``` ```).
   - Never leave code as bare indented text that could be confused with paragraph content.
   - Make sure code block fences are not accidentally joined with surrounding prose.

   9.6 Clean joins between structural elements
   - When converting HTML to markdown, ensure that adjacent HTML elements (e.g., a `</table>` followed by a `<p>`) produce separate markdown blocks separated by blank lines.
   - Bad (table row merged with paragraph):
     ```
     | **Plan** | Enterprise |The admin can configure this setting from...
     ```
   - Good:
     ```
     | **Plan** | Enterprise |

     The admin can configure this setting from...
     ```

   9.7 File header format
   - Every file must begin with:
     ```
     # {Article Title}

     Source: {original-url}

     ---
     ```
   - The `Source:` line preserves provenance. The `---` horizontal rule separates metadata from content.

10. Post-Processing Validation

    After downloading, run these checks on every output file. Fix any failures before considering the task complete.

    10.1 Line-wrap detection
    - Scan for lines that end without sentence-ending punctuation (`.!?:)>`) where the next non-blank line starts with a lowercase letter or a known continuation word (`the`, `a`, `of`, `in`, `to`, `for`, `and`, `or`, `is`, `are`, `with`, `that`, `which`, etc.).
    - Any such occurrence is almost certainly a broken paragraph that should be a single line.
    - Use `scripts/scan_linebreaks.py` to detect these. It reports severity per directory.

    10.2 PUA character scan
    - Scan for any character in the range U+E000–U+F8FF. Zero occurrences is the target.

    10.3 Structural integrity spot-check
    - Open 3–5 files per directory and verify:
      - Headings render correctly (not joined with body text).
      - Tables render correctly (rows not merged with adjacent paragraphs).
      - Code blocks open and close properly.
      - List items are not split across lines.
      - The `Source:` header and `---` separator are present.

    10.4 Automated unwrap (if needed)
    - If line-wrap issues are found, run `scripts/unwrap_paragraphs.py` to fix them.
    - This script joins wrapped paragraph lines while preserving headings, lists, code blocks, tables, frontmatter, and other structural markdown elements.
    - Usage: `python3 scripts/unwrap_paragraphs.py [--dry-run] [directory ...]`
    - Always run with `--dry-run` first to review the scope of changes.

11. Common Pitfalls by Source Type

    11.1 Zendesk Help Center sites (Figma, Superhuman, Clio, Handshake, Zendesk)
    - The JSON API (`/api/v2/help_center/`) returns article body as HTML.
    - `markdownify` tends to produce 80-char wrapped output. Always unwrap after conversion.
    - Indented content within list items (continuation paragraphs) is especially prone to wrapping.

    11.2 Static HTML sites (Stripe, AWS, Kubernetes, Procore)
    - Content extracted with BeautifulSoup + markdownify may preserve the source page's line breaks.
    - Code blocks on these sites are often inline with language-selector tabs. Make sure the selector UI chrome is stripped and only the code remains inside fences.

    11.3 PDF extraction (EPIC)
    - PDF text extraction (e.g., PyMuPDF/fitz) produces the most artifacts:
      - Hard line breaks at column boundaries (every 60–80 chars).
      - PUA characters (U+F0B7 etc.) used as bullet markers.
      - Missing blank lines between sections.
      - Figure captions and body text run together.
    - Always post-process with paragraph joining, PUA removal, and structural formatting fixes.
    - Split large PDFs into per-chapter files.

    11.4 JavaScript-rendered sites (QuickBooks)
    - Requires headless browser (Playwright) to get rendered content.
    - Extra UI elements (tooltips, accordions, modals) may leak into extracted text. Strip aggressively.

    11.5 Google Support (Gmail)
    - SSR HTML with custom structure. Rate-limit at ≥2s delay (Google throttles aggressively).
    - Topic/answer page structure requires following `/mail/topic/{id}` and `/mail/answer/{id}` links.
