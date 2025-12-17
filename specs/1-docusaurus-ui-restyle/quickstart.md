# Quickstart for Docusaurus UI Restyle

This guide provides the essential steps for a developer to set up and run the Docusaurus project to work on the UI customization feature.

## Prerequisites

- Node.js (LTS version recommended)
- npm or yarn

## Setup & Execution

1.  **Navigate to the book's source directory:**
    ```bash
    cd book_source
    ```

2.  **Install Dependencies:**
    Install the project dependencies, including Docusaurus and React.
    ```bash
    npm install
    ```
    *Note: This will also install `react-icons` once it is added to `package.json`.*

3.  **Run the Development Server:**
    This command starts the local development server and opens up a browser window.
    ```bash
    npm run start
    ```

4.  **View the Project:**
    The site will be running at `http://localhost:3000`. The server supports hot-reloading, so changes to CSS and React components will be reflected live in the browser.

## Key Files for Development

- **Global Styles**: `book_source/src/css/custom.css`
- **Homepage Component**: `book_source/src/pages/index.js`
- **Site Configuration (Navbar, Footer)**: `book_source/docusaurus.config.js`
- **Component Overrides (Swizzling)**: `book_source/src/theme/`
