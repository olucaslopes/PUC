# Computação Paralela em Python

Essa atividade tem como o objetivo proporcionar ao aluno a prática da  programação paralela por meio das etapas de modelagem do problema usando paralelismo SIMD e a implementação da solução na linguagem Python.

A descrição completa da atividade está disponível no arquivo [Laboratorio SD CDIA 01 1.pdf](./material-de-apoio/Laboratorio%20SD%20CDIA%2001%201.pdf)
## Experimentos

### **Experimento 01: Multiplicação de Matrizes**

Considerando a importância dessa operação matemática para a área de computação, cumpra as seguintes etapas propostas para o experimento.  
 
**Etapa I:** Implementar um programa sequencial na linguagem Python para multiplicação 
de duas matrizes NxN. Após a implementação faça os testes necessários.

**Etapa  II:**  Após  a  implementação  faça  uma  análise  do  desempenho  do  algoritmo 
implementado e calcule o tempo para a computação da operação considerando uma matriz 
de dimensão 500X500. Inicialize com dados aleatórios antes do processamento.  

**Etapa III:** Implementar um programa paralelo em Python usando Numba para 
multiplicação de duas matrizes NxN. Utilize um conjunto de 4 threads para o 
processamento paralelo.  

**Etapa IV:** Calcule o tempo para a computação da operação considerando uma matriz de 
dimensão 500X500 e conjuntos de 2, 4 e 9 threads. Inicialize com dados aleatórios antes 
do processamento. 

**Etapa V:** Calcule o SpeedUp da solução paralela proposta na etapa III. Indique no final 
do cálculo as informações de configuração do hardware utilizado (CPU, Clock, Cache, 
memória RAM e SO). 
### **Experimento 02 – Produto Escalar**

**Etapa  I:**  Implementar  um  programa  sequencial  na  linguagem  Python  que  calcule  o 
produto escalar entre dois vetores (u e v) de tamanho 100. Após a implementação faça os 
testes necessários.

**Etapa  II:**  Após  a  implementação  faça  uma  análise  do  desempenho  do  algoritmo 
implementado  e  calcule  o  tempo  para  a  computação  da  operação  considerando  dois 
vetores de tamanho 100. Inicialize com dados aleatórios antes do processamento.

**Etapa  III:**  Implementar  um  programa  paralelo  em  Python  usando  Numba  para  calcule 
produto escalar de dois vetores de tamanho 100. Utilize um conjunto de 4 threads para o 
processamento paralelo.

**Etapa IV:** Calcule o tempo para a computação do produto escalar considerando 2, 4 e 8 
threads. Inicialize com dados aleatórios antes do processamento.

**Etapa V:** Calcule o SpeedUp da solução paralela proposta na etapa III. Indique no final 
do cálculo as informações de configuração do hardware utilizado (CPU, Clock, Cache, 
memória RAM e SO).

### **Experimento 03 – Análise do Projeto Integrador**