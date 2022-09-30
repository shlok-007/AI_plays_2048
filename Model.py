from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
import pickle as pk

nm=input("Enter your name: ")

pos_data=np.array(np.genfromtxt('position_data_'+nm+'.csv',delimiter=",",dtype=int))
target_data=np.array(np.genfromtxt('target_data_'+nm+'.csv',delimiter=",",dtype=int))

# dataset={target_names:np.array(["w","a","s","d"]),data:pos_data,target:target_data}

X = pos_data
Y = target_data

clf = RandomForestClassifier()

print("Training the model on your data")

clf.fit(X, Y)

print("Feature importances\n",clf.feature_importances_)

model_file=open('model_'+nm+'.bin', 'wb')

pk.dump(clf, model_file)

model_file.close()

# loaded_model = pk.load(open('model_1.bin', 'rb'))
