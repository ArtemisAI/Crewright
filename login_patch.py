import signal
import sys
import os

# Mock signals for Windows
if os.name == 'nt':
    for sig in ['SIGHUP', 'SIGTSTP', 'SIGQUIT', 'SIGALRM', 'SIGUSR1', 'SIGUSR2', 'SIGPIPE', 'SIGBUS', 'SIGCHLD', 'SIGCONT', 'SIGIO', 'SIGIOT', 'SIGKILL', 'SIGPROF', 'SIGPWR', 'SIGSTOP', 'SIGSYS', 'SIGTRAP', 'SIGURG', 'SIGVTALRM', 'SIGWINCH', 'SIGXCPU', 'SIGXFSZ']:
        if not hasattr(signal, sig):
            setattr(signal, sig, 1)

from crewai.cli.cli import login

if __name__ == "__main__":
    try:
        login()
    except Exception as e:
        print(f"Error logging in: {e}")
