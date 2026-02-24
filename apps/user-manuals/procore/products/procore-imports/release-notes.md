# Procore Imports - Release Notes - Procore

Source: https://support.procore.com/products/procore-imports/release-notes

---

Below are the notable changes to Procore Imports.

## Recent Changes

#### Procore Imports 1.6.3 (02/05/2026)

- Enhanced ERP Integration Validation: The system now checks ERP status to accurately detect integrated companies before importing cost codes.

#### Procore Imports 1.6.2 (12/24/2025)

- Added support for three new languages: Portuguese (Portugal), Chinese Traditional (Taiwan), and Norwegian Bokmål.
- Fixed connection issue to Procore for Government.

#### Procore Imports 1.6.1 (11/12/2025)

- Tiered Segments: Fixed an issue where tiered segment imports would fail when parent segments already existed in the system.
- Submittals: Improved submittal import validation to prevent upload failures.

#### Procore Imports 1.6.0 (10/08/2025)

- Imports Template: Spec Section Area has been added to Import Template.
- Procore Imports is now compatible with Procore for Government.

#### Procore Imports 1.5.9 (08/11/2025)

- **Configurable fieldsets support** – Updated Procore Imports API calls to honor configurable fieldset settings, ensuring imported data respects custom configurations.
- Resolved a problem where the auto-update process was not working as expected.
- Updated translations for the latest microservice modules.

#### Procore Imports 1.5.7 (05/15/2025)

- Enhanced translations for better clarity and consistency.

#### Procore Imports 1.5.6 (04/03/2025)

- Fixed an issue that blocked the import of vendors whose names contained trailing spaces
- Enhanced various translations for better clarity and consistency

#### Procore Imports 1.5.5 (02/24/2025)

- Resolved an issue preventing the import of additional items into a custom segment when the parent item already exists
- Implemented a restriction to block special characters in email addresses for users and vendors
- Enhanced various translations for better clarity and consistency

#### Procore Imports 1.5.4 (11/14/2024)

- Add translations for Polish, French, Chinese and Japanese
- Katakana transliterations are added to Kanji characters found in Excel sheet when importing

#### Procore Imports 1.5.3 (07/16/2024)

- Fix an issue with Japanese translation

#### Procore Imports 1.5.2 (05/03/2024)

- Fixed a performance issue with project dropdown when a company has many projects

#### Procore Imports 1.5.1 (04/16/2024)

- Fix an issue with Japanese translation
- Fix an issue with Portuguese translation
- Performance improvement

#### Procore Imports 1.5.0 (12/18/2023)

- Support for Japanese language
- Fixed issue related to Schedule tool

#### Procore Imports 1.4.9 (09/27/2023)

- New bobcat package version, 2.2.11
- TLS 1.2
- Bug fixes and performance improvements

#### Procore Imports 1.4.8 (01/31/2023)

- Possibility to upload Schedule import file to the Documents tool in the Schedules folder
- Fix Vendors import with certain Companies

#### Procore Imports 1.4.7 (01/25/2023)

- Sign Imports tool by new trusted certificate
- Improve translations