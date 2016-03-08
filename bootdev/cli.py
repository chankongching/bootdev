#!/usr/bin/env python
import optparse
import re
import os
import subprocess
import boto3

def initialize():
  print "initialize"
  from os.path import expanduser
  home = expanduser("~")
  if os.path.isfile(home + "/.aws/config"):
    print "AWS credrentials config exists"
  else:
    print "AWS credrentials config NOT exists"
         
def main():
  p = optparse.OptionParser()
  p.add_option('-i', '--init', action="callback", callback=initialize)
#  print p.parse_args(['-i'])
#  options, arguments = p.parse_args()
  print "test"

#  p.add_option('--name', '-l', default="world")
#  options, arguments = p.parse_args()
#  line = re.sub(r"http.*?\.coconuts.co\/", "",options.name)
#  path = re.sub(r"\/([^\/]+)$", "",line)
#  print 'Hello %s' % options.name
#  if not os.path.exists("/var/www/html/" + path):
#    os.makedirs("/var/www/html/" + path)
#  CURR_DIR = os.getcwd()
#  #CMD = "wget http://" + CURR_DIR + "/ " + line + " /var/www/html/" + path
#  CMD = "wget http://bali.coconuts.co/" + line + " -P /var/www/html/" + path
#  print CMD
#  os.system(CMD)
  #from subprocess import call
  #call([CMD])
  #print re.search('(?<=\/)\w+', CURR_DIR)
  #print line
         
if __name__ == '__main__':
  main()


