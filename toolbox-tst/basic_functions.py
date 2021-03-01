def my_mean(samples):
    '''returns the mean of the observations'''
    mu = 0
    for sample in samples:
        mu += sample
    return mu / len(samples)


def my_standard_deviation(samples):
    '''returns the standard deviation of the observations'''
    squared_sum = 0
    mu = my_mean(samples)
    for sample in samples:
        squared_sum += (sample - mu)**2
    return ((1/(len(samples)-1)) * squared_sum)**0.5


def my_mode(samples):
    '''returns the mode of the observations'''
    value_counter = {"mode": samples[0]}
    for value in samples:
        if value in value_counter:
            value_counter[value] += 1
        else:
            value_counter[value] = 1
        if value_counter[value] > value_counter[value_counter["mode"]]:
            value_counter["mode"] = value
    return value_counter["mode"]


def my_median(samples):
    '''returns the median of the observations'''
    samples.sort()
    samples_size = len(samples)
    if samples_size % 2:
        return samples[(samples_size // 2)]
    return (samples[(samples_size // 2) - 1] + samples[(samples_size // 2)]) / 2
