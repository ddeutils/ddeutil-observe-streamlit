# Observe Application: Streamlit

[![size](https://img.shields.io/github/languages/code-size/ddeutils/ddeutil-observe-streamlit)](https://github.com/ddeutils/ddeutil-observe-streamlit)
[![gh license](https://img.shields.io/github/license/ddeutils/ddeutil-observe-streamlit)](https://github.com/ddeutils/ddeutil-observe-streamlit/blob/main/LICENSE)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The **Lightweight Observe Application** that was created by [Streamlit](https://streamlit.io/)
package.

> [!NOTE]
> This project is the migration project from [Observe](https://github.com/ddeutils/ddeutil-observe)
> that use FastAPI be application but this project use Streamlit.

## :round_pushpin: Installation

```shell
pip install -U ddeutil-observe-streamlit
```

> :egg: **Docker Images** supported:
>
> | Docker Image               | Python Version | Support |
> |----------------------------|----------------|:-------:|
> | ddeutil-observe:latest     | `3.9`          |   :x:   |
> | ddeutil-observe:python3.10 | `3.10`         |   :x:   |
> | ddeutil-observe:python3.11 | `3.11`         |   :x:   |
> | ddeutil-observe:python3.12 | `3.12`         |   :x:   |
> | ddeutil-observe:python3.12 | `3.13`         |   :x:   |

## :beers: Getting Started

This project implement the best scalable Streamlit application structure.
For the first phase, I will use the SQLite be a backend database that keep
all workflow and schedule data.

### Main Page

```text

```

### Workflow Release Page

```text

```

## :cookie: Configuration

> [!IMPORTANT]
> The config value that you will set on the environment should combine with
> prefix, component, and name which is `OBSERVE_{component}_{name}` (Upper case).

| Environment     | Component | Default           | Description                  |
|:----------------|:---------:|:------------------|:-----------------------------|

## :speech_balloon: Contribute

I do not think this project will go around the world because it has specific propose,
and you can create by your coding without this project dependency for long term
solution. So, on this time, you can open [the GitHub issue on this project :raised_hands:](https://github.com/ddeutils/ddeutil-observe-streamlit/issues)
for fix bug or request new feature if you want it.
