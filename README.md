## Corsica 

### Introduction

Corsica is a RESTful service for generating random samples of some common probability distributions. It is powered by Python's [NumPy](http://www.numpy.org/) and meant to be a readily available RESTful service. 

### Why Corsica?

Samples of random variables can be helpful in many settings. Having a service to generate them on demand would be even more helpful. Corsica tries to accomplish this in a light and straightforward way. All that's needed is an Internet connection and a utility like `curl` or [`Invoke-RestMethod`](https://msdn.microsoft.com/powershell/reference/5.1/microsoft.powershell.utility/Invoke-RestMethod) if you are using Windows/PowerShell.

### Ok, But Why the Name - Corsica?

[Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method) are a set of approaches where numerical results are calculated using random numbers. This applies to a broad class of problems from financial options pricing to statistical mechanics. Due to applying stochastic approaches to deterministic problems, Monte Carlo methods are named after a famous destination for gambling. 

Corsica is an island region of France approximately 300 kilometers from Monte Carlo. Corsica is close enough to get to Monte Carlo fairly easily (with a little work) but is also an island unto itself. This is the motivation for the name of this service.

### Supported Distributions

Currently supported probability distributions are:
- [the (continuous) uniform distribution](https://en.wikipedia.org/wiki/Uniform_distribution)
- [the normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
- [the exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution)

### Example Usage

The usage of Corsica is pretty straightforward. You can send a request to a utility like `curl` using the following URL format:
```bash
https://[corsica-domain-host]/corsica/[distribution-name]/?[optional-parameter-list]
```
where [terms in brackets] are modified as needed.

Currently Corsica is being hosted on App Engine. We can generate ten random sample according to a standard normal distribution like this:
```bash
curl "https://corsica-160818.appspot.com/corsica/normal/"
```

The result of this call wil include a JSON response that looks like this:
```
{
    "samples": [
    -1.2096389665914025,
    -1.2178412840647694,
    0.87484478860914194,
    -0.10221096468421056,
    -1.4029492254105926,
    -0.58021804765788776,
    1.6849096449134444,
    -0.92958572655255245,
    0.91775972948358275,
    0.31236704243695446
    ]
}
```
By default all distribution requests return ten samples. This can be changed by including a parameter `n` as part of the request.

Suppose we wanted thirty samples of a normal distribution with a mean of 100 and standard deviation of 10, then the call would look like this:
```bash
curl "https://corsica-160818.appspot.com/corsica/normal/?mu=100&sigma=10&n=30"
```

If we wanted six samples of a uniformly distributed random variable from the interval `[-1,1]` then the call would look like this:
```bash
curl "https://corsica-160818.appspot.com/corsica/uniform/?a=-1&b=1&n=6"
```

And lastly, we might want fifty samples of a standard exponential distribution (ie having rate parameter of 1) which would look like this:
```bash    
curl "https://corsica-160818.appspot.com/corsica/exponential/?lambda=1&n=50
```

Parameters are optional for each service request. Parameter names try to follow probability theory conventions so please see links above for any confusion about what are acceptable parameter values for each distribution if you aren't sure. If problems persist, please talk to your local statistician.

### The Technical Details

Corsica was made using the following languages and tools:

- [Python](https://www.python.org/) 2.7.12 (and not Python 3.+ for reasons I won't get into)
- NumPy was used for the random number generation and manipulation
- [Flask](http://flask.pocoo.org/) was used as the RESTful API framework
- App hosting was provided by [Google App Engine](http://flask.pocoo.org/).

### Questions or Concerns?

Pull requests and issues are gratefully welcome on this project! Please let me know if I've made any glaring errors or omissions. 

You can also find me on [Twitter](https://twitter.com/joshin4colours). Thank you for your interest!