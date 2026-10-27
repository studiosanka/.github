# .github (Studio Sanka organisation)

GitHub treats a public repository called `.github` in an organisation specially. This one holds the files every Studio Sanka repository shares.

| File | What it does |
|---|---|
| `profile/README.md` | The front page of the organisation on GitHub (with the logo: `logo-light.png` for the light theme, `logo-dark.png` for the dark one) |
| `ISSUE_TEMPLATE/` | The issue forms every repository offers (unless it has its own) |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md` | Shown in each repository's "community" links |
| `pull_request_template.md` | For maintainers (we are not taking outside pull requests) |

Details about Studio Sanka (who we are, what we believe, the people) live on the **website**, not here. The profile README stays short and links to it.

## Before this repository is made public

Run `python scripts/check.py`. It lists these, which need a decision from Studio Sanka:

1. ~~A contact address for the code of conduct~~ (done: studiosankahq@gmail.com).
2. **The website.** It is marked "coming soon" in `profile/README.md` and `SUPPORT.md`, with no link. When it is live, add its address there and in `profile/README.md`'s repository table.
3. **Private vulnerability reporting** switched on (organisation settings, or each repository), so `SECURITY.md` works.
4. **Labels** `build-problem` and `enhancement` created in each repository (the issue forms ask for them; GitHub creates `bug` and `question` itself). Without them the forms still work, only the label is skipped.
5. **The wording "non-profit".** The profile README says "Not a company. No profit. Free, forever." like the website, because the website's notes advise against calling Studio Sanka a "non-profit" unless an organisation is registered. The `sixeyes` README does say "non-profit"; decide which wording you want everywhere.

## Publishing

Create a public repository named exactly `.github` in the `studiosanka` organisation and push this folder to it. The profile appears on `github.com/studiosanka` within a few minutes.

Licence of these text files: [CC-BY-4.0](LICENSE). The code of conduct is the [Contributor Covenant](https://www.contributor-covenant.org) 2.1 (CC BY 4.0).

*Developed with AI assistance from [Claude](https://www.anthropic.com/claude) (Anthropic); the decisions and review are by the Studio Sanka team.*
