#!/usr/bin/env python3
"""
CS4348 Project 1 - Encryption Program
Implements Vigenère cipher for encrypt/decrypt operations
Communicates via stdin/stdout with specific command format
"""

import sys


class VigenereCipher:
    """Handles Vigenère cipher encryption and decryption"""
    
    def __init__(self):
        self.passkey = None
    
    def set_passkey(self, key):
        """Set the encryption/decryption key"""
        if not key:
            return False
        self.passkey = key.upper()
        return True
    
    def encrypt(self, text):
        """
        Encrypt text using Vigenère cipher
        Returns encrypted text or None if no passkey set
        """
        if not self.passkey:
            return None
        
        text = text.upper()
        result = ""
        key_index = 0
        
        for char in text:
            if char.isalpha():
                # Get the shift value from the current key character
                key_char = self.passkey[key_index % len(self.passkey)]
                shift = ord(key_char) - ord('A')
                
                # Apply Caesar shift using the key character
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                result += encrypted_char
                key_index += 1
            else:
                # Non-alphabetic characters pass through unchanged
                result += char
        
        return result
    
    def decrypt(self, text):
        """
        Decrypt text using Vigenère cipher  
        Returns decrypted text or None if no passkey set
        """
        if not self.passkey:
            return None
        
        text = text.upper()
        result = ""
        key_index = 0
        
        for char in text:
            if char.isalpha():
                # Get the shift value from the current key character
                key_char = self.passkey[key_index % len(self.passkey)]
                shift = ord(key_char) - ord('A')
                
                # Apply reverse Caesar shift
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                result += decrypted_char
                key_index += 1
            else:
                # Non-alphabetic characters pass through unchanged
                result += char
        
        return result


def main():
    """Main program loop - handles commands from stdin"""
    cipher = VigenereCipher()
    
    try:
        while True:
            # Read command from stdin
            line = input().strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Parse command and argument
            parts = line.split(' ', 1)
            command = parts[0].upper()
            argument = parts[1] if len(parts) > 1 else ""
            
            # Handle each command type
            if command == "QUIT":
                break
                
            elif command == "PASS":
                if argument:
                    if cipher.set_passkey(argument):
                        print("RESULT")
                    else:
                        print("ERROR Failed to set passkey")
                else:
                    print("ERROR No passkey provided")
                    
            elif command == "ENCRYPT":
                if not argument:
                    print("ERROR No text to encrypt")
                    continue
                    
                result = cipher.encrypt(argument)
                if result is not None:
                    print(f"RESULT {result}")
                else:
                    print("ERROR Password not set")
                    
            elif command == "DECRYPT":
                if not argument:
                    print("ERROR No text to decrypt")
                    continue
                    
                result = cipher.decrypt(argument)
                if result is not None:
                    print(f"RESULT {result}")
                else:
                    print("ERROR Password not set")
                    
            else:
                print(f"ERROR Unknown command: {command}")
                
    except EOFError:
        # Handle EOF gracefully (when stdin is closed)
        pass
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        pass


if __name__ == "__main__":
    main()