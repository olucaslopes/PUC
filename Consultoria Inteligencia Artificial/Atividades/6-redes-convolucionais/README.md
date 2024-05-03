# Começando com redes neurais convolucionais

Data de entrega: 27/04/2024

## **Exercícios**

### Resumo dos modelos

Todos os modelos forem treinamos em um dataset de test, validados em um dataset de validação e os resultados de acurácia abaixo são resultado do teste em um dataset de teste. O número de neurônios e camadas é igual para todos os modelos, a não ser as diferenças descritas no nome dos modelos.

| Modelo | Acurácia | Tempo de treinamento |
| --- | --- | --- |
| Dense Layers + Dropout |  0.855 | 10 s |
| Convolutional Model with MaxPooling2D | 0.984 | 1 min 16 s |
| Convolutional Model without MaxPooling2D | 0.982 | 2 min 49 s |
| Convolutional Model with AveragePooling2D | 0.984 | 47 s |

### 1. Compare a acurácia deste modelo com o do modelo desenvolvido anteriormente para a mesma base de dados. Faça gráficos para mostrar a melhoria do modelo atual em relação ao anterior.

O modelo com redes convolucionais apresentou uma acurácia significativamente maior em relação ao modelo anterior no conjunto de dados de teste. A acurácia do modelo anterior foi de 0.85, enquanto a acurácia do modelo com redes convolucionais foi de 0.98.

### 2. Retire as camadas de MaxPooling2D e compare o resultado do modelo com o do modelo anterior

O modelo sem as camadas de MaxPooling2D demorou significativaente mais para treinar e apresentou uma acurácia menor em relação ao modelo com as camadas de MaxPooling2D. A acurácia do modelo sem as camadas de MaxPooling2D foi de 0.97, enquanto a acurácia do modelo com as camadas de MaxPooling2D foi de 0.98.

### 3. Em vez de MaxPooling2D, use AveragePooling2D e compare o resultado do modelo com o do modelo anterior.

O modelo com AveragePooling2D apresentou uma acurácia levemente maior em relação ao modelo com MaxPooling2D e um tempo de treinamento bem próximo.