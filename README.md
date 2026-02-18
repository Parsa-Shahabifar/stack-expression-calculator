# 🧮 Stack Expression Calculator

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-success?style=for-the-badge)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)

A robust and efficient mathematical expression evaluator written in Python. This project implements a custom **Stack Data Structure** from scratch to parse and calculate mathematical expressions using the **Shunting-yard algorithm** (Infix to Postfix conversion).

It provides both a lightweight **Command Line Interface (CLI)** and a modern **Graphical User Interface (GUI)** built with Tkinter.

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Algorithm & Logic](#-algorithm--logic)
- [Project Architecture](#-project-architecture)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [License](#-license)

---

## 🔭 Overview

This project serves as a practical implementation of fundamental computer science concepts. It avoids Python's built-in `eval()` function, opting instead to manually parse strings, manage operator precedence, and evaluate results using a Last-In-First-Out (LIFO) stack mechanism.

**Core Capabilities:**

- Handles complex nested parentheses.
- Respects mathematical order of operations (PEMDAS).
- Supports right-associative operators (like exponentiation).

---

## ✨ Key Features

### ⚙️ Core Engine

- **Custom Stack Implementation:** A pure Python implementation of the Stack data structure with standard operations (`push`, `pop`, `peek`, `is_empty`).
- **RPN Conversion:** Converts standard Infix notation (e.g., $A + B$) to Reverse Polish Notation (e.g., $A B +$).
- **Precise Evaluation:** Step-by-step evaluation of Postfix strings.

### 🧮 Supported Operations

| Symbol | Operation      | Associativity |
| :----: | :------------- | :------------ |
|  `+`   | Addition       | Left          |
|  `-`   | Subtraction    | Left          |
|  `*`   | Multiplication | Left          |
|  `/`   | Division       | Left          |
|  `^`   | Exponentiation | **Right**     |
| `( )`  | Grouping       | -             |

### 🖥️ User Interfaces

1.  **CLI:** Fast, text-based input for quick calculations and debugging.
2.  **GUI:** A visual calculator interface built with `tkinter` for end-users.

---

## 🧠 Algorithm & Logic

The calculator operates in a two-phase pipeline:

### Phase 1: Infix to Postfix (Parsing)

The engine transforms human-readable expressions into machine-friendly format using a stack to manage operator priority.

**Example Transformation:**
$$ (A + B) \times C \rightarrow A B + C \times $$

### Phase 2: Postfix Evaluation (Calculation)

The Postfix expression is traversed from left to right:

1.  **Operands** (numbers) are pushed onto the stack.
2.  **Operators** pop the top two elements, perform the calculation, and push the result back.
3.  The final remaining element is the answer.

---

## 📂 Project Architecture

```text
stack-expression-calculator/
├── calculator/                 # Core Logic Package
│   ├── __init__.py
│   ├── stack.py                # Stack Data Structure Class
│   ├── checking_priority.py    # Operator Precedence Rules
│   ├── infix_to_postfix.py     # Shunting-yard Algorithm
│   └── postfix_to_result.py    # RPN Evaluator
│
├── gui/                        # UI Package
│   ├── __init__.py
│   └── app.py                  # Tkinter Main Window & Logic
│
├── tests/                      # Test Suite
│   └── test_calculator.py      # Unit Tests
│
├── main.py                     # CLI Entry Point
├── requirements.txt            # Project Dependencies
└── README.md                   # Documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.10** or higher.

### Installation

1.  **Clone the repository:**

```bash
    git clone https://github.com/Parsa-Shahabifar/stack-expression-calculator.git
    cd stack-expression-calculator
```

## 💻 Usage Guide

### 1. Command Line Interface (CLI)

Execute the `main.py` script to run the interactive console calculator.

```bash
python3 main.py
```

**Sample Session:**
text
Enter Expression: 3 + 4 \* 2 / ( 1 - 5 ) ^ 2
Result: 3.5

### 2. Graphical User Interface (GUI)

Launch the visual application window.

```bash
python3 app.py
```

_Alternatively, run `python gui/app.py` depending on your path configuration._

---

## 👤 Author

**Parsa Shahabifar**

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
