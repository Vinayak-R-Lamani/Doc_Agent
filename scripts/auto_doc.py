import subprocess
from datetime import datetime 

files = subprocess.check_output(
    ["git", "diff", "--name-only", "HEAD~1", "HEAD"]
).decode().splitlines() 

now  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

log = f"#\n## Update: {now}\n\n" 

for file in files:
    log += f"- changed : {file}\n" 

with open("docs/changelog.md", "a") as f:
    f.write(log) 
    
print("CHANGELOG.md updated successfully!")