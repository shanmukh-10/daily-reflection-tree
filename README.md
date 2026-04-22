# daily-reflection-tree

This repository contains my submission for the DT Fellowship Assignment: Daily Reflection Tree.

## Project Overview

I designed a deterministic reflection agent that guides users through an end-of-day self-reflection process using a structured decision tree. The system does not use any LLM at runtime. Instead, it uses fixed-choice questions, predefined branching logic, and summary nodes to provide a predictable and auditable reflection experience.

## Reflection Axes Covered

The tree progresses through three psychological axes in sequence:

1. **Locus of Control** – ownership vs external blame
2. **Orientation** – contribution vs entitlement
3. **Radius of Concern** – self-focus vs broader awareness

## Repository Structure
/tree/reflection-tree.tsv → Main tree structure in TSV format
/tree/reflection-tree.json → JSON version of the tree
/tree/tree-diagram.md → Visual flow of the decision tree
/write-up.md → Design rationale and approach

## Design Approach
* Fixed-option questions only
* Deterministic branching paths
* Reflection nodes based on selected answers
* Final summary based on accumulated signals
* Clean and readable data structure

## Objective
The goal of this project is to convert human reflection into a structured system that encourages self-awareness, contribution mindset, and wider perspective.

## Author
Shanmukh Reddy

