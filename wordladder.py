class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


"""""
start word = hit
ending word = cog

figure out which letters to change, one at a time, so that we go from hit -> cog

start word = hit 
ending word = cog

hit --> hot --> hog --> cog

sail -> tail -> toil  -> coil  -> coal -> coat  ->  boat
sail -> 

""" ""


def find_ladder(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path
            for neighbors in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbors)
                q.enqueue(path_copy)
    return None


word_set = set()
with open("words.txt") as f:
    for line in f:
        word = line.strip()
        word_set.add(word)
import string

letters = list(string.ascii_lowercase)


def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w == word:
                continue
            if w in word_set:
                neighbors.append(w)
    return neighbors


print(find_ladder("sail", "boat"))
print(find_ladder("fuck", "shit"))

