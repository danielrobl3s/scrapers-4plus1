# scrapers-4plus1
Scrapers to scrape real-state websites


# Project Setup

This guide will walk you through installing Python, creating a virtual environment, and installing the project dependencies using `requirements.txt`.

## Prerequisites

1. **Install Python**  
   - Download and install the latest version of Python from the official website:  
     [https://www.python.org/downloads/](https://www.python.org/downloads/)  
   - During installation, **make sure to check the box** that says **"Add Python to PATH"**.

2. **Verify Python Installation**  
   Open a terminal (Command Prompt or PowerShell on Windows, or a terminal on macOS/Linux) and run:

   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```

   You should see the installed version of Python.

---

## Step 1: Create a Virtual Environment

A virtual environment helps you manage dependencies locally for the project without affecting your global Python setup.

1. **Navigate to your project folder**:

   ```bash
   cd /path/to/your/project
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   ```

   This will create a `venv/` folder containing the virtual environment files.

---

## Step 2: Activate the Virtual Environment

- **On Windows**:

   ```bash
   venv\Scripts\activate
   ```

- **On macOS/Linux**:

   ```bash
   source venv/bin/activate
   ```

   After activation, your terminal prompt should show `(venv)` to indicate that the virtual environment is active.

---

## Step 3: Install Dependencies

With the virtual environment activated, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Step 4: Verify Installation

To confirm that all dependencies were installed correctly, you can list the installed packages:

```bash
pip list
```

---

## Step 5: Deactivate the Virtual Environment

When you're done working in the virtual environment, you can deactivate it by running:

```bash
deactivate
```

---

## Optional: Update Dependencies

If you need to update dependencies in the `requirements.txt` file:

1. Install new packages or update existing ones:

   ```bash
   pip install <package_name> --upgrade
   ```

2. Save the current dependencies to the `requirements.txt` file:

   ```bash
   pip freeze > requirements.txt
   ```

---

## Troubleshooting

- **Python not recognized**: Ensure that Python is installed and added to your PATH.  
- **Pip not recognized**: You may need to install `pip` separately, or use:

   ```bash
   python -m pip install <package>
   ```

---
