#https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
   s_lst = list(string)
   s_lst[position] = character
   string_value = "".join(s_lst)

   return string_value

if __name__ == '__main__':
   s = input()
   i, c = input().split()
   s_new = mutate_string(s, int(i), c)
   print(s_new)
