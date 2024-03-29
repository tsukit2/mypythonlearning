def buildConnectionString(params):
   """Build a connection string from a diction of parameters.

   Return string."""
   return ";".join(["%s=%s" % (k,v) for k, v in params.items()])

if __name__ == "__main__":
   myParams = {"server": "mypilgrim", \
               "database":"master", \
               "uid":"sa", \
               "pwd":"secret"\
               }
   print buildConnectionString(myParams)


