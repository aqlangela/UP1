import pickle

class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = [];
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0
        
    def get_total_words(self):
        return self.total_words
        
    def get_msg_size(self):
        return self.total_msgs
        
    def get_msg(self, n):
        return self.msgs[n]
        
    # implement
    def add_msg(self, m):
        self.msgs.append(m)
        
    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):
        words = m.split(" ")
        for word in words:
            try:
                self.index[word].append(l)
            except:
                self.index[word] = [l]
        
    # implement: query interface
    '''
    return a list of tuples. If we index the first sonnet (p1.txt), then
    calling this function with term 'thy' will return the following:
    [(7, " Feed'st thy light's flame with self-substantial fuel,"),
     (9, ' Thy self thy foe, to thy sweet self too cruel:'),
     (9, ' Thy self thy foe, to thy sweet self too cruel:'),
     (12, ' Within thine own bud buriest thy content,')]          
    '''                      
    def search(self, term):
        msgs = []
        indexes = []
        if term in self.index.keys():
            index = self.index[term]
        else:
            return "No results found."
        for index in indexes:
            msgs.append(self.get_msg(index))
        return msgs


class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()
        
        # Implement: 1) open the file for reading, then call
        # the base class's add_msg_and_index
    def load_poems(self):
        lines = open("AllSonnets.txt", "r").readlines()
        n_lines = []
        for l in lines:
            l = l.rstrip("\n")
            n_lines.append(l)
        for nl in n_lines:
            self.add_msg_and_index(nl)
    
        # Implement: p is an integer, get_poem(1) returns a list,
        # each item is one line of the 1st sonnet
    def get_poem(self, p):
        poem = []
        if p > 0 and p < 155:
            start = self.int2roman[p] + "."
            end = self.int2roman[p+1] + "."
            s_num = 0
            e_num = 0
            for i in range(self.get_msg_size()):
                if self.get_msg(i) == start:
                    s_num = i
                elif self.get_msg(i) == end:
                    e_num = i
                    break
                else:
                    e_num = i
            for j in range(s_num, e_num):
                poem.append(self.get_msg(j))
        else:
            raise ValueError("Index out of range")
        return poem

if __name__ == "__main__":
    # The next three lines are just for testing
    # You are encouraged to add to this and create your own tests!
    # Call your functions as you implement them and see if they work
    sonnets = PIndex("AllSonnets.txt")
    p3 = sonnets.get_poem(3)
    print(p3)
    s_love = sonnets.search("love")
    print(s_love)