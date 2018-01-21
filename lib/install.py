"""
Functions related to the install
"""
from lib import piera

def main():
    """
    dummy install
    """
    print "Install"

def find_methode(package):
    '''
    Find the prefered install methode for the package,
    by searching across the local config files
    '''
    prefered = ""

    data_backend = piera.Hiera("./examples/local/hiera.yaml")
    assert data_backend.get("key") == "value"

    print prefered
    print package

def pre_install(package):
    '''
    Grab and execute steps prior to install
    '''

    data_backend = piera.Hiera("./examples/local/hiera.yaml")
    data_backend.get("standard_version", package=package)
    install = data_backend.get("INSTALL", package=package, os_family='debian')
    print install.PRE
