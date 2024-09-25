import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.reshape(list, (3, 3))

    # Funções para calcular as estatísticas
    def calc_mean(matrix):
        return [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()]
    
    def calc_variance(matrix):
        return [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    
    def calc_std_dev(matrix):
        return [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()]
    
    def calc_max(matrix):
        return [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]
    
    def calc_min(matrix):
        return [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    
    def calc_sum(matrix):
        return [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    
    # Dicionário com as estatísticas calculadas
    calculations = {
        'mean': calc_mean(matrix),
        'variance': calc_variance(matrix),
        'standard deviation': calc_std_dev(matrix),
        'max': calc_max(matrix),
        'min': calc_min(matrix),
        'sum': calc_sum(matrix)
    }

    return calculations
