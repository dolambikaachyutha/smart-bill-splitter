# 🧾 Smart Bill Splitter

A colorful, interactive command-line tool to split restaurant or group bills fairly — either equally among everyone or based on what each person ordered.
✨ Features

- **Equal Split** — Divide the total bill evenly among all members
- **Unequal Split** — Each person pays for their own order, with tip and GST shared equally
- **GST & Tip Support** — Automatically calculates and distributes tax and tip
- **Bill History** — Saves every split to a local `history.txt` file with timestamps
- **Clear History** — Wipe the history log with a single option
- **Colorful CLI** — Uses `colorama` for a clean, color-coded terminal experience
## 📸 Demo
==================================================
         Welcome to smart bill splitter!
==================================================
How do you want to split the bill:
1. Equal split
2. Split by each person's food order or unequal split
3. View history of bill splits
4. Clear history
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Achyutha Dolambika/smart-bill-splitter.git
cd smart-bill-splitter
```

### 2. Install dependencies

```bash
pip install colorama
```

### 3. Run the program

```bash
python bill_splitter.py
```

---

## 🚀 Usage

### Equal Split
Enter the total bill, tip %, GST %, and number of people — everyone pays the same amount.

### Unequal Split
Enter each person's name and what they ordered. Tip and GST are shared equally, but the food cost is individual.

### View History
All past splits are saved automatically to `history.txt` with date and time.

### Clear History
Wipes `history.txt` clean.

---

## 📁 Project Structure

```
smart-bill-splitter/
│
├── bill_splitter.py   # Main program
├── history.txt        # Auto-generated split history (created on first run)
└── README.md
```

---

## 📦 Dependencies

| Package    | Purpose                        |
|------------|--------------------------------|
| `colorama` | Colored terminal output        |
| `os`       | Screen clearing                |
| `time`     | Animated delay effects         |
| `datetime` | Timestamping history entries   |

Install all dependencies:

```bash
pip install colorama
`
## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for:

- New split modes (e.g., percentage-based)
- Export history to CSV or PDF
- GUI version using Tkinter or a web framework

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

Made with ❤️ by [Your Name](https://github.com/your-username)
