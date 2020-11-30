# basepy
> Opinionated layout for Python 3 projects.

![industry_robot](docs/construction_plan.png)

`basepy` uses:
- [Pipenv](https://pipenv.pypa.io/en/latest/) as package management tool.
- [setuptools](https://setuptools.readthedocs.io/en/latest/) as build/distribution system.
- [pytest](https://docs.pytest.org/en/latest/) as a test runner.
- [click](https://click.palletsprojects.com/en/7.x/) as a package to build command line interfaces.

## How to use basepy
1. Clone: `> git clone git@github.com:glenacota/basepy.git; cd basepy`
2. Reinit git: `> rm -rf .git/; git init`
3. Adapt package(s) structure (rename, add/delete)
4. Update `README.md` and `docs/`
5. Update `LICENSE`: https://choosealicense.com/
6. Update PipFile: https://realpython.com/pipenv-guide/
7. Update `setup.py` (or delete it you don't need to distribute or install the project)
8. Code!

## Installation
### MacOs / Linux

`> pipenv shell`
`> pipenv install --ignore-pipfile`

## Usage example
A few useful examples of how this project can be used.

*[from pipenv]*

`# output a random greeting`
`> python basepy greet`
`# show help`
`> python basepy greet --help`
`# greet someone in particular`
`> python basepy greet --names Super Mario`
`# greet multiple persons`
`> python basepy greet --names Super Mario,Luigi Mario`
`# greet like a pirate`
`> python basepy greet --names LeChuck --as-a-pirate`

## Development setup
How to install all development dependencies and how to run an automated test-suite.

`> pipenv shell`
`> pipenv install --dev`

To run the tests:
`> pytest`

## Release History
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