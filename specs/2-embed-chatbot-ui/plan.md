# Implementation Plan: Embed Chatbot UI

**Branch**: `2-embed-chatbot-ui` | **Date**: 2025-12-17 | **Spec**: [specs/2-embed-chatbot-ui/spec.md]
**Input**: Feature specification from `specs/2-embed-chatbot-ui/spec.md`

## Summary

This feature will embed the existing chatbot into the Docusaurus book application as a floating UI element. The chatbot will be triggered by a circular floating button at the bottom right of the screen. When clicked, the chatbot will appear in a slide-in panel from the right. The implementation will involve integrating the existing React-based chatbot components into the Docusaurus application and styling them to match the book's look and feel.

## Technical Context

**Language/Version**: TypeScript/JavaScript (Docusaurus)
**Primary Dependencies**: React, Docusaurus
**Storage**: N/A
**Testing**: Jest, React Testing Library
**Target Platform**: Web
**Project Type**: Web application (Docusaurus)
**Performance Goals**: The chatbot should load and respond without any noticeable delay.
**Constraints**: The chatbot must not disrupt the user's reading experience.
**Scale/Scope**: The chatbot will be available on all pages of the Docusaurus book.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Spec-Driven Development**: Does a `spec.md` exist and is it referenced?
- [X] **Architectural Planning**: Is this `plan.md` being created to define the technical approach?
- [X] **Task-Based Execution**: Will a `tasks.md` be created from this plan?
- [X] **Record Keeping**: Will PHRs and ADRs be created as needed?
- [X] **Test-Driven Development**: Are test creation tasks included if applicable?

## Project Structure

### Documentation (this feature)

```text
specs/2-embed-chatbot-ui/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
book_source/
└── src/
    ├── components/
    │   ├── ChatbotWidget.css
    │   └── ChatbotWidget.tsx
    ├── hooks/
    │   └── useChatbot.ts
    ├── services/
    │   └── ChatbotApiService.ts
    ├── theme/
    │   └── DocItem/
    │       └── Content/
    │           └── index.js
    └── types.ts
```

**Structure Decision**: The existing Docusaurus structure will be used. The chatbot components will be added to the `book_source/src` directory.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| | | |
