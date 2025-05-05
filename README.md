# Automated Code Development using GitHub Actions

## 🔧 Overview
This project demonstrates automatic Python code generation and versioning using GitHub Actions.

## 🧠 How it Works
- `src/auto_generator.py` creates a new Python function inside `src/generated_code.py`
- GitHub Actions runs this script when a push is made to `main`, or manually triggered
- The newly generated file is committed and pushed back to the repository

## 📁 Project Structure
- `.github/workflows/main.yml` – Workflow file for GitHub Actions
- `src/auto_generator.py` – Script that generates code
- `src/generated_code.py` – Output file (auto-generated)
- `requirements.txt` – Python dependencies (pytest)
- `README.md` – Project documentation

## 🚀 Future Ideas
- Use AI (like ChatGPT API) for smarter code generation
- Add unit tests and lint checks
