"""
from sklearn.cluster import KMeans
import numpy as np
from numpy import genfromtxt
import itertools
from scipy.spatial import distance
from sklearn.metrics import silhouette_score
from collections import defaultdict

actual_label = genfromtxt('/home/acer/PycharmProjects/SOMBatchTest_fix/SOMPY-master/data_set/spherical_5_2.csv', delimiter=',',usecols=(2))
actual_label=actual_label.tolist()
print actual_label

Idata = genfromtxt('/home/acer/PycharmProjects/SOMBatchTest_fix/SOMPY-master/data_set/spherical_5_2.csv', delimiter=',',usecols=(0,1))
print Idata.shape

"""
def cal_Db(centers):
    distance_list = []
    for a, b in itertools.combinations(centers, 2):
        #print "a,b  : ", a,b
        d1 = distance.euclidean(a, b)
        #print "distance : ", d1
        #print "----------------------"
        distance_list.append(d1)
    Db = max(distance_list)
    return Db

def cal_Ew(Idata, label, centers):
    Ew=0
    for i in range(len(label)):
        Ew+= distance.euclidean(Idata[i], centers[label[i]])
    return Ew


def cal_Et(Idata ):
    Et=0
    barycenter=np.mean(Idata)
    #print "means of Idata : ", barycenterprint "oooo"
    for i in Idata:
        d = distance.euclidean(i,barycenter)
        Et+=d
    return Et

def cal_pbm_index(K, Idata, obtained_centers, obtained_label):
    Db=cal_Db(obtained_centers)
    Ew=cal_Ew(Idata, obtained_label, obtained_centers)
    Et=cal_Et(Idata)
    #print Db,Ew, Et
    x=(1/float(K))*(Et/Ew)*((Db))
    #print x
    pbm_index=x*x
    return pbm_index



cluster =  KMeans(n_clusters=n,init=X) #KMeans(n_clusters=n)
cluster.fit(Idata)
obtained_centers = cluster.cluster_centers_
obtained_label = cluster.predict(Idata)


print "centers : ", obtained_centers
print "labels : ", obtained_label
print "\n PBM index : ", cal_pbm_index(n, Idata, obtained_centers, obtained_label)

#from sklearn.metrics.cluster.supervised import adjusted_rand_score
#new_ari = adjusted_rand_score(actual_label, obtained_label)




"""
def calculate_dunn_index( data, label,n_cluster=0):
    data=data.tolist()
    d1=[]
    d2=[]
    d3=[]
    cluster_data=defaultdict(list)
    for i in range (n_cluster):
        for j in range (len(label)):
            if label[j]==i:
                cluster_data[i].append(data[j])
    for k,v in cluster_data.iteritems():
        cluster_list=cluster_data[k]
        for i in range (len(cluster_list)):
            temp1=cluster_list[i]
            for j in range(len(cluster_list)):
                temp2 = cluster_list[j]
                dist = np.linalg.norm(np.asarray(temp1) - np.asarray(temp2))
                d1.insert(j,dist)
            d2.insert(i,max(d1))
            d1=[]
        d3.insert(k,max(d2))
        d2=[]
    xmax= max(d3)
    #################################################################################################
    #Calcuation of minimum distance
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    for k, v in cluster_data.iteritems():
        cluster_list=cluster_data[k]
        for j in range(len(cluster_list)):
            temp1=cluster_list[j]
            for key,value in cluster_data.iteritems():
                if not key==k:
                    other_cluster_list=cluster_data[key]
                    for index in range ((len(other_cluster_list))):
                        temp2=other_cluster_list[index]
                        dist=np.linalg.norm(np.asarray(temp1)-np.asarray(temp2))
                        d1.insert(index,dist)
                    d2.insert(key,min(d1))
                    d1=[]
            d3.insert(j,min(d2))
            d2=[]
        d4.insert(k,min(d3))
    xmin=min(d4)
    dunn_index= xmin/xmax
    return dunn_index


n=5
X = np.array([[5.81,9.792917],
              [10.380698, 14.215349],
              [13.987600,10.116400],[10.021698,6.437547],[9.758393,10.545536]], np.float64)
cluster =  KMeans(n_clusters=n,init=X) #KMeans(n_clusters=n)
cluster.fit(Idata)
obtained_centers = cluster.cluster_centers_
obtained_label = cluster.predict(Idata)

from sklearn.metrics.cluster.supervised import adjusted_rand_score
new_ari = adjusted_rand_score(actual_label, obtained_label)
print "centers : ", obtained_centers
#print Idata[1]
print "labels : ", obtained_label
print "\n PBM index : ", cal_pbm_index(n, Idata, obtained_centers, obtained_label)
print "ARI : ", new_ari
ss = silhouette_score(Idata,obtained_label)
print "Sil SCore :",  ss
print "dunn index :", calculate_dunn_index(Idata, obtained_label, n_cluster=n)

"""

