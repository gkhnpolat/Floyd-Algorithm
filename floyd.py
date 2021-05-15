# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:12:15 2021

@author: Gp
"""

#FLOYD ALGORİTMASI S TABLOSU KODLARI
#Çok boyutlu dizi ve matriksler için kullanacağımız kütüphaneyi ekledik
import numpy as np
INF = 1000000000
dizi = ["A","B","C","D","E","F","G","H","S"]
#Graftaki değerlerimizin matrise dönüştürülmüş hali
graph = np.array( [[0, 4, INF, 5, INF, INF, 2, INF, INF], [4, 0, INF, INF, INF, 3, 1, 5, INF],  [INF, INF, 0, 2, 1, 3, INF, INF, 3],
         [5, INF, 2, 0, INF, 2, 1, INF, INF],  [INF, INF, 1, INF, 0, INF, INF, 1, 2], [INF, 3, 3, 2, INF, 0, INF, 2, INF],
         [2, 1, INF, 1, INF, INF, 0, INF, INF],  [INF, 5, INF, INF, 1, 2, INF, 0, 1], [INF, INF, 3, INF, 2, INF, INF, 1, 0]] )
v = len(graph)
#Matris oluşturma  ve Floyd Algoritmasının uygulanması
print("*****Floyd Algoritması S tablosunun oluşturulması*****")
print()
for i in range(0, v):
    print(" ",dizi[i], end='')
print();       
p = np.zeros(graph.shape)
for i in range(0,v):
    for j in range(0,v):
        p[i,j] = i
        if (i != j and graph[i,j] == 0): 
            p[i,j] = -30000 
            graph[i,j] = 30000 
for k in range(0,v):
    for i in range(0,v):
        for j in range(0,v):
            if graph[i,j] > graph[i,k] + graph[k,j]:
                graph[i,j] = graph[i,k] + graph[k,j]
                p[i,j] = p[k,j]
# Oluşturulan yeni matrisin yazdırılması
print(p)
print("----------------------------------------------------------------")
#FLOYD ALGORİTMASI D TABLOSU KODLARI
def floyd_warshall(vertex, adjacency_matrix):
    # En kısa yolların hesaplanması
    for k in range(0, vertex):
        for i in range(0, vertex):
            for j in range(0, vertex):
                # Değerlerin kıyaslanması
                adjacency_matrix[i][j] = min(adjacency_matrix[i][j],
                                             adjacency_matrix[i][k] + adjacency_matrix[k][j])
    print("\t"+"\t"+"****Floyd Algoritması D Tablosu****")
    #Matrisi oluşturma ve Floyd Algoritmasının uygulanması
    print("yol/yol", end='')
    for i in range(0, vertex):
        print("\t",dizi[i], end='')
    print();
    for i in range(0, vertex):
        print(dizi[i], end='')
        for j in range(0,vertex):
            print("\t{:d}".format(adjacency_matrix[i][j]), end=' ')
        print();
#Grafn matrise dönüştürülmüş hali
adjacency_matrix = [[0, 4, INF, 5, INF, INF, 2, INF, INF],
         [4, 0, INF, INF, INF, 3, 1, 5, INF],
         [INF, INF, 0, 2, 1, 3, INF, INF, 3],
         [5, INF, 2, 0, INF, 2, 1, INF, INF],
         [INF, INF, 1, INF, 0, INF, INF, 1, 2],
         [INF, 3, 3, 2, INF, 0, INF, 2, INF],
         [2, 1, INF, 1, INF, INF, 0, INF, INF],
         [INF, 5, INF, INF, 1, 2, INF, 0, 1],
         [INF, INF, 3, INF, 2, INF, INF, 1, 0]
        ]
floyd_warshall(9, adjacency_matrix);
