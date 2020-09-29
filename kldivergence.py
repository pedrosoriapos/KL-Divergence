def kldivergence(x, y, epsilon_factor, n_iter):
    
    # Outliers correction
    quant99 = np.quantile(x, .99)
    x = np.array([i if i < quant99 else quant99 for i in x])
    
    # Interval size & buckets
    interval_size = (np.max(x) - np.min(x)) / n_iter
    buckets = np.arange(np.min(x), np.max(x) + interval_size, interval_size)
    
    # Splitting Distributions
    x1 = x[y == 0]
    x2 = x[y == 1]
    
    # Probability Distributions
    px1 = np.array([len(x1[(x1 >= buckets[i]) & (x1 < buckets[i + 1])]) for i in range(n_inter)]) / len(x1)
    px2 = np.array([len(x2[(x2 >= buckets[i]) & (x2 < buckets[i + 1])]) for i in range(n_inter)]) / len(x2)
    
    # Epsilon
    minpx1 = np.min(px1[px1 != 0])
    minpx2 = np.min(px2[px2 != 0])
    epsilon = np.min([minpx1, minpx2]) / epsilon_factor
    px1 = np.array([epsilon if i == 0 else i for i in px1])
    px2 = np.array([epsilon if i == 0 else i for i in px2])
    
    # KL Divergence
    klx1x2 = np.array([i * np.log(i / j) for i, j in zip(px1, px2)]).sum()
    klx2x1 = np.array([i * np.log(i / j) for i, j in zip(px2, px1)]).sum()
    
    return klx1x2, klx2x1
