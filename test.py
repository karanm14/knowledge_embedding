# You need to write down your own code here
# Task: Given any head entity name (e.g. Q30) and relation name (e.g. P36), you need to output the top 10 closest tail entity names.
# File entity2vec.vec and relation2vec.vec are 50-dimensional entity and relation embeddings.
# If you use the embeddings learned from Problem 1, you will get extra credits.
#entity2vec.txt and #relation2vec.txt
import numpy as np
import sys

# You need to write down your own code here
# Task: Given any head entity name (e.g. Q30) and relation name (e.g. P36), you need to output the top 10 closest tail entity names.
# File entity2vec.vec and relation2vec.vec are 50-dimensional entity and relation embeddings.
# If you use the embeddings learned from Problem 1, you will get extra credits.
import numpy as np
import sys

USE = "folder"

L1=True
def read_vec_by_id(file):
    e = {}
    f = open("%s/%s2id.txt" % (USE, file), "r").readlines()
    g = open("%s/%s2vec.vec" % (USE, file), "r").readlines()
    f.pop(0)
    for k in f:
        i, r = k.split()
        v = [float(k) for k in g[int(r)].split()]
        e[i] = np.asarray(v)
    return e
   

def search(vec, entity, return_n=10):
    distance = {}
    for k, v in entity.items():
        if L1:
            distance[k] = np.linalg.norm(vec - v, ord=1)
        else:
            distance[k] = np.linalg.norm(vec - v, ord=2)    
    distance = sorted(distance.items(), key=lambda k: k[1])
    return distance[:return_n]

    
def main():
    entity = read_vec_by_id("entity")
    relation = read_vec_by_id("relation")
    
    while True:
        choice = raw_input("Find Tail Entity given closest head entity and relation? [Y/n] ").lower()
        assert choice in ["y", "n"]
        if choice == "y":
            entity_id = raw_input("Entity: ")
            relation_id = raw_input("Relation: ")
            tail_vec = entity[entity_id] + relation[relation_id]
            tail_ids = search(tail_vec, entity)
            for i, k in enumerate(tail_ids):
                print("%0d Tail: %6s Score: %.4f" % (i + 1, k[0], k[1]))
        else:
            print("Given head and tail entity the closest relation is")
            entity_id1 = raw_input("Entity 1: ")
            entity_id2 = raw_input("Entity 2: ")
            rel_vec = entity[entity_id1] - entity[entity_id2]
            rel_ids = search(rel_vec, relation)
            for i, k in enumerate(rel_ids):
                print("%0d Tail: %6s Score: %.4f" % (i + 1, k[0], k[1]))
        choice = raw_input("Exit? [Y/n] ").lower()
        assert choice in ["y", "n"]
        if choice == "y":
            sys.exit()

            
if __name__ == "__main__":
    main()