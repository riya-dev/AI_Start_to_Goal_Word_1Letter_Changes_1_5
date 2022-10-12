# Name: Riya Dev
# Date: 10/19/2020
import time

class HeapPriorityQueue():
   # copy your HeapPriorityQueue() from Lab3
   def __init__(self):
      self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
      self.current = 1        # to make this object iterable

   def next(self):            # define what __next__ does
      if self.current >=len(self.queue):
         self.current = 1     # to restart iteration later
         raise StopIteration
    
      out = self.queue[self.current]
      self.current += 1
   
      return out

   def __iter__(self):
      return self
      
   __next__ = next

   def isEmpty(self):
      return len(self.queue) == 1    # b/c index 0 is dummy

   def swap(self, a, b):
      self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

   # Add a value to the heap_pq
   def push(self, value):
      self.queue.append(value)
      # write more code here to keep the min-heap property
      self.heapUp(len(self.queue)-1)

   # helper method for push      
   def heapUp(self, k):
      while k > 1: # ALL GOOD
         parent = k // 2
         # print("parent", self.queue[parent], "k", self.queue[k])
         if (self.queue[parent] < self.queue[k]): # if current larger than parent, swap
            return
         self.swap(parent, k)
         k = parent
               
   # helper method for reheap and pop
   def heapDown(self, k, size):
      left, right = 2 * k, 2 * k + 1

      if left == size and self.queue[k] > self.queue[size]: # last case
         self.swap(k, size)
      
      elif right <= size:
         min = (left if self.queue[left] <= self.queue[right] else right)
   
         if self.queue[k] > self.queue[min]:
            self.swap(k, min)
            self.heapDown(min, size)
   
   # make the queue as a min-heap            
   def reheap(self):
      for x in range(len(self.queue)//2, 0, -1):
         self.heapDown(x, size)
   
   # remove the min value (root of the heap)
   # return the removed value            
   def pop(self):
      # Your code goes here
      self.swap(1, len(self.queue)-1)
      pop = self.queue.pop()
      self.heapDown(1, len(self.queue)-1)
      return pop
      
   # remove a value at the given index (assume index 0 is the root)
   # return the removed value   
   def remove(self, index):
      # Your code goes here
      self.swap(index + 1, len(self.queue)-1) #swap with last index, index + 1 because of dummy
      pop = self.queue.pop()
      self.heapDown(index + 1, len(self.queue)-1)
      return pop
      
def dist_heuristic(state, goal = "_123456789ABCDEF", size=4):
   count = 0
   for i in range(0, len(state)):
      if state[i] != goal[i]: count += 1
   return count

def display_path(path_list, size):
   for n in range(size):
      for path in path_list:
         print (path[n*size:(n+1)*size], end = " "*size)
      print ()
   print ("\nThe shortest path length is :", len(path_list))
   return ""

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

def a_star(start, goal, words_set):
   heuristic = dist_heuristic
   frontier = HeapPriorityQueue()
   h = heuristic(start)
   explored = {}
   explored[start] = h
   frontier.push((h, start, [start]))
   
   while not frontier.isEmpty():
      p = frontier.pop()
      if p[1] == goal:
         display_path(p[2], 4)
         return ""
      for a in generate_adjacents(p[1], words_set):
         g = len(p[2]) + 1
         h = heuristic(a)
         if a not in explored or explored[a] > h + g:
            frontier.push((h + g, a, p[2]+[a]))
            explored[a] = h + g
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
   path = (a_star(initial, goal, words_set))
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