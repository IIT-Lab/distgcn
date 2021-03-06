import time
import numpy as np
from utils import *

def evaluate(sess, model, features, support, placeholders):
    t_test = time.time()
    feed_dict_val = construct_feed_dict4pred(features, support, placeholders)
    outs_val = sess.run([model.outputs_softmax], feed_dict=feed_dict_val)
    return (time.time() - t_test), outs_val[0]

def findNodeEdges(adj):
    nn = adj.shape[0]
    edges = []
    for i in range(nn):
        edges.append(adj.indices[adj.indptr[i]:adj.indptr[i+1]])
    return edges

def isis_v2(edges, nIS_vec_local, cn):
    return np.sum(nIS_vec_local[edges[cn]] == 1) > 0

def isis(edges, nIS_vec_local):
    tmp = (nIS_vec_local==1)
    return np.sum(tmp[edges[0]]*tmp[edges[1]]) > 0

def fake_reduce_graph(adj):
    reduced_node = -np.ones(adj.shape[0])
    reduced_adj = adj
    mapping = np.arange(adj.shape[0])
    reverse_mapping = np.arange(adj.shape[0])
    crt_is_size = 0
    return reduced_node, reduced_adj, mapping, reverse_mapping, crt_is_size

def fake_local_search(adj, nIS_vec):
    return nIS_vec.astype(int)

