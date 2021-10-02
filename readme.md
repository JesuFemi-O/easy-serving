# Easy Serving!

Serve your ML models as restful apis without any knowledge of building rest apis!

# How it works

All you have to do is run a cli command, telling easy-serving where to find your pickled model and it would automatically start a server and serve your model for you out of the box

# Features

- [x ] serve a single model
- [ x] api documentation out of the box wit swagger via fast api
- [ ] access an interactive UI that makes it easy to intereact with your model
- [ ] serve a multiple versions of a single model
- [ ] serve mutile models
- [ ] serve multiple versions of the different models

# Work in progress

The motivation for easy serving is to allow people serve ML models out of the box as restful apis in a manner that is platform agnostic. Personally, I have been working on ways to integrate other types of model serving options to [Cruise](https://github.com/JesuFemi-O/Cruise) and easy-serving is one of the tools that would make it very much possible

Easy serving uses fast api for model serving

easy serving is still heavily in development mode and I am happily building in the open. I look forward to sharing new features and publishing it very soon.

# Test in Dev mode!

- clone the repository

- create a virtual environment and start it

```bash
py -m venv venv

source venv/bin/activate

```

- cd into easy-serving folder

```bash
cd easy-serving
```

- install easy-serving in dev mode

```bash
pip install --editable .
```

- serve your ML model

```bash
easy-serving -m /path/to/model.pkl
```

- navgate to the swagger UI

```bash
localhost:5000/docs
```

Happy Hacking! :rocket:
