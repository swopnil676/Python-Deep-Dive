morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'S': '...',   'T': '-',     'W': '.--'
}

text = "PYTHON"


# Method 1
code = ' '.join(morse.get(c, '?') for c in text)
# Syntax : dictionary.get(key, default_value)

print(f"Morse: {code}")


# Method 2
result = []

for c in text:
    result.append(morse.get(c, '?'))

code = ' '.join(result)