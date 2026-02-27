Your task is specified in `./docs/web-app-design-guide.md` and `./docs/web-app-data-guide.md`. The corresponding documentation for this environment is located at `./{docs_source}`. This documentation can be a folder with multiple files, or it can be an entry point that links together multiple files in the folder.

When developing the environment, make sure you also follow `./docs/environment-protocol.md`.

You can use `/frontend-design` skill which has been installed when necessary.

After generating the app, write `APP_DESCRIPTION.md` in the app directory with:
- Summary of what the app does and its main sections/pages
- Complete list of implemented features and UI interactions
- Data model: all entities, their fields, and relationships
- Navigation structure and how to reach each section
- Available form controls, dropdowns, toggles, and their options
- Seed data summary: what entities exist, their names/values
This file will be used by a separate task-generation step.