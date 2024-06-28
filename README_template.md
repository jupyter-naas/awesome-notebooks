# Naas Templates[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
(aka the "awesome-notebooks") 

## What is the objective of this repository ?
The objective of this repository is to create the largest catalog of production-ready Jupyter Notebooks templates. With those templates, it becomes easy to create data products (analytical dashboards, automation/AI engines and more).

Each of these templates adheres to a consistent framework, designed to expedite your coding process. While these templates are designed for ease of use, some may require data science skills for setup, particularly those that interface with third-party tools via API. These templates can function independently, but they also serve as integral components of data products. Consider them as the essential parts needed to assemble your 'car engine'. By developing these templates and ensuring their standalone functionality, we streamline the process of data product development, as we already comprehend the operation of some parts within it.

All templates are readily accessible on [GitHub](https://github.com/jupyter-naas/awesome-notebooks) or via [Naas Search](https://naas.ai/search).

![](https://site.naas.ai/assets/images/NaasSearch-1a3b28f814a61bfcbb1511997970a62d.gif)

## How is organized a template?

To ensure the quality of the templates, we have defined a framework. Each notebook shall be organized as follow.

### Header

- **Naas logo**
- **# Title**: "Tool - Action of the notebook", as h1. An "Open in Naas" button will be added automatically by the CI/CD when a notebook is merged to the master branch.
- **Tags:** hashtags relevant to the topics covered in the notebook, as text
- **Author:** name and social profile link of the author(s), as text
- **Last update:** YYYY-MM-DD (Created: YYYY-MM-DD): The last update date refers to when the notebook was last edited, while the created date corresponds to when the notebook was initially merged.
- **Description:** a one-liner explaining the benefits of the notebooks for the user, as text
- **References:** list of references and websites utilized in the creation of this notebook

![](https://site.naas.ai/assets/images/Templates_Header-891c53c6f58b031412f54f2c47f3bf6b.PNG)

### Outline

- **## Input**: list of all the variables, credentials, that needs to be setup, as h2
- **## Model**: list the functions applied to the data, as h2
- **## Output**: list the assets to be used by the user and its distribution channels if any, as h2

![](https://site.naas.ai/assets/images/Templates_Outline-60c612f83174a61f9bd9d3d912dccc2b.PNG)

## Providing Feedback

At the top of the notebook, you'll find a link for providing feedback on the notebook you're using. This could be:

- A suggestion for a new feature that could enhance the notebook
- Documentation improvements to make it more user-friendly
- Notification of a typographical error
- A simple word of praise (🙂)

Upon clicking this link, you'll be redirected to a Google form where you can provide more information. We will endeavor to contact the notebook creator for improvements or seek community assistance during our bi-monthly community calls that aim to create new templates or enhance existing ones.

![](https://site.naas.ai/assets/images/Templates_GiveFeedback-0b6357200a2e2ffb4dfd6d4d451b2f57.PNG)

## Reporting A Bug

Since all our templates are open-source, errors may occasionally occur. We apologize for any inconvenience that may cause and request your support in reporting these issues to help us rectify them. To report a bug, click on the link at the top of the notebook. You will be redirected to GitHub to create an issue. Please attach screenshots to help us understand the bug, and provide any other information that could assist us in reproducing the issue. We will strive to respond as quickly as possible to resolve the issue.

![](https://site.naas.ai/assets/images/Templates_BugReport-9005de95d2490678d263e65ed41b59e7.PNG)

## How to contribute?

### Pre-requisites
Register for the [Open Source Contributor Program](https://bit.ly/3F8Jsjr) so we can add you to the team of contributors in the Naas GitHub organization.

To start working on our repository, you **MUST** be a part of our [open-source contributors team](https://github.com/orgs/jupyter-naas/teams/opensource-contributors). 

Please check your email and validate the invitation before you begin working on a new issue.

### Step 1: Create or Select an Issue

- Identify or propose an issue you wish to work on. It could be a snippet of Python code, an API integration with a tool you are using, or an automation leveraging existing templates with our scheduler, asset, or webhook features. 
- Make sure the description is clear and concise.
- Tag yourself in the Assignees section.
- Click on "Create a new branch" on the Development section on the right side.
- Mentionned @FlorentLvr in a comment to let us you started working on it.

### Step 2: Technical Setup

- Create your [GitHub personal access token](https://github.com/settings/tokens). Select “No expiration” and tick only the first section repository and keep your token safe as you won’t be able to generate it again. This token will allow you to commit, push and pull directly on our repository.
- Clone the awesome-notebooks repository and switch to the branch you created.

```bash
# First, clone the repository
git clone https://github.com/jupyter-naas/awesome-notebooks.git

# Navigate into the cloned directory
cd awesome-notebooks

# Fetch all branches from the repository
git fetch

# Checkout to the specific branch you want
git checkout branch_name
```

### Step 3: Work on Your Notebook

If a draft of a template (generated with our AI system) has been already created, you can directly start working on it.
Otherwise, you kick start manually:
- Create a folder named with the source tool (if it's not already created).
- Copy/Paste template.ipynb at the root of the repository
- Rename the template following this format: `Toolname_Function.ipynb`.

Start working on your notebook. Commit your work every time you make significant progress. You can use the UI interface inside your Naas Lab server to do this.

- All new files will be found in the untracked section, all modified files in the unstaged section.
- Once you want to commit, add your notebook to staged by clicking on the + and create a commit message. We recommend following the commit convention and starting your message with “feat:” if it's an improvement or “fix:” if it's a bug fix, followed by a clear commit message. Here are some examples:
    - feat: update tags, author, and description
    - feat: developing function in model to…
    - fix: adding try except to manage error on…
- Once you're satisfied with the result, push to the branch.

```bash
# Navigate into the cloned directory
cd awesome-notebooks

# Add new template
git add Tool/Tool_Your_template.ipynb

# Commit with message
git commit -m "feat: xxxx"

# Push your work
git push
```

### Step 4: Open a Pull Request

Open a Pull Request and add a Templates Maintainer as Reviewer: Florent (@FlorentLvr).

- Comment on the Pull Request with a brief summary of what you've done.
- You will now discuss your work on the PR. If any changes are made, ensure you pull the branch before working on it again by clicking on the button at the top.
- Expect feedback and merge within the next 48-72 hours.

### Step 5: Promote Your Work

Once merged, promote your work on LinkedIn, Twitter, and other social media channels! (Optional, but people need to know you are awesome 😉). Explain why you did this notebook and how it could be useful. You can use the certificate generated once the PR is merged to display your work and add the tag open source contributor on your LinkedIn profile. We will be happy to have you in our community.

Thank you!

### Step 6: Become a Templates Maintainer

If you want to contribute more frequently to Naas, you can become a templates maintainer. This status will offer you the right to be sponsored by Naas for your contributions done every month, ranging from $50 to $250. To become a templates maintainer, you must have completed at least 5 notebooks (which ensures you've mastered our process) and created 5 social media content promoting your template or Naas.

Then, you will be introduced to our template maintainer program and will have a dedicated team with the core team to assist you in developing integrations, automations, or AI systems.

## Support us on social media

We are committed to sharing templates and giving shout outs to the contributors on our social media platforms, you can support us on:

- [Twitter](https://twitter.com/JupyterNaas) for fast updates
- [LinkedIn](https://www.linkedin.com/company/naas-ai/) for more elaborated posts and articles
- [Youtube](https://www.youtube.com/channel/UCKKG5hzjXXU_rRdHHWQ8JHQ/videos) for demos and tutorials

# Templates list

[[DYNAMIC_LIST]]


<br/>
Contact us on support@naas.ai if you need any help or join our [Slack community](https://join.slack.com/t/naas-club/shared_invite/zt-1970s5rie-dXXkigAdEJYc~LPdQIEaLA)
