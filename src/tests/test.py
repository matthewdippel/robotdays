#!/usr/bin/env python
import sys
import os

def run(verbosity=1,doctest=False,numpy=True):
    """Run RobotDays tests.
    Parameters
    ----------
    verbosity: integer, optional
      Level of detail in test reports.  Higher numbers provide  more detail.
    doctest: bool, optional
      True to run doctests in code modules
    numpy: bool, optional
      True to test modules dependent on numpy
    """
    try:
        import nose
    except ImportError:
        raise ImportError(\
            "The nose package is needed to run the NetworkX tests.")

    sys.stderr.write("Running RobotDays tests:\n")
    nx_install_dir=os.path.join(os.path.dirname(__file__), os.path.pardir)
    # stop if running from source directory
    if os.getcwd() == os.path.abspath(os.path.join(nx_install_dir,os.path.pardir)):
        raise RuntimeError("Can't run tests from source directory.\n"
                           "Run 'nosetests' from the command line.")

    argv=[' ','--verbosity=%d'%verbosity,
          '-w',nx_install_dir,
          '-exe']
    if doctest:
        argv.extend(['--with-doctest','--doctest-extension=txt'])


    sys.path.append(os.path.join('..', 'App'))
    nose.run(argv=argv)

if __name__=="__main__":
    run(2)
