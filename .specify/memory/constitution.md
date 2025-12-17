<!--
- Version change: 0.0.0 -> 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] -> I. Spec-Driven Development
  - [PRINCIPLE_2_NAME] -> II. Architectural Planning
  - [PRINCIPLE_3_NAME] -> III. Task-Based Execution
  - [PRINCIPLE_4_NAME] -> IV. Record Keeping
  - [PRINCIPLE_5_NAME] -> V. Test-Driven Development
- Added sections: None
- Removed sections:
  - [PRINCIPLE_6_NAME]
  - [SECTION_2_NAME]
  - [SECTION_3_NAME]
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
- Follow-up TODOs: None
-->
# Gemini CLI Book Constitution

## Core Principles

### I. Spec-Driven Development
All features must begin with a clear specification (`spec.md`) outlining user stories, requirements, and success criteria. This ensures clarity and alignment before implementation.

### II. Architectural Planning
Significant features require a `plan.md` that defines the technical approach, dependencies, and project structure. Key architectural decisions must be justified.

### III. Task-Based Execution
Work is broken down into granular, testable tasks within `tasks.md`. This enables parallel work, clear progress tracking, and incremental implementation.

### IV. Record Keeping
Every user prompt and agent response is recorded in a Prompt History Record (PHR). Significant architectural choices are documented in Architectural Decision Records (ADRs).

### V. Test-Driven Development
Where applicable, tests should be written before implementation, following a Red-Green-Refactor cycle to ensure correctness and maintainability.

## Governance

This Constitution is the single source of truth for development standards. All development activities, reviews, and automated processes MUST adhere to these principles. Amendments require a documented proposal, review, and an update to this document, including a version increment.

**Version**: 1.0.0 | **Ratified**: 2025-12-15 | **Last Amended**: 2025-12-15