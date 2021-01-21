## Corsica 

### Introduction

Corsica is a RESTful service for generating random samples of some common probability distributions. Basically, it's random samples as a service (RSaaS).

### Why Corsica?

Samples of random variables can be helpful in many settings. Having a service to generate them on demand would be even more helpful. Corsica tries to accomplish this in a light and straightforward way. All that's needed is an Internet connection and a utility like `curl` or [`Invoke-RestMethod`](https://msdn.microsoft.com/powershell/reference/5.1/microsoft.powershell.utility/Invoke-RestMethod) if you are using Windows/PowerShell. You can also use your favourite mainstream browser like Chrome or Firefox instead if you prefer.

### Ok, But Why the Name - Corsica?

[Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method) are a set of approaches where numerical results are calculated using random numbers. This applies to a broad class of problems from financial options pricing to statistical mechanics. Due to applying stochastic approaches to deterministic problems, Monte Carlo methods are named after a famous destination for gambling. 

Corsica is an island region of France approximately 300 kilometers from Monte Carlo. Corsica is close enough to get to Monte Carlo fairly easily (with a little work) but is also an island unto itself. This is the motivation for the name of this service.

### Supported Distributions

Currently supported probability distributions are:
- [the (continuous) uniform distribution](https://en.wikipedia.org/wiki/Uniform_distribution)
- [the normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
- [the exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution)

### Example Usage

See the [interactive documentation](https://corsica.joshgrant.online/docs) for examples of how to generate samples of each distribution.

### Technical Details

This is a cutting art, state of the edge project, built with:

- [FastAPI](https://fastapi.tiangolo.com/) for the API layer
- [Deta](https://docs.deta.sh/) for hosting the application
- [Pipenv](https://pipenv.pypa.io/en/latest/) for general dependency management and scripting

### Questions or Concerns?

Let me know how I'm doing. Please try this out and post bugs or issues. 

You can also find me on [Twitter](https://twitter.com/joshin4colours). Thank you for your interest.