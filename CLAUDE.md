## Agents

This project has three specialized agents. Use them via the `Task` tool with the appropriate `subagent_type`.

### dp100-study-evaluator
- **When to use:** After the student completes work on a notebook, exercise, script, or explains a concept related to DP-100 exam preparation.
- **Triggers:** Student submits notebook code (01-10.ipynb), updates `src/train.py` or `src/score.py`, answers practice questions, or explains concepts from the learning plan.
- **What it does:** Evaluates work against the day's learning objectives, checks Azure ML SDK v2 correctness, assesses exam readiness, and gives structured feedback (strengths, improvements, exam tips).
- **How to invoke:**
  ```
  Task(subagent_type="dp100-study-evaluator", prompt="Evaluate the student's work on notebook 03 (MLflow logging)")
  ```

### claude-md-compliance-checker
- **When to use:** IMPORTANT: This agent must be used proactively after generating code, creating files, making architectural decisions, or completing any substantive task. It is also triggered automatically by the `Stop` hook before the assistant finishes responding.
- **Triggers:** Any code generation, file creation/modification, notebook edits, or architectural decisions.
- **What it does:** Audits all recent actions against this CLAUDE.md file. Checks repo structure compliance, content compliance (correct key concepts for the topic), naming conventions, and behavioral directives. Produces a structured compliance report.
- **How to invoke:**
  ```
  Task(subagent_type="claude-md-compliance-checker", prompt="Verify compliance of the recently created/modified files against CLAUDE.md")
  ```

### dp100-assignment-maker
- **When to use:** When the student needs a new notebook assignment or exercise created based on the DP-100 learning plan. This includes starting a new day's topic, requesting practice exercises, or scaffolding the next notebook.
- **Triggers:** Student is ready for a new day/topic, asks "what should I work on next?", finishes a notebook and wants the next one, or requests extra practice on a specific topic.
- **What it does:** Reads `docs/LEARNING_PLAN.md`, identifies the target topic, reviews existing notebooks for conventions, and creates a well-structured Jupyter notebook outline with scaffolded exercises, exam tips, and progressive difficulty.
- **How to invoke:**
  ```
  Task(subagent_type="dp100-assignment-maker", prompt="Create notebook assignment for Day 3 (MLflow logging)")
  ```

### Agent usage rules
1. After generating or modifying any code/files, **always** run the `claude-md-compliance-checker` before finishing.
2. When a student submits work for review, use `dp100-study-evaluator` to give feedback.
3. When a student is ready for a new topic or asks for the next assignment, use `dp100-assignment-maker` to create the notebook.
4. Agents can be run in parallel when applicable (e.g., evaluating student work AND checking compliance simultaneously).
