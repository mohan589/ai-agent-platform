# Enterprise AI Agent Platform (MCP-based)

## Overview

This project is a **production-grade AI Agent Platform** designed for enterprise workflows. It demonstrates how to safely deploy autonomous AI agents with tools, guardrails, auditability, and human-in-the-loop controls.

Unlike demo chatbots, this system focuses on **reliability, security, and governance** — the hard problems companies actually care about.

---

## What This Project Shows

* How to design **AI-native backend systems**, not just prompts
* Multi-agent orchestration using MCP-style tools
* Secure OAuth-based access control for AI actions
* Deterministic outputs with schema validation
* Full audit trail of AI decisions
* Clear separation between reasoning, tools, and execution

This mirrors how modern enterprises are adopting AI internally.

---

## High-Level Architecture

```
Client / CI / Internal Tools
        ↓
FastAPI Gateway (Auth, RBAC)
        ↓
Agent Orchestrator Service
  ├─ Policy Engine
  ├─ Prompt Registry (versioned)
  ├─ Tool Router
  ├─ Eval & Validation Layer
        ↓
MCP Agents
  ├─ API Test Generation Agent
  ├─ Security Review Agent
  ├─ Compliance & Audit Agent
        ↓
Artifacts (Tests, Reports, Logs)
```

---

## Core Components

### 1. FastAPI Gateway

**Responsibilities:**

* OAuth / JWT authentication
* Role-based access control (RBAC)
* Request validation
* Rate limiting

This ensures agents never act outside authorized boundaries.

---

### 2. Agent Orchestrator

The brain of the system.

**Responsibilities:**

* Selecting which agent(s) to run
* Managing tool permissions per agent
* Enforcing policies (what agents can/cannot do)
* Retrying or escalating on failure

Key idea: **Agents are powerful, but never autonomous without limits**.

---

### 3. Prompt Registry

* All prompts are versioned
* Each execution records prompt hash + version
* Enables reproducibility and audits

This is critical for enterprise trust and debugging.

---

### 4. Tool Router

Agents do not call services directly.

Instead:

* Agents request a tool
* Tool Router validates permission
* Executes tool with strict schemas

Prevents prompt injection and tool misuse.

---

### 5. Evaluation & Validation Layer

Before outputs are accepted:

* JSON schema validation
* Rule-based checks
* Optional human approval

No raw LLM output reaches production blindly.

---

## Agents Included

### API Test Generation Agent

**Input:**

* Swagger / OpenAPI spec
* MongoDB schema

**Output:**

* Mocha + Chai test cases
* Positive & negative scenarios
* Faker-based mock data

**Why it matters:** Replaces repetitive QA work while improving coverage.

---

### Security Review Agent

**Input:**

* API specs
* Auth configuration
* Dependency metadata

**Output:**

* Auth flaws
* Missing validations
* Security risks
* CVE references

**Why it matters:** AI-assisted AppSec is becoming mandatory.

---

### Compliance & Audit Agent

**Input:**

* Agent decisions
* Tool calls
* Logs

**Output:**

* Human-readable audit report
* Decision rationale
* Prompt & tool trace

**Why it matters:** Regulators and enterprises demand explainability.

---

## Repo Structure

```
ai-agent-platform/
├─ api/
│  ├─ main.py
│  ├─ auth/
│  ├─ routes/
│  └─ middleware/
├─ orchestrator/
│  ├─ agent_manager.py
│  ├─ policy_engine.py
│  ├─ tool_router.py
│  └─ eval_engine.py
├─ agents/
│  ├─ test_generator/
│  ├─ security_reviewer/
│  └─ compliance_agent/
├─ tools/
│  ├─ swagger_parser.py
│  ├─ mongo_reader.py
│  └─ repo_writer.py
├─ prompts/
│  ├─ v1/
│  └─ v2/
├─ storage/
│  ├─ audit_logs/
│  └─ outputs/
└─ README.md
```

---

## Key Engineering Principles Demonstrated

* **AI is probabilistic → systems must be deterministic**
* **Tools > raw text generation**
* **Every AI action must be auditable**
* **Human override is a feature, not a failure**

---

## Why This Matters for Hiring Managers

This project demonstrates:

* Senior-level system design
* Production AI safety thinking
* Security-first architecture
* Enterprise readiness

It answers the question:

> "Can this engineer be trusted to deploy AI in a real company?"

---

## Who This Is For

* AI Platform Engineers
* Backend Engineers moving into AI
* Security Engineers working with LLMs
* Companies building internal AI tooling

---

## Next Extensions

* CI/CD integration
* Cost & latency monitoring
* Multi-model routing
* Agent performance benchmarking

---

## Final Note

AI will not replace engineers who **design, control, and govern AI systems**.

This project is about owning the system — not just calling a model.
