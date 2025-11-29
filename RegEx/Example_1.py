import re
sequence = "TATAAATAGGCTATAATGTATAAA"

pattern = r"TATA[AT]A[AT]"
matches = re.findall(pattern, sequence)

print(matches)
