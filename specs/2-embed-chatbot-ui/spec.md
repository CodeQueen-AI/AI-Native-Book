# Feature Specification: Embed Chatbot UI

**Feature Branch**: `2-embed-chatbot-ui`
**Created**: 2025-12-17
**Status**: Draft
**Input**: User description: "I want the chatbot to be embedded inside my book application, not as a separate page. On the side at the bottom of the book interface, there should be a circular floating button with a logo or emoji inside it. When the user clicks on this circle, the chatbot should open (for example, as a popup or slide-in panel). Please implement the UI behavior, styling, and integration so the chatbot works smoothly within the book layout while continuing to communicate with the existing backend chat API"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Open and Close Chatbot (Priority: P1)

As a user reading the book, I want to be able to open and close the chatbot panel using a floating button, so that I can access the chatbot without leaving the page I am on.

**Why this priority**: This is the core functionality of the feature.

**Independent Test**: The floating button is visible on all book pages. Clicking the button opens the chatbot panel, and clicking it again (or a close button on the panel) closes the panel.

**Acceptance Scenarios**:

1. **Given** a user is on any book page, **When** the page loads, **Then** a circular floating button is visible at the bottom right of the screen.
2. **Given** the chatbot panel is closed, **When** the user clicks the floating button, **Then** the chatbot panel opens.
3. **Given** the chatbot panel is open, **When** the user clicks the floating button (or a close button on the panel), **Then** the chatbot panel closes.

---

### User Story 2 - Interact with Chatbot (Priority: P2)

As a user with the chatbot panel open, I want to be able to ask questions and get answers from the chatbot, so that I can get help with the book content.

**Why this priority**: This is the main purpose of the chatbot.

**Independent Test**: The chatbot panel contains the chatbot UI. The user can type a question, send it, and see the response from the backend.

**Acceptance Scenarios**:

1. **Given** the chatbot panel is open, **When** the user types a question into the input field and clicks "Send", **Then** the question is sent to the backend chat API.
2. **Given** the backend returns a successful response, **When** the frontend receives the response, **Then** the answer and sources are displayed in the chatbot panel.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST display a circular floating button on all book pages.
- **FR-002**: System MUST open a chatbot panel when the floating button is clicked.
- **FR-003**: System MUST close the chatbot panel when the floating button is clicked again, or when a close button on the panel is clicked.
- **FR-004**: The chatbot panel MUST contain the chatbot UI, including an input field, a send button, and a display area for the conversation.
- **FR-005**: The chatbot UI MUST communicate with the existing backend chat API at `http://localhost:8000/chat`.
- **FR-006**: The chatbot panel SHOULD be a slide-in panel from the right side of the screen. [NEEDS CLARIFICATION: What should be the exact behavior of the chatbot opening? A popup, a slide-in panel, or something else?]
- **FR-007**: The floating button SHOULD have a logo or emoji inside it. [NEEDS CLARIFICATION: What logo or emoji should be used for the floating button?]

### Key Entities *(include if feature involves data)*

- **Chatbot Panel**: A UI component that contains the chatbot interface.
- **Floating Button**: A circular button that toggles the visibility of the chatbot panel.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: The floating button is visible on 100% of book pages.
- **SC-002**: The chatbot panel can be opened and closed with a single click.
- **SC-003**: Users can successfully send a message to the chatbot and receive a response within 3 seconds.
- **SC-004**: The chatbot integration does not increase the page load time by more than 10%.
