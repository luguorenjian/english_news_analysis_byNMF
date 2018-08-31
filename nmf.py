#coding:utf-8
from numpy import *

# 同じ形の行列AとBに対しA-Bのフロベニウスノルムの２乗を返す
def squared_frobenius_norm(A,B):
    norm=0
    for i in range(shape(A)[0]):
        for j in range(shape(A)[1]):
            norm+=pow(A[i,j]-B[i,j],2)
    return norm

# Vの各行ベクトルの成分の値の和が１になるように正規化する．
# ただしUVの値は変わらないようにする．
def normalize_V(U,V):
    for i in range(shape(V)[0]):
        total=0
        for j in range(shape(V)[1]):
            total+=V[i,j]
        for j in range(shape(V)[1]):
            V[i,j]/=total
        for k in range(shape(U)[0]):
            U[k,i]*=total
    return U,V

# 非負値行列Aに対する非負値行列因子分解でえられる２つの行列U,Vを返す
def factorize(A,dim=10,iteration_num=100,seed=0):
    # Aの行数と列数を得る
    dim_row,dim_column=shape(A)

    # ランダムに値を埋めた初期行列U,Vを求める
    random.seed(seed)
    U=matrix([[random.random() for j in range(dim)] for i in range(dim_row)])
    V=matrix([[random.random() for j in range(dim_column)] for i in range(dim)])

    #更新式を指定した回数だけ繰り返し適用する
    for i in range(iteration_num):
        # 現在のA-UVのフロベニウスノルムの２乗の値costを計算する
        cost=squared_frobenius_norm(A,U*V)
        # 10回毎にcostを表示する
        if i%10==0: print cost
        # すでにA=UVとなる行列分解を達成していれば抜ける
        if cost==0: break

        # Uの更新を行う
	U = array(U)*(array(A*V.T)/array(U*V*V.T))
	U=matrix(U)

        ##### ここをプログラミング #####
        
        # Vの更新を行う
	V = array(V)*(array(U.T*A)/array((V.T*U.T*U).T))
	V=matrix(V)
        ##### ここをプログラミング #####

    # UVの値を変えずにVのベクトルを正規化してからU,Vを返す
    return normalize_V(U,V)

def factorize_S(A,dim=10,seed=0,min_imp=1.1e-15):
    # Aの行数と列数を得る
    dim_row,dim_column=shape(A)

    # ランダムに値を埋めた初期行列U,Vを求める
    random.seed(seed)
    U=matrix([[random.random() for j in range(dim)] for i in range(dim_row)])
    V=matrix([[random.random() for j in range(dim_column)] for i in range(dim)])

    i = 0
    cost_bfr = squared_frobenius_norm(A,U*V)
    cost_aft = 0.0
    
    while (cost_bfr-cost_aft>min_imp):
        # 現在のA-UVのフロベニウスノルムの２乗の値costを計算する
        	cost_bfr=squared_frobenius_norm(A,U*V)
	 	i = i+1
        # 10回毎にcostを表示する
        	if i%10==0: print cost_bfr

        # Uの更新を行う
		U = array(U)*(array(A*V.T)/array(U*V*V.T))
		U=matrix(U)

        ##### ここをプログラミング #####
        
        # Vの更新を行う
		V = array(V)*(array(U.T*A)/array((V.T*U.T*U).T))
		V=matrix(V)
        ##### ここをプログラミング #####

		cost_aft=squared_frobenius_norm(A,U*V)	
	
    # UVの値を変えずにVのベクトルを正規化してからU,Vを返す
    return normalize_V(U,V)
