# Reverse Engineering & Binary Patching

In this project, I worked on analyzing ELF binaries using IDA and Python to reverse engineer their behavior and patch them without having access to the source code. I focused on understanding low-level logic, crafting alternative control flows, and modifying executable files to change how they behave—all while keeping the original structure mostly intact.

## 📁 Project Structure

```
q1/
├── q1a.py       # Re-implemented the logic of msgcheck binary in Python
├── q1b.py       # Fixed an invalid .msg file by updating the checksum byte
├── q1c.py       # Alternative fix: appended a new correction byte to pass validation
├── q1d.py       # Patched the binary to always show "valid message"
├── q1e.py       # Patched the binary to always return 0, no matter the input

q2/
├── q2.py        # Patched readfile binary to execute shell commands starting with #!
├── patch1.asm   # Redirects execution from a small deadzone to the full patch
├── patch2.asm   # Handles logic: execute #! lines via system(), skip otherwise
```

## ✅ What I Did

### 🔍 Question 1: Reverse Engineering `msgcheck`

* **q1a.py**: I reverse engineered the logic of the `msgcheck` ELF binary and re-implemented the message validation check in Python.
* **q1b.py**: Created a function that fixes corrupted message files by calculating the expected checksum and replacing a single byte.
* **q1c.py**: Designed an alternative approach by appending a new byte that corrected the checksum while minimally modifying the original data.
* **q1d.py**: Patched the binary so it always prints `"valid message"` regardless of the message content.
* **q1e.py**: Patched the binary to always return `0` (success), even if the message content is invalid—without modifying its visible output.

### 🛠 Question 2: Patching `readfile`

* **q2.py**: This was a more advanced challenge. I patched the `readfile` binary so that lines starting with `#!` are executed as shell commands instead of being printed. Regular lines are still printed normally.
* Used **two patch zones**:

  * **patch1.asm**: A small redirection patch placed in a limited-size deadzone.
  * **patch2.asm**: The main logic placed in a larger deadzone, handling the condition and calling `system()` if needed.

## 🧪 How to Run

All scripts are written in Python 3 and tested on a Linux VM with IDA installed.

Examples:

```bash
python3 q1a.py 01.msg         # Re-check if message is valid
python3 q1b.py 02.msg         # Fix invalid .msg file
python3 q1d.py msgcheck       # Patch binary to always say "valid"
python3 q2.py readfile        # Patch readfile binary to run shell commands
```

Make the patched binaries executable:

```bash
chmod +x msgcheck.patched
chmod +x readfile.patched
```

## 🛠 Tools & Skills

* **Python 3** – for scripting and patch automation
* **IDA Free** – for binary disassembly and control flow analysis
* **infosec.core.assemble** – for assembling custom x86 instructions into bytes
* **Binary patching** – changing ELF executables manually using offsets and deadzones
* **x86 Assembly** – writing custom logic to replace and extend original binary behavior

---

This project really sharpened my skills in reverse engineering, assembly, and program behavior manipulation. It also gave me hands-on experience in identifying control flow points, modifying them safely, and automating the process with scripts and injected code.
