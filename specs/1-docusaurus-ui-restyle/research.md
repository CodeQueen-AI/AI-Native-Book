# Research & Decisions for Docusaurus UI Restyle

This document records the technical research and decisions made to resolve ambiguities in the implementation plan.

## 1. Testing Strategy

### Decision
Use **Cypress** for end-to-end (E2E) testing.

### Rationale
The feature is heavily UI-focused, involving visual styling, layout, and animations. E2E tests provide the most value by verifying the final outcome and user flows in a real browser environment. While Jest could be used for unit tests, the components for this feature are expected to have minimal logic, making E2E testing a more efficient and effective use of development time.

### Alternatives Considered
- **Jest with JSDOM**: Good for unit-testing component logic but cannot accurately verify visual aspects like colors, fonts, layout, or animations.
- **Manual Testing**: Prone to human error and not repeatable automatically. It will be used for exploratory testing, but not as the primary validation method.

## 2. Custom Font Integration

### Decision
Import the **Poppins** font from Google Fonts by adding `<link>` tags to the `headTags` array in `docusaurus.config.js`.

### Rationale
This is the standard, documented, and most performant method for loading external fonts in a Docusaurus project. The font is loaded efficiently in the HTML `<head>`, and can then be applied globally and reliably in `src/css/custom.css` by overriding Docusaurus's default CSS variables (e.g., `--ifm-font-family-base`).

### Alternatives Considered
- **CSS `@import`**: Using `@import` inside `custom.css` is a valid method, but it can negatively impact page load performance as the import is processed later than `<link>` tags in the head.

## 3. UI Effects (Glow)

### Decision
Implement the glowing effect using the standard CSS **`box-shadow`** property.

### Rationale
The required "soft glowing / light shine effect" on a rectangular, rounded-corner box is the exact use case for `box-shadow`. It is lightweight, requires no JavaScript or external libraries, is highly performant, and can be easily animated with CSS transitions for hover effects.

### Alternatives Considered
- **`filter: drop-shadow()`**: This CSS property is more appropriate for creating glow effects around non-rectangular shapes (e.g., a transparent PNG icon), not a simple box.
- **JavaScript Libraries**: Using a JS library for this simple effect would add unnecessary bundle size and complexity.

## 4. Icon Library

### Decision
Use the **`react-icons`** library.

### Rationale
`react-icons` is the de-facto standard for including a wide variety of icons in React projects. Its key benefit is tree-shaking, which ensures that only the icons being used are included in the final application bundle. This is highly efficient and keeps the application size minimal.

### Alternatives Considered
- **Manual SVG Imports**: Manually importing SVGs as React components is possible but becomes cumbersome to manage, scale, and style consistently.
- **Full Font Library via CSS (e.g., Font Awesome CSS)**: This approach is less efficient as it often involves loading an entire font file with many unused icons, bloating the application.

## 5. Theming and Layout Customization (Navbar/Footer)

### Decision
Prioritize configuration-based customization in `docusaurus.config.js` for the navbar and footer. Fall back to component **swizzling** (ejecting) only if absolutely necessary.

### Rationale
Docusaurus is designed to be customized via its configuration file first. This is the simplest, safest, and most maintainable approach. Swizzling provides maximum power but creates a maintenance debt, as the ejected component is disconnected from theme updates. Therefore, it should only be used as a last resort if the configuration options are insufficient to meet a specific design requirement (e.g., a highly custom button style that cannot be achieved with CSS alone).
