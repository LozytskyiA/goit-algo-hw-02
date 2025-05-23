from collections import deque

def is_palindrome(text: str) -> bool:
    normalized_text = ''.join(ch.lower() for ch in text if ch.isalnum())
    char_deque = deque(normalized_text)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True
