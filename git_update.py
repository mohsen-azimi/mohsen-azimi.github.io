import subprocess


# ", "*.json", "*.txt", "*.sh", "*.yml", "*.ipynb", "*.csv", "*.tsv", "*.xlsx",
# "*.xls", "*.pdf", "*.jpg", "*.jpeg", "*.png", "*.gif", "*.svg", "*.mp4", "*.mov",
# "*.avi", "*.mp3", "*.wav", "*.zip", "*.tar", "*.gz", "*.7z", "*.rar", "*.bz2",
# "*.apk", "*.exe", "*.dmg", "*.iso", "*.bin", "*.img", "*.deb", "*.rpm", "*.msi",
# "*.jar", "*.war", "*.ear", "*.class", "*.dll", "*.so", "*.lib", "*.a", "*.o",
# "*.obj", "*.pyc", "*.out", "*.log", "*.tmp", "*.temp", "*.bak", "*.swp", "*.swo", "*.swn", "*.swo
def git_add_commit_push():
    subprocess.run(["git", "config", "--local", "core.autocrlf", "false"])  # to avoid the warning of CRLF/LF,

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "updated"])
    subprocess.run(["git", "push", '-f'])


if __name__ == '__main__':
    git_add_commit_push()
