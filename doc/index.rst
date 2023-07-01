===================
Welcome to PINAR!
===================

.. image:: guide/img/PINAR_logo_QR.png
   :align: center
   :alt: PINAR Logo

PINAR means Fountain and is a probabilistic natural catastrophe impact model, that also calculates averted damage (benefit) thanks to adaptation measures of any kind (from grey to green infrastructure, behavioural, etc.).

PINAR is primarily developed and maintained by the `Mohammadreza Alipour, Mohammadreza Hatami, Negin Ghahremani`_ at `Zanjan Red Crescent`_.

This is the documentation of the PINAR core module which contains all functionalities necessary for performing pinar risk analysis and appraisal of adaptation options.

Jump right in:

* :doc:`Getting Started <guide/Guide_get_started>`
* :doc:`Installation <guide/install>`
* :doc:`Overview <tutorial/1_main_pinar>`
* `GitHub Repository <https://github.com/MamarezaAlipour/pinar_python>`_
* :doc:`Module Reference <pinar/pinar>`

.. ifconfig:: readthedocs

   .. hint::

      ReadTheDocs hosts multiple versions of this documentation.
      Use the drop-down menu on the bottom left to switch versions.
      ``stable`` refers to the most recent release, whereas ``latest`` refers to the latest development version.

.. admonition:: Copyright Notice

   Copyright (C) 2022-2023, PINAR contributors listed in AUTHORS.md.

   PINAR is free software: you can redistribute it and/or modify it under the
   terms of the GNU General Public License as published by the Free
   Software Foundation, version 3.

   PINAR is distributed in the hope that it will be useful, but WITHOUT ANY
   WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
   PARTICULAR PURPOSE.  See the GNU General Public License for more details.

   You should have received a copy of the GNU General Public License along
   with PINAR. If not, see https://www.gnu.org/licenses/.


.. toctree::
   :hidden:

   GitHub Repositories <https://github.com/MamarezaAlipour>

.. toctree::
   :maxdepth: 1
   :caption: User Guide
   :hidden:

   guide/Guide_Introduction
   Getting Started <guide/Guide_get_started>
   guide/install
   Running PINAR on Euler <guide/Guide_Euler>


.. toctree::
   :caption: API Reference
   :hidden:
   
   Python Modules <pinar/pinar>


.. toctree::
   :maxdepth: 2
   :caption: Tutorials
   :hidden:

   Overview <tutorial/1_main_pinar>
   Python Introduction <tutorial/0_intro_python>
   Hazard <tutorial/hazard>
   Exposures <tutorial/exposures>
   Impact <tutorial/impact>
   Uncertainty Quantification <tutorial/unsequa>
   tutorial/pinar_engine_Forecast
   Google Earth Engine <tutorial/pinar_util_earth_engine>
   tutorial/pinar_util_api_client


.. toctree::
   :maxdepth: 1
   :caption: Developer Guide
   :hidden:

   Development with Git <guide/Guide_Git_Development>
   guide/Guide_PINAR_Tutorial
   guide/Guide_Configuration
   guide/Guide_Continuous_Integration_and_Testing
   guide/Guide_Reviewer_Checklist
   guide/Guide_PythonDos-n-Donts
   Performance and Best Practices <guide/Guide_Py_Performance>
   Coding Conventions <guide/Guide_Miscellaneous>
   Building the Documentation <README>