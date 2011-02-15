import re 

leading_spaces_to_dots = re.compile('^( *)')
line_number = 0
with open('roman1.py', encoding='utf8') as a_file:
   for a_line in a_file:
      line_number += 1
      a_line = leading_spaces_to_dots.sub(lambda m: '.' * len(m.group(1)) if m.group(1) else '' , a_line)
      print('{:>4} {}'.format(line_number, a_line.rstrip()))

