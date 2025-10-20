#!/usr/bin/env python
"""
CS4348 Project 1 - Logger Program
Logs messages with timestamps to a specified file
Usage: python logger.py <log_file>
"""

import sys
import datetime


def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python logger.py <log_file>", file=sys.stderr)
        sys.exit(1)
    
    log_file = sys.argv[1]
    
    try:
        with open(log_file, 'a') as f:
            while True:
                try:
                    # Read log message from stdin
                    line = sys.stdin.readline()
                    if not line:  # EOF
                        break
                    
                    line = line.rstrip()
                    if not line:
                        continue
                    
                    # Check for quit command
                    if line == "QUIT":
                        break
                    
                    # Parse message: first word = action, rest = message
                    parts = line.split(' ', 1)
                    action = parts[0]
                    message = parts[1] if len(parts) > 1 else ""
                    
                    # Get current timestamp in required format
                    now = datetime.datetime.now()
                    timestamp = now.strftime("%Y-%m-%d %H:%M")
                    
                    # Write log entry
                    log_entry = f"{timestamp} [{action}] {message}\n"
                    f.write(log_entry)
                    f.flush()  # Ensure immediate write
                    
                except EOFError:
                    break
                    
    except IOError as e:
        print(f"Error opening log file '{log_file}': {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()