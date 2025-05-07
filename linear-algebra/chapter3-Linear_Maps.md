# Chapter 3 Linear Maps

### 3A Vector Space of Linear Maps

+ Linear map (선형사상) 두 벡터 공간 V와 W 사이의 함수 T: V → W은 두 가지 가정을 만족해야함
  + additivity (가법성) T(u+v) = Tu + Tv (all u,v는 V에 속함)
  + homogeneity (동차성, 스칼라곱보존) T(𝜆v) = 𝜆(Tv) (all lambda는 F에 속함, all v는 V에 속함)
  + 참고: 보통 함수 \( T(v) \)를 간단히 \( Tv \)로 표기한다.
+ ℒ(V,W) = V에서 W로 연결되는 모든 linear map의 집합을 의미함, ℒ(V)는 V에서 V로 연결되는 linear map이며, ℒ(V,V)와 동일한 의미임
+ V의 기저 v1, ..., vn 과 W의 임의 벡터 w1, ..., wn 이 주어지면, Tv_k = w_k 를 만족하는 유일한 선형사상 T: V → W 가 존재함
+ linear map T:U → V, S:V → W가 주어졌을때, 그 곱 ST:U → W는 ST(u)=S(T(u))로 정의됨
  + 곱 \( ST \)는 다음 성질을 만족함:
    + (결합법칙) \( (T_1 T_2) T_3 = T_1 (T_2 T_3) \)
    + (항등원) \( TI = IT = T \) (정의역/공역에 맞는 항등사상 \( I \))
    + (분배법칙) \( (S_1 + S_2)T = S_1T + S_2T \), \( S(T_1 + T_2) = ST_1 + ST_2 \)

