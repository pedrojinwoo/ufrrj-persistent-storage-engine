# Persistent Key-Value Storage Engine (Phase 1)

[![University](https://img.shields.io/badge/University-Computer%20Science-blue)](https://portal.ufrrj.br/)
[![License](https://img.shields.io/badge/license-MIT-green)](#)
[![Status](https://img.shields.io/badge/status-active-success)]()

## 🎓 Academic Context & Overview
This repository contains the first implementation milestone for the **Data Structures II / Storage Systems** course project. The primary goal is to design and implement a persistent **Key-Value Storage Engine** from scratch—capable of storing, retrieving, deleting, and safely recovering data on secondary memory (disk) after unexpected system interruptions (crashes), without relying on external DBMS solutions like SQLite or RocksDB.

This initial phase focuses on core persistence foundations, deterministic crash recovery via log replay, and strict adherence to the automated evaluation protocol (`ED2Bench`).

---

## 🛠️ Tech Stack & Architecture Choices
* **Core Language:** [Indique sua linguagem, ex: Python 3.x / C / Go / Rust]
* **Storage Model:** **Append-Only Log (WAL-inspired)** combined with an in-memory Hash Index (`key -> byte offset`).
* **Interface:** Command-Line Interface (CLI) processing JSON Lines (`.jsonl`) communication workloads.

### Architectural Rationale
1. **Append-Only Log:** Provides $O(1)$ sequential write performance, maximizing write throughput and drastically simplifying data serialization on disk.
2. **In-Memory Indexing:** Maps keys directly to their physical byte offsets in the log file, ensuring fast $O(1)$ lookups for point queries (`GET`).
3. **Deterministic Crash Recovery:** During initialization (`init`), the engine performs a linear scan (replay) of the log file to reconstruct the valid state in memory, correctly handling update overwrites and deletion markers (`tombstones`).

---

## 🚀 Interface & Command Protocol

The engine operates via standardized CLI commands interacting with a target data directory:

```bash
# Initialize data directory
/engine init --data-dir /data

# Run a workload sequence (JSONL format)
/engine run --data-dir /data --input /input/workload.jsonl --output /output/results.jsonl

# Verify structural data integrity
/engine verify --data-dir /data

# Describe engine metadata
/engine describe
```

### Supported Workload Operations (JSONL)

* PUT: {"id": 1, "op": "put", "key": 91, "value": "abc"}
* GET: {"id": 2, "op": "get", "key": 91}
* DELETE: {"id": 3, "op": "delete", "key": 91}

## 🔬 Experimental Analysis & Robustness
To validate correctness under pressure, the engine was tested against multiple verification vectors:

* Durability Test: Verified data availability after abrupt process termination and reloading.
* Tombstone Handling: Ensured deleted keys correctly evaluate to not_found status without leaking disk blocks.
* Log Replay Performance: Measured initialization overhead relative to log file size.

## 🤖 AI-Assisted Engineering
In accordance with course guidelines, generative AI tools were utilized collaboratively for architectural brainstorming, edge-case debugging, and test structure planning. All underlying implementation decisions, correctness proofs, and code structures were thoroughly reviewed, tested, and defended by the development team.