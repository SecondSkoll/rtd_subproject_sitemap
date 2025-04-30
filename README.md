# rtd_subproject_sitemap

Generates a sitemap from an RTD project.

## Requirements

* An access token (available in your [profile settings](https://app.readthedocs.com/accounts/tokens/))
* Python 3
* The `generate_sitemap.py` script

## How to run

1.  Export your RTD access token via the command line:

    `export TOKEN=<access token>`

2.  (Optional) Change the URL in the script.

    Note: `?limit=50` can also be changed to support a different number of subprojects.

3.  Run the script with Python 3:

    `python3 generate_sitemap.py`