# Tasks: Docusaurus UI Restyle for Robotics Book

**Input**: Design documents from `/specs/1-docusaurus-ui-restyle/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

---

## Phase 1: Setup

**Purpose**: Install new dependencies required for the feature.

- [x] T001 Install `react-icons` dependency in `book_source/package.json`
- [x] T002 [P] Install `cypress` as a dev dependency in `book_source/package.json`
- [x] T003 [P] Configure Cypress by creating `cypress.config.js` in the `book_source/` directory.
- [x] T004 [P] Add a `cy:run` command to the `scripts` in `book_source/package.json` for running e2e tests.

---

## Phase 2: Foundational Theming (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T005 Add Poppins font `<link>` tags to the `headTags` array in `book_source/docusaurus.config.js`
- [x] T006 [P] In `book_source/src/css/custom.css`, define CSS variables for the color palette: primary accent (#FF0066), black background, and white text.
- [x] T007 [P] In `book_source/src/css/custom.css`, set the global background to black and default text color to white for the `:root` or `html, body` elements.
- [x] T008 [P] In `book_source/src/css/custom.css`, apply the Poppins font globally by setting `--ifm-font-family-base` and `--ifm-heading-font-family`.
- [x] T009 In `book_source/src/css/custom.css`, create a reusable CSS class for the consistent rectangular button style (background, border, text color, no rounded corners).
- [x] T010 In `book_source/src/css/custom.css`, add the hover effect (background/text color swap) to the reusable button class.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Homepage (Priority: P1) 🎯 MVP

**Goal**: Create a visually striking, futuristic homepage that engages users and provides a clear path to the book's content.

**Independent Test**: Load the root URL of the development server. The new homepage should appear with all specified sections and styles. Clicking the "Start Learning" or "Start Reading" button should navigate to the book's introductory chapter.

### Implementation for User Story 1

- [x] T011 [US1] In `book_source/src/pages/index.js`, clear the default content and create the basic structure for the new homepage with sections for Hero, About, Stats, Modules, and CTA.
- [x] T012 [P] [US1] In `book_source/src/pages/index.js`, implement the Hero Center Box component with the specified text: "The Future of Robotics • ROS 2 & Isaac Sim • 2025 Edition".
- [x] T013 [P] [US1] In `book_source/src/css/custom.css`, add styling for the Hero Center Box, including rounded corners, the accent text color, and the `box-shadow` glow effect.
- [x] T014 [P] [US1] In `book_source/src/pages/index.js`, implement the main centered heading with "The Future of" on one line and "Physical AI & Humanoid Robotics" on the second line.
- [x] T015 [P] [US1] In `book_source/src/css/custom.css`, apply the correct white and accent colors to the parts of the main heading.
- [x] T016 [P] [US1] In `book_source/src/pages/index.js`, add the two-line intro paragraph below the main heading.
- [x] T017 [P] [US1] In `book_source/src/pages/index.js`, add the primary "Start Learning" button and ensure it navigates to the book's intro page.
- [x] T018 [P] [US1] In `book_source/src/pages/index.js`, implement the two-column "About the Course" section with a heading, paragraph, and 3 feature boxes using icons from `react-icons`.
- [x] T019 [P] [US1] In `book_source/src/css/custom.css`, style the "About the Course" section, including the feature boxes and accent-colored icons.
- [x] T020 [P] [US1] In `book_source/src/pages/index.js`, implement the "Stats" section with 4 stat blocks (e.g., "04 Modules").
- [x] T021 [P] [US1] In `book_source/src/css/custom.css`, style the "Stats" section, applying accent color to numbers and white to labels.
- [x] T022 [P] [US1] In `book_source/src/pages/index.js`, implement the "Modules & Features" grid with 6 boxes, each containing an icon, heading, and description.
- [x] T023 [P] [US1] In `book_source/src/css/custom.css`, style the "Modules & Features" grid boxes, including the subtle glow/border hover effect.
- [x] T024 [P] [US1] In `book_source/src/pages/index.js`, implement the final centered call-to-action text and the "Start Reading" button.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Consistent Theming (Priority: P2)

**Goal**: Ensure the entire site, including the header, footer, and all book pages, has a consistent, clean, and futuristic dark theme.

**Independent Test**: Navigate to any book chapter. The header and footer should be correctly styled, and all text and colors should match the new theme.

### Implementation for User Story 2

- [x] T025 [US2] In `book_source/docusaurus.config.js`, modify the `themeConfig.navbar` object to add a robot icon 🤖 and the "Get Started" button on the right.
- [x] T026 [US2] In `book_source/docusaurus.config.js`, ensure the "Get Started" button in the navbar navigates to the book's intro page.
- [x] T027 [US2] In `book_source/src/css/custom.css`, apply the reusable button class to the navbar's "Get Started" button if possible, or add custom styles to match.
- [x] T028 [P] [US2] In `book_source/docusaurus.config.js`, modify the `themeConfig.footer` object to have a minimal layout, the course name, current year, and a futuristic tagline.
- [x] T029 [P] [US2] In `book_source/src/css/custom.css`, style the footer to ensure it has a black background, white text, and uses the accent color as specified.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently and cohesively.

---

## Phase 5: Polish & Testing

**Purpose**: Ensure high quality, handle edge cases, and verify all requirements are met.

- [x] T030 [P] Review all pages on multiple screen sizes (desktop, tablet, mobile) and add responsive styles to `book_source/src/css/custom.css` to fix layout issues.
- [x] T031 [P] Verify that all buttons ("Get Started", "Start Learning", "Start Reading") are visually identical and have the same hover effect.
- [x] T032 [P] Create a Cypress test file in `book_source/cypress/e2e/homepage.cy.js` to verify the homepage loads and the main CTA button works.
- [x] T033 [P] Create a Cypress test file in `book_source/cypress/e2e/theme.cy.js` to verify that navigating to a doc page shows the correct font, colors, and custom header/footer.
- [x] T034 Run all Cypress tests via `npm run cy:run` and ensure they pass.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion. BLOCKS all user stories.
- **User Stories (Phase 3 & 4)**: Depend on Foundational phase completion.
- **Polish & Testing (Phase 5)**: Depends on all user stories being complete.

### User Story Dependencies

- **User Story 1 (Homepage)**: Can start after Foundational (Phase 2).
- **User Story 2 (Consistent Theming)**: Can start after Foundational (Phase 2).

### Parallel Opportunities

- Once the Foundational phase is complete, work on User Story 1 (Homepage) and User Story 2 (Consistent Theming) can proceed in parallel.
- Many styling tasks within a phase are marked with [P] and can be worked on in parallel, as they primarily affect the same CSS file.
- All testing tasks in the final phase can be run in parallel.
