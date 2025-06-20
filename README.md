# Reverse Engineering & Binary Patching

This project includes solutions for a reverse engineering and binary patching exercise using Python and IDA. The tasks involve analyzing ELF binaries, modifying program behavior, and changing outputs without access to the original source code.

## 📁 Project Structure
q1/
├── q1a.py # Checks if a .msg file is valid using the same logic as msgcheck binary
├── q1b.py # Fixes invalid messages by correcting a single byte
├── q1c.py # Provides an alternative fix by appending a correction byte
├── q1d.py # Patches the binary to always print "valid message"
├── q1e.py # Patches the binary to always return 0, but still prints the original message

q2/
├── q2.py # Patches the readfile binary so lines starting with #! are executed as shell commands
├── patch1.asm # Redirects execution to patch2 from a small deadzone
├── patch2.asm # Executes system() on lines starting with #!


## 🔍 Overview of Tasks

### ✅ Question 1: Message Checker (`msgcheck`)
- **q1a.py**: Re-implements the logic of the binary to check if a `.msg` file is valid.
- **q1b.py**: Fixes an invalid message by modifying the total checksum byte.
- **q1c.py**: Fixes a message by adding a new byte that corrects the checksum.
- **q1d.py**: Patches the binary to always follow the "valid" branch.
- **q1e.py**: Patches the binary to return `0` (success) for any input, without changing output.

### ✅ Question 2: File Reader (`readfile`)
- **q2.py**: Patches the `readfile` binary to detect lines starting with `#!` and execute them as shell commands. Other lines are printed normally.
- **patch1.asm**: Injected into a small deadzone, redirects to `patch2`.
- **patch2.asm**: Injected into a large deadzone, checks the line and calls `system()` if needed.

## 🧪 How to Run

Each patch or checker is a self-contained Python script.

Examples:

```bash
python3 q1a.py 01.msg         # Check message validity
python3 q1b.py 02.msg         # Fix invalid message
python3 q1d.py msgcheck       # Patch msgcheck to always validate
python3 q2.py readfile        # Patch readfile to run #! lines
```
Make sure to chmod +x patched binaries before running them:
bash
chmod +x msgcheck.patched
chmod +x readfile.patched
🔧 Tools Used
Python 3
IDA Free (for disassembly and patch analysis)
infosec.core.assemble (for assembling x86 instructions)
ELF binary patching and reverse engineering

