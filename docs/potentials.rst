Potential energy
================

Common interface
----------------

Every potential class is a plain-old struct of parameters and provides two
functions :code:`evaluate_energy` and :code:`evaluate_force`.

.. code:: cpp

   struct binary_potential
   {
       ...

       md::scalar evaluate_energy(md::vector r) const;
       md::vector evaluate_force(md::vector r) const;
   };


Potentials
----------

.. list-table::

   * - :cpp:class:`constant_potential`
     - constant energy

   * - :cpp:class:`harmonic_potential`
     - harmonic oscillator

   * - :cpp:class:`spring_potential`
     - harmonic oscillator

   * - :cpp:class:`semispring_potential`
     - harmonic oscillator

   * - :cpp:class:`lennard_jones_potential`
     - Lennard-Jones 12-6

   * - :cpp:class:`wca_potential`
     - Lennard-Jones 12-6 with cut-off at the energy minimum

   * - :cpp:class:`softcore_potential`
     - soft-core repulsion

   * - :cpp:class:`softwell_potential`
     - soft-well attraction



References
----------

.. cpp:class:: constant_potential

A potential with constant energy:

.. math::
   u(\boldsymbol{r}) = \varepsilon



.. cpp:class:: harmonic_potential

A long-range, attractive potential of the form:

.. math::
   u(\boldsymbol{r}) = \frac{K}{2} r^2


.. cpp:class:: spring_potential

A long-range, attractive potential of the form:

.. math::
   u(\boldsymbol{r}) = \frac{K}{2} \left( r - b \right)^2


.. cpp:class:: semispring_potential

A long-range, attractive potential of the form:

.. math::
   u(\boldsymbol{r}) = \frac{K}{2} \left( r - b \right)^2
   \qquad
   \left( r > b \right)


.. cpp:class:: lennard_jones_potential

A long-range potential of the form:

.. math::
   u(\boldsymbol{r})
     = \varepsilon \Big(
         \Big( \frac{\sigma}{r} \Big)^{12} -
         \Big( \frac{\sigma}{r} \Big)^6
       \Big)


.. cpp:class:: wca_potential

A short-range, repulsive potential of the form:

.. math::
   u(\boldsymbol{r})
     = \varepsilon \Big(
         \Big( \frac{\sigma}{r} \Big)^{12} -
         \Big( \frac{\sigma}{r} \Big)^6
       \Big)
   \quad
   \left( r < \sigma \right)


.. cpp:class:: softcore_potential

A short-range, repulsive potential of the form:

.. math::
   u(\boldsymbol{r})
     = \varepsilon \Big(
         1 -
         \Big( \frac{r}{\sigma} \Big)^p
       \Big)^q
   \quad
   \left( r < \sigma \right)


.. cpp:class:: softwell_potential

A long-range, attractive potential of the form:

.. math::
   u(\boldsymbol{r})
     = -\frac{\varepsilon}{1 + (r / \sigma)^p}

.. code:: cpp

   // Define attractive interactions.
   
   md::softwell_potential pot = {
       .energy         = 2.0,   // epsilon parameter
       .decay_distance = 0.5    // sigma parameter
   };
   
   auto softwell = system.add_forcefield(
       md::make_pairwise_forcefield(pot)
   );
   softwell->add_pair(0, 1);


