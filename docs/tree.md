## How to Use the `tree` Command in Lazykit

This document explains how to use the `tree` command in Lazykit to visualize your project's directory structure, with options for detailed context and exclusions.

### Command Overview

The `lazykit tree` command provides a structured view of your project, similar to the `tree` utility, but with enhanced capabilities to extract and display project-specific metadata and summaries.

### Usage

```bash
lazykit tree [OPTIONS]
```

### Options

*   `-c, --context <DIR>`:
    Specifies the root directory to scan.
    **Default:** `.` (current directory).

*   `-x, --exclude-dir <DIR> [<DIR>...]`:
    One or more additional directory names to exclude from the tree. These are applied in addition to the default exclusions.

*   `-X, --exclude-file <FILE> [<FILE>...]`:
    One or more additional file names to exclude from the tree. These are applied in addition to the default exclusions.

*   `-n, --no-defaults`:
    Disables the default set of built-in exclusions. When this flag is present, directories like `.git` and `__pycache__` will be included in the output unless they are manually excluded with `-x`.
    **Default Exclusions (hidden by default):**
    *   **Directories:** `.git`, `__pycache__`, `.venv`, `node_modules`, `.mypy_cache`, `dist`, `build`
    *   **Files:** `.DS_Store`

*   `-l, --long`:
    Enables "long" format output. This flag triggers a more intensive crawl that extracts and displays additional information for each file, including file size, inferred language, summaries, and other metadata sourced from docstrings and `@kit:` magic comments.

*   `-s, --show-content`:
    Shows a preview of the file's content in the long format view. This flag requires `-l` or `--long` to be active.

### Examples

1.  **Basic Tree View:**
    Display a tree structure of the current directory. This automatically uses the default exclusions, hiding directories like `.git` and `node_modules`.

    ```bash
    lazykit tree
    ```

2.  **Tree View Without Default Exclusions:**
    Show the complete, unfiltered tree, including normally hidden directories like `__pycache__` and `.git`.

    ```bash
    lazykit tree -n
    ```

3.  **Tree View with Additional Exclusions:**
    Display the tree while excluding the `docs` and `tests` directories in addition to the built-in defaults.

    ```bash
    lazykit tree -x docs tests
    ```

4.  **Tree View Excluding Specific Files:**
    Display the tree while excluding `README.md` and any `temp.txt` files, in addition to the built-in defaults.

    ```bash
    lazykit tree -X README.md temp.txt
    ```

5.  **Long Format (Detailed Context):**
    Get a comprehensive view of your project, including file sizes and summaries. This still uses the default exclusions.

    ```bash
    lazykit tree --long
    ```

6.  **Long Format with Content Preview:**
    Get a detailed view that also includes a snippet of each file's content.

    ```bash
    lazykit tree --long --show-content
    ```

7.  **Long Format from a Different Context with Custom Exclusions:**
    Crawl the `my_project` directory, show detailed context, and exclude the `dist` directory and any `config.json` files.

    ```bash
    lazykit tree -c my_project --long -x dist -X config.json
    ```

### How Context is Extracted (`--long` format)

When you use the `--long` flag, `lazykit` performs a deep scan of your files to extract rich context. You can control this by formatting your code comments and docstrings.

#### 1. Magic Comments with `@kit:` (For Any File Type)

This is the most direct way to add metadata. `lazykit` scans for comments with the syntax: `COMMENT_PREFIX @kit:KEY: VALUE`.

*   **Syntax:** `# @kit:description: A brief explanation of this file.`
*   **Purpose:** Adds key-value pairs to a file's metadata.
*   **Common Keys:** `description`, `author`, `status`, `usage`.

**Example (`database.py`):**
```python
# @kit:description: Handles all database connection and query logic.
# @kit:status: stable
import sqlalchemy
# ...
```

#### 2. Disabling Content Parsing

To prevent `lazykit` from reading a specific file's content, add an ignore comment anywhere inside it.

*   **Syntax:** `# @kit:ignore`

#### 3. Automatic Summaries

`lazykit` also automatically infers a primary summary from certain files:

*   **Python Files (`.py`):** The **first line of the module-level docstring** is used as the summary.
    ```python
    """Defines all the API endpoints for the user resource."""
    from flask import Blueprint
    # ...
    ```
*   **`pyproject.toml`:** The `description` field from the `[project]` section is used as the file summary. Other fields like `name`, `version`, and `license` are also extracted as metadata.
*   **`package.json`:** The `description` field is used as the file summary. Other fields like `name`, `version`, and `author` are also extracted.

#### How Summaries and Metadata Combine

`lazykit` intelligently combines this information. An automatic summary (from a docstring) and `@kit` comments can exist in the same file without conflict.

*   **Docstring/Description Field** -> Populates the main `summary`.
*   **`@kit:` Comments** -> Add key-value pairs to the `metadata`.

**Example Output (`utils.py`):**
```
├── utils.py [Python] (1 KB)
│     ↪ summary: A collection of helper functions for data manipulation.
│     ↪ description: Provides reusable functions for string and list processing.
│     ↪ status: wip
```

### Configuring Exclusions with `.lazykitignore`

For project-wide, persistent exclusion rules, you can create a `.lazykitignore` file in the root of your project. This works very similarly to a `.gitignore` file and is the recommended way to manage standard exclusions.

The rules from this file are automatically combined with any exclusions you provide on the command line (e.g., `-x`, `-X`).

#### Syntax and Rules:

*   The file must be named `.lazykitignore` and placed in the root directory you are scanning.
*   Each line specifies one pattern.
*   Standard glob patterns like `*` (wildcard) and `?` (single character) are supported.
*   Blank lines are ignored.
*   Lines beginning with `#` are treated as comments and are ignored.

There are two types of exclusion patterns:

**1. Full Exclusion (Standard Patterns)**

Any pattern that doesn't start with an exclamation mark (`!`) will completely remove matching files or directories from the tree output.

*   `build/`: Excludes the `build` directory and everything inside it.
*   `*.log`: Excludes any file ending with the `.log` extension.

**2. Content-Only Exclusion (Patterns with `!`)**

If a pattern is prefixed with an exclamation mark (`!`), the matching file will **still appear in the tree**, but `lazykit` will not attempt to read its content. This is useful for large, auto-generated, or binary files that you want to see listed but don't need context from.

*   This exclusion is only relevant when using the `--long` flag.
*   The file's summary will state that the content was ignored by a pattern.

#### Example `.lazykitignore` file:

```
# This is a comment and will be ignored.

# --- Full Exclusions ---
# Exclude standard build and dependency directories
dist/
build/
node_modules/

# Exclude all log and temporary files
*.log
*.tmp
*.swp

# --- Content-Only Exclusions ---
# The file 'big_data.csv' will be listed in the tree, but its
# content will not be read, saving processing time.
!data/big_data.csv

# Don't parse the content of any auto-generated API client files.
!src/api/generated_client.py
```
