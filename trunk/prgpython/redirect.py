from io import StringIO
import sys
import os

class OutputRedirector:
   def __init__(self, redirect):
      self.old = sys.stdout
      self.redirect = redirect

   def __enter__(self):
      sys.stdout = self.redirect
      return self

   def __exit__(self, exc_type, exc_value, traceback):
      sys.stdout = self.old


def countit(to):
   for n in range(to):
      print(n)


if __name__ == '__main__':
   print('Count normally:')
   countit(10)

   with OutputRedirector(StringIO()) as output:
      countit(10)

   print('Count redirect:')
   print(output.redirect.getvalue())

   with OutputRedirector(StringIO()) as output:
      os.system('ls')

   print('Result of ls')
   print(output.redirect.getvalue())
      

