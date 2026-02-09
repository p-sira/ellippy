<h1 align="center">
    <a href="https://github.com/p-sira/ellip/">
        <img src="https://github.com/p-sira/ellippy/blob/main/logo/ellippy-logo.svg?raw=true" alt="EllipPy" width="350">
    </a>
</h1>

<p align="center">
    <a href="https://opensource.org/license/BSD-3-clause">
        <img src="https://img.shields.io/badge/License-BSD--3--Clause-brightgreen.svg" alt="License">
    </a>
    <a href="https://pypi.org/project/ellippy">
        <img src="https://img.shields.io/pypi/v/ellippy?label=pypi%20package" alt="PyPI Package">
    </a>
    <a href="https://pypi.org/project/ellippy">
        <img src="https://static.pepy.tech/personalized-badge/ellippy?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=BRIGHTGREEN&left_text=downloads" alt="Total Downloads">
    </a>
    <a href="https://p-sira.github.io/ellippy">
        <img src="https://img.shields.io/badge/Docs-github.io-blue" alt="Documentation">
    </a>
    <a style="border-width:0" href="https://doi.org/10.21105/joss.09386">
        <img src="https://joss.theoj.org/papers/10.21105/joss.09386/status.svg" alt="DOI badge" >
    </a>
</p>

**EllipPy** is an elliptic integral library for Python, powered by Rust. All functions support numpy and parallelization. EllipPy features high accuracy and performance. For more details on testing and benchmarks, please refer to [Ellip](https://github.com/p-sira/ellip).

## Quick Start

```python
from ellippy import *
import numpy as np

ellipk(m=np.array([0.1, 0.2, 0.3, 0.4, 0.5])) # [1.61244135 1.6596236  1.71388945 1.77751937 1.85407468]

ellippiinc(n=0.1, phi=np.pi / 4, m=0.25) # 0.1003043379500434

cel(kc=0.5, p=0.1, a=1.0, b=-1.0) # -5.2310275365518795

elliprf(x=[0.1, 0.2, 0.3], y=[0.2, 0.4, 0.8], z=[0.3, 0.5, 0.7]) # [2.29880489 1.68455225 1.32157804]

jacobi_zeta(phi=np.pi / 3, m=0.5) # 0.13272240254017148
```

To install EllipPy, use your preferred package manager:

```shell
pip install ellippy
```

```shell
uv add ellippy
```

## Features
- Legendre's complete integrals
    - `ellipk`: Complete elliptic integral of the first kind (K).
    - `ellipe`: Complete elliptic integral of the second kind (E).
    - `ellippi`: Complete elliptic integral of the third kind (Π).
    - `ellipd`: Complete elliptic integral of Legendre's type (D).
- Legendre's incomplete integrals
    - `ellipf`: Incomplete elliptic integral of the first kind (F).
    - `ellipeinc`: Incomplete elliptic integral of the second kind (E).
    - `ellippiinc`: Incomplete elliptic integral of the third kind (Π).
    - `ellipdinc`: Incomplete elliptic integral of Legendre's type (D).
- Bulirsch's integrals
    - `cel`: General complete elliptic integral in Bulirsch's form.
    - `cel1`: Complete elliptic integral of the first kind in Bulirsch's form.
    - `cel2`: Complete elliptic integral of the second kind in Bulirsch's form.
    - `el1`: Incomplete elliptic integral of the first kind in Bulirsch's form.
    - `el2`: Incomplete elliptic integral of the second kind in Bulirsch's form.
    - `el3`: Incomplete elliptic integral of the third kind in Bulirsch's form.
- Carlson's symmetric integrals
    - `elliprf`: Symmetric elliptic integral of the first kind (RF).
    - `elliprg`: Symmetric elliptic integral of the second kind (RG).
    - `elliprj`: Symmetric elliptic integral of the third kind (RJ).
    - `elliprc`: Degenerate elliptic integral of RF (RC).
    - `elliprd`: Degenerate elliptic integral of the third kind (RD).
- Miscellaneous functions
    - `jacobi_zeta`: Jacobi Zeta function (Z). 
    - `heuman_lambda`: Heuman Lambda function (Λ0).

## Citation

EllipPy is based on a Rust library, Ellip. The paper is published in the [Journal of Open Source Software](https://joss.theoj.org/papers/10.21105/joss.09386). If EllipPy is helpful to your work, please consider citing Ellip:

```text
Pornsiriprasert, S., (2026). Ellip: An Elliptic Integral Library for Rust. Journal of Open Source Software, 11(118), 9386, https://doi.org/10.21105/joss.09386
```

Bibtex format:

```bibtex
@article{Pornsiriprasert2026,
    doi = {10.21105/joss.09386}, 
    url = {https://doi.org/10.21105/joss.09386}, 
    year = {2026}, 
    publisher = {The Open Journal}, 
    volume = {11}, number = {118}, pages = {9386},
    author = {Pornsiriprasert, Sira}, 
    title = {Ellip: An Elliptic Integral Library for Rust}, 
    journal = {Journal of Open Source Software} } 
```
