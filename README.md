![](https://github.com/cwendt94/espn-api/workflows/Espn%20API/badge.svg)
![](https://github.com/cwendt94/espn-api/workflows/Espn%20API%20Integration%20Test/badge.svg) [![codecov](https://codecov.io/gh/cwendt94/espn-api/branch/master/graphs/badge.svg)](https://codecov.io/gh/cwendt94/espn-api) [![Join the chat at https://gitter.im/ff-espn-api/community](https://badges.gitter.im/ff-espn-api/community.svg)](https://gitter.im/ff-espn-api/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![PyPI version](https://badge.fury.io/py/espn-api.svg)](https://badge.fury.io/py/espn-api)

## ESPN API
See the upstream repository https://github.com/cwendt94/espn-api for usage instructions on the API.

## Sugested install method:
Clone the repo and pip install in editable mode.
```
git clone https://github.com/gayverjr/ff-espn-api
cd ff-espn-api
pip install -e .
```

    

## Things relevant to our leagues
### Scripts for analysis
The recap_scripts folder contains relevant scripts for stats. All scripts need to be edited each time to update the week.
- recap.py: runs the analysis of trophies, 
- power_rankings.py: runs the analysis of power rankings. 
- game_report.py: used to take a closer look at each game individually
- team_reports.py used for the mid-season big stats collection

### Developed analysis submodules
I have written some routines and added them to my custom version of the package. This is why editable install is nice, we can 
edit these as we like without having to reinstall each time. These files are located in espn_api/football

- trophies.py
- power_rankings.py
- team_report.py