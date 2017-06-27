import os, sys, shutil, platform, shlex, subprocess
# from  import Popen, PIPE, STDOUT

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
        if file != "factor.bf":
          res += os.system("bin"+div+binary+(" %s" % os.path.join(subdir, file)))
  sys.exit(0)

if __name__ == "__main__":
  main()