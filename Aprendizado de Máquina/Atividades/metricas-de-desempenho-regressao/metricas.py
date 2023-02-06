"""
Contém métricas úteis para avaliar modelos de regressão
"""
def mae(y, y_hat):
    """
    Calcula o MAE
        Parameters
    ----------
    y: list
        Target true value
    
    y_hat: list
        Target predicted value
        
    Returns
    -------
    mae: float
        Value of Mean Absolute Error
    """
    n = len(y)
    soma = 0
    for i in range(n):
        soma += abs(y[i] - y_hat[i])
    return soma / n


def mape(y, y_hat, e=1e-24):
    """
    Calcula o MAPE (Percentual do Erro Médio Absoluto)
    
    Parameters
    ----------
    y: list
        Target true value
    
    y_hat: list
        Target predicted value
    e: float
        Arbitrary value to be used in case of division by zero
        
    Returns
    -------
    mape: float
        Value of Mean Absolute Percentage Error
    """
    
    n = len(y)
    
    soma = 0
    for i in range(n):
        soma += abs(y[i] - y_hat[i]) / max(abs(y[i]), e)
    
    return soma / n

def mse(y, y_hat):
    """
    Calcula o MSE (Erro Quadrático Médio)
    
    Parameters
    ----------
    y: list
        Target true value
    
    y_hat: list
        Target predicted value
        
    Returns
    -------
    mse: float
        Value of Mean Squared Error
    """
    
    n = len(y)

    soma = 0
    for i in range(n):
        soma += (y[i] - y_hat[i])**2
    
    return soma / n

def rmse(y, y_hat):
    """
    Calcula o RMSE (Raiz Quadrada do Erro Quadrático Médio)
    
    Parameters
    ----------
    y: list
        Target true value
    
    y_hat: list
        Target predicted value
        
    Returns
    -------
    rmse: float
        Value of Root Mean Squared Error
    """
    
    n = len(y)

    soma = 0
    for i in range(n):
        soma += (y[i] - y_hat[i])**2
    
    return (soma / n)**0.5

def r2(y, y_hat):
    """
    Calcula o r2 (Coeficiente de Determinação)
    
    Parameters
    ----------
    y: list
        Target true value
    
    y_hat: list
        Target predicted value
        
    Returns
    -------
    r_squared: float
        Value of Coefficient of Determination
    """
    mean_y = sum(y) / len(y)
    n = len(y)
    
    top_sum = 0
    for i in range(n):
        top_sum += (y[i] - y_hat[i])**2
    
    bottom_sum = 0
    for i in range(n):
        bottom_sum += (y[i] - mean_y)**2
        
    return 1 - (top_sum/bottom_sum)

def medae(y, y_hat):
    """
    Calcula o MAE (Erro Absoluto Mediano)
    
    Parameters
    ----------
    y: list
        Target true value
    
    y_hat: list
        Target predicted value
        
    Returns
    -------
    medae: float
        Value of Median Absolute Error
    """
    
    n = len(y)
    abs_diff = list()
    
    for i in range(n):
        abs_diff.append(
            abs(y[i] - y_hat[i])
        )

    sorted_abs_diff = sorted(abs_diff)
    # print('sorted_abs_diff:', sorted_abs_diff)
    
    # if the sample is odd, the median is the middle number
    if n % 2 == 1:
        return float(sorted_abs_diff[n//2])
    
    # otherwise, the median is the mean of the two middle numbers
    else:
        middle_right_index = n//2
        middle_left_index = middle_right_index - 1
        return (sorted_abs_diff[middle_left_index] + sorted_abs_diff[middle_right_index]) / 2