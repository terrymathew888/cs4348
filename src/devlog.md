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

## 2025-10-18 [10:52] - Session 1 Start

### Goal
Implement and test the encryption program with Vigenère cipher.

### Plan
1. Create VigenereCipher class with encrypt/decrypt methods
2. Add command parsing (PASS, ENCRYPT, DECRYPT, QUIT)  
3. Test with spec example: PASS HELLO → ENCRYPT HELLO → RESULT OIWWC
4. Add proper error handling

---

## 2025-10-18 [TIME] - Session 1 End

### Completed
- ✅ Implemented VigenereCipher class
- ✅ Added command parsing and error handling
- ✅ Tested with specification example - works correctly
- ✅ Added sys.stdout.flush() for pipe communication
- ✅ Created test_input.txt for efficient testing

### Problems Solved
1. **Python setup**: Installed Python 3.13, uses `python` command on Windows
2. **Cipher math**: Verified manually (H+H=O, E+E=I, etc.) 
3. **Pipe communication**: Added flush() calls after studying cpu.py/mem.py examples

### Testing Results
```
ENCRYPT HELLO → ERROR Password not set ✅
PASS HELLO → RESULT ✅  
ENCRYPT HELLO → RESULT OIWWC ✅
DECRYPT OIWWC → RESULT HELLO ✅
```

---