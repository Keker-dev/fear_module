# fear_module

![Python 3.8, 3.9, 3.10, 3.11, 3.12](https://img.shields.io/pypi/pyversions/fear_module?color=blueviolet)

**fear_module** - this module is a Python library for creating troll applications!


**FEAR** - is an entertainment project. Be **careful** with him. **It is not subject to monetization**.


## Installation

Install the current version with [PyPI](https://github.com/Keker-dev/fear_module.git):

```bash
pip install fear_module
```

Or from Github:
```bash
pip install https://github.com/Keker-dev/fear_module.git
```

## Usage

```python
TOKEN = os.getenv('TOKEN')

club_house_session = ClubHouse(TOKEN, 'v3')
club_house = club_house_session.get_api()
```

## Example

Create a new Story in the first Project that is returned from the API in the all projects list.

*If you installed a module from PyPi, you should to import it like this: ``` from clubhouse_api import ClubHouse ```*

*If from GitHub or source: ``` from club_house_api import ClubHouse ```*

```python
from club_house_api import ClubHouse
import asyncio
import os

TOKEN = os.getenv('API_TOKEN')

club_house_session = ClubHouse(TOKEN, 'v3')
club_house = club_house_session.get_api()

async def main():

    all_projects = await club_house.projects()
    first_project_id = all_projects[0]['id']

    new_story = {'name': 'My new story', 'project_id': first_project_id}
    story = await club_house.stories.create(**new_story)
    print(story)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```


## Contributing

Bug reports and/or pull requests are welcome


## License

The module is available as open source under the terms of the **MIT License**


