# Name: Riya Dev
# Date: 10/17/2020
# updated. it takes a bit long - up to 55 seconds on my computer
import time

def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it '''
   adj_set = set()
   # TODO 1: adjacents
   # Your code goes here
   for i in range(0, 6):
      part1 = current[:i]
      part2 = current[i+1:]
      #print("part 1 ", part1, "part 2 ", part2)
      
      for word in words_set:
          if part1 == word[:i] and part2 == word[i+1:] and word != current:
            adj_set.add(word)
            #print(word)
            
   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def generate_path(s, explored):
   l = []
   
   while explored[s] != "":
      l.append(s)
      s = explored[s]
      
   l = l[::-1]
   
   return l[:-1]
   
def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   frontier = [[start], [goal]]
   explored = [{start: ""}, {goal: ""}]
   k = 1
   
   while frontier[0] and frontier[1]:
      k = 1 - k
      temp = frontier[k][:]
      frontier[k] = []
      
      while temp:
         s = temp.pop(0)
         if s in frontier[1 - k]:
            return [start] + generate_path(s, explored[0]) + [s] + generate_path(s, explored[1])[::-1] + [goal]
         for a in generate_adjacents(s, words_set):
            if a not in explored[k]:
               frontier[k].append(a)
               explored[k][a] = s
   return None 
   
def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   
   #print ("Check generate_adjacents():", check_adj(words_set))
   
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path = (bi_bfs(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''