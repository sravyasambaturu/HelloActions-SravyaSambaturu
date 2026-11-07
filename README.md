# HelloActions-SravyaSambaturu

A simple Hello World project that runs a Python program with GitHub Actions.

## How the workflow works

**Purpose of the `on` section:** It defines the events that start the workflow. Here it runs when code is pushed to main.

**What `workflow_dispatch` does:** It lets me start the workflow by hand with the "Run workflow" button in the Actions tab.

**What `runs-on` specifies:** The type of virtual machine (runner) that runs the job. `ubuntu-latest` is a GitHub-hosted Linux machine.

**Why `actions/checkout` is needed:** The runner starts empty. Checkout downloads my repository's code onto it so the workflow can use `hello.py`.

**What the language setup action does:** `actions/setup-python` installs and configures the chosen Python version on the runner.

**Compiling versus running:** Compiling translates source code into an executable (for example `javac` for Java) before it runs. Running executes the program. Python is interpreted, so my workflow only prepares (checks the version) and then runs.

**Where to see the output:** In the Actions tab, open the workflow run, open the job, and expand the "Run the Python program" step in the log.

**Workflow, job, and step:** A workflow is the whole automated process defined in one YAML file. A job is a group of steps that runs on one runner. A step is a single task inside a job, either an action (`uses`) or a shell command (`run`).

## AI use

I used Claude (an AI assistant) to help me understand the lab instructions. I created the repository, wrote the code, ran the workflow both automatically and manually, and checked the output myself.
