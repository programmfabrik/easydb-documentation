import os
import re

def fix_buttons_repl_func(matchobj):
    repl = '<code class="'+matchobj.group(2)+'">'+matchobj.group(1)+'</code>'
    return repl

for dname, dirs, files in os.walk(os.getcwd()):
    for fname in files:
        if not fname.endswith('md'):
            continue

        fn = dname + "/" + fname
        with open(fn) as mdf:
            lines = mdf.readlines()

        print("File:", fn, len(lines), "lines.")
        with open(fn, "w") as mdf:
            for md_line in lines:
                # fix buttons
                md_line = re.sub("`(.+?)`{\.(.+?)}", fix_buttons_repl_func, md_line)
                mdf.write(md_line)
