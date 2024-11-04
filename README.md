# Instruction
*Running program*

**python controller.py**

If you use other python running command (e.g. python3),
you **have to set it in runners.json**.

(e.g. change {python: "python"} to {python: "python3"} inside runners.json).

*Default configuration*

By default, pseudo_random_number_generator.py 
is used as pseudo random number generator.

If you would like to change it (e.g. to generator2.py) run:

**python controller.py generator2.py**   or 

**python controller.py <my_generator>**,

where <my_generator> is name of your generator.

*Range of random numbers*


Default generator - pseudo_random_number_generator.py generates integer from [0, 100].

generator2.py generates integers from [-1000, 1000].
