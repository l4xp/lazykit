# **lazykit**

An extensible CLI project automation tool.

**lazykit** is a command-line utility designed to streamline common project automation tasks, making project setup and maintenance more efficient. It provides built-in commands for generating boilerplate files like `README.md` and `LICENSE`, analyzing project structure, and is built with an extensible plugin architecture for future custom automations.

---

## ✨ Features

- **Project Initialization:** Quickly set up new projects with `lazykit init`.
- **License Generation:** Generate `LICENSE` files for your project, supporting various open-source licenses (MIT, Apache, GPLv3, BSD, Creative Commons, etc.) with `lazykit gen-license`.
- **README Generation:** Automatically generate `README.md` files based on project context using `lazykit gen-readme`.
- **File Tree Visualization:** Display your project's directory structure with `lazykit tree`, allowing for exclusions.
- **Extensible Architecture:** Easily extend with custom plugins to add new commands and workflows.
- **Contextual Understanding:** Utilizes project context (file trees, comments, metadata) to provide intelligent automation.

---

## 🚀 Installation

You can install `lazykit` directly from the cloned repository.

### Option 1: Clone only the `lazykit` directory using Git sparse-checkout

```bash
# 1. Clone the directory
git clone --no-checkout https://github.com/ljzh04/TinyProjects.git lazykit
cd lazykit
git sparse-checkout init --cone
git sparse-checkout set lazykit/
git checkout main  # Or your desired branch, e.g., 'master'
cd lazykit

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run or add lazykit/ to your shell PATH
python -m lazykit [OPTIONS]
````

### Option 2: Clone the whole monorepo (simple, but may be large)

```bash
# 1. Clone the repository (if you haven't already)
git clone https://github.com/ljzh04/TinyProjects.git
cd TinyProjects/lazykit

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run or add lazykit/ to your shell PATH
python -m lazykit [OPTIONS]
```

---

## 💡 Usage

`lazykit` operates through a CLI interface with subcommands for specific tasks.

### General Command Structure

```bash
lazykit <command> [options]
```

---

### Available Commands

#### `lazykit init`

Initialize a lazykit project in the current directory or a specified path.

```bash
lazykit init [--path <DIR>]
```

* `--path <DIR>`: Directory to initialize lazykit in (defaults to current directory).

---

#### `lazykit gen-license`

Generate a `LICENSE` file for your project.

```bash
lazykit gen-license [-c DIR] [-o FILE] [-t TYPE] [--overwrite]
```

* `-c, --context-dir DIR`: Directory to crawl for project context.
* `-o, --output FILE`: Output file path (default: LICENSE).
* `-t, --type TYPE`: License type (e.g., MIT, Apache, GPLv3).
* `--overwrite`: Overwrite existing license file if present.

**Example:**

```bash
lazykit gen-license -t MIT -o LICENSE
```

---

#### `lazykit gen-readme`

Generate a `README.md` file for your project.

```bash
lazykit gen-readme [-c DIR] [-o FILE] [--overwrite]
```

* `-c, --context-dir DIR`: Directory to crawl for project context.
* `-o, --output FILE`: Output path for README (default: README.md).
* `--overwrite`: Overwrite existing README if present.

**Example:**

```bash
lazykit gen-readme -o README.md
```

---

#### `lazykit tree`

Show the project file tree, with support for exclusion.

```bash
lazykit tree [-c DIR] [-x [DIR ...]] [-X [FILE ...]] [-n] [-l]
```

* `-c, --context-dir DIR`: Directory to crawl.
* `-x, --exclude-dir [DIR ...]`: Directories to exclude.
* `-X, --exclude-file [FILE ...]`: Files to exclude.
* `-n, --no-summary`: Omit tree summary.
* `-l, --list-only`: List files without tree structure.

**Example:**

```bash
lazykit tree -x venv .git -X *.pyc
```

---

## ⚙️ Configuration

`lazykit` uses a configuration system (`lazykit/core/config.py`) to manage global and user-specific settings.

Example configurable settings:

* **Default License Type:** Preferred license for `gen-license`.
* **LLM Provider and Model:** Configure LLM features (e.g., OpenAI `gpt-4`) for intelligent generation.

---

## 🔌 Extensibility and Plugins

`lazykit` supports a plugin-based architecture. Plugins placed in the `plugins/` directory can dynamically extend functionality.

* Each plugin can expose a `register()` function to hook into the CLI.
* Plugins can add new subcommands or modify existing behaviors.

---

## 📂 Project Structure

```text
lazykit/
├── commands/             # Built-in CLI commands (gen_license, gen_readme, init, tree)
├── core/                 # Core business logic
│   ├── config.py         # Config and path handling
│   ├── context.py        # Project context (file trees, comments, metadata)
│   ├── extractors.py     # Extracts content like docstrings
│   └── generator.py      # File/template generation logic
├── docs/                 # Documentation
├── plugins/              # User/developer plugins
├── templates/            # File templates
│   ├── license/          # License templates
│   └── readme/           # README templates
├── utils.py              # Common helper functions
├── __init__.py           # Package init
├── __main__.py           # Entrypoint: `python -m lazykit`
├── .lazykitignore        # Ignore rules for context crawling
├── cli.py                # Main CLI parser
├── pyproject.toml        # Build and metadata
└── requirements.txt      # Python dependencies
```

---

## 🤝 Contributing

Contributions are welcome!

To contribute:

1. Fork the repository.
2. Create a feature/bugfix branch.
3. Implement changes and ensure tests pass.
4. Submit a pull request with a clear description.

For significant changes, please open an issue for discussion first.

---

## 📄 License

This project is licensed under the **MIT License** — see the `LICENSE` file for details.

```
