# Looker Renew Template

This repository is a template for all Looker projects at Renew. It has a few key
features:
1. Integration with CI (CircleCI)
2. Integration with LookML linter ([LAMS](https://looker-open-source.github.io/look-at-me-sideways/rules.html))
3. A sample view and model

This repo attempts to follow best practices as explained by [this article](https://discourse.looker.com/t/introducing-lams-a-lookml-style-guide-and-linter/10603).

## Bootstrapping a new Looker project
1. Go to github.com and click on the plus icon. Click on create new project.
2. On create [page](github.com/new) start with a repository template: renewdotcom/renew-looker-template. Then name your project and keep it private. Create.
3. Now you should see the repository in Github where it says generated from renewdotocom/renew-looker-template.
4. Go to looker.com and enter development mode.
5. Under develop > [Manage projects](https://renewrenew.looker.com/projects)
6. Create New LookML Project (need to be admin for this step and config)
7. On the [new project page](https://renewrenew.looker.com/projects/new) for project name put the same name as the github repo. For starting point put Blank Project. Then create Project.
8. On the next page (lookML IDE) there should be a section and or button labeled Configure Git. Click on that and it should ask for the repository URL.
9. Go back to your project page on Github. Copy the clone or download url (with SSH) (looks like: git@github.com:renewdotcom/renew-looker...) Then click continue.
10. Copy the deploy key from looker then go to github repo > settings > deploy keys add new key. For title you can write looker. Paste the rsa key in the key section. Check off the allow write access. Then click add key.
11. Go back to looker and click test and continue. If it succeeds (as in you copy and pasted the key correctly) then you will go back to the IDE.
12. Pull from master/production.
13. Now onto configuring circleci (which will add linting)
14. Go to ciricleci.com > add project. Search for your project then click add. For language put other. Then click on start building. DO NOT follow the circleci steps. The configurations are already in the repo!
15. On the [jobs page](https://circleci.com/gh/renewdotcom) click on the gear icon for your project name. Then click on environment variables on the side.
16. Add the following environment variables: GITHUB_REPO_NAME = <name of your repo>, GITHUB_REPO_OWNER = <usually renewdotcom but in general whichever account name is the owner of the repo> and GITHUB_USER_TOKEN = <This is the user who will comment's deploy token. Usually this is renewdeploy. Contact admins to get this token>
17. You should see a job run: \<name of your repo> >> master >> 1 (lint-lookML). You should see "No errors found"
18. Go back to the [projects page](https://renewrenew.looker.com/projects) and configure your project and model names. Save.
19. Rejoice! Enjoy! Hack away!

### Important things to remember while contibuting code
1. Your development branch should NOT be the default looker gives you but rather your ticket number and branch name should match (REN-1234-xyz-thing)
2. After you push a commit go to the pull request on github and look at the linter output. It appears as a comment in the discussion.
