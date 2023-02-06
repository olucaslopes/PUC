"""
Contém métricas úteis para avaliar modelos de regressão
"""

def mae(y, y_hat):
    """
    Calcula o MAE
    """
    n = len(y)
    y = np.array(y)
    y_hat = np.array(y_hat)
    return np.sum(np.abs(y - y_hat)) / n


def mape(y, y_hat):
    """
    Calcula o MAPE (Percentual do Erro Médio Absoluto)
    """
    
    n = len(y)
    y = np.array(y)
    y_hat = np.array(y_hat)
    
    residual = y-y_hat
    abs_y = np.abs(y)
    
    return np.sum(np.abs(y - y_hat) / np.where(abs_y > residual, abs_y, residual))/n

