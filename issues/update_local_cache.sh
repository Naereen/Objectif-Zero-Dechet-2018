#!/usr/bin/env bash
wget -np -k -e robots=off -r -l 1 https://github.com/Naereen/Objectif-Zero-Dechet-2018/{milestones,issues,labels}/

# gh2md -t $(cat ~/.gh2md_token) Naereen/Objectif-Zero-Dechet-2018 zero-dechet-issues.md
