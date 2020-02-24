import sys
import subprocess

if __name__ == '__main__':
    try:
        p = subprocess.Popen(['git','log','-1','--format=%h'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            git_hash= out.decode().strip()
    except Exception:
        sys.exit(-1)
    sys.stdout.write(git_hash)
    sys.stdout.flush()
    sys.exit(0)
