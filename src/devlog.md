# CS4348 Project 1 Development Log

## 2025-10-18 [10:20] - Project Start

### Project Overview
Building a multi-process encryption system with three programs:
- **Logger**: Timestamps and logs activities  
- **Encryption**: Vigenère cipher operations
- **Driver**: Main interface using pipes to coordinate other programs

**Language**: Python with subprocess module for pipe communication  
**Environment**: VS Code on Windows, targeting cs1/cs2 compatibility

### Development Plan
1. Session 1: Encryption program
2. Session 2: Logger program  
3. Session 3: Driver program basics
4. Session 4: User interface and history
5. Session 5: Integration testing
6. Session 6: Final testing and docs

---

## 2025-10-18 [10:30] - Session 1 Start

### Goal
Implement and test the encryption program with Vigenère cipher.

### Plan
1. Create VigenereCipher class with encrypt/decrypt methods
2. Add command parsing (PASS, ENCRYPT, DECRYPT, QUIT)  
3. Test with spec example: PASS HELLO → ENCRYPT HELLO → RESULT OIWWC
4. Add proper error handling

---

## 2025-10-18 [10:52] - Session 1 End

### Completed
-  Implemented VigenereCipher class
-  Added command parsing and error handling
-  Tested with specification example - works correctly
-  Added sys.stdout.flush() for pipe communication
-  Created test_input.txt for efficient testing

### Problems Solved
1. **Python setup**: Installed Python 3.13, uses `python` command on Windows
2. **Cipher math**: Verified manually (H+H=O, E+E=I, etc.) 
3. **Pipe communication**: Added flush() calls after studying cpu.py/mem.py examples

### Testing Results
```
ENCRYPT HELLO → ERROR Password not set 
PASS HELLO → RESULT   
ENCRYPT HELLO → RESULT OIWWC 
DECRYPT OIWWC → RESULT HELLO 
```

---

## 2025-10-18 [8:50] - Session 2 Start

### Goal
Implement and test the logger program with proper timestamp formatting.

### Plan
1. Create logger.py that accepts log file name as command line argument
2. Read log messages from stdin until "QUIT"
3. Parse messages: first word = action, rest = message
4. Write to log file with format: "YYYY-MM-DD HH:MM [ACTION] MESSAGE"
5. Test with various message types and verify timestamp format
6. Add error handling for file I/O issues

### Key Requirements
- Command line: `python logger.py <log_file>`
- Input format: "ACTION message text"
- Output format: "2025-10-18 14:30 [ACTION] message text"
- Stop on "QUIT" command

---

## 2025-10-18 [9:53] - Session 2 End

### Completed
-  Implemented logger.py with command line argument parsing
-  Added proper timestamp formatting: "YYYY-MM-DD HH:MM [ACTION] MESSAGE"
-  Implemented message parsing (first word = action, rest = message)
-  Added file I/O with append mode and immediate flushing
-  Created test_logger_input.txt for testing
-  Switched to Command Prompt terminal for better testing compatibility
-  Added error handling for invalid file paths

### Problems Solved
1. **Timestamp format**: Used strftime("%Y-%m-%d %H:%M") for exact specification format
2. **Message parsing**: Used split(' ', 1) to separate action from message correctly

### Testing Results
```
Input: "START Logging system started"
Output: "2025-10-18 15:30 [START] Logging system started" 

Input: "COMMAND password"
Output: "2025-10-18 15:30 [COMMAND] password" 

Input: "START" (empty message)
Output: "2025-10-18 15:30 [START] " 
```

---

## 2025-10-19 [9:58] - Session 3 Start

### Goal
Implement driver program with subprocess management and basic user interface.

### Plan
1. Create driver.py that accepts log file as command line argument
2. Launch logger and encryption subprocesses using Popen
3. Set up pipe communication (stdin/stdout) with both processes
4. Implement basic menu system (password, encrypt, decrypt, history, quit)
5. Test subprocess coordination and communication
6. Add proper process cleanup on exit

### Key Requirements from cpu.py/mem.py Examples
- Use `Popen(['python', 'program.py'], stdin=PIPE, stdout=PIPE, encoding='utf8')`
- Remember to use `flush()` for immediate pipe communication
- Handle process termination with QUIT commands
- Test basic process coordination before adding full UI

### Technical Approach
1. Start with basic subprocess creation and testing
2. Add simple communication (send one command, get response)
3. Gradually build up to full menu system
4. Add history management and error handling

---

## 2025-10-19 [10:05] - Session 3 End

### Completed
-  Implemented complete driver.py with subprocess management
-  Created logger and encryption subprocesses using Popen
-  Set up pipe communication (stdin/stdout) with both processes
-  Implemented full menu system (password, encrypt, decrypt, history, quit)
-  Added history management for strings (excluding passwords)
-  Input validation (letters and spaces only)
-  Proper process cleanup on exit
-  Error handling for subprocess communication

### Problems Solved
1. **Subprocess communication**: Used Popen with PIPE and encoding='utf8'
2. **Process coordination**: Applied patterns from cpu.py/mem.py examples
3. **Menu system**: Implemented user-friendly interface with clear options
4. **History management**: Stores strings but not passwords as required
5. **Input validation**: Uses regex to check for letters and spaces only
6. **Process cleanup**: Sends QUIT to both processes and handles timeouts

### Testing Results
Complete workflow test:
1. **Set password "SECRET"** → Password set successfully 
2. **Encrypt "HELLO"** → Result: encrypted string 
3. **Check history** → Shows HELLO and encrypted result 
4. **Decrypt using history** → Result: HELLO 
5. **Clean exit** → All processes terminated properly 

### Key Implementation Details
- **Logger communication**: One-way pipe (stdin only)
- **Encryption communication**: Two-way pipes (stdin/stdout)
- **History management**: List of strings, excludes passwords
- **User interface**: Menu-driven with input validation
- **Error handling**: Graceful handling of process failures

### Log File Verification
```
[START] Driver program started
[COMMAND] password / encrypt / decrypt / history
[RESULT] Password set / Encrypted: XXX / Decrypted: XXX
[ERROR] Any error conditions
[END] Driver program exiting
```

---


