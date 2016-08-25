#!/usr/bin/python -tt

import os
import sys
import subprocess

class gits(object):
  """docstring for gits"""
  def __init__(self, git1, git2):
    super(gits, self).__init__()
    self.git1 = git1
    self.git2 = git2
  def git_subtree(self):
    a = self.git1
    b = self.git2
    os.chdir(b)
    c = 'git subtree add --prefix=git1 '+git1+' master'
    #print c
    process = subprocess.Popen(c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutput, stderroutput = process.communicate()
    #print os.getcwd() + ' pwdforsubtree '+stdoutput+ stderroutput + '  errs'
    #print a + '  git2 from class gits'
    #print b + '  git1 from class gits'




class tags(object):
  """docstring for tags"""
  def __init__(self, git2):
    super(tags, self).__init__()
    self.git1 = git1
    self.git2 = git2
    self.vgitdescribe = 'git describe --tags'
    self.add_tag_str = 'git tag -f'
      ### fatal: Not a git repository (or any of the parent directories): .git
      ### fatal: No names found, cannot describe anything.
  def check_tag(self, dir):
    pwd = os.getcwd()
    os.chdir(dir)
    process = subprocess.Popen(self.vgitdescribe,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutput, stderroutput = process.communicate()
    print stdoutput + '^^^ out'
    print stderroutput + '^^^ err'
    os.chdir(pwd)
    try:
      tag = int(stdoutput)
      return tag
    except ValueError:
      errchk = stderroutput[9]
      if errchk == 't':
        raise Exception('~~~***      ***      ***~~~\n        ~~~***###NOT a git repo!###***~~~')
      else:
        return None
  def add_tag(self):
    #print a + '  git2 from class gits'
    tag = self.check_tag(self.git2)
    if tag == None:
      tag = self.check_tag(self.git1)
    if tag == None:
      tag = 0
    else:
      tag += 1
    a = self.add_tag_str.split()
    a.append(str(tag))
    print a
    os.chdir(git2)
    process = subprocess.Popen(" ".join(a), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdoutput, stderroutput = process.communicate()
    print ' '.join(a)
    print stdoutput + stderroutput + 'errs & out'
    print os.getcwd() + ' pwd \n'


def do_stuff(git1,git2):
  pwd=  os.getcwd()
  a = gits(git1,git2)
  os.chdir(pwd)
  b = tags(git2)
  os.chdir(pwd)
  b.check_tag(git1)
  os.chdir(pwd)
  b.check_tag(git2)
  os.chdir(pwd)
  a.git_subtree()
  os.chdir(pwd)
  b.add_tag()
  print "Job done!"
  pass


# Calls the above functions with interesting inputs.
def main():
  print 'Git task'
if len(sys.argv) != 3:
  print 'usage: ./try.py git1 folder git2 folder'
  sys.exit(1)
git1 = sys.argv[1]
git2 = sys.argv[2]
if os.path.isdir(git1) and os.path.isdir(git2):
  do_stuff(git1,git2)
else:
  print 'unknown option: ' + git1 +"  "+git2+" ;"
  sys.exit(1)

if __name__ == '__main__':
  main()
