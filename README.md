# basepy
> Opinionated layout for Python 3 projects.

![industry_robot](docs/construction_plan.png)

`basepy` uses:
- [Pipenv](https://pipenv.pypa.io/en/latest/) as package management tool.
- [setuptools](https://setuptools.readthedocs.io/en/latest/) as build/distribution system.
- [pytest](https://docs.pytest.org/en/latest/) as a test runner.

## How to use basepy
1. Clone: `> git clone git@github.com:glenacota/basepy.git; cd basepy`
2. Checkout the branch with the project layout you need (see the [list below](###-available-layouts))
3. Reinit git: `> rm -rf .git/; git init`
4. Adapt package(s) structure (rename, add/delete)
5. Update `README.md` and `docs/`
6. Update `LICENSE`: https://choosealicense.com/
7. Update PipFile: https://realpython.com/pipenv-guide/
8. Update `setup.py` (or delete it you don't need to distribute or install the project)
9. Code!

### Available layouts
Different layouts are available in different branches. The list is below:
- `master` branch: basic single-package project
- `basepy-cli` branch: CLI project (uses [Click](https://click.palletsprojects.com/en/7.x/))

## Installation
### MacOs / Linux

`> pipenv shell`
`> pipenv install --ignore-pipfile`

## Usage example
A few useful examples of how this project can be used.

*[from pipenv]*

`> python basepy`

## Development setup
How to install all development dependencies and how to run an automated test-suite.

`> pipenv shell`
`> pipenv install --dev`

To run the tests:
`> pytest`

## Release History
- 0.0.2
  - Add base layout for cli projects (`basepy-cli` branch) 
- 0.0.1
  - Work in progress

## Meta
- glenacota - [Medium](https://medium.com/@guido.lenacota) - [Linkedin](https://www.linkedin.com/in/guidolenacota)
- Distributed under the MIT license. See `LICENSE` for more information.

## Contributing
1. Fork it: https://github.com/glenacota/basepy/fork
2. Create a feature branch: `> git checkout -b {{branch_name}}`
3. Commit: `> git commit -am "{{commit_message}}"`
4. Push: `> git push origin {{branch_name}}`
5. Create a Pull Request to upstream