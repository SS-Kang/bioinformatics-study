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
   
### 3B Null Spaces and Ranges

+ Linear map T의 null space는 T(v)=0이 되는 V의 모든 벡터로 이루어진 부분집합임 (For 𝑇 ∈ ℒ(𝑉, 𝑊))
  + null 𝑇 = {𝑣 ∈ 𝑉 ∶ 𝑇𝑣 = 0}
  + 만약 T가 V to W의 zero map일 경우, 즉 Tv=0, 𝑣 ∈ 𝑉 null T = V
  + null space는 부분공간 (1) 0벡터 포함, 덧셈 스칼라곱에 닫혀 있음
+ Linear map T가 injective(단사)하다는 의미는 T(u)=T(v) → u=v, 즉 다른 입력은 절대 같은 출력을 가질 수 없다는 의미임
  + Let 𝑇 ∈ ℒ(𝑉, 𝑊). T가 injective하다면 null T = {0}임
+ Linear map 𝑇 ∈ ℒ(𝑉, 𝑊)의 range는 T(v) 꼴로 표현될수 있는 W의 모든 벡터들의 집합
+ range T는 {Tv ∈ W | v ∈ V}로 정의되며, 항상 W의 부분공간(subspace)이다.
+ Surjective (전사) 출력 공간을 빠짐없이 다 채우는 함수
  + A function 𝑇∶ 𝑉 → 𝑊 is called surjective if its range equals 𝑊
+ Linear map T에 대해 입력 공간 V의 차원은 null space와 range의 차원(dim) 합과 같음
  + Rank-Nullity Theorem: dim V = dim null T + dim range T
+ 저차원 space로 이동하는 linear map은 injective하지 않음 dim null T = dim V - dim range T = dim V - dim W > 0
+ 고차원 space로 이동하는 linear map은 surjective하지 않음 W를 모두 채울 수 없음
  + dim V < dim W 인 경우, T는 절대 surjective가 될 수 없음 (range T ⊊ W)
  + dim range T = dim V - dim null T ≤ dim V < dim W
+ 미지수가 방정식 수보다 많은 homogeneous linear system (동차선형시스템)은 항상 0이 아닌 해(nonzero solution)를 가짐
  +  A: 𝑚×𝑛행렬, m 행 row = 방정식 수 / n 열 column = 미지수 수
  <!-- 이미지 크기 조절 (width 600px) -->
  <img src="https://github.com/user-attachments/assets/eb4a2739-0fa0-45f4-9907-f166d78b7f02" width="600">
+  방정식 수가 변수 수보다 많은 선형 시스템은 어떤 상수항들을 선택하면 해가 없는 경우도 존재함 = 방정식들이 서로 모순된다는 의미

### 3C Matrices

+ 
