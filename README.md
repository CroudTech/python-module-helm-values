# Installation

pip3 install --user git+ssh://git@github.com/CroudTech/python-module-helm-values.git

# Usage

## Get values for helm release:

```
Usage: reckoner_values [OPTIONS]

  Build all possible s3 paths for values files

Options:
  --namespace TEXT      The namespace for the release
  --chart TEXT          The name of the chart
  --app TEXT            The app name for the release  [required]
  --extrafiles TEXT     Extra file names to search for
  --extravalues TEXT    Full paths to extra values files
  --destination TEXT    The destination for downloaded values files
  --bucket TEXT         The source s3 bucket name  [required]
  --output [json|helm]  The source s3 bucket name  [required]
  --region TEXT         The target region
  --help                Show this message and exit.
```

## Update Reckoner / Autohelm file with value files:

```
Usage: update_reckoner_file [OPTIONS]

Options:
  --source TEXT  The source autohelm file  [required]
  --dest TEXT    The destination autohelm file  [required]
  --region TEXT  The target region  [required]
  --values TEXT  Path to the values files  [required]
  --help         Show this message and exit.
```