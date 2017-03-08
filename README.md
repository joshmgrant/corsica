### Introduction

Corsica is a restful service for generating random samples of some common probability distributions. It is powered by Python's [NumPy](http://www.numpy.org/) and meant to be a readily available restful service. 

### Why Corsica?

Samples of random variables can be helpful in many settings. Having a service to generate them on demand would be even more helpful. Corsica tries to accomplish this in a light and straightforward way. All that's needed is an Internet connection and a utility like `curl`.

### Ok, But Why the Name - Corsica?

[Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method) are an approach where numerical results are calculated using random numbers. This applies to a broad class of problems from financial options pricing to statistical mechanics. Due to applying stochastic approaches to deterministic problems, Monte Carlo methods are named after a famous destination for gambling. 

Corsica is an island region of France approximately 300 kilometers from Monte Carlo. Corsica is close enough to get to Monte Carlo fairly easily (with a little work). This is the motivation for the name of this service.

### Supported Distributions

Currently supported probability distributions are:
- the Uniform distribution
- the Normal distribution
- the exponential distribution