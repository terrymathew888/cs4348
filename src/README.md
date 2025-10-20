# CS4348 Project 1 - Encryption System

## Files and Roles

- **encryption.py** - Vigenère cipher program, handles PASS/ENCRYPT/DECRYPT/QUIT commands
- **logger.py** - Logging program, timestamps messages in format "YYYY-MM-DD HH:MM [ACTION] MESSAGE"  
- **driver.py** - Main program, coordinates other programs using subprocess pipes
- **devlog.md** - Development log documenting 4 implementation sessions

## How to Run

```bash
# On Linux (cs1/cs2):
python3 driver.py <log_file>

## Example Usage

```bash
python3 driver.py activity.log
```

Then use the menu:
1. Set password
2. Encrypt text  
3. Decrypt text
4. View history
5. Quit

## Implementation Notes

- Uses subprocess.Popen for inter-process communication
- Vigenère cipher converts all input to uppercase
- History stores strings but not passwords
- Input validation: letters and spaces only
- Proper process cleanup on exit

## Testing

All components tested individually and integrated. Specification compliance verified.
Comprehensive test suite available in test_system.py and compliance_check.py.
