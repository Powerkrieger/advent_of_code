all_dirs2 = []

class Node:

    def __init__(self, data):
        self.parent = None
        self.content = []
        self.dir = data
        self.size = 0


    def insert_size(self, size):
        self.size += size
        #print(self.size)
        if self.parent:
            self.parent.insert_size(size)

    def insert(self, data):
        if type(data) == type(Node("/")):
            data.parent = self
        self.content.append(data)


    def move_to(self, string: str):
        if string.startswith("$ cd .."):
            return self.parent
        if string.startswith("$ cd"):
            elem1 = string[5:].strip()
            for elem2 in self.content:
                if type(elem2) == type(Node("/")) and elem2.dir == elem1:
                    return elem2

    def PrintTree(self):
        for data in self.content:
            if type(data) == Node:
                data.PrintTree()
            else:
                print(data)
        print(self.dir)

    def list_those(self):
        sum = 0
        for data in self.content:
            if type(data) == type(Node("/")):
                sum += data.list_those()

                #if data.size <= 100000:
                    #print(str(data.dir) + " - " + str(data.size))
                #sum += int(data.size)
            else:
                sum += int(data)

        all_dirs2.append([sum, self.dir])
        return sum

    def all_dirs(self):
        all_dirs = []
        for data in self.content:
            if type(data) == type(Node("/")):
                all_dirs.extend(data.all_dirs())
                all_dirs.append([data.size, data.dir])
        return all_dirs

with open("input_day_07.txt", "r+") as file1:
    root = Node("/")
    active = root
    sum = 0
    for line in file1:
        #print(type(active))
        if line.startswith("$ cd") and not line.startswith("$ cd /"):
            active = active.move_to(line.strip())
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            data = line[4:].strip()
            active.insert(Node(data))
        elif line.strip() != "" and not line.startswith("$ cd /"):
            size, name = line.split(" ")
            active.insert_size(int(size))
            active.insert(int(size))
            sum += int(size)

    print("used:")
    print(sum)
    print(root.list_those())


    filesystem_size = 70000000
    needed_size = 30000000
    free_space = filesystem_size-sum
    print("free space:" + str(free_space))
    needed_space = needed_size-free_space

    print("needed: " + str(needed_space))

    dir1 = None
    max = filesystem_size
    for size, dir2 in all_dirs2:
        if size < needed_space:
            continue
        elif size < max:
            max = size
            dir1 = dir2

    print("dir " + str(dir1) + " with size " + str(max))
