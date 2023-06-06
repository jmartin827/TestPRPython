# Minimum Viable GitHub Actions Pytest PR Example
Shows how to do a setup where a PR won't be merged unless the Pytest tests passes.
A push to any branch or PR to the `main` branch will trigger the GitHub Actions workflow.

## Setup
Simply use the code within this repo's Main branch as a template for your own repo.

Specifically the following files are needed for a minimum viable example:
- .github/workflows/tests.yaml (GitHub Actions--loaded manually into GitHub Actions GUI
- tests/pytest.ini (Pytest configuration. May not be needed)
- tests/test_basic.py (Pytest test file)

**Within GitHub:**

Branch protection rule:
- Enable: Require status checks to pass before merging 
- Enable: Require branches to be up to date before merging 
- Status Checks Required:  "build (3.10)" or whatever you named the GitHub Actions workflow


### TODO
- Document or link to steps to setup GitHub Action from this repo as additional resource
- Use a linter to check the code formatting
- Have more than a single GitHub Actions workflow required as a "status check" before merging
- Consider if it is equitable to have every push to a branch trigger the GitHub Actions workflow
- See what other features should be added to the GitHub Actions workflow