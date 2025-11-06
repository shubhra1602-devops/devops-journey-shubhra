# Welcome to My DevOps Journey  <!-- Large heading -->

This guide explains, in plain English, what each command does and *why* it’s needed.  
If you’re new to Python or programming — this is the right starting point!

---

## Virtual Environment

### Step 1: Create a Virtual Environment

`python -m venv venv`

1. Creates a virtual environment folder named `venv`.
2. A virtual environment is an isolated Python environment with its own `python` and `pip`.  
   It keeps project dependencies separate from system Python so one project’s libraries don’t break another project.

---

### Step 2: Activate the Virtual Environment

`venv\Scripts\Activate`

1. Windows command to activate that virtual environment. After activation, your shell uses the `venv`’s `python` and `pip`.
2. On macOS/Linux, the command is `source venv/bin/activate`.
3. When activated, you’ll typically see `(venv)` at the start of your prompt.

---

### Step 3: Install Flask

`pip install flask`

1. Installs the Flask web framework into the active virtual environment (not system Python).  
   `pip` is Python’s package installer.
2. If not activated, packages may install globally (not what you want). That’s why activation is important.

---

### Step 4: Save Dependencies

`pip freeze > requirements.txt`

1. `pip freeze` lists all installed packages and exact versions (e.g. `Flask==2.3.0`).  
   The `>` redirects that list into a file `requirements.txt`.
2. Why: `requirements.txt` records which libraries and versions your project needs.  
   Another dev (or CI/CD) can run `pip install -r requirements.txt` to install the same versions.

<hr style="border: 2px solid #d1c1c1ff; margin: 40px 0;">

## Recreate Environment on Another Machine

*Later (or on another machine): recreate environment*
```bash
python -m venv venv
source venv/bin/activate # or venv\Scripts\Activate on Windows
pip install -r requirements.txt
```

<hr style="border: 2px solid #d1c1c1ff; margin: 40px 0;">

## What those `.gitignore` entries mean

1. `venv/` — don’t commit the virtual environment to Git. It’s large, machine-specific, and can be recreated with `python -m venv` + `pip install -r requirements.txt`.
2. `__pycache__/` — Python creates cached bytecode files here. Not source code; ignore them.
3. `*.pyc` — compiled Python files (bytecode). Ignore.
4. `.env` — file that often contains environment variables (like API keys, DB passwords). Don’t commit secrets to version control.
5. **Short reason:** keep your repository small, portable, and secret-free.

<hr style="border: 2px solid #d1c1c1ff; margin: 40px 0;">

## Markdown Basics Cheat Sheet

| Task | Markdown Syntax | Example |
|------|-----------------|----------|
| **Bold** | `**text**` | **Bold** |
| *Italic* | `*text*` | *Italic* |
| Heading 1 | `# Heading` | # Heading |
| Heading 2 | `## Heading` | ## Heading |
| Inline code | `` `code` `` | `pip install flask` |
| Code block | ``` ```language … ``` ``` | see examples above |
| List | `- item` | - item |
| Horizontal line | `---` | --- |

<hr style="border: 2px solid #d1c1c1ff; margin: 40px 0;">

# Docker File

### Step 1 — Create Your Dockerfile

### Step 2 — Build Your Docker Image
`docker build -t flask-app-shubhra .`

**-t flask-app-shubhra** gives your image a name (tag)
**.** means "use the current directory"

### Step 3 — Verify Your Image
`docker images`

### Step 4 — Run Your Flask App Inside a Container
`docker run -d -p 5000:5000 flask-app-shubhra`

**-d** = Detached mode (runs in background)
**-p 5000:5000** = Maps your system’s port 5000 → container’s port 5000

### Step 5 — Test It!
Now open your browser and visit:
👉 http://127.0.0.1:5000
You should see:
Hello, Shubhra! Welcome to your first Flask App 🚀

### Step 6 — Verify and Stop the Container
**List running containers:**
`docker ps`

**Stop it:**
`docker stop <container_id>`

<hr style="border: 2px solid #d1c1c1ff; margin: 40px 0;">
