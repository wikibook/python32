import glob
import os.path
ndir = nfile = 0

def traverse( dir, depth ):
  global ndir, nfile
  for obj in glob.glob( dir+'/*'):
    if depth==0:
      prefix = '|--'
    else:
      prefix = '|' + '   '*depth + '|--'
    if os.path.isdir( obj ):
      ndir+=1
      print( prefix + os.path.basename(obj) )
      traverse( obj, depth+1 )
    elif os.path.isfile( obj ):
      nfile+=1
      print( prefix + os.path.basename( obj ) )
    else:
      print( prefix + 'unknown object :', obj )

if __name__=='__main__':
  traverse( '.', 0 )
  print( '\n', ndir, 'directories,', nfile,'files' )
  input()