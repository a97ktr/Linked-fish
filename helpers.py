# helpers.py
import sys

def print_progress_bar(iteration, total, length=50):
    percent = (iteration / total) * 100
    bar = '█' * int(length * iteration // total) + '-' * (length - int(length * iteration // total))
    sys.stdout.write(f'\r|{bar}| {percent:.2f}% Complete')
    sys.stdout.flush()

def remove_repeated_phrases(text):
    phrases = [line.strip() for line in text.splitlines() if line.strip()]
    unique_phrases = list(dict.fromkeys(phrases))
    return '\n'.join(unique_phrases)
