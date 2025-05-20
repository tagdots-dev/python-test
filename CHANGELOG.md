# CHANGELOG

## 0.1.31 (2025-05-20)

### Refactor

- propagate cd staging changes to production

## 0.1.30 (2025-05-20)

### Fix

- skipped steps on PR merge caues empty tag name
- on CD staging workflow, skipped-all-jobs shows as failure
- pin pip command with hash

### Refactor

- switch pypi publishing from shell to GHA

## 0.1.29 (2025-05-20)

### Fix

- fix version from tag_name to ref_name

## 0.1.28 (2025-05-20)

### Fix

- fix error in CD production where it could not find dist folder

## 0.1.27 (2025-05-20)

### Fix

- fix missing slack messages

## 0.1.26 (2025-05-20)

### Fix

- misc typos

## 0.1.25 (2025-05-20)

## 0.1.24 (2025-05-20)

## 0.1.23 (2025-05-20)

## 0.1.22 (2025-05-20)

### Fix

- fix tag name not passed from ENV VAR on workflow

## 0.1.21 (2025-05-20)

### Fix

- address coddql finding
- update optional dependencies and add tool.pyproject-fmt section
- ossf initiative to pin hash to GitHub Actions

### Refactor

- break up CD into staging and production

## 0.1.20 (2025-05-15)

## 0.1.19 (2025-05-08)

### Feat

- add stale workflows, issues, pr, and branches

## 0.1.18 (2025-05-04)

## 0.1.17 (2025-05-03)

### Feat

- add new reusable-notify workflow and GH app github bot secret

### Fix

- prevent push-git-tag from running if CI fail

## 0.1.16 (2025-04-29)

## 0.1.15 (2025-04-29)

## 0.1.14 (2025-04-29)

## 1.89 (2025-04-29)

## 0.1.13 (2025-04-29)

## 0.1.12 (2025-04-29)

### Feat

- replace pypi secret source

## 0.1.11 (2025-04-28)

### Feat

- add workflow id

## 0.1.10 (2025-04-28)

### Feat

- publish to PyPI

### Fix

- change url to google

## 0.1.9 (2025-04-24)

### Refactor

- re-organize ci workflow and reusable workflow

## 0.1.8 (2025-04-23)

## 0.1.7 (2025-04-22)

## 0.1.6 (2025-04-21)

## 0.1.5 (2025-04-18)

### Feat

- add and update workflows
- add workflow release

### Fix

- fix release
- resolve empty git commit hash

## 0.1.0 (2025-04-16)

### Feat

- add package

### Fix

- fix pyproject by append src folder to package
