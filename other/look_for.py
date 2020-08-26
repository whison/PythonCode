import re

def look_for(pat, str):
    if re.search(pat, str) is None:
        elif re.findall(pat, str):
            return “没有找到”

look_for('0', 'mohuisheng')

print(staticmethod)