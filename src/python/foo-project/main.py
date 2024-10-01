import subprocess
import sys
from pathlib import Path

out = Path(sys.argv[1])
subprocess.run([sys.executable, "-m", "build", "src/python/foo-project"], check=True)
subprocess.run(["cp", "-R","src/python/foo-project/dist/", out.parent.as_posix()], check=True)
