 Conversation with Gemini

FELLOWS' ENGINEERING GUIDE

AI-Native Engineering Sprint — CampusFlow

6-HOUR TEAM CHALLENGE  |  2 FELLOWS PER TEAM  |  100 MARKS  |  PYTHON + AI LEARNING + GITHUB


YOUR MISSION: Build a working product. Learn with AI. Verify everything. Review each other's code before merging.

This is your practical, step-by-step guide. Read the mission once, then follow the six-hour checkpoints. You are not expected to know every concept in advance; you ARE expected to learn deliberately, test your decisions, and collaborate professionally.

START HERE | WHAT SUCCESS LOOKS LIKE

    Your team delivers a command-line helpdesk app called CampusFlow with ticket creation, priority calculation, assignment, status changes, queue, reporting, JSON storage, and automated tests.
    Both fellows independently contribute Python code and tests on their own Git branches.
    Each fellow authors a pull request (PR), reviews the other fellow's PR, and receives approval before merging into main.
    Each fellow records at least three verified AI learning interactions, including one AI suggestion independently corrected, improved, or rejected.
    Your team runs the complete test suite on main and demonstrates the project together within six hours. 

NON-NEGOTIABLE: A project that works but has no genuine GitHub review, no tests, or no evidence of AI-assisted learning is NOT a complete submission.

1 | UNDERSTAND THE PRODUCT YOU ARE BUILDING

1.1 The real-world problem

Learn2Earn campus staff receive technical support requests: Wi-Fi outages, faulty laptops, broken development environments, and inaccessible platforms. Informal reports get lost. Build CampusFlow, a Python command-line ticket manager that records problems, prioritizes work, assigns responsibility, and tracks progress.

Think like engineers: Which inputs does the system need? What must it calculate? What could go wrong? What should be preserved after the program closes?

1.2 Ticket fields (required)

Each ticket stores: id, title, category, urgency, affected_users, priority, status, and assigned_to.

EXAMPLE (Python dictionary):

{

  "id": "T001",

  "title": "Campus Wi-Fi is down",

  "category": "Network",

  "urgency": "high",

  "affected_users": 15,

  "priority": "critical",

  "status": "open",

  "assigned_to": None

}

    Ticket IDs are unique and automatically generated (T001, T002, T003, …).
    Allowed categories: Network, Hardware, Software, Other.
    Allowed urgency levels: low, medium, high.
    Title must not be blank. affected_users must be a positive integer (not zero, a negative number, a decimal, or text).
    Accept and normalize valid case variations consistently; display useful errors for invalid input. 

1.3 Calculate priority exactly as specified

Your function must check the following rules IN THIS ORDER and apply the first match:

RULE 1   high urgency AND 10 or more affected users  →  critical

RULE 2   high urgency OR 10 or more affected users    →  high

RULE 3   medium urgency OR 3 or more affected users   →  medium

RULE 4   all remaining valid tickets                  →  low

Important: This engine is ordinary Python business logic, not an AI model. You use AI to LEARN and BUILD, not as the priority engine itself.

1.4 Build these seven features

    F1 — CREATE: Collect ticket details, validate inputs, calculate priority, assign a unique ID and store the record.
    F2 — LIST / VIEW: Show all tickets and details for one chosen ticket.
    F3 — ASSIGN: Assign a ticket to a non-empty staff member name; reject unknown ticket IDs.
    F4 — WORKFLOW: Support open → in_progress → resolved. Do not move an unassigned ticket into in_progress. A resolved ticket may only be modified after an explicit reopen that sets it to open.
    F5 — WORK QUEUE: Show open, unresolved tickets in critical → high → medium → low order; break priority ties using the earlier numeric ticket ID.
    F6 — REPORTS: Show total tickets and breakdowns by status and priority; handle zero tickets correctly.
    F7 — PERSISTENCE: Save to JSON and reload on startup. Missing file should allow a fresh start; malformed JSON should produce a clear error rather than silently erase data. IDs must remain unique after reload. 

Create a menu that keeps running until Exit. The interface can be text-only. Do not spend sprint time building a GUI or website.

1.5 Decide what 'done' means

☐ All seven features are available from a functioning CLI menu.

☐ The specified priority examples produce correct results.

☐ Invalid inputs and transitions are rejected WITHOUT corrupting stored tickets.

☐ Tickets survive a restart using JSON.

☐ At least eight meaningful automated tests pass on the integrated main branch.

☐ Both PRs have genuine partner review, approval, and merge evidence.

2 | BEFORE CODING: WORK AS A TWO-PERSON ENGINEERING TEAM

2.1 Agree on responsibilities

Suggested ownership (you may agree on equivalent balanced ownership):

ENGINEER A: ticket creation, input validation, and priority engine; write matching automated tests.

ENGINEER B: assignment, lifecycle, queue, and reports; write matching automated tests.

BOTH: agree on data structures and function contracts; integrate JSON persistence; review each other's code; complete AI learning logs and technical defence.

Each person must write real application code AND tests. One person doing all implementation while the other only watches or writes the README does not satisfy the team rules.

2.2 Agree on function contracts

Before writing features, discuss these questions together:

☐ Where is the ticket collection stored and how is it passed between functions?

☐ How does a function signal invalid input (exception or structured error), and how does the CLI display it?

☐ What is the expected return value when a ticket is created, assigned, or updated?

☐ Which module owns loading/saving JSON and how do other modules call it?

☐ How can we test business logic without asking for interactive input inside each test?

Record your agreements in docs/design-decisions.md. Keep decisions simple; the goal is agreement, not perfect architecture.

2.3 Example project layout (suggested)

campusflow/

├── README.md

├── .gitignore

├── main.py

├── campusflow/

│   ├── __init__.py

│   ├── tickets.py

│   ├── workflow.py

│   ├── storage.py

│   └── reports.py

├── tests/

│   ├── test_tickets.py

│   ├── test_workflow.py

│   └── test_storage.py

└── docs/

    ├── ai-learning-log.md

    └── design-decisions.md

Use Python's standard library, including unittest and json. You do not need a framework, database, AI SDK, or API key. Exclude runtime files like data/tickets.json and developer-local files from Git.

3 | SIX-HOUR GUIDED SPRINT

PHASE 1 — 00:00–00:20 | SET UP THE REPOSITORY

Together, create ONE GitHub repository named campusflow-<team-id> (or a similarly clear name). Invite your partner as a collaborator and ensure both can push their own branches. Initialize main with a README and .gitignore. Clone the repository to each computer.

☐ Both fellows can open the repository and see main.

☐ Both fellows have Git configured with their own account and identity.

☐ README states the project goal and team members.

☐ .gitignore includes .venv/, __pycache__/, *.pyc, .env and data/tickets.json.

Evidence checkpoint: GitHub repository URL, both collaborators, initial commit.

PHASE 2 — 00:20–00:50 | PLAN BEFORE IMPLEMENTING

Read the seven features together. Create GitHub Issues with clear acceptance criteria, for example: “Create a ticket with valid data” and “Reject affected_users=0”. Decide which fellow owns each feature and agree on shared function contracts.

☐ A GitHub Issue exists for each major work area (combine small related tasks where practical).

☐ Each fellow has a clear coding task and a matching test responsibility.

☐ docs/design-decisions.md records agreed interfaces and ownership.

☐ You can explain how both feature branches will work together before merging.

Evidence checkpoint: Issue list and design-decisions document.

PHASE 3 — 00:50–01:30 | LEARN WITH AI BEFORE YOU BUILD

Individually choose TWO topics you are unsure about (for example JSON persistence, Python exception handling, unittest assertions, safe list operations, Git branches, or PR reviews). Do not ask AI to build the full CampusFlow project.

Complete a small learning loop for each topic:

    State what you currently understand and the specific point you do not understand. 

2. Ask AI for an explanation and a SMALL unrelated example.

3. Run or adapt a tiny experiment yourself; predict the result before executing it.

4. Verify the result from the output, a test, or official reference documentation.

5. Explain what you learned in your own words and how it will help your feature.

This is the first part of your AI learning log. Complete at least one additional entry during coding/debugging to reach three per fellow.

☐ Each fellow has at least two initial AI learning entries or experiments.

☐ Each fellow can explain a concept learned without repeating an AI response word for word.

Evidence checkpoint: two learning experiments per fellow.

PHASE 4 — 01:30–03:55 | IMPLEMENT, TEST, COMMIT

Work on separate feature branches. Build the agreed functions and write automated tests. Keep changes focused; make meaningful incremental commits. Use AI for explanations, investigating test failures, edge cases and design critique; VERIFY every suggestion.

Suggested cadence: implement a small requirement → test locally → inspect git diff/status → commit → continue.

☐ Both fellows have meaningful code commits on their own branches.

☐ Core functionality is separated enough to unit-test.

☐ At least eight meaningful tests are planned and being implemented.

☐ Invalid-input cases are tested, not just successful paths.

☐ Each fellow has at least three AI log entries, with one documented critical evaluation.

Evidence checkpoint: published feature branches, commits, test files, AI logs.

PHASE 5 — 03:55–05:00 | OPEN AND REVIEW PULL REQUESTS

Engineer A opens a PR from A's feature branch to main. Engineer B reviews it. Engineer B opens a PR and Engineer A reviews it. Each reviewer must inspect real code, check requirements, run relevant tests where practical, and leave at least TWO substantive review observations before approval.

If there is a real blocking problem, request changes. The author commits a correction to the same branch, pushes it and asks for re-review. Only merge after approval and passing relevant tests.

☐ Each fellow authored at least one feature PR.

☐ Each fellow reviewed the other fellow's PR.

☐ PRs include a clear description, Issue reference and test evidence.

☐ Review comments are meaningful (not merely “LGTM” or “good code”).

☐ Every blocking issue is resolved and the final reviewer approval is visible.

☐ No one self-approved or merged an unreviewed PR.

Evidence checkpoint: links to two reviewed PRs. If the second branch is behind main after the first merge, update it from main, resolve conflicts, rerun tests and obtain approval on the final changes.

PHASE 6 — 05:00–05:40 | INTEGRATE AND POLISH

Run the whole project from latest main. Run every automated test, verify JSON round-trip persistence and unique IDs after reload, and check an invalid status transition. Fix integration defects through a new reviewed PR—not by bypassing the workflow.

☐ Both approved feature PRs are merged into main.

☐ The CLI works from main on a clean run.

☐ Automated tests are passing on main.

☐ README contains clear run/test instructions and honest known limitations.

☐ Learning log and design-decisions documents are committed.

Evidence checkpoint: main commit, passing test output, complete documentation.

PHASE 7 — 05:40–06:00 | DEMONSTRATE AND DEFEND

You have 20 minutes for the team's final demonstration and technical explanation. Both fellows must speak about their own work.

Demonstration route: create several tickets → show priority output → reject an invalid ticket → assign and progress a ticket → reject an invalid transition → display ordered queue/report → save and reload → run automated tests → show both PR reviews.

☐ Engineer A explains one implementation decision and a relevant test.

☐ Engineer B explains one implementation decision and a relevant test.

☐ Both fellows explain one AI suggestion they verified, changed or rejected.

☐ Both fellows can show the PR they authored and the PR they reviewed.

Evidence checkpoint: shared repository and PR links, test results, and individual explanations.

4 | PROFESSIONAL GIT WORKFLOW: COPYABLE GUIDE

4.1 Use a proper branch name

Format: <type>/<issue-number>-<short-description>. Lowercase words, hyphens between words, and an actual GitHub Issue number when available.

GOOD BRANCH NAMES

feat/1-ticket-creation

feat/2-status-workflow

fix/7-invalid-status-transition

test/8-ticket-validation

docs/9-readme-setup


AVOID

john-work

branch2

final-final

new-stuff

4.2 Create a feature branch from latest main

git clone <repository-url>

cd <repository-folder>

git switch main

git pull origin main

git switch -c feat/1-ticket-creation

4.3 Inspect and commit a small piece of work

git status

git diff

git add campusflow/tickets.py tests/test_tickets.py

git commit -m "feat: implement ticket creation"

git push -u origin feat/1-ticket-creation

Professional commit examples: feat: add ticket creation validation; test: cover priority boundaries; fix: reject invalid status transitions; docs: document running tests. Stage relevant files rather than blindly including unrelated changes.

4.4 Open your PR on GitHub

On GitHub: select your pushed branch → Compare & pull request → base: main / compare: your feature branch → add a concise title → fill out description and test evidence → link related Issue → request review from your partner.

You must not create a PR with no meaningful description, nor merge it before partner review.

4.5 Review your partner's PR professionally

On GitHub: open Pull requests → your partner's PR → Files changed. Read the actual code; compare the implementation with the requirements; inspect test additions. Comment on specific lines where possible. To test it locally, fetch the branch and run its tests in a non-editing checkout:

git fetch origin

git switch --detach origin/feat/2-status-workflow

python -m unittest discover -s tests -v

# Return to your usual branch

git switch main

The feature branch shown is an example. Replace it with the actual name of the PR branch. Detached checkout lets you inspect the exact remote snapshot without modifying your partner's branch.

Your review should explain a concern or a verified check. Examples: “If affected_users is zero, this function currently accepts it; please add a test and validation.” or “I ran the tests and confirmed the high+10 boundary gives critical.”

If blocking issues exist, choose Request changes. If the change is ready, choose Approve. After your partner updates the branch, review the final code before approval. The author cannot approve their own PR.

4.6 Update a feature branch when main changes

If your partner's first PR is merged before yours, update your branch and retest. One beginner-friendly approach:

git switch main

git pull origin main

git switch feat/2-status-workflow

git merge main

# Resolve any conflicts by reading both changes carefully.

python -m unittest discover -s tests -v

git add <resolved-files>

git commit    # Only if a merge commit is pending.

git push

A merge conflict is not a disaster: inspect markers, decide the correct combined behaviour with your partner, remove the markers, rerun tests, and push the resolved branch. If unsure, ask for explanation—not for someone to erase the conflict blindly.

Professional standard: no direct work on main, no unreviewed merge, no secrets in commits, no fabricated tests or reviews.

5 | HOW TO USE AI LIKE AN ENGINEER

5.1 Your learning cycle

Understand the task → identify what you don't know → ask AI a focused question → experiment in a small isolated example → verify → apply the learning → test your application.

5.2 Prompts you may use as starting points

LEARNING: “Explain json.dump() and json.load() with a five-line example unrelated to CampusFlow. Then quiz me. I want to write my own code.”

DESIGN: “I plan to store tickets in a list of dictionaries. What trade-offs should I consider for updates, lookup, and testing? Do not code my project.”

DEBUGGING: “Here is my failing test and traceback. Help me isolate likely causes. Give experiments first, not a complete rewrite.”

TESTING: “Here are my acceptance criteria. Which edge cases should I test, and why? Give descriptions rather than finished project tests.”

CODE REVIEW: “Here is a small diff. Point out risks and questions for a human reviewer. I will verify your claims myself.”

5.3 Individual AI learning-log entry template

## Fellow: <your name>

### Interaction #1 — <concept/topic>

Problem: <what I needed to learn>

My initial understanding: <in my own words>

Prompt to AI: <my actual prompt>

Useful AI guidance: <brief summary>

My independent experiment/test: <what I ran and observed>

Verification source or result: <test result/reference>

Decision: <accepted, improved or rejected and why>

Related file/commit: <path, test name, SHA or PR link>

What I can now explain without AI: <my words>

Do this for at least THREE meaningful interactions per fellow. At least ONE must document how you corrected, improved or rejected an AI suggestion after checking it. Keep the log truthful; do not fabricate a flaw or pretend to have verified something you did not run.

AI usage is required, but copy-pasting a full app without understanding or testing it does not count as engineering learning.

6 | AUTOMATED TESTING: LEARN TO PROVE IT WORKS

You must write at least EIGHT meaningful automated tests using unittest. A useful test has a clear expectation and an assertion. Include normal cases, invalid inputs, boundaries, and persistence.

6.1 Required acceptance scenarios (prioritize these)

☐ High urgency + 12 affected users → critical priority.

☐ High urgency + 2 affected users → high priority.

☐ Low urgency + 4 affected users → medium priority.

☐ Low urgency + 1 affected user → low priority.

☐ Zero affected users → rejected.

☐ Unassigned ticket cannot move to in_progress.

☐ Assigned ticket can progress through open → in_progress → resolved.

☐ Open-ticket queue sorted by priority and then numeric ID.

☐ Save and reload JSON preserves existing tickets.

☐ Create a ticket after reload without duplicating IDs.

Recommended extra cases: empty report, unknown ticket ID, blank title, invalid urgency, invalid transition, reopening, corrupted JSON, and ties in the work queue.

6.2 Test command

python -m unittest discover -s tests -v

Do not just say 'the tests pass'. Run them and inspect the output. A failing test is valuable feedback; fix the underlying requirement and run again. Do not modify tests merely to make a broken implementation appear correct.

7 | PR DESCRIPTION TEMPLATE

Copy this outline into each GitHub pull request and complete it honestly.

PR TITLE: feat: <short meaningful change>

Related Issue: Closes #<number>


WHAT CHANGED?

    <features and files modified> 


HOW DOES IT WORK?

    <approach and key decisions> 


HOW DID I TEST IT?

    Command: python -m unittest discover -s tests -v
    Actual result: <pass/fail details>
    Edge cases: <what I verified> 


WHAT DID I LEARN WITH AI?

    Concept: <topic>
    My verification: <experiment or test>
    Changed/rejected advice: <if applicable> 


REVIEWER NOTES

    What I want my partner to check: <specific risk/question> 


KNOWN LIMITATIONS

    <honest known gaps> 

8 | README CHECKLIST

☐ Project title and clear problem statement.

☐ Both fellows' names/roles and a short contribution summary.

☐ Python version and setup instructions.

☐ How to run the CLI and available menu options.

☐ How to run the tests and what they cover.

☐ How ticket priority and status rules work.

☐ Where tickets are saved and how to start fresh.

☐ Known limitations and future improvements.

☐ Links to both reviewed PRs (or a GitHub PR index).

9 | ASSESSMENT: HOW YOUR WORK IS SCORED

FUNCTIONAL IMPLEMENTATION — 40 marks

15 — Ticket creation and priority engine.

10 — Assignment and status management.

10 — Open-ticket queue and reporting.

5 — JSON persistence.

TESTING AND RELIABILITY — 15 marks

15 — Automated tests, meaningful assertions, invalid-input cases, and reliable behaviour.

PROFESSIONAL GIT WORKFLOW — 20 marks

5 — Branch naming and commit quality.

5 — PR descriptions and traceable individual work.

10 — Substantive partner reviews, approval, and correct merges.

AI-NATIVE ENGINEERING — 20 marks

5 — Conceptual learning with AI.

5 — Independent experiments and verification.

5 — Critical evaluation of AI suggestions.

5 — Quality and credibility of learning logs.

TECHNICAL DEFENCE — 5 marks

5 — Working explanation, demonstration, README and individual understanding.

TOTAL: 100 marks. Feature functionality and integrated test outcomes are assessed as team work. Git contributions, AI learning and individual understanding are assessed per fellow; you do not automatically earn another fellow's process marks.

10 | FINAL SUBMISSION CHECKLIST

☐ Paste the GitHub repository link (main branch).

☐ Paste Engineer A's PR link and Engineer B's PR link.

☐ Confirm both PRs have real cross-reviews and final approvals.

☐ Show the actual unittest result from latest main.

☐ Complete README.md, docs/design-decisions.md, and docs/ai-learning-log.md.

☐ Both fellows can explain their own code and what they learned using AI.

☐ Prepare a live demonstration including one invalid input, one valid lifecycle change, queue/report, and persistence.

Final individual reflection (each fellow answers)

    Which feature did you personally implement, and how do you know it works? 

2. What did AI teach you that you did not understand at the start?

3. Give one example where you verified, changed, or rejected an AI suggestion.

4. What did you learn from reviewing your partner's PR?

5. What would you improve next if the team had another hour?

11 | QUICK SELF-CHECK: ARE WE REALLY WORKING LIKE ENGINEERS?

☐ We understand the problem before writing code.

☐ We can explain each implementation decision.

☐ We use AI to learn, test, compare, and question—not blindly paste.

☐ We write tests for important behaviour and run them.

☐ We use Git branches with descriptive names and meaningful commits.

☐ We check each other's code before merging.

☐ We take responsibility for mistakes and fix them transparently.

☐ We communicate respectfully and share knowledge.


FINAL PRINCIPLE

“AI is your learning partner, not your replacement. Git is how you collaborate, not just where you upload code. A pull request invites careful review, not automatic approval. Your team succeeds when BOTH fellows understand what they have built and can demonstrate it with evidence.” _Ezennia Kingsley


summerize evrything i nned to know about this project before i begin and and a guild to approaching this

Here is a complete summary of everything you need to know about the CampusFlow AI-Native Engineering Sprint, followed by a step-by-step tactical guide to approaching it.
Part 1: Everything You Need to Know (Summary)
1. Project Overview & Deliverable

    Goal: Build CampusFlow, a Python Command-Line Interface (CLI) technical support ticket manager.

    Format: 6-Hour Sprint with a 2-person team (100 Marks total).

    Stack: Pure Python (standard library only: unittest, json), Git & GitHub. No frameworks, external packages, databases, or AI APIs needed.

2. Core Functional Requirements (7 Features)
ID	Feature	Requirements & Business Rules
F1	Create Ticket	Collect title (non-blank), category (Network, Hardware, Software, Other), urgency (low, medium, high), and affected_users (positive integer >0). Calculate priority and assign unique sequential ID (T001, T002, ...).
F2	List / View	Display all tickets in a list, or view full details for a specific chosen ticket.
F3	Assign	Assign ticket to a non-empty staff name. Reject requests for non-existent ticket IDs.
F4	Workflow	

Lifecycle: open → in_progress → resolved.

• Cannot move to in_progress if assigned_to is empty/None.

• Resolved tickets can only be modified if explicitly reopened back to open.
F5	Work Queue	Display unresolved tickets sorted by priority: critical → high → medium → low. Break priority ties using the earlier numeric ID (e.g., T001 before T002).
F6	Reports	Display total ticket count and breakdowns by status and priority. Safely handle zero-ticket scenarios.
F7	Persistence	Save/load data to/from JSON (data/tickets.json). Handle missing file gracefully (start fresh). Handle malformed JSON with clear error (do not overwrite/erase). Ensure new ticket IDs remain unique after reload.
3. Strict Priority Calculation Algorithm

Your function must evaluate rules in this exact order and stop at the first match:
RULE 1:RULE 2:RULE 3:RULE 4:​urgency=="high"ANDaffected_users≥10urgency=="high"ORaffected_users≥10urgency=="medium"ORaffected_users≥3All remaining valid tickets​⟶critical⟶high⟶medium⟶low​
4. Non-Negotiable Non-Functional Rules

    Testing: At least 8 automated unit tests using Python's built-in unittest module passing on main.

    Git Workflow:

        No direct commits to main (except repository initialization).

        Feature branch naming convention: <type>/<issue-number>-<short-description> (e.g., feat/1-ticket-creation).

        Both fellows must author at least 1 Pull Request (PR) and leave at least 2 substantive code review observations on their partner's PR before approving and merging.

    AI Learning Logs: Each fellow must log 3 distinct AI learning interactions in docs/ai-learning-log.md. At least 1 entry per fellow must document an AI suggestion that was independently corrected, improved, or rejected.

5. Mark Distribution (100 Marks)

    40 Marks: Functional Implementation (F1–F7 working via CLI)

    20 Marks: Professional Git Workflow (Branching, commit quality, PR descriptions, cross-reviews)

    20 Marks: AI-Native Engineering (Learning logs, experiments, critical evaluation)

    15 Marks: Testing & Reliability (unittest coverage, invalid input handling)

    5 Marks: Technical Defense & Live Demo (20-min team presentation at end)

Part 2: Step-by-Step Approach Guide

Follow this minute-by-minute timeline to complete the sprint successfully.
Phase 1: Setup & Contract Agreements (00:00 – 00:50)
Step 1: Git & Repository Setup (20 mins)

    Engineer A: Create GitHub repo campusflow-<team-id> with .gitignore (ignore .venv/, __pycache__/, data/tickets.json) and a basic README.md. Invite Engineer B.

    Both fellows clone the repository locally and verify identity config:
    Bash

    git config user.name "Your Name"
    git config user.email "your.email@example.com"

Step 2: Division of Responsibilities & Contract Agreement (30 mins)

Split the work clearly and create GitHub Issues:

    Engineer A (Creation & Priority Engine):

        Issues: Ticket Creation (F1), Priority Logic, Input Validation, Unit Tests for Creation/Priority.

    Engineer B (Lifecycle, Queue, Reports & Persistence):

        Issues: Assignment (F3), Status Workflow (F4), Work Queue (F5), Reports (F6), JSON Persistence (F7), Unit Tests for Workflow/Storage.

Document data structure and function signatures in docs/design-decisions.md:
Python

# Standard Ticket Schema
{
    "id": "T001",           # str
    "title": "Wi-Fi Down",  # str (non-blank)
    "category": "Network", # str (Network|Hardware|Software|Other)
    "urgency": "high",      # str (low|medium|high)
    "affected_users": 15,   # int (>0)
    "priority": "critical", # str (critical|high|medium|low) - calculated
    "status": "open",       # str (open|in_progress|resolved)
    "assigned_to": None     # str or None
}

Phase 2: AI Learning Loop (00:50 – 01:30)

Before writing project code, complete 2 required AI learning logs:

    Identify a concept you are unsure about (e.g., Python unittest.assertRaises, handling malformed JSON, custom exceptions).

    Prompt AI for an explanation with a small, unrelated code snippet.

    Run a tiny test locally to verify the behavior.

    Record your findings in docs/ai-learning-log.md using the required template:

Markdown

## Fellow: [Your Name]
### Interaction #1 — [Topic]
- **Problem:** Need to know how to handle file-not-found in JSON loading.
- **My understanding:** Try-except block catches FileNotFoundError.
- **Prompt to AI:** "Show a 5-line example of safe json loading in Python when file might not exist."
- **Useful Guidance:** AI suggested catching `FileNotFoundError` and `json.JSONDecodeError`.
- **Experiment & Result:** Tested with missing file; returned empty dict correctly.
- **Decision:** Accepted and adapted for `storage.py`.
- **What I can explain:** Difference between missing file and corrupted content.

Phase 3: Implementation & Local Testing (01:30 – 03:55)
1. Create Feature Branches
Bash

# Engineer A
git switch -c feat/1-ticket-creation

# Engineer B
git switch -c feat/2-workflow-storage

2. Code Structure

    campusflow/tickets.py: calculate_priority(urgency, affected_users), create_ticket(...), input validation.

    campusflow/workflow.py: assign_ticket(...), update_status(...), get_sorted_queue(...).

    campusflow/storage.py: load_tickets(filepath), save_tickets(filepath, tickets).

    campusflow/reports.py: generate_report_summary(tickets).

    main.py: CLI loop handling inputs and displaying outputs.

3. Write Automated Tests Simultaneously

Write test files in tests/:

    Test boundary conditions (e.g., high urgency + 10 users vs 9 users).

    Test invalid states (e.g., zero affected_users, moving unassigned ticket to in_progress).

Run tests using:
Bash

python -m unittest discover -s tests -v

Phase 4: Peer Code Review & Merging (03:55 – 05:00)

    Push feature branches to GitHub:
    Bash

    git push -u origin feat/1-ticket-creation

    Open Pull Requests using the PR Description Template from Section 7 of the specification.

    Cross-Review Process:

        Fetch partner's branch locally to test:
        Bash

        git fetch origin
        git switch --detach origin/feat/2-workflow-storage
        python -m unittest discover -s tests -v
        git switch main

        Go to GitHub PR → Files Changed.

        Leave at least 2 substantive review observations on specific lines (e.g., checking edge case handling or exception types).

        Approve & Merge PR #1 into main.

    Update PR #2 from Main:
    Bash

    git switch main
    git pull origin main
    git switch feat/1-ticket-creation
    git merge main
    python -m unittest discover -s tests -v
    git push

        Partner approves and merges PR #2.

Phase 5: Integration & Polish (05:00 – 05:40)

    Switch to main and pull all updates:
    Bash

    git switch main
    git pull origin main

    Run full test suite on main:
    Bash

    python -m unittest discover -s tests -v

    Run main.py end-to-end to verify the CLI menu options (F1–F7).

    Verify JSON persistence manually: create tickets → exit app → restart app → verify tickets remain and next ticket gets a unique ID (T00X).

    Finalize README.md, docs/design-decisions.md, and docs/ai-learning-log.md.

Phase 6: Final Technical Defense & Demo (05:40 – 06:00)

Prepare to walk through the following 5-minute live demonstration:

    Create Tickets: Demonstrate input validation by entering 0 affected users (must reject), then enter valid inputs to create tickets.

    Priority Verification: Show calculated priorities match the specified rules.

    Assign & Progress: Assign a ticket to a staff member, progress it open → in_progress → resolved. Show that an unassigned ticket cannot move to in_progress.

    Queue & Report: Show the queue sorted by priority (critical first) and earlier ticket ID, followed by summary reports.

    Persistence & Tests: Close CLI, reopen to show saved data, run python -m unittest discover -s tests -v, and show GitHub PR review histories.

get me a full working code

Here is a complete, fully modular, standard-library-only Python implementation of CampusFlow, structured exactly as specified in the engineering guide.
Project Structure
Plaintext

campusflow/
├── README.md
├── .gitignore
├── main.py
├── campusflow/
│   ├── __init__.py
│   ├── tickets.py
│   ├── workflow.py
│   ├── storage.py
│   └── reports.py
├── tests/
│   ├── test_tickets.py
│   ├── test_workflow.py
│   └── test_storage.py
└── docs/
    ├── ai-learning-log.md
    └── design-decisions.md

File 1: .gitignore
Code snippet

.venv/
__pycache__/
*.pyc
.env
data/tickets.json

File 2: campusflow/__init__.py
Python

"""CampusFlow AI-Native Engineering Sprint Package."""

File 3: campusflow/tickets.py
Python

"""Ticket creation, input validation, and priority engine logic."""

ALLOWED_CATEGORIES = {"Network", "Hardware", "Software", "Other"}
ALLOWED_URGENCIES = {"low", "medium", "high"}

def calculate_priority(urgency: str, affected_users: int) -> str:
    """Calculate priority based on strict non-overlapping rules in order:
    RULE 1: high urgency AND >=10 affected users -> critical
    RULE 2: high urgency OR >=10 affected users -> high
    RULE 3: medium urgency OR >=3 affected users -> medium
    RULE 4: all remaining valid tickets -> low
    """
    urgency_clean = str(urgency).strip().lower()
    
    if urgency_clean == "high" and affected_users >= 10:
        return "critical"
    if urgency_clean == "high" or affected_users >= 10:
        return "high"
    if urgency_clean == "medium" or affected_users >= 3:
        return "medium"
    return "low"


def validate_ticket_inputs(title: str, category: str, urgency: str, affected_users: int):
    """Validate user inputs for ticket creation."""
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title must not be blank.")
    
    category_clean = category.strip().capitalize() if isinstance(category, str) else ""
    if category_clean not in ALLOWED_CATEGORIES:
        raise ValueError(f"Invalid category '{category}'. Must be one of {sorted(ALLOWED_CATEGORIES)}.")
    
    urgency_clean = urgency.strip().lower() if isinstance(urgency, str) else ""
    if urgency_clean not in ALLOWED_URGENCIES:
        raise ValueError(f"Invalid urgency level '{urgency}'. Must be low, medium, or high.")
    
    if not isinstance(affected_users, int) or isinstance(affected_users, bool) or affected_users <= 0:
        raise ValueError("Affected users must be a positive integer greater than zero.")
    
    return title.strip(), category_clean, urgency_clean, affected_users


def generate_next_id(existing_tickets: list) -> str:
    """Generate a unique incrementing ticket ID formatted like T001, T002, etc."""
    max_num = 0
    for t in existing_tickets:
        tid = t.get("id", "")
        if tid.startswith("T") and tid[1:].isdigit():
            max_num = max(max_num, int(tid[1:]))
    return f"T{max_num + 1:03d}"


def create_ticket(title: str, category: str, urgency: str, affected_users: int, existing_tickets: list) -> dict:
    """F1: Validate inputs, compute priority, generate unique ID, and return ticket dict."""
    valid_title, valid_cat, valid_urg, valid_users = validate_ticket_inputs(
        title, category, urgency, affected_users
    )
    
    priority = calculate_priority(valid_urg, valid_users)
    ticket_id = generate_next_id(existing_tickets)
    
    return {
        "id": ticket_id,
        "title": valid_title,
        "category": valid_cat,
        "urgency": valid_urg,
        "affected_users": valid_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None
    }

File 4: campusflow/workflow.py
Python

"""Ticket assignment, lifecycle workflow transitions, and work queue sorting."""

ALLOWED_STATUSES = {"open", "in_progress", "resolved"}
PRIORITY_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def assign_ticket(tickets: list, ticket_id: str, staff_name: str) -> dict:
    """F3: Assign a ticket to a non-empty staff member name."""
    if not isinstance(staff_name, str) or not staff_name.strip():
        raise ValueError("Staff member name cannot be empty.")
    
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["assigned_to"] = staff_name.strip()
            return ticket
            
    raise KeyError(f"Ticket ID '{ticket_id}' not found.")


def update_status(tickets: list, ticket_id: str, new_status: str) -> dict:
    """F4: Manage ticket lifecycle (open -> in_progress -> resolved) and reopening."""
    clean_status = new_status.strip().lower()
    if clean_status not in ALLOWED_STATUSES:
        raise ValueError(f"Invalid status '{new_status}'. Allowed: open, in_progress, resolved.")
        
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            current_status = ticket["status"]
            
            # Resolved tickets must be explicitly reopened first
            if current_status == "resolved" and clean_status != "open":
                raise ValueError("Resolved tickets can only be modified by reopening to 'open'.")
            
            # Cannot move to in_progress if unassigned
            if clean_status == "in_progress" and not ticket["assigned_to"]:
                raise ValueError("Cannot move an unassigned ticket into 'in_progress'. Assign staff first.")
                
            ticket["status"] = clean_status
            return ticket
            
    raise KeyError(f"Ticket ID '{ticket_id}' not found.")


def get_work_queue(tickets: list) -> list:
    """F5: Order unresolved tickets by critical -> high -> medium -> low priority,
    breaking ties using earlier numeric ticket ID.
    """
    unresolved = [t for t in tickets if t["status"] != "resolved"]
    
    def sort_key(ticket):
        p_rank = PRIORITY_RANK.get(ticket["priority"], 99)
        # Extract numeric portion of ID (e.g. T001 -> 1)
        raw_id = ticket["id"]
        num_id = int(raw_id[1:]) if raw_id.startswith("T") and raw_id[1:].isdigit() else 999999
        return (p_rank, num_id)

    return sorted(unresolved, key=sort_key)

File 5: campusflow/storage.py
Python

"""JSON storage persistence routines."""

import json
import os


def load_tickets(filepath: str) -> list:
    """F7: Load tickets from a JSON file. Return empty list if file missing.
    Raise ValueError if JSON content is corrupt.
    """
    if not os.path.exists(filepath):
        return []
        
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("JSON root element must be a list of tickets.")
            return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Corrupted storage file at {filepath}: {str(e)}")


def save_tickets(filepath: str, tickets: list) -> None:
    """F7: Write tickets array out to JSON cleanly."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tickets, f, indent=2)

File 6: campusflow/reports.py
Python

"""Reporting module for ticket analytics."""

def generate_reports(tickets: list) -> dict:
    """F6: Show total tickets and breakdowns by status and priority."""
    report = {
        "total": len(tickets),
        "status_breakdown": {"open": 0, "in_progress": 0, "resolved": 0},
        "priority_breakdown": {"critical": 0, "high": 0, "medium": 0, "low": 0}
    }
    
    for ticket in tickets:
        st = ticket.get("status")
        pr = ticket.get("priority")
        if st in report["status_breakdown"]:
            report["status_breakdown"][st] += 1
        if pr in report["priority_breakdown"]:
            report["priority_breakdown"][pr] += 1

    return report

File 7: main.py
Python

"""CLI entrypoint for CampusFlow Helpdesk System."""

import os
from campusflow.tickets import create_ticket
from campusflow.workflow import assign_ticket, update_status, get_work_queue
from campusflow.storage import load_tickets, save_tickets
from campusflow.reports import generate_reports

STORAGE_FILE = os.path.join("data", "tickets.json")


def display_ticket(t: dict):
    assigned = t['assigned_to'] if t['assigned_to'] else 'Unassigned'
    print(f"[{t['id']}] {t['title']}")
    print(f"   Category: {t['category']} | Urgency: {t['urgency']} | Affected Users: {t['affected_users']}")
    print(f"   Priority: {t['priority'].upper()} | Status: {t['status']} | Assigned: {assigned}")
    print("-" * 65)


def print_menu():
    print("\n=================== CAMPUSFLOW CLI ===================")
    print("1. Create Ticket (F1)")
    print("2. List All / View Ticket (F2)")
    print("3. Assign Ticket (F3)")
    print("4. Update Status Workflow (F4)")
    print("5. View Work Queue (F5)")
    print("6. View Reports (F6)")
    print("7. Exit & Save (F7)")
    print("======================================================")


def main():
    try:
        tickets = load_tickets(STORAGE_FILE)
        print(f"Loaded {len(tickets)} tickets from {STORAGE_FILE}.")
    except Exception as e:
        print(f"Error loading tickets: {e}")
        tickets = []

    while True:
        print_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            print("\n--- CREATE TICKET ---")
            title = input("Enter title: ")
            category = input("Enter category (Network/Hardware/Software/Other): ")
            urgency = input("Enter urgency (low/medium/high): ")
            users_in = input("Enter affected users count: ")
            
            try:
                users_cnt = int(users_in)
                ticket = create_ticket(title, category, urgency, users_cnt, tickets)
                tickets.append(ticket)
                save_tickets(STORAGE_FILE, tickets)
                print(f"\nSUCCESS: Ticket created with ID {ticket['id']} and Priority [{ticket['priority'].upper()}].")
            except ValueError as ve:
                print(f"\nERROR: {ve}")

        elif choice == "2":
            print("\n--- LIST / VIEW TICKETS ---")
            if not tickets:
                print("No tickets found.")
                continue
            
            sub = input("Type 'ALL' to list all, or enter specific Ticket ID (e.g. T001): ").strip()
            if sub.upper() == "ALL":
                for t in tickets:
                    display_ticket(t)
            else:
                found = next((t for t in tickets if t["id"].upper() == sub.upper()), None)
                if found:
                    display_ticket(found)
                else:
                    print(f"Ticket '{sub}' not found.")

        elif choice == "3":
            print("\n--- ASSIGN TICKET ---")
            tid = input("Enter Ticket ID to assign: ").strip().upper()
            staff = input("Enter Staff Name: ").strip()
            try:
                ticket = assign_ticket(tickets, tid, staff)
                save_tickets(STORAGE_FILE, tickets)
                print(f"\nSUCCESS: Ticket {tid} assigned to '{ticket['assigned_to']}'.")
            except (KeyError, ValueError) as err:
                print(f"\nERROR: {err}")

        elif choice == "4":
            print("\n--- UPDATE STATUS ---")
            tid = input("Enter Ticket ID: ").strip().upper()
            st = input("Enter new status (open / in_progress / resolved): ").strip().lower()
            try:
                ticket = update_status(tickets, tid, st)
                save_tickets(STORAGE_FILE, tickets)
                print(f"\nSUCCESS: Ticket {tid} status updated to '{ticket['status']}'.")
            except (KeyError, ValueError) as err:
                print(f"\nERROR: {err}")

        elif choice == "5":
            print("\n--- WORK QUEUE (Sorted by Priority & ID) ---")
            queue = get_work_queue(tickets)
            if not queue:
                print("No unresolved tickets in queue.")
            else:
                for t in queue:
                    display_ticket(t)

        elif choice == "6":
            print("\n--- SYSTEM REPORT ---")
            report = generate_reports(tickets)
            print(f"Total Tickets: {report['total']}")
            print("Status Breakdown:")
            for k, v in report["status_breakdown"].items():
                print(f"  - {k}: {v}")
            print("Priority Breakdown:")
            for k, v in report["priority_breakdown"].items():
                print(f"  - {k}: {v}")

        elif choice == "7":
            save_tickets(STORAGE_FILE, tickets)
            print("\nData saved. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please pick between 1 and 7.")


if __name__ == "__main__":
    main()

File 8: tests/test_tickets.py
Python

import unittest
from campusflow.tickets import calculate_priority, create_ticket, validate_ticket_inputs


class TestTicketCreation(unittest.TestCase):

    def test_priority_rules(self):
        # Rule 1: High + >=10 -> Critical
        self.assertEqual(calculate_priority("high", 12), "critical")
        
        # Rule 2: High + <10 -> High
        self.assertEqual(calculate_priority("high", 2), "high")
        
        # Rule 2: Low + >=10 -> High
        self.assertEqual(calculate_priority("low", 10), "high")
        
        # Rule 3: Low + 4 -> Medium
        self.assertEqual(calculate_priority("low", 4), "medium")
        
        # Rule 4: Low + 1 -> Low
        self.assertEqual(calculate_priority("low", 1), "low")

    def test_invalid_affected_users(self):
        with self.assertRaises(ValueError):
            validate_ticket_inputs("Wi-Fi down", "Network", "high", 0)

    def test_ticket_creation_success(self):
        existing = [{"id": "T001"}]
        ticket = create_ticket("Server outage", "Hardware", "high", 15, existing)
        self.assertEqual(ticket["id"], "T002")
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")


if __name__ == "__main__":
    unittest.main()

File 9: tests/test_workflow.py
Python

import unittest
from campusflow.workflow import assign_ticket, update_status, get_work_queue


class TestWorkflow(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {"id": "T001", "priority": "low", "status": "open", "assigned_to": None},
            {"id": "T002", "priority": "critical", "status": "open", "assigned_to": None},
            {"id": "T003", "priority": "critical", "status": "open", "assigned_to": None},
        ]

    def test_unassigned_in_progress_rejection(self):
        with self.assertRaises(ValueError):
            update_status(self.tickets, "T001", "in_progress")

    def test_valid_lifecycle(self):
        assign_ticket(self.tickets, "T001", "Alice")
        update_status(self.tickets, "T001", "in_progress")
        self.assertEqual(self.tickets[0]["status"], "in_progress")
        
        update_status(self.tickets, "T001", "resolved")
        self.assertEqual(self.tickets[0]["status"], "resolved")

    def test_work_queue_sorting(self):
        queue = get_work_queue(self.tickets)
        # Should rank Criticals first, breaking tie with earlier numeric ID (T002 before T003)
        ordered_ids = [t["id"] for t in queue]
        self.assertEqual(ordered_ids, ["T002", "T003", "T001"])


if __name__ == "__main__":
    unittest.main()

File 10: tests/test_storage.py
Python

import os
import json
import unittest
import tempfile
from campusflow.storage import load_tickets, save_tickets


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.test_dir.name, "tickets.json")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_missing_file_returns_empty(self):
        res = load_tickets(self.file_path)
        self.assertEqual(res, [])

    def test_roundtrip_save_load(self):
        data = [{"id": "T001", "title": "Test Ticket"}]
        save_tickets(self.file_path, data)
        loaded = load_tickets(self.file_path)
        self.assertEqual(data, loaded)

    def test_corrupted_json_raises_value_error(self):
        with open(self.file_path, "w") as f:
            f.write("{invalid json content")
            
        with self.assertRaises(ValueError):
            load_tickets(self.file_path)


if __name__ == "__main__":
    unittest.main()

File 11: README.md
Markdown

# CampusFlow — AI-Native Helpdesk Engineering Sprint

CampusFlow is a robust Python command-line ticket management tool designed for university technical support staff.

## Features
- **F1 Ticket Creation:** Instant validation and automatic multi-tier priority calculation.
- **F2 View Tickets:** Full ticket details and status inspectability.
- **F3 Assignment:** Route tickets to assigned support engineers.
- **F4 Status Lifecycle:** Enforces strict transition rules (`open` -> `in_progress` -> `resolved`).
- **F5 Priority Work Queue:** Deterministic sorting by criticality level and ticket ID sequence.
- **F6 System Metrics:** Summary breakdown reporting.
- **F7 Persistence:** Full state persistence to JSON with fault tolerance for corrupted data.

## Execution & Testing

### Running the Application
```bash
python main.py

Running Automated Test Suite
Bash

python -m unittest discover -s tests -v


---

### File 12: `docs/design-decisions.md`

```markdown
# Design Decisions & Contracts

## 1. Ticket Data Schema
Tickets are represented as standard Python dictionaries:
- `id` (str): Unique sequential string identifier (`T001`, `T002`, ...).
- `title` (str): Non-empty title description.
- `category` (str): `Network`, `Hardware`, `Software`, or `Other`.
- `urgency` (str): `low`, `medium`, or `high`.
- `affected_users` (int): Strict integer $> 0$.
- `priority` (str): Calculated as `critical`, `high`, `medium`, or `low`.
- `status` (str): `open`, `in_progress`, or `resolved`.
- `assigned_to` (str or None): Name of assigned engineer.

## 2. Interface Contracts
- Input functions throw standard `ValueError` or `KeyError` exceptions on violation; the CLI layer catches these exceptions to display readable messages to users without crashing.

File 13: docs/ai-learning-log.md
Markdown

# AI Learning Log

## Fellow 1: [Name]
### Interaction #1 — Custom Exceptions vs standard ValueError
- **Problem:** Unsure how to cleanly communicate validation failures without breaking execution.
- **AI Prompt:** "What are the trade-offs in Python between defining custom exception classes vs using built-in ValueError for input validation?"
- **Experiment & Verification:** Tested raising ValueError and catching it specifically inside `main.py`. Confirmed clean user message display.

## Fellow 2: [Name]
### Interaction #1 — Sorting via Tuples in Python
- **Problem:** Needed to sort by priority rank string and numeric ID simultaneously.
- **AI Prompt:** "How does key function tuple return work in sorted() for multi-criteria ordering?"
- **Experiment & Verification:** Executed a tiny experiment comparing `(priority_rank, numeric_id)` tuple pairs. Verified tie-breaker functionality in `test_workflow.py`.

Verification

Run the automated test suite directly from your terminal:
Bash

python -m unittest discover -s tests -v


Gemini is AI and can make mistakes.
