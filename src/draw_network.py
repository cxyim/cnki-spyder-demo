import networkx as nx
import matplotlib.pylab as plt
import csv
from pprint import pprint as fprint
plt.rcParams["font.sans-serif"]=["SimHei"]

def get_all_bigram_of_list(target_list):
    res_list = list()
    for i in range(0,len(target_list)-1):
        for j in range(i+1,len(target_list)):
            #print(i,j)
            res_list.append((target_list[i],target_list[j]))
    return res_list

def test():
    test_list = list("abcd")
    fprint(test_list)
    fprint(get_all_bigram_of_list(test_list))
    

def draw():
    input_file = open("res.csv","r",encoding="utf-8")
    csv_reader = csv.reader(input_file,delimiter="\t")

    tuple_list = list()
    single_author_list = list()
    for row in csv_reader:
        name_list = row[1].split(";")
        if len(name_list) > 1:
            tuple_list.extend(get_all_bigram_of_list(name_list))
        else:
            single_author_list.append(name_list[0])
    
    print("single_author_list",len(single_author_list))
    print("tuple_list",len(tuple_list))
    #fprint(tuple_list)  

    node_set = set()
    rel_set = set()
    freq_dict = dict()
    for a,b in tuple_list[:2000]:
        node_set.add(a)
        node_set.add(b)
        rel_set.add((a,b))
        freq_dict[a] = freq_dict.get(a,0)+1
        freq_dict[b] = freq_dict.get(b,0)+1
    print("node_set",len(node_set))
    print("rel_set",len(rel_set))

    node_size_list = [x*3 for x in freq_dict.values()]

    graph = nx.Graph()
    graph.add_nodes_from(node_set)
    graph.add_edges_from(rel_set)

    plt.figure(figsize=(20,16),dpi=300)
    nx.draw_networkx(graph,pos=nx.spring_layout(graph),node_size=node_size_list,node_color="gray",edge_color="gray",alpha = 0.5,font_size=3,font_color="black")
    plt.savefig(r"graph.png")
    
if __name__ == "__main__":
    #test()
    draw()
