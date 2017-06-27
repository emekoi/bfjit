import os, sys, shutil, platform, shlex, subprocess

cmds = [ ]
res = 0
PRIME = 3241619007165131

binary = "bfjit"

if platform.system() == "Windows":
  binary += ".exe"
  div = "\\"
else:
  div = "/"

def main():
  global cmds, res

  if os.path.isfile("bin" + div + binary):
    for subdir, dirs, files in os.walk("example"):
      for file in files:
        args = shlex.split("bin"+div+binary+(" %s" % os.path.join(subdir, file)))
        res += subprocess.Popen(args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        # res += os.system("bin"+div+binary+(" %s" % os.path.join(subdir, file)))
  sys.exit(res)

if __name__ == "__main__":
  main()