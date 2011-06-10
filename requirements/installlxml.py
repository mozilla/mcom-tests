cmd="STATIC_DEPS=true easy_install 'lxml>=2.2alpha1'"
try:
   import lxml
   print 'libxml already installed'
except ImportError, e:
    import commands
    commands.getoutput(cmd)
   
