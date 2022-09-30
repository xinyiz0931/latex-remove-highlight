import re
# remain_revised = True 
revised_remain = False 
revise_cmd = 'red' # \red{somthing}
delete_cmd = 'del' # \del{something}

red = []
delete = []
with open('manuscript.txt') as f:
    s = f.read()

# ----------------------- delete command: remove -----------------------------------
for i, c_left in enumerate(s):
    if c_left == '\\' and s[i+1:i+1+len(delete_cmd)] == delete_cmd and s[i+1+len(delete_cmd)] != '}':
        s_after = s[i:]
        # j = s_after.index("}")
        js = [m.start() for m in re.finditer('}', s_after)] 
        for j in js:
            if s[i:i+j+1].count('{') == s[i:i+j+1].count('}'):
                delete.append(s[i:i+j+1])
                break
for d in delete:
    s = s.replace(d, "")

# ------------------------ revise command: red -> black ---------------------------
if not revised_remain:
    for i, c_left in enumerate(s):
        if c_left == "\\" and s[i+1:i+1+len(revise_cmd)] == revise_cmd and s[i+1+len(revise_cmd)] != '}':
            s_after = s[i:]
            # j = s_after.index("}")
            js = [m.start() for m in re.finditer('}', s_after)] 
            for j in js:
                if s[i:i+j+1].count('{') == s[i:i+j+1].count('}'):
                    red.append(s[i:i+j+1])
                    break

    for r in red:
        s = s.replace(r, r[1+len(revise_cmd)+1:-1])

print("write to new file ... ")
with open('manuscript_new.txt', 'w') as fr:
    fr.write(s)

print("copy to clipboard, just use ctrl+v to paste")
import pyperclip
pyperclip.copy(s)
spam = pyperclip.paste()


