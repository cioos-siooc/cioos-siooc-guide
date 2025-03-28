# CIOOS Data Management Guide

The [CIOOS Data Management Guide](http://10.0.2.5:8880/) is an [MkDocs](https://www.mkdocs.org/) project that presents the recommended best practices for managing data within the Canadian Integrated Ocean Observing System (CIOOS). This guide is designed to help data managers adopt FAIR (Findable, Accessible, Interoperable, and Reusable) and CARE (Collective Benefit, Authority to Control, Responsibility, and Ethics) principles in their workflows.

## Features

- Comprehensive documentation on data management best practices.
- Multilingual support (English and French).
- Visual assets and guides to assist in implementation.

## Development

### Live Page

From the actual reference page, you like to work on, click on the Edit link button near the top corner. <svg xmlns="http://www.w3.org/2000/svg" height=20 viewBox="0 0 24 24"><path d="M10 20H6V4h7v5h5v3.1l2-2V8l-6-6H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h4zm10.2-7c.1 0 .3.1.4.2l1.3 1.3c.2.2.2.6 0 .8l-1 1-2.1-2.1 1-1c.1-.1.2-.2.4-.2m0 3.9L14.1 23H12v-2.1l6.1-6.1z"></path></svg>

This will send you to the repository associated document. Make the desired edits, commit changes to the branch right away.

The changes should be reflected on the live page shortly.

### Local Development

To run and develop the project locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/cioos-data-management-guide.git
   cd cioos-data-management-guide
   ```

2. **Install the package manager uv**
    See [UV documentation](https://docs.astral.sh/uv/getting-started/installation/) on how to install it within the different environments:

3. **Create local environment with UV**
    `uv venv`

4. **Run mkdocs in development mode**
    `uv run mkdocs server`

5. **Apply changes**

6. **Commit changes and push**

For further documentation, refer to the [`mkdocs-material` theme documentation](https://squidfunk.github.io/mkdocs-material/).

We are also using some extensions:
- Multilanguage: https://ultrabug.github.io/mkdocs-static-i18n/getting-started/quick-start/
- 

## Continuous Integration

Live web site is made available at: http://10.0.2.5:8880/
