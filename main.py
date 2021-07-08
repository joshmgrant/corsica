from typing import Optional
import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from corsica.distributions import uniform
from corsica.distributions import normal
from corsica.distributions import exponential

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from grpc import ssl_channel_credentials


# resource describes app-level information that will be added to all spans
resource = Resource(attributes={
    "service.name": "corsica"
})

# create new trace provider with our resource
trace_provider = TracerProvider(resource=resource)

# create exporter to send spans to Honeycomb
otlp_exporter = OTLPSpanExporter(
    endpoint="api.honeycomb.io:443",
    insecure=False,
    credentials=ssl_channel_credentials(),
    headers=(
        ("x-honeycomb-team", os.environ.get("HONEYCOMB_API_KEY")),
        ("x-honeycomb-dataset", "corsica_overall")
    )
)

# register exporter with provider
trace_provider.add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

# register trace provider
trace.set_tracer_provider(trace_provider)


app = FastAPI(
    title="Corisca - Random Numbers as a Service",
    description="Corsica is a service that provides lists of random samples on demand.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("http-handler"):
        with tracer.start_as_current_span("uniform_single"):
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

    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("http-handler"):
        with tracer.start_as_current_span("uniform_list"):
            values_list = uniform(size, lower_bound, upper_bound)

    return {"lower": lower_bound, "upper": upper_bound, "values": values_list}


@app.get("/normal/",
         tags=["Distributions"],
         summary="Continuous Normal Distribution - Single Value",
         description="Returns a single random value from a standard normal distribution")
def get_single_normal():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("http-handler"):
        with tracer.start_as_current_span("normal_single"):
            value = normal(1, 0.0, 1.0)

    return {"value": value}


@app.get("/normal/{size}",
         tags=["Distributions"],
         summary="Normal Distribution",
         description="Returns a list of samples of a normal distribution with mean mu and variance sigma^2")
def get_normal(size: int, mu: Optional[float] = None, sigma: Optional[float] = None):
    mu = mu if mu else 0.0
    sigma = sigma if sigma else 1.0

    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("http-handler"):
        with tracer.start_as_current_span("normal_list"):
            values_list = normal(size, mu, sigma)

    return {"mu": mu, "sigma": sigma, "values": values_list}


@app.get("/exponential/",
         tags=["Distributions"],
         summary="Continuous Exponential Distribution - Single Value",
         description="Returns a single random value from a standard exponential distribution")
def get_single_exponential():
    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("http-handler"):
        with tracer.start_as_current_span("exponential_single"):
            value = exponential(1, 1.0)

    return {"value": value}


@app.get("/exponential/{size}",
         tags=["Distributions"],
         summary="Exponential Distribution",
         description="Returns a list of samples of an exponential distribution with parameter lam`")
def get_exponential(size: int, lam: Optional[float] = None):
    lam = lam if lam else 1.0

    tracer = trace.get_tracer(__name__)
    with tracer.start_as_current_span("http-handler"):
        with tracer.start_as_current_span("exponential_list"):
            values_list = exponential(size, lam)

    return {"lambda": lam, "values": values_list}
