# Hidden Markov Model (HMM) in Bioinformatics

---

## 1. Introduction

Hidden Markov Model(HMM)은 **숨겨진 상태(hidden state)** 를 갖는 **Markov Chain** 기반의 통계적 모델이다.  
특히 **DNA 서열 분석**, **단백질 서열 정렬**, **유전자 예측**, **변이 탐지** 등 다양한 **바이오인포매틱스(Bioinformatics)** 분야에서 핵심적인 역할을 한다.

**Markov Chain 기반**이란, "현재 상태"가 오직 "바로 직전 상태"에만 의존하고, 그 이전의 이력(history)에는 독립적이라는 성질을 의미한다.  
즉, 시스템이 어떻게 현재 상태에 도달했는지는 중요하지 않고, 현재 상태만이 미래 상태에 영향을 준다.  
이러한 Markov 성질을 기본으로, HMM은 '실제 상태'(hidden state)는 관측할 수 없고 그 실제 상태가 만든 '관측된 데이터'(observation)만을 통해 간접적으로 실제 상태를 추론하는 모델이다.

---

## 2. HMM Components

HMM은 다음과 같은 구성 요소를 가진다:

| 구성요소 | 설명 |
|:---------|:-----|
| **State (상태)** | 시스템이 특정 시점에 존재하는 내부 상태 (숨겨져 있음, 관측 불가) |
| **Observation (관측값)** | 숨겨진 상태로부터 방출된 실제 관측 가능한 데이터 |
| **Transition Probability (전이 확률, A)** | 한 상태에서 다른 상태로 이동할 확률, HMM에는 숨겨진 상태가 여러 종류 있을 수 있음 |
| **Emission Probability (방출 확률, B)** | 특정 상태에서 특정 관측값이 발생할 확률, 각 상태는 자신만의 Emission Probability (방출 확률) 분포를 가짐 |
| **Initial Probability (초기 확률, π)** | 시점 0에서 특정 상태에 있을 확률 분포 |

---

## 3. Formal Definition

Hidden Markov Model은 수학적으로 다음과 같이 정의된다:

- \( N \): 상태(state)의 수
  - 시스템이 가질 수 있는 서로 다른 숨겨진 상태(hidden states)의 총 개수.
  - 예: Fair Coin, Loaded Coin → \( N = 2 \)

- \( M \): 관측 기호(observation symbol)의 수
  - 각 상태로부터 생성될 수 있는 서로 다른 관측 데이터의 종류.
  - 예: 앞면(Heads, H), 뒷면(Tails, T) → \( M = 2 \)

- \( A = \{a_{ij}\} \): 전이 확률
  - 현재 상태 \(i\)에서 다음 상태 \(j\)로 이동할 확률.

- \( B = \{b_j(k)\} \): 방출 확률
  - 상태 \(j\)에서 관측 기호 \(k\)가 발생할 확률.

- \( \pi = \{\pi_i\} \): 초기 확률 분포
  - 시작할 때 상태 \(i\)에 있을 확률.

요약하면, HMM은 파라미터 \( \lambda = (A, B, \pi) \) 로 완전히 정의된다.

---

## 4. Key Problems in HMM

HMM을 사용할 때 해결해야 하는 주요 문제들은 다음과 같다:

| 문제 | 설명 | 해결 알고리즘 |
|:-----|:----|:--------------|
| **Evaluation Problem** | 주어진 관측 시퀀스에 대해, 해당 시퀀스를 생성할 확률을 계산한다. | **Forward Algorithm** |
| **Decoding Problem** | 주어진 관측 시퀀스에 대해, 가장 가능성 높은 숨겨진 상태(hidden state) 시퀀스를 추정한다. | **Viterbi Algorithm** |
| **Learning Problem** | 오직 관측 시퀀스만 주어졌을 때, 모델의 파라미터(A, B, π)를 학습한다. | **Baum-Welch Algorithm** (EM 기반) |

> **관측 시퀀스 (Observation Sequence)**:  
> 우리가 실제로 관찰할 수 있는 데이터들의 연속을 의미한다.  
> 예를 들어, 동전을 다섯 번 던졌을 때 나온 결과가 `H, T, H, H, T` 라면, 이 데이터들의 나열이 관측 시퀀스이다.

---

## 5. Applications in Bioinformatics

HMM은 바이오인포매틱스 분야에서 광범위하게 활용된다:

- **Gene Prediction**: DNA 염기서열로부터 유전자 영역(엑손, 인트론 등)을 예측
  - 예: **GENSCAN**, **GeneMark**
- **Protein Sequence Alignment**: 단백질 서열에서 도메인 구조를 찾거나 패밀리를 정렬
  - 예: **HMMER**, **Pfam** 데이터베이스
- **Variant Calling and Phasing**: SNP와 같은 변이를 검출하고, 염색체 별 유래를 추적
  - 예: WhatsHap, GATK Read-backed phasing
- **RNA Secondary Structure Prediction**: RNA의 2차 구조를 예측하는 데 사용

---

## 6. Detailed Example: Biased Coin Toss

### Problem Setup
어떤 카지노에서 두 종류의 동전을 사용한다고 가정한다:

- **Fair Coin (F)**: 앞면과 뒷면이 나올 확률이 각각 50%
- **Loaded Coin (L)**: 앞면이 75%, 뒷면이 25% 확률로 나온다

카지노는 플레이 중에 동전을 바꿀 수 있으며, 각각의 상태 변화는 확률적으로 일어난다.

### Model Parameters

- 상태(State): {Fair (F), Loaded (L)}
- 관측값(Observation): {앞면 (H), 뒷면 (T)}
- 전이 확률(Transition probabilities, A):
  - F → F: 0.9
  - F → L: 0.1
  - L → L: 0.8
  - L → F: 0.2
- 방출 확률(Emission probabilities, B):
  - F: H(0.5), T(0.5)
  - L: H(0.75), T(0.25)
- 초기 확률(Initial probabilities, π):
  - F: 0.5
  - L: 0.5

### Task

관측 시퀀스가 `H T H H T` 일 때:

- 이 시퀀스를 생성할 확률은? (Forward Algorithm 사용)
- 가장 가능성 높은 동전 상태 시퀀스는? (Viterbi Algorithm 사용)

### 직관적 해석
- 공정한 동전일 경우 H, T는 비슷한 확률로 발생.
- 조작된 동전일 경우 H가 더 자주 발생.
- 관측값을 바탕으로 카지노가 언제 동전을 바꿨을지를 추론할 수 있다.

---

## 7. References

- L. Rabiner, "A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition", *Proceedings of the IEEE*, 1989.
- S. Eddy, "Profile hidden Markov models", *Bioinformatics*, 1998.
- Burge and Karlin, "Prediction of complete gene structures in human genomic DNA", *Journal of Molecular Biology*, 1997.

---

## 8. example code

- [Viterbi-based HMM Phasing Example](hmm_example.py)
