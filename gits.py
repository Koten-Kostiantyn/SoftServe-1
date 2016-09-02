#!/usr/bin/python -tt
# ver 1.2
# kotkotkot@i.ua

import os
import sys
import subprocess

def bash(command,debug=0):  # here we execute bash commands (git subtree, etc)
### I dont wont to create class. I think it is better choise here
### Correct me if I'm wrong
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdoutput, stderroutput = process.communicate()
  if debug == 1:          # debug section, show all output of bash commands
    print 'BEGIN  stdoutput '
    print stdoutput
    print 'END  stdoutput '
    print 'BEGIN  stderroutput '
    print stderroutput
    print 'END  stderroutput '
  if stderroutput != '':
    if 'fatal:' in stderroutput.split():
      raise Exception(stderroutput)
    print stderroutput
  return stdoutput

class gits(object):
  """docstring for gits"""
  def __init__(self, git1, git2):
    super(gits, self).__init__()
    self.git1 = git1
    self.git2 = git2
    self.subtree = 'git subtree add --prefix='
    self.branch_list = []
    self.check_git = 'git rev-parse --git-dir'
    self.push_origin_master_str = 'git push origin master'
    self.branch_str_get = "git remote show origin | grep tracked | awk '{print $1}' ORS=' '"
  def git_subtree(self,branch,count):            # execute command git subtree
    a = self.git1
    self.checkout(branch)
    os.chdir(self.git2)
    if count != 1:
      c = self.subtree+os.path.basename(a)+'_'+branch+' '+a+' '+branch
    else:
      c = self.subtree+os.path.basename(a)+' '+a+' '+branch
    print c
    bash(c)
  def is_it_git_repo(self,dir):     # here we check if it is a git repo in directory
    pwd = os.getcwd() 
    os.chdir(dir) 
    bash(self.check_git)
  def push_origin_master(self):
    bash(self.push_origin_master_str)
    pass
  def get_branches(self):       # using magic(git,grep,awk) we getting all branch names
    a = self.git1
    os.chdir(a)
    branch_str = bash(self.branch_str_get)
    list = branch_str.split()
    a = []
    print self.branch_str_get
    for x in list:
      a.append(x)
    return a
  def checkout(self,branch):      # creating local branch to able to do git subtree
    os.chdir(self.git1)
    if branch != 'master':
      d = 'git checkout -b '+branch+' origin/'+branch
      print d
      bash(d)
    pass

###########################################################
### This stuff should be rewritten
###########################################################
class tags(object):
  """docstring for tags"""
  def __init__(self, git2):
    super(tags, self).__init__()
    self.git1 = git1
    self.git2 = git2
    self.vgitdescribe = 'git describe --tags'
    self.add_tag_str = 'git tag -f'
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

def do_stuff_and_tags(git1,git2):
  pwd =  os.getcwd()
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
###########################################################
### This stuff should be rewritten END                     
########################################################### 

def do_stuff(git1,git2):
  a = gits(git1,git2)
  a.is_it_git_repo(git1)
  a.is_it_git_repo(git2)
  branches = a.get_branches()
  print len(branches)
  print 'lenbrabch'
  for x in branches:
    a.git_subtree(x,len(branches))
  #a.push_origin_master()
  print "Job done!"
  pass

def main():
  if len(sys.argv) not in range(3,5): # 5 is not in range!
    print 'usage: ./try.py git1 folder git2 folder (optional -t to merge tags)'
    print 'we will merge repo1 ---> repo2'
    sys.exit(1)
  git1 = os.path.abspath(sys.argv[1]) ### full path everytime
  git2 = os.path.abspath(sys.argv[2])
  if len(sys.argv) == 4: tag_arg = sys.argv[3]
  else: tag_arg = None
  if os.path.isdir(git1) and os.path.isdir(git2): #if you with to use tags,
    if tag_arg == '-t':                           #but i don't reccomend for now 
      do_stuff_and_tags(git1,git2)
    else:
      do_stuff(git1,git2)                         # start algorythm
  else:
    print 'unknown option: ' + git1 +"  "+git2+" ;"
    sys.exit(1)
  
if __name__ == '__main__':
  main()