<!--数の偶奇判定 -->

```mermaid
flowchart TD
A[start] --->  B[num]
B ---> C[num % 2 == 0]
C --->|Yes| D
C --->|No| E
D[偶数]
E[奇数]
```
