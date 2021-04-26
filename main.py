from typing import Optional

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from corsica.distributions import uniform
from corsica.distributions import normal
from corsica.distributions import exponential

origins = [
    "https://corsica.joshgrant.online/",
    "http://corsica.joshgrant.online/",
    "http://localhost:5000/"
]

app = FastAPI(
    title="Corisca - Random Numbers as a Service",
    description="Corsica is a service that provides lists of random samples on demand.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
@app.get("/corsica")
def read_root():
    """
    Root of the project, should return some kind of helpful documentation for users.
    """
    return RedirectResponse("https://github.com/joshmgrant/corsica/blob/main/README.md")


@app.get("/uniform/",
         tags=["Distributions"],
         summary="Continuous Uniform Distribution - Single Value",
         description="Returns a single random value from a standard uniform distribution")
def get_single_uniform():
    value = uniform(1, 0.0, 1.0)
    return {"value": value}


@app.get("/uniform/{size}",
         tags=["Distributions"],
         summary="Continuous Uniform Distribution",
         description="Returns a list of samples of a uniform distribution on the interval [a,b]")
def get_uniform(size: int, lower_bound: Optional[float] = None, upper_bound: Optional[float] = None):
    lower_bound = lower_bound if lower_bound else 0.0
    upper_bound = upper_bound if upper_bound else 1.0

    if lower_bound > upper_bound:
        lower_bound, upper_bound = upper_bound, lower_bound

    values_list = uniform(size, lower_bound, upper_bound)
    return {"lower": lower_bound, "upper": upper_bound, "values": values_list}


@app.get("/normal/",
         tags=["Distributions"],
         summary="Continuous Normal Distribution - Single Value",
         description="Returns a single random value from a standard normal distribution")
def get_single_normal():
    value = normal(1, 0.0, 1.0)
    return {"value": value}


@app.get("/normal/{size}",
         tags=["Distributions"],
         summary="Normal Distribution",
         description="Returns a list of samples of a normal distribution with mean mu and variance sigma^2")
def get_normal(size: int, mu: Optional[float] = None, sigma: Optional[float] = None):
    mu = mu if mu else 0.0
    sigma = sigma if sigma else 1.0

    values_list = normal(size, mu, sigma)
    return {"mu": mu, "sigma": sigma, "values": values_list}


@app.get("/exponential/",
         tags=["Distributions"],
         summary="Continuous Exponential Distribution - Single Value",
         description="Returns a single random value from a standard exponential distribution")
def get_single_exponential():
    value = exponential(1, 1.0)
    return {"value": value}


@app.get("/exponential/{size}",
         tags=["Distributions"],
         summary="Exponential Distribution",
         description="Returns a list of samples of an exponential distribution with parameter lam`")
def get_exponential(size: int, lam: Optional[float] = None):
    lam = lam if lam else 1.0

    values_list = exponential(size, lam)
    return {"lambda": lam, "values": values_list}
