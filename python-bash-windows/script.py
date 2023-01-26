import subprocess
from shutil import which 

args = [
    which('bash'),
    'script.sh',
]

result = subprocess.run(
    args,
    capture_output=True,
    text=True,
    check=False,
)

print(result)

if result.returncode != 0:
    print("STDOUT:") 
    print(result.stdout)
    print("--") 
    print("STDERR:") 
    print(result.err)
    print("--") 

exit(result.returncode)
