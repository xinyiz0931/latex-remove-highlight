import re
# remain_revised = True 
revised_remain = False 
revise_command = 'red' # \red{somthing}
delete_command = 'del' # \del{something}

red = []
delete = []
with open('content.txt') as f:
    s = f.read()

# ----------------------- delete command: remove -----------------------------------
for i, c_left in enumerate(s):
    if c_left == '\\' and s[i+1:i+4] == delete_command and s[i+4] != '}':
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
        if c_left == "\\" and s[i+1:i+4] == revise_command and s[i+4] != '}':
            s_after = s[i:]
            # j = s_after.index("}")
            js = [m.start() for m in re.finditer('}', s_after)] 
            for j in js:
                if s[i:i+j+1].count('{') == s[i:i+j+1].count('}'):
                    red.append(s[i:i+j+1])
                    break

    for r in red:
        print(r[5:-1])
        s = s.replace(r, r[5:-1])

print("write to new file ... ")
with open('content_new.txt', 'w') as fr:
    fr.write(s)
