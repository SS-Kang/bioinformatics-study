# HMM 기반 Viterbi 알고리즘을 사용한 Phasing (SNP 5개 이상)
# ===============================================================
# 이 코드는 SNP 수가 많아졌을 때 가능한 haplotype 조합의 폭발을 피하기 위해
# HMM 모델과 Viterbi 알고리즘을 사용하여 최적의 haplotype allele path를 추정한다.

from itertools import product

# 1. SNP 정보 (pos: (ref, alt)) - SNP 5개 예시
variants = {
    1: ('A', 'C'),
    2: ('T', 'G'),
    3: ('G', 'A'),
    4: ('C', 'T'),
    5: ('G', 'T')
}

# 2. Read 정보: (id, {snp_pos: observed_allele})
reads = [
    ('read1', {1: 'A', 2: 'T', 3: 'G'}),
    ('read2', {2: 'G', 3: 'A', 4: 'C'}),
    ('read3', {3: 'A', 4: 'T', 5: 'T'}),
    ('read4', {1: 'C', 2: 'G', 3: 'A'}),
    ('read5', {2: 'T', 3: 'G', 4: 'C'}),
]

# 3. 상태 정의: 각 SNP 위치에서 hap 선택 (0=ref, 1=alt)
states = [0, 1]

# 4. 전이 확률 (hap switch penalty)
trans_prob = {
    0: {0: 0.99, 1: 0.01},  # 같은 hap 유지 99%, 전환 1%
    1: {0: 0.01, 1: 0.99}
}

# 5. 방출 확률 설정
match = 0.9
mismatch = 0.1

# 6. Viterbi 테이블 초기화
V = [{}]  # 시간 t=0, 각 상태에 대한 확률을 저장할 리스트
path = {}  # 최적 경로 저장

# SNP 위치 순서
positions = sorted(variants.keys())

# === t = 0 초기화 ===
### 첫 번째 SNP 위치(pos0)에서 각 상태(ref/alt)에 대해
### 해당 allele이 read들과 얼마나 잘 일치하는지 방출 확률 계산
pos0 = positions[0]
for s in states:
    allele = variants[pos0][s]  ### 예: s=0 → 'A', s=1 → 'C'
    prob = 1.0
    for _, obs in reads:
        if pos0 in obs:
            ### 예: read1에서 pos0=1이고 A이면 match → 0.9
            prob *= match if obs[pos0] == allele else mismatch
    V[0][s] = prob  ### 시점 0에서 상태 s에 있을 확률 저장
    path[s] = [s]   ### 초기 상태 경로 설정

# === t >= 1 재귀 계산 ===
### 각 시점 t (SNP 위치)에 대해 모든 상태 s를 탐색하며
### 이전 시점에서의 최적 경로를 이어붙이고 최대 확률을 선택
for t in range(1, len(positions)):
    V.append({})
    new_path = {}
    pos = positions[t]  ### 현재 SNP 위치

    for curr_state in states:
        allele = variants[pos][curr_state]  ### 현재 상태의 allele 예: T or G 등

        # 방출 확률 계산: 현재 allele이 read들과 얼마나 일치하는지
        emission = 1.0
        for _, obs in reads:
            if pos in obs:
                emission *= match if obs[pos] == allele else mismatch

        # 이전 상태들 중 가장 높은 확률 경로 선택
        max_prob, prev_st = max(
            (
                V[t-1][prev_state] * trans_prob[prev_state][curr_state] * emission,
                prev_state
            )
            for prev_state in states
        )

        V[t][curr_state] = max_prob  ### 현재 시점의 상태 확률 저장
        new_path[curr_state] = path[prev_st] + [curr_state]  ### 경로 업데이트

    path = new_path  ### 경로 갱신

# === 종료: 마지막 시점에서 최적 상태 선택 ===
final_state = max(V[-1], key=V[-1].get)
best_path = path[final_state]  ### 최적의 hap 선택 경로 (ref/alt 시퀀스)

# === 결과 해석 ===
hap1 = [variants[pos][s] for pos, s in zip(positions, best_path)]
hap2 = [variants[pos][1 - s] for pos, s in zip(positions, best_path)]

print("=== Viterbi 기반 Phasing 결과 ===")
print("Haplotype 1:", hap1)
print("Haplotype 2:", hap2)
print("Best state path:", best_path)

# output
=== Viterbi 기반 Phasing 결과 ===
Haplotype 1: ['C', 'G', 'A', 'T', 'T']
Haplotype 2: ['A', 'T', 'G', 'C', 'G']
Best state path: [1, 1, 1, 1, 1]

