import os, sys, shutil, platform

cmds = [ ]
res = 0

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
        res += os.system("bin"+div+binary+(" %s" % os.path.join(subdir, file)))
  sys.exit(res)

if __name__ == "__main__":
  main()