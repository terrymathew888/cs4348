#!/usr/bin/env python
"""
CS4348 Project 1 - Driver Program
Main program that coordinates logger and encryption subprocesses
Usage: python driver.py <log_file>
"""

import sys
import subprocess
import re
from subprocess import Popen, PIPE


class DriverProgram:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger_process = None
        self.encryption_process = None
        self.history = []
    
    def start_processes(self):
        """Start the logger and encryption subprocesses"""
        try:
            # Start logger process
            self.logger_process = Popen(
                ['python', 'logger.py', self.log_file],
                stdin=PIPE,
                encoding='utf8',
                bufsize=0
            )
            
            # Start encryption process
            self.encryption_process = Popen(
                ['python', 'encryption.py'],
                stdin=PIPE,
                stdout=PIPE,
                encoding='utf8',
                bufsize=0
            )
            
            print("Processes started successfully!")
            self.log_message("START", "Driver program started")
            return True
            
        except Exception as e:
            print(f"Error starting processes: {e}")
            return False
    
    def log_message(self, action, message):
        """Send a log message to the logger process"""
        if self.logger_process and self.logger_process.stdin:
            try:
                log_entry = f"{action} {message}\n"
                self.logger_process.stdin.write(log_entry)
                self.logger_process.stdin.flush()
            except Exception as e:
                print(f"Error logging message: {e}")
    
    def send_to_encryption(self, command):
        """Send command to encryption process and get response"""
        if not self.encryption_process:
            return "ERROR Encryption process not available"
        
        try:
            self.encryption_process.stdin.write(f"{command}\n")
            self.encryption_process.stdin.flush()
            response = self.encryption_process.stdout.readline().strip()
            return response
        except Exception as e:
            return f"ERROR Communication failed: {e}"
    
    def test_basic_communication(self):
        """Test basic communication with both processes"""
        print("\n=== Testing Basic Communication ===")
        
        # Test logging
        print("Testing logger...")
        self.log_message("TEST", "Basic communication test")
        
        # Test encryption (should fail - no password set)
        print("Testing encryption without password...")
        response = self.send_to_encryption("ENCRYPT HELLO")
        print(f"Response: {response}")
        
        # Set password and test again
        print("Setting password...")
        response = self.send_to_encryption("PASS SECRET")
        print(f"Response: {response}")
        
        print("Testing encryption with password...")
        response = self.send_to_encryption("ENCRYPT HELLO")
        print(f"Response: {response}")
        
        print("=== Communication Test Complete ===\n")
    
    def validate_letters_only(self, text):
        """Check if text contains only letters and spaces"""
        return re.match(r'^[a-zA-Z\s]*$', text) is not None
    
    def get_string_choice(self, prompt):
        """Get user choice between history and new string"""
        while True:
            print(f"\n{prompt}")
            print("1. Enter new string")
            print("2. Use string from history")
            
            if not self.history:
                print("(History is empty - you must enter a new string)")
                return self.get_new_string()
            
            choice = input("Choice (1 or 2): ").strip()
            
            if choice == "1":
                return self.get_new_string()
            elif choice == "2":
                return self.get_from_history()
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def get_new_string(self):
        """Get a new string from user with validation"""
        while True:
            text = input("Enter string: ").strip()
            if not text:
                print("Empty string not allowed.")
                continue
            
            if not self.validate_letters_only(text):
                print("Error: String must contain only letters and spaces.")
                continue
            
            return text
    
    def get_from_history(self):
        """Let user select from history"""
        while True:
            print("\nHistory:")
            for i, item in enumerate(self.history, 1):
                print(f"{i}. {item}")
            print(f"{len(self.history) + 1}. Enter new string instead")
            
            try:
                choice = int(input(f"Select (1-{len(self.history) + 1}): "))
                
                if 1 <= choice <= len(self.history):
                    return self.history[choice - 1]
                elif choice == len(self.history) + 1:
                    return self.get_new_string()
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
    
    def show_menu(self):
        """Display the main menu"""
        print("\n" + "="*40)
        print("Encryption System")
        print("="*40)
        print("1. password - Set encryption password")
        print("2. encrypt  - Encrypt a string")
        print("3. decrypt  - Decrypt a string")
        print("4. history  - Show string history")
        print("5. quit     - Exit the program")
        print("="*40)
    
    def password_command(self):
        """Handle password command"""
        self.log_message("COMMAND", "password")
        
        password = self.get_string_choice("Set password:")
        
        # Send to encryption program (use PASS command)
        response = self.send_to_encryption(f"PASS {password.upper()}")
        
        if response.startswith("RESULT"):
            print("Password set successfully.")
            self.log_message("RESULT", "Password set")
        else:
            print(f"Error setting password: {response}")
            self.log_message("ERROR", f"Password set failed: {response}")
    
    def encrypt_command(self):
        """Handle encrypt command"""
        self.log_message("COMMAND", "encrypt")
        
        text = self.get_string_choice("Text to encrypt:")
        
        # Add to history if it's not already there
        if text not in self.history:
            self.history.append(text)
        
        # Send to encryption program
        response = self.send_to_encryption(f"ENCRYPT {text.upper()}")
        
        if response.startswith("RESULT"):
            result = response[7:]  # Remove "RESULT " prefix
            print(f"Encrypted text: {result}")
            
            # Add result to history
            if result not in self.history:
                self.history.append(result)
            
            self.log_message("RESULT", f"Encrypted: {result}")
        else:
            print(f"Encryption failed: {response}")
            self.log_message("ERROR", f"Encryption failed: {response}")
    
    def decrypt_command(self):
        """Handle decrypt command"""
        self.log_message("COMMAND", "decrypt")
        
        text = self.get_string_choice("Text to decrypt:")
        
        # Add to history if it's not already there
        if text not in self.history:
            self.history.append(text)
        
        # Send to encryption program
        response = self.send_to_encryption(f"DECRYPT {text.upper()}")
        
        if response.startswith("RESULT"):
            result = response[7:]  # Remove "RESULT " prefix
            print(f"Decrypted text: {result}")
            
            # Add result to history
            if result not in self.history:
                self.history.append(result)
            
            self.log_message("RESULT", f"Decrypted: {result}")
        else:
            print(f"Decryption failed: {response}")
            self.log_message("ERROR", f"Decryption failed: {response}")
    
    def history_command(self):
        """Handle history command"""
        self.log_message("COMMAND", "history")
        
        if not self.history:
            print("History is empty.")
        else:
            print("\nHistory:")
            for i, item in enumerate(self.history, 1):
                print(f"{i}. {item}")
        
        self.log_message("RESULT", "History displayed")
    
    def cleanup(self):
        """Clean up processes on exit"""
        print("\nShutting down...")
        
        # Send QUIT to encryption process
        if self.encryption_process:
            try:
                self.send_to_encryption("QUIT")
                self.encryption_process.wait(timeout=5)
            except Exception:
                self.encryption_process.terminate()
        
        # Send QUIT to logger process
        if self.logger_process:
            try:
                self.log_message("END", "Driver program exiting")
                self.log_message("QUIT", "")
                self.logger_process.stdin.close()
                self.logger_process.wait(timeout=5)
            except Exception:
                self.logger_process.terminate()
        
        print("Cleanup complete!")

    def run(self):
        """Main program execution"""
        if not self.start_processes():
            return
        
        print("Welcome to the Encryption System!")
        
        try:
            while True:
                self.show_menu()
                
                command = input("Enter command: ").strip().lower()
                
                if command in ['1', 'password']:
                    self.password_command()
                elif command in ['2', 'encrypt']:
                    self.encrypt_command()
                elif command in ['3', 'decrypt']:
                    self.decrypt_command()
                elif command in ['4', 'history']:
                    self.history_command()
                elif command in ['5', 'quit']:
                    break
                elif command == 'test':  # Hidden test command
                    self.test_basic_communication()
                else:
                    print("Invalid command. Please try again.")
                    self.log_message("ERROR", f"Invalid command: {command}")
                    
        except KeyboardInterrupt:
            print("\nProgram interrupted by user")
        finally:
            self.cleanup()


def main():
    if len(sys.argv) != 2:
        print("Usage: python driver.py <log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    driver = DriverProgram(log_file)
    driver.run()


if __name__ == "__main__":
    main()