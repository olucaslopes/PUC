import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def plot_comparacao_implementacoes(tempo_por_implementacao: dict):
    """
    Plota gráfico de barras que no eixo y mostra o tempo gasto
    em uma implementação de computação distribuída e no eixo x
    mostra cada um dos diferentes tipos de implementação.

    Args
    -----
        tempo_por_implementacao: dict [str -> float]

    Returns
    -------
        None
    """
    df = pd.DataFrame(tempo_por_implementacao.items(), columns=['implementação', 'tempo'])

    ganho_velocidade = df.copy()
    ganho_velocidade = df.assign(
        ganho=(ganho_velocidade['tempo'] / ganho_velocidade['tempo'].shift(-1)).round(1),
        atual=ganho_velocidade['tempo'].shift(-1)
        ).rename(columns={'tempo':'anterior'}).iloc[:-1].replace({np.nan: 0, np.inf: 0})
    
    ax = df.plot(x='implementação', y='tempo', kind='bar')
    for container in ax.containers:
        labels = [f'{i}s' for i in container.datavalues.round(2)]
        ax.bar_label(container, labels, fmt='%d')
        plt.suptitle('Performance por tipo de implementação', weight='bold', x=0.25, size=14)
        plt.title('A implementação paralela com mais threads apresentou melhor performance',)
        plt.yscale('log')
        plt.ylabel('Tempo (segundos)')
        plt.yticks([10**k for k in range(2)], [f'{10**k}s' for k in range(2)])
        plt.xlabel('')
        plt.xticks(rotation=0)
        zip_items = zip(ganho_velocidade['ganho'], ganho_velocidade['anterior'], ganho_velocidade['atual'])
        for index, (ganho, anterior, atual) in enumerate(zip_items):
            plt.annotate(f'{ganho}x\nmais rápido', xy=(index+1, atual), xytext=(index+0.5, anterior*0.6),
                        arrowprops=dict(facecolor='black', shrink=0.05, width=3, alpha=0.9), ha='center', size=9)
        plt.show()