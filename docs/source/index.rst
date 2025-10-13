EllipPy Documentation
=====================

.. raw:: html

   <h1 align="center">
      <a href="https://github.com/p-sira/ellip/">
         <img src="_static/ellippy-logo.svg" alt="EllipPy" width="350">
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
   </p>

----

**EllipPy** is an elliptic integral library for Python, powered by Rust. All functions support numpy and parallelization. EllipPy features high accuracy and performance. For more details on testing and benchmarks, please refer to [Ellip](https://github.com/p-sira/ellip).

Quick Start
-----------

.. code:: python

   from ellippy import *
   import numpy as np

   ellipk(m=np.array([0.1, 0.2, 0.3, 0.4, 0.5])) # [1.61244135 1.6596236  1.71388945 1.77751937 1.85407468]

   ellippiinc(n=0.1, phi=np.pi / 4, m=0.25) # 0.1003043379500434

   cel(kc=0.5, p=0.1, a=1.0, b=-1.0) # -5.2310275365518795

   elliprf(x=[0.1, 0.2, 0.3], y=[0.2, 0.4, 0.8], z=[0.3, 0.5, 0.7]) # [2.29880489 1.68455225 1.32157804]

   jacobi_zeta(phi=np.pi / 3, m=0.5) # 0.13272240254017148


To install EllipPy, use your prefered package manager:

.. code:: shell
   
   pip install ellippy

.. code:: shell
   
   uv add ellippy

|

.. currentmodule:: ellippy

Submodules
==========

.. autosummary::
   :nosignatures:

   legendre
   bulirsch
   carlson
   misc
   
|

Legendre's Integrals
====================

``ellippy.legendre``

.. automodule:: ellippy.legendre

Complete Elliptic Integrals
-----------------------------

.. rubric:: Functions

.. autosummary::
   :toctree: functions
   :nosignatures:
   
   ellipk
   ellipe
   ellippi
   ellipd

Incomplete Elliptic Integrals
-------------------------------

.. rubric:: Functions

.. autosummary::
   :toctree: functions
   :nosignatures:

   ellipf
   ellipeinc
   ellippiinc
   ellippiinc_bulirsch
   ellipdinc

|

Bulirsch's Integrals
====================

``ellippy.bulirsch``

.. automodule:: ellippy.bulirsch
   
   .. rubric:: Functions

   .. autosummary::
      :toctree: functions
      :nosignatures:
   
      cel
      cel1
      cel2
      el1
      el2
      el3
   
|

Carlson's Symmetric Integrals
=============================

``ellippy.carlson``

.. automodule:: ellippy.carlson
   
   .. rubric:: Functions

   .. autosummary::
      :toctree: functions
      :nosignatures:
   
      elliprc
      elliprd
      elliprf
      elliprg
      elliprj
   
|

Miscellaneous Functions
=======================

``ellippy.misc``

.. automodule:: ellippy.misc

   .. rubric:: Functions

   .. autosummary::
      :toctree: functions
      :nosignatures:
   
      heuman_lambda
      jacobi_zeta
   
|
