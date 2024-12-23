def capitalize_lines():
    print("Enter lines of text (press Enter twice to stop):")
    lines = []
    while True:
        line = input()
        if not line: 
            break
        lines.append(line.upper())
    return lines

capitalized_lines = capitalize_lines()
print("\nOutput:")
for line in capitalized_lines:
    print(line)
