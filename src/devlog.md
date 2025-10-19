# CS4348 Project 1 Development Log

## 2025-10-18 [10:20] - Initial Planning Session

### Project Understanding
After reading through the project specifications, I understand that I need to implement a multi-process encryption system with three components:

1. **Logger Program**: Accepts log messages via stdin and writes timestamped entries to a log file
2. **Encryption Program**: Handles Vigenère cipher operations (encrypt/decrypt) via stdin/stdout communication  
3. **Driver Program**: Main user interface that coordinates the other two programs using pipes

### Key Technical Requirements
- Must use system calls for inter-process communication (Python: subprocess module)
- Vigenère cipher implementation (case-insensitive, letters only)
- Error handling for invalid input
- History management for strings (but not passwords)
- Proper logging of all operations

### Development Environment
- Using VS Code for development
- Python 3 for implementation
- Testing locally but ensuring compatibility with cs1/cs2 machines
- Using git for version control with detailed commit history

### Overall Development Plan
Implementing in Python using subprocess module for pipe communication:

1. **Session 1**: Implement and test the encryption program (Vigenère cipher)
2. **Session 2**: Implement and test the logger program  
3. **Session 3**: Implement basic driver program with process management
4. **Session 4**: Add user interface, history management, and error handling
5. **Session 5**: Integration testing and debugging
6. **Session 6**: Final testing and documentation

---

## 2025-10-18 [10:24] - Session 1 Start

### Thoughts Since Last Session  
- Reviewed Vigenère cipher algorithm - polyalphabetic substitution cipher
- Key insight: only process letters, ignore other characters
- Need to handle case-insensitive input by converting to uppercase
- The cipher repeats the key across the text

### Session Goals
- Implement complete encryption program (encryption.py)
- Test Vigenère cipher encryption and decryption algorithms
- Implement proper command parsing (PASS, ENCRYPT, DECRYPT, QUIT)
- Test with specification example: PASS HELLO → ENCRYPT HELLO → RESULT OIWWC
- Ensure proper error handling and response format

### Implementation Plan
1. Create VigenereCipher class with set_passkey, encrypt, and decrypt methods
2. Implement main command parsing loop with proper input/output format
3. Test cipher math manually to verify correctness
4. Test with specification examples
5. Add comprehensive error handling for edge cases

---