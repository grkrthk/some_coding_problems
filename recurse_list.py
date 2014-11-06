import re

def recurse(string):

      if len(string)==1:
                     return [string];
      my_letter = string[0];
      rest_letters = string[1:];
      my_list_str = list();    

      returned_list = recurse(rest_letters);      
      for each_string in iter(returned_list):             
              for i in range (0, len(each_string)):
                           mod_string = each_string[:i] + my_letter + each_string[i:]
                           my_list_str.append(mod_string);                                                      
              my_list_str.append(each_string + my_letter);

      return my_list_str

my_list = recurse("win")
print my_list
