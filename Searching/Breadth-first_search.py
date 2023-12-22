import collections


def need_person(name, desired_name):
    return name == desired_name


def search(name, desired_name, graph):
    search_queue = collections.deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if need_person(person, desired_name):
                return print("The entered name is among your neighbors: " + person)
            else:
                search_queue += graph[person]
                searched.append(person)
    return print("There are no people with that name among your neighbors")


dict = {'A': ['B', 'C', 'D'],
        'B': ['A', 'G', 'H'],
        'C': ['A', 'E'],
        'D': ['A', 'F', 'G'],
        'E': ['C', 'J', 'L'],
        'F': ['D', 'J'],
        'G': ['B', 'D', 'K'],
        'H': ['B', 'I'],
        'I': ['H'],
        'J': ['E', 'F'],
        'K': ['G'],
        'L': ['E']}
print("A, B, C, D, E, F, G, H, I, J, K, L")
desired_name = input("Enter the letter you want to find (from the ones shown above): ")
search('A', desired_name, dict)
