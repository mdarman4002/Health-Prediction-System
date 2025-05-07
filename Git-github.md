# Health Prediction System - Git Setup Guide

## Step 1: Initialize Git in Your Project Directory
```bash
git init
```

## Step 2: Connect Your Project to the GitHub Repository
```bash
git remote add origin https://github.com/mdarman4002/Health-Prediction-System.git
```

## Step 3: Add All Files to Git (Stage Changes)
```bash
git add .
```

## Step 4: Commit Your Changes
```bash
git commit -m "Initial commit - Health Prediction System"
```

## Step 5: Set the Branch to Main (If Not Already Set)
```bash
git branch -M main
```

## Step 6: Push to GitHub
```bash
git push -u origin main
```

## Step 7: Future Updates (After the Initial Push)
For future updates, just use:
```bash
git add .
git commit -m "Your commit message"
git push
```
## when I got error
PS D:\HealthCare Project> git push -u origin main
To https://github.com/mdarman4002/Health-Prediction-System.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/mdarman4002/Health-Prediction-System.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
PS D:\HealthCare Project> 

Option 1: Pull and Merge (Recommended)
Fetch the remote changes:
```bash
git fetch origin
```
Merge the changes:
```bash
git pull origin main --allow-unrelated-histories
```
Now, try pushing again:
```bash
git push -u origin main
```
