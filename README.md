Enigma
======

An Enigma encoder/decoder, writtern in python, created to satisfy a long-held
curiosity I've had with the machine. I've chosen to structure the program in a
way that reflects the physical device, even though this may not be the best way
to perform the encoding, in order to aid understanding and better demonstrate
how the prototype works.

Running Tests
-------------
I'd recomend using [virtualenv][1] (and [virtualenvwrapper][2]). The tests are
run using [tox][3], and the dependencies are managed using [pip][4].

```
➜ pip install -r requirements.xt
➜ tox
  ...
  ...
  ...
  py27: commands succeeded
  py36: commands succeeded
  congratulations :)
```

 [1]: https://virtualenv.pypa.io
 [2]: http://virtualenvwrapper.readthedocs.io
 [3]: https://tox.readthedocs.io
 [4]: https://pypi.python.org/pypi/pip
