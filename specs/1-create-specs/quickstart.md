# Quickstart for "Create Specs from `specify.txt`"

This guide explains how to use the `/sp.specify` command with a `specify.txt` file.

## Prerequisites

-   Ensure you have a `specify.txt` file in your project's root directory.

## Step 1: Create `specify.txt`

Create a file named `specify.txt` and add your requirements. For example:

```text
Feature: User Authentication

User Story 1 (P1): As a user, I want to be able to log in with my email and password.
  - Given I am on the login page, When I enter my correct credentials, Then I am redirected to my dashboard.

Functional Requirement FR-001: The system MUST securely store user passwords.

Success Criterion SC-001: Users can log in successfully within 2 seconds.
```

## Step 2: Run the `/sp.specify` command

Invoke the specify command. By default, it will look for `specify.txt` in the current directory and output to `specs/1-create-specs/spec.md`.

```bash
python -m src.commands.specify_command make-specs
```

If `specify.txt` has not changed since the last `spec.md` generation, the command will exit without regenerating. To force regeneration, use the `--force` flag:

```bash
python -m src.commands.specify_command make-specs --force
```

You can also specify an input file or output directory:

```bash
python -m src.commands.specify_command make-specs --input-file my_requirements.txt --output-dir my_specs_folder/
```


## Step 3: Review the generated `spec.md`

The system will generate a `spec.md` file in a new feature directory (e.g., `specs/1-create-specs/spec.md`). Review this file for correctness and address any `[NEEDS CLARIFICATION]` markers.
