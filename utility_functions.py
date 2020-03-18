import scipy.stats as st
from typing import Tuple
from scipy.stats import t


def CI(CL:float, sigma:float, n:int, xbar:float, E:bool=False) -> Tuple(int, int):
    """[Find confidence interval for the true mean]
    
    Arguments:
        int {} -- [description]
    
    Keyword Arguments:
        CL {float, sigma} -- [description] (default: {False)->Tuple(int})
    
    Returns:
        [type] -- [description]
    """    
    if E:
        return st.norm.ppf(((1-CL)/2)) * sigma / np.sqrt(n)
    else:
        return (xbar - st.norm.ppf(((1-CL)/2)) * sigma / np.sqrt(n), xbar + st.norm.ppf(((1-CL)/2)) * sigma / np.sqrt(n))

print(CI(CL=0.99, sigma = 5.7, n = 30, xbar = 79))

print(CI(CL=0.95, sigma = 13.4, n = 96, xbar = 114.4, E=True))

def prob(upper:float, lower:float, mu:float, sigma:float, E: false) -> float:
    """[return probability between 2 points]
    
    Arguments:
        upper {float} -- [description]
        lower {float} -- [description]
        mu {float} -- [description]
        sigma {float} -- [description]
        E {false} -- [description]
    
    Returns:
        float -- [description]
    """    
    return st.norm.cdf((upper - mu)/sigma) - st.norm.cdf((lower - mu)/sigma)

print(prob(upper=25.3,lower=19.7,mu=22.0,sigma=2.4))


def prob_sample(upper:float, lower:float, mu:float, sigma:float, n:float) -> float:
    """[return probability between two points for a sample]
    
    Arguments:
        upper {float} -- [description]
        lower {float} -- [description]
        mu {float} -- [description]
        sigma {float} -- [description]
        n {float} -- [description]
    
    Returns:
        float -- [description]
    """    
    return st.norm.cdf((upper - mu)/(sigma/np.sqrt(n))) - st.norm.cdf((lower - mu)/(sigma/np.sqrt(n)))
print(prob_sample(upper=1050,lower=950,mu=1000,sigma=350,n=50 ))

def z_value(area: float) -> float:
    """[Return z-value given area to the left of the std normal curve]
    
    Arguments:
        area {float} -- [description]
    
    Returns:
        float -- [description]
    """    
    return st.norm.ppf(area)

z_value(0.86)

#%%

def t_value(area: float, df: float) -> float:
    """[return t-value given area to the right]
    
    Arguments:
        area {float} -- [description]
        df {float} -- [description]
    
    Returns:
        float -- [description]
    """    
    return t.ppf(area, df=df)

t_value(area=(1-0.01),df=20)

# %%
