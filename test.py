import os, sys, shutil, platform

cmds = [ ]
res = 0

def main():
  global cmds, res

  if os.path.isfile("bin/conf"):
    for subdir, dirs, files in os.walk("example"):
      for file in files:
        if platform.system() == "Windows":
          cmds += [ "bin\\bfjit %s" % os.path.join(subdir, file) ]
        else:
          cmds += [ "bin/bfjit %s" % os.path.join(subdir, file) ]

    for cmd in cmds:
      res += os.system(cmd)
    
  sys.exit(res)

if __name__ == "__main__":
  main()