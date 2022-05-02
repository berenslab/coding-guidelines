![workflow-status](https://github.com/sarmueller/github-workflows/actions/workflows/python_workflow.yml/badge.svg) 

# Coding Guidelines
The purpose of these guidelines is to maintain and improve the quality of certain repositories where errors may have high impact within the group, such as data parsers or more generally repos that multiple people rely on. 

Please adhere to these guidelines specifically for the following projects:
- [eyepacs](https://github.com/berenslab/eyepacs)

## Authors

Process for implementing changes:
1. Do not work in the main branch directly!
2. Prepare your changes in a separate branch with an appropriate name, e.g. "lisak-bug-parser-error"
3. Before you are done, make sure your branch is up to date with the latest changes in the main branch by merging main into feature. If you are working on a forked version of the repository rebasing to the latest commit on main should be your preferred choice. More on this [here](https://medium.datadriveninvestor.com/git-rebase-vs-merge-cc5199edd77c).
4. Make sure your code works (for now: no specific rules around testing - just do your reasonable best).
5. Push your branch to github anytime.
6. Create a pull request (PR) and assign a reviewer. Use common sense - for very minor changes like typos or small changes in docstrings, it could make sense to assign it to yourself.
7. The reviewer looks through your contribution and if it looks good, will merge it to master.

### Coding Style
- You should follow the [Google style guidelines](https://google.github.io/styleguide/pyguide.html) for Python. In particular for formatting docstrings. Write docstrings in markdown if you can.
- Before you merge a pull request, you must format your code with [black](https://pypi.org/project/black/) and run [isort](https://pypi.org/project/isort/).
    - An example [github workflow](.github/workflows/python_workflow.yml) for black and isort formatting checks is provided in this repo. 
- You are encouraged to adhere to [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for your commit messages. i.e. git commit -m "fix(core): fixes a bug in some function."
- You are encouraged to use type hinting
    ```python
    def pick_row(x: np.ndarray, idx: int = 0) -> np.ndarray: 
        return x[i]
    ```
- The use of [pyright](https://github.com/Microsoft/pyright) or [mypy](http://mypy-lang.org/) for static type checking is also highly recommended.

## Reviewers
- No specific rules for reviewing for now. Do your best to ensure the proposed changes make sense.
- Use the comment functionality on github.
- Be constructive, polite and pragmatic. If you think it's necessary of it could be beneficial/of interest for the author, you can also comment on style. However, please consider everyone's priorities.
- If you think more people should be involved in deciding whether a change should take place, include them in the review process (assign them on github).

## Everyone
Use Github for communicating about the code whenever possible. Use issues with appropriate labels, and consider enabling Github Discussions in a repo's general settings. If necessary, communicate in dedicated slack channels, but avoid communication in private conversations.

## Please also consider
- Who is affected by your changes? Include them in the PR review and approval process.
- Are your changes relevant enough for others to be included in a shared codebase? Think about how it will affect downstream tasks for others. Consider implementing your changes locally, e.g. in a personal fork, if you don't see any benefit for others.
- Consider including these guidelines in individual repositories with external collaborators.

## Additional Information
Feel free to link here any material to make us better coders, e.g.: 
- Tutorials on unit testing, e.g. [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html#create-your-first-test)
- [Pull main branch into another branch](https://www.delftstack.com/howto/git/git-pull-master-into-branch/)
- [Slides](https://docs.google.com/presentation/d/1AJG5WTQeUqHU4czdVNK9KQFzZK7cSV7S_0ch7ebm7KU/edit#slide=id.gda54aabedc_7_0) used in kickoff meeting on 28 April 2022