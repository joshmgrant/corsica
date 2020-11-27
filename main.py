from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from corsica.distributions import uniform
from corsica.distributions import normal
from corsica.distributions import exponential

app = FastAPI()


@app.get('/')
@app.get("/corsica")
def read_root():
    html_content = """
    <title>Corsica</title>
    <body>
        <h1>Hello! Welcome to Corsica!</h1>
        <br />
        <p>Corsica provides random numbers as a service</p>
        <p>See the <a href="https://github.com/joshmgrant/corsica">project</a> for more information.
    </body>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/uniform/{size}")
def get_uniform(size: int, lower_bound: Optional[float] = None, upper_bound: Optional[float] = None):
    lower_bound = lower_bound if lower_bound else 0.0
    upper_bound = upper_bound if upper_bound else 1.0

    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound
    
    values_list = uniform(size, lower_bound, upper_bound)
    return {"lower": lower_bound, "upper": upper_bound, "values": values_list}

@app.get("/normal/{size}")
def get_normal(size: int, mu: Optional[float] = None, sigma: Optional[float] = None):
    mu = mu if mu else 0.0
    sigma = sigma if sigma else 1.0
    
    values_list = normal(size, mu,sigma)
    return {"mu": mu, "sigma": sigma, "values": values_list}

@app.get("/exponential/{size}")
def get_exponential(size: int, lam: Optional[float] = None):
    lam = lam if lam else 1.0
    
    values_list = exponential(size, lam)
    return {"lambda": lam, "values": values_list}

