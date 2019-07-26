# Renew Looker Template

This repository is a template for all Looker projects at Renew. It has a few key features:
1. Integration with CI (CircleCI)
2. Integration with LookML linter ([LAMS](https://looker-open-source.github.io/look-at-me-sideways/rules.html))
3. Use of best paractices (See Below)
4. Example Looker code

****

# Bootstrapping a New Project
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

15. On the [jobs page](https://circleci.com/gh/renewdotcom) click on the gear icon for your project name. Then click on enviroment variables on the side.
16. Add the following environment variables: GITHUB_REPO_NAME = <name of your repo>, GITHUB_REPO_OWNER = <usually renewdotcom but in general whichever account name is the owner of the repo> and GITHUB_USER_TOKEN = <This is the user who will comment's deploy token. Usually this is renewdeploy. Contact admins to get this token>
17. Go to your repo at github.com/renewdotcom/<your repo>. Go to the teams tab and add the renew deploy user with write access. Else you will see errors like: "github.GithubException.UnknownObjectException: 404 {'documentation_url': 'https://developer.github.com/v3/repos/#get', 'message': 'Not Found'}
Exited with code 1"
18. You should see a job run: \<name of your repo> >> master >> 1 (lint-lookML). You should see "No errors found"
19. Go back to the [projects page](https://renewrenew.looker.com/projects) and configure your project and model names. Save.
20. Rejoice! Enjoy! Hack away!

****

# When Contibuting Code

## 1. Branches and Merges
When starting a new project, please create a new branch (from Master) with the Jira ticket ID and a short descriptor. Do not use the default branch Looker gives you (with your name in it). When committing, always prefix commits with the ticket ID followed by a short description of what changed. Always follow the [commit messages guidelines](https://renewdotcom.atlassian.net/wiki/spaces/REN/pages/220823553/Development+Lifecycle#DevelopmentLifecycle-CommitMessages) found in Confluence. Once the branch is ready to be merged, please open a pull request for review. At this point, the changes will be linted and any errors will be posted as a comment of the PR.

****

## 2. Style Guide and Linting
We are using a [style guide called LAMS (Look At Me Sideways)](https://github.com/looker-open-source/look-at-me-sideways) and have a linter setup in CircleCI to enforce the style guide. It's recommended to [read the style guide](https://looker-open-source.github.io/look-at-me-sideways/rules.html) to understand what to expect for linting.

****

## 3. Folders & Model Files
While this is a touch abstract, the goal is to always create a folder and a model together for each major set of data being manupilated. It might be easier to think of this as the data set at an abstract level. For example, contracts have star ratings that are calculated from measures and domains. There are several files that make up this data set, but when you boil it down, it is all related to star ratings. Therefore, there's a `star_ratings` model file that lives in a folder with the same name.

#### 3a. Includes
A model should always be explicit, therefore it should explicitly include only the views in which the model is using.

#### 3b. File Denoting
Please always be very explicit with the setup of your model file. This includes reasoning for file versions (if multiple) and other items such as derived tables.

****

## 4. View Files
The goal is to organize the files in the way that allows multiple Looker users to manipulate a single table without adding redundant parameters, while also not creating exhaustive, hard to navigate, files in the process.

#### 4a. Naming Convention
Please use the following naming convention when naming a view file:
- `["dt".]<schema>.<table>[.use_case]`

It's generally recommended to rename the file after using the option "Create View from Table".

- Optionally, where literally "dt." is used for any derived table (persistent or otherwise)
- `<schema>` is the name of the schema (e.g. "part_d")
- `<table>` is the name of the table (e.g. "summary_2016")
- When a table being extended or derived, there should be a short use case desc for how the file was reorganized or changed

#### 4b. Naming Convention Example
- If you import a table called `summary_2016` from the `part_d` schema, than the view file should be renamed to: `part_d.summary_2016`
- If the aforementioned view is extended for a new project, called "Formulary Research", the view file might be named something similar to: `part_d.summary_2016.formulary_research`
- If you were to create a derived table to group the aforementioned view to be grouped by the `drug_name` dimension, the view file might be named something similar to: `dt.part_d.summary_2016.groupby_drugname`

#### 4c. View Parameter Name
The name of the view parameter should always align with the name of the file. For example, if the view file is called `part_d.summary_2016` than the name of the view should be `part_d_summary_2016`

#### 4d. Base Views (Tables)
Whenever a new table is added into Looker, a new view should be created and be stored at the root directory (even if Looker creates it for you). It should follow the above naming convention resulting in a simple `schema.table` file name. This file should align with the style guide and serve as the universal base in which other views can extend from. It should not be home to any custom measures or dimensions. A base table should only contain a single view parameter, while extended files can contain multiple parameters when it makes sense.

#### 4e. Extended Views
When referencing a view within a model, an new view file that is extended from the base should be created. This file should contain model specific measures and dimensions.

#### 4f. Cross Reference Params
When creating a measure or dimension that references multiple views, always denote this in the comment and store the parmeters in the primary view (think "left" of a join). Due to the nature of how we organize our files, this should be an extended file and never in the base view file.

#### 4g. Derived Tables (DT)
When creating a derived table from an explore, always denote that the explore is relied on by a derived table with a clear comment. It is generally recommended to include the link to the explore from when the DT was created.

## Workflow (Nota Bene: Anyone using LookML and developing must read this section)
1. On looker's web IDE you make some commits.
2. You push commits to GH (with or without PR open)
3. If PR is open you go to the PR and you will see a comment from a user, RenewDeploy, who is outputing the linting errors
4. If PR is not open at the time of push 1 of 2 scenarios will happen:
    1. If there are no linting errors then your circle job will succeed. When the PR is opened no comment will be shown because at the time of the push there was no PR open. You can continue as usual.
    2. If there are linting errors then your circle job will fail. When the PR is opened there will be no comment explaining why the job failed. You can click into the details of the failed job (the circleci job called lint-lookml) then you can hit re-run on the top left. Or you can push another commit to the PR. After either action is done you should see the comments pop up on the PR as usual.
