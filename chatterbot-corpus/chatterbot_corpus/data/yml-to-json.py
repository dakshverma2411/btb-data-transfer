# import os
# from os import listdir
# import yaml
# import json
# import tensorflow as tf
# import tensorflow_hub as hub 
import numpy as np

# GOOGLE_EMBEDDINGS_TF_HUB_URL = "https://tfhub.dev/google/universal-sentence-encoder/4"

# ROOT_PATH = "D:\\Minor-Project\\chatterbot-corpus\\chatterbot_corpus\\data\\english"

# os.chdir(ROOT_PATH)

# files = os.listdir()
# l = []
# for file in files:
# 	if file[-3:] == 'yml':
# 		with open(ROOT_PATH+'\\'+file, 'r') as f:
# 			try:
# 				parsed_yaml=yaml.safe_load(f)
# 				l.extend(parsed_yaml['conversations'])
# 			except yaml.YAMLError as exc:
# 				print(exc)

# # d = {'conversations':l}
# l1 = [i[0] for i in l]
# print(len(l1))

# with tf.device('/CPU:0'):
# 	embed = hub.load(GOOGLE_EMBEDDINGS_TF_HUB_URL)

# with tf.device('/CPU:0'):
# 	embeddings = np.array(embed(l1))
# 	print(embeddings.shape)
# 	print(embeddings)
# 	np.save("dataset.npy", embeddings)

a = np.load("D:\\Minor-Project\\chatterbot-corpus\\chatterbot_corpus\\data\\english\\dataset.npy")
print(a.shape[0])