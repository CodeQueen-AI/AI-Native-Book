# Actionable Tasks: Embed Chatbot UI

**Feature**: Embed Chatbot UI

This document outlines the actionable tasks required to implement the "Embed Chatbot UI" feature, based on the provided design artifacts.

## Phase 1: Setup

- [X] T001 Create a new component `FloatingChatbotButton` in `book_source/src/components/FloatingChatbotButton.tsx`.
- [X] T002 Create the corresponding CSS file `book_source/src/components/FloatingChatbotButton.css`.
- [X] T003 Create a new component `ChatbotPanel` in `book_source/src/components/ChatbotPanel.tsx`.
- [X] T004 Create the corresponding CSS file `book_source/src/components/ChatbotPanel.css`.

## Phase 2: Foundational Tasks

- [X] T005 [P] Implement the `FloatingChatbotButton` component in `book_source/src/components/FloatingChatbotButton.tsx`. This component should render a circular button with a chat bubble icon.
- [X] T006 [P] Style the `FloatingChatbotButton` component in `book_source/src/components/FloatingChatbotButton.css` to be a circular floating button at the bottom right of the screen.
- [X] T007 [P] Implement the `ChatbotPanel` component in `book_source/src/components/ChatbotPanel.tsx`. This component will contain the `ChatbotWidget` and will be hidden by default.
- [X] T008 [P] Style the `ChatbotPanel` component in `book_source/src/components/ChatbotPanel.css` to be a slide-in panel from the right.

## Phase 3: User Story 1 - Open and Close Chatbot

**Goal**: As a user reading the book, I want to be able to open and close the chatbot panel using a floating button, so that I can access the chatbot without leaving the page I am on.

**Independent Test**: The floating button is visible on all book pages. Clicking the button opens the chatbot panel, and clicking it again (or a close button on the panel) closes the panel.

- [X] T009 [US1] Create a new React context to manage the state of the chatbot panel (open/closed) in `book_source/src/context/ChatbotUIContext.tsx`.
- [X] T010 [US1] Wrap the root component of the Docusaurus application with the `ChatbotUIProvider` in `book_source/src/theme/Root.js`.
- [X] T011 [US1] Implement the logic in `FloatingChatbotButton.tsx` to toggle the state of the chatbot panel when the button is clicked.
- [X] T012 [US1] Implement the logic in `ChatbotPanel.tsx` to show or hide the panel based on the state from the `ChatbotUIContext`.
- [X] T013 [US1] Add a close button to the `ChatbotPanel` component that will close the panel when clicked.

## Phase 4: User Story 2 - Interact with Chatbot

**Goal**: As a user with the chatbot panel open, I want to be able to ask questions and get answers from the chatbot, so that I can get help with the book content.

**Independent Test**: The chatbot panel contains the chatbot UI. The user can type a question, send it, and see the response from the backend.

- [X] T014 [US2] Integrate the `ChatbotWidget` component into the `ChatbotPanel` component in `book_source/src/components/ChatbotPanel.tsx`.
- [X] T015 [US2] Pass the `ChatbotApiService` to the `ChatbotWidget` component.

## Phase 5: Polish & Cross-Cutting Concerns

- [X] T016 Ensure the chatbot panel is responsive and works well on different screen sizes.
- [X] T017 Add accessibility features to the chatbot components.
- [X] T018 Write unit tests for the new components.

## Dependencies

- User Story 2 is dependent on User Story 1.

## Parallel Execution

- Tasks marked with `[P]` can be executed in parallel.

## Implementation Strategy

The implementation will follow an MVP-first approach. User Story 1 will be implemented first, followed by User Story 2. This will ensure that the core functionality of opening and closing the chatbot is working before adding the chatbot interaction.
