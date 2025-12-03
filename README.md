# Advent of Code 2025 — Solutions

Welcome to my Advent of Code 2025 workspace. This repository contains my problem solutions organized by day and language. The goal is to solve each puzzle clearly, idiomatically, and with small reproducible scripts you can run locally.

**Repository Structure**
- `Day<N>/` — folder for day N puzzles. Each day may contain one or more solution files (Python, C++, etc.), sample input files, and notes.
- `README.md` — this file.

**Goals & Conventions**
- Clean, readable solutions with sensible naming and small helper functions.
- Prefer plain Python scripts for portability. Use other languages (C++, etc.) where noted.
- Keep each day self-contained: input files and solution files live in the day's folder.
- Use `input.data` as the default input filename in each day's folder.

**How to run**
1. Change to the day folder, for example:

```bash
cd Day1
```

2. Run the Python solution (if present):

```bash
python3 main.py
```

3. For compiled languages (C/C++), build with the included tasks or your toolchain. Example (g++):

```bash
g++ -std=c++17 main.cpp -o main
./main
```

**Testing and examples**
- If a problem includes example input in the puzzle statement, you can add it as `input.example` and run the script against it for quick verification.

**Style notes**
- Keep logic explicit and avoid one-liner hacks unless they improve clarity.
  
- Add short comments where the algorithm is non-obvious.

**Contributing / Personal workflow**
- This repository is my personal Advent calendar. If you want to suggest improvements, open an issue or a PR with a clear description and tests/examples.

Enjoy browsing — and happy coding!
