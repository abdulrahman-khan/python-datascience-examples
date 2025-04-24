import numpy as np
from lightfm import LightFM
from lightfm.datasets import fetch_movielens
from lightfm.evaluation import precision_at_k

#get data
data = fetch_movielens(mine_ratings=4.0)


print(repr(data['train']))
print(repr(data['train']))