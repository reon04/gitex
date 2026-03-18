import subprocess
import argparse
import psutil

gitex_help = "list and show general help for all subcommands from the gitex extension"
yeet_help = "force-push to the remote repository"
seet_help = "force-push to the remote repository safely (uses --force-with-lease and --force-if-includes)"
amend_help = "amend changes to the last commit without editing the commit message"
lol_help = "add all files to the staging area, amend them to the last commit and force-push them to the remote repository"
back_help = "roll back by one commit (or optionally specify the number of commits to roll back by)"
baack_help = "roll back by two commits"
baaack_help = "roll back by three commits"
fire_help = "rescue changes in case of fire (commit and push changes, suspend system)"

def gitex():
  parser = argparse.ArgumentParser(prog="git gitex", usage="git <command>", description="These are special Git subcommands added by the gitex extension, which are mostly shortcuts for other Git commands or combinations of git commands.", color=False, add_help=False)
  parser.add_argument("gitex", nargs="?", help=gitex_help)
  parser.add_argument("yeet", nargs="?", help=yeet_help)
  parser.add_argument("seet", nargs="?", help=seet_help)
  parser.add_argument("amend", nargs="?", help=amend_help)
  parser.add_argument("lol", nargs="?", help=lol_help)
  parser.add_argument("back", nargs="?", help=back_help)
  parser.add_argument("baack", nargs="?", help=baack_help)
  parser.add_argument("baaack", nargs="?", help=baaack_help)
  parser.add_argument("fire", nargs="?", help=fire_help)
  parser.parse_args()
  parser.print_help()

def yeet():
  parser = argparse.ArgumentParser(prog="git yeet", description=yeet_help, color=False)
  parser.parse_args()
  subprocess.run("git push -f")

def seet():
  parser = argparse.ArgumentParser(prog="git seet", description=seet_help, color=False)
  parser.parse_args()
  subprocess.run("git push --force-with-lease --force-if-includes")

def amend():
  parser = argparse.ArgumentParser(prog="git amend", description=amend_help, color=False)
  parser.parse_args()
  if subprocess.run("git add *").returncode != 0: exit(1)
  subprocess.run("git commit --amend --no-edit")

def lol():
  parser = argparse.ArgumentParser(prog="git lol", description=lol_help, color=False)
  parser.parse_args()
  if subprocess.run("git add *").returncode != 0: exit(1)
  if subprocess.run("git commit --amend --no-edit").returncode != 0: exit(1)
  subprocess.run("git push -f")

def back():
  parser = argparse.ArgumentParser(prog="git back", description=back_help, color=False)
  parser.add_argument("-n", default=1, help="number of commits to roll back by")
  args = parser.parse_args()
  subprocess.run(f"git reset --hard HEAD~{args.n}")

def baack():
  parser = argparse.ArgumentParser(prog="git baack", description=baack_help, color=False)
  parser.parse_args()
  subprocess.run("git reset --hard HEAD~2")

def baaack():
  parser = argparse.ArgumentParser(prog="git baaack", description=baaack_help, color=False)
  parser.parse_args()
  subprocess.run("git reset --hard HEAD~3")

def fire():
  parser = argparse.ArgumentParser(prog="git fire", description=fire_help, color=False)
  parser.parse_args()
  if subprocess.run("git add *").returncode != 0: exit(1)
  if subprocess.run('git commit --allow-empty -m "rescue changes from burning up"').returncode != 0: exit(1)
  if subprocess.run("git push -f").returncode != 0: exit(1)
  if psutil.LINUX:
    subprocess.run("systemctl suspend")
  elif psutil.WINDOWS:
    subprocess.run("rundll32.exe powrprof.dll,SetSuspendState")
  elif psutil.OSX:
    subprocess.run("pmset sleepnow")
