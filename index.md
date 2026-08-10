---
instructor: Federico Mora
instructor_url: https://federico.morarocha.ca
term: Fall '26
schedule: Tues 3:00-5:50pm
location: DC 2585
---

**⚠ DRAFT:** This syllabus will change substantially before the term begins.
{: .draft-banner}

# CS846: FMxAI

This course surveys important ideas and literature at the intersection of formal
methods and artificial intelligence.

## Grading

Our meetings will be centered around paper discussions. Attendance, reading of
assigned papers, and participation are essential. The grading scheme reflects
that:

- 25% participation;
- 25% discussion lead; and
- 50% project.


## Discussions

Every student will lead a paper discussion. 


## Projects

Every project must contain new research---a new idea or insight---and an
element of both formal methods and artificial intelligence.

The main deliverables (in chronological order) will be:

1. proposal;
2. mini presentation;
3. final presentation; and
4. report.

### Guidelines for Proposal

The proposal must contain a problem definition and a brief literature survey.
It should be at most one page long and use a reasonable font.

### Guidelines for Mini Presentation

The mini presentation should cover the contents of the proposal, a quick status
update, and a timeline for the remainder of the term. The mini presentation
should be at most five minutes long.

### Guidelines for Final Presentation

The final presentation should build on the mini presentation. It should contain
an updated problem definition, an updated literature survey, and final results.
The final presentation should be at most 15 minutes long.

### Guidelines for Report

The report should be a conference paper-style writeup. 

## Reading List

The readings below span nine themes: **SSC** syntactic and semantic constraints on LLM outputs, **LCD** learning constraints from data, **ATU** agents and tool-use, **SAT** satisfiability and satisfiability modulo theories, **PRA** program analysis, **AUF** autoformalization, **NSP** neuro-symbolic programming, **SUP** superoptimization, and **TPR** theorem proving. Use the dropdown in the table's rightmost column to narrow the list to a single theme.

| Title | Link | Topics |
| --- | --- | --- |
| Learning Regular Sets from Queries and Counterexamples | [Angluin, I&C '87](https://swt.informatik.uni-freiburg.de/teaching/WS2019-20/AutomataTheory/Learning%20Automata%20%28Caveat%20not%20related%20to%20Machine%20Learning?month:int=4&year:int=2025&orig_query=) | LCD |
| Mining Specifications | [Ammons et al., POPL '02](https://haoxintu.github.io/files/10-Mining%20specifications.pdf) | LCD |
| SATzilla: Portfolio-based Algorithm Selection for SAT | [Xu et al., JAIR '08](https://arxiv.org/abs/1111.2249) | SAT |
| Stochastic Superoptimization | [Schkufza et al., ASPLOS '13](https://dl.acm.org/doi/10.1145/2490301.2451150) | SUP |
| Learning to Solve SMT Formulas | [Balunović et al., NeurIPS '18](https://www.sri.inf.ethz.ch/publications/balunovic2018learnsmt) | SAT |
| How To Generate Text: Using Different Decoding Methods For Language Generation With Transformers | [von Platen, Blog '20](https://huggingface.co/blog/how-to-generate) | ATU, SSC |
| Learning Concise Models from Long Execution Traces | [Jeppu et al., DAC '20](https://arxiv.org/abs/2001.05230) | LCD |
| MedleySolver: Online SMT Algorithm Selection | [Pimpalkhare et al., SAT '21](https://www.pure.ed.ac.uk/ws/files/248374419/MedleySolver_PIMPALKHARE_DOA05072021_AFV.pdf) | SAT |
| PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models | [Scholak et al., EMNLP '21](https://aclanthology.org/2021.emnlp-main.779/) | SSC |
| Scallop: A Language for Neurosymbolic Programming | [Li et al., PLDI '23](https://dl.acm.org/doi/pdf/10.1145/3591280) | NSP |
| Grammar Prompting for Domain-Specific Language Generation with Large Language Models | [Wang et al., NeurIPS '23](https://arxiv.org/pdf/2305.19234) | SSC |
| Synthetic Programming Elicitation for Text-to-Code in Very Low-Resource Programming and Formal Languages | [Mora et al., NeurIPS '24](https://arxiv.org/pdf/2406.03636) | AUF, SSC |
| LLM Meets Bounded Model Checking: Neuro-symbolic Loop Invariant Inference | [Wu et al., ASE '24](https://dl.acm.org/doi/10.1145/3691620.3695014) | LCD, PRA |
| Specgen: Automated Generation Of Formal Program Specifications Via Large Language Models | [Ma et al., ICSE '25](https://dl.acm.org/doi/10.1109/ICSE55347.2025.00129) | AUF, LCD |
| Let a Neural Network Be Your Invariant | [Giacobbe et al., NeurIPS '25](https://openreview.net/forum?id=qBPb7g1SEa) | LCD, PRA |
| Large Language Model Powered Symbolic Execution | [Li et al., OOPSLA '25](https://doi.org/10.1145/3763163) | PRA |
| Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving | [ByteDance Seed, Arxiv '25](https://arxiv.org/pdf/2507.23726) | TPR |
| Learning Context-Free Grammars for Grammar-Constrained Decoding via Declarative Agentic Programming with Guarantees | [Cheang et al., Arxiv '26](https://arxiv.org/abs/2608.05493) | ATU, LCD |
| Reinforcement Learning from Human Feedback, Chapter 13 | [Lambert, Textbook '26](https://rlhfbook.com/c/13-tools) | ATU |
| Agentic Verification of Software Systems | [Tu et al., FSE '26](https://arxiv.org/abs/2511.17330) | PRA |
| Domain-Specific Hyperspecialization (For SAT) | [Green, Blog '26](https://c.mov/lymphosat/) | SAT |
| Constrained Adaptive Rejection Sampling | [Parys et al., ICML '26](https://arxiv.org/pdf/2510.01902) | SSC |
| ChopChop: A Programmable Framework for Semantically Constraining the Output of Language Models | [Nagy et al., POPL '26](https://arxiv.org/pdf/2509.00360) | SSC |
