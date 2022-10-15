#!/usr/bin/env python3
import datetime
starttime=datetime.datetime.now()
##########################################################################################
##
##  this program reads an english text and writes out each sentence.
##
##########################################################################################

## ---------------------------------------------------------------------------------------
##  concatenate project directory paths
project     = '\\Users\\cd0sm\\Documents\\CSHOUNDS'
project     = '/Users/lfhawley/Documents/WHITE/Computing/Code/Python/Projects/cdmenard'

program     = '/sentences'              # the program name w/out the suffix '.py'

executables = '/code/executables'
modules     = '/code/modules'

inputdir    = '/data/input'

outputpath  = '/data/output'            # general output 'path'...
outputdir   = '/data/output'+program    # ...to the directory for this program's output

## ---------------------------------------------------------------------------------------
##  print directory paths
print()
print('is everything where it should be?....')
print()
print('project path: ',project)
print('executable:   ',executables+program+'.py')
print('modules dir:  ',project+modules)
print('input  dir:   ',inputdir)
print('output dir:   ',outputdir)
print()

## ---------------------------------------------------------------------------------------
## python modules
import sys                  ##  'system' - python class enabling imports of custom modules
sys.path.insert(0, project+modules) ##  'sys' invoking the path to 'modules'

## ---------------------------------------------------------------------------------------
## custom modules
import filewin   as fw      ##  win terminal file creation commands

## ---------------------------------------------------------------------------------------
## functions
def somefunction(x,y):
    return

## ---------------------------------------------------------------------------------------
## allocate new output directory
fw.delete(project+outputpath)              # delete output directory and path
fw.define(project+outputpath)              # define output path
fw.define(project+outputpath+program)      # define output directory
fw.permission(project+outputpath+program)  # grant permission for the output dir

print('did the output directory get created?....')
print('output directory: ',project+outputpath+program)
print()

## ---------------------------------------------------------------------------------------
##  open input file for read / open output file for write
filename="/houndofthebaskervilles.txt"

inputpathname=  (project+inputdir+filename)
outputpathname= (project+outputdir+filename)

print('is the input where it should be?....')
print('input file:  ',inputpathname)
print()
print('is this a valid file name for the output?....')
print('output file: ',outputpathname)
print()

## ---------------------------------------------------------------------------------------
##  open input file for read / open output file for write
input =open(inputpathname,'r')
output=open(outputpathname,'w')
print('did the output file get created?....')
print('output file: ',outputpathname)
print()

## ---------------------------------------------------------------------------------------
##  main loop

linesread=0
lineswritten=0

for line in input:
	linesread=linesread+1
	#print(line)
	output.write(line)
	lineswritten=lineswritten+1

input.close
output.close


## ---------------------------------------------------------------------------------------
##  reporting

print("----------------------")
print('Totals for',program)
print()
print('  lines read from ',inputdir+filename,linesread)
print('  lines written to',outputdir+filename,lineswritten)
print()

##  get endtime and runtime
endtime=datetime.datetime.now()
runtime=(endtime-starttime)

print("----------------------")
print("started: ",starttime)
print("ended:   ",endtime)
print()

#content=dir()
#print('CONTENT   ',content)

## ---------------------------------------------------------------------------------------
##  end of job
