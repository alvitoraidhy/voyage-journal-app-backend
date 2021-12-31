{
  pkgs ? import <nixpkgs> {}
}:
pkgs.mkShell {
  name="dev-environment";
  buildInputs = [
    # Python
    pkgs.python39
    pkgs.python39.pkgs.pip
    pkgs.python39.pkgs.setuptools
    pkgs.python39.pkgs.wheel

    # Formatter
    pkgs.python39.pkgs.black
  ];
  shellHook =
  ''
    # Tells pip to put packages into $PIP_PREFIX instead of the usual locations.
    # See https://pip.pypa.io/en/stable/user_guide/#environment-variables.
    export PIP_PREFIX=$(pwd)/_build/pip_packages;
    export PYTHONPATH="$PIP_PREFIX/${pkgs.python3.sitePackages}:$PYTHONPATH";
    export PATH="$PIP_PREFIX/bin:$PATH";
    unset SOURCE_DATE_EPOCH;

    echo "Python v3.9";
    echo "Start developing...";
  '';
}
