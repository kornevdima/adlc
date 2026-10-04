#!/usr/bin/env python3
"""Add 60 generated concept pages to a vault (wiki-query large-vault case).

Four domains of 15 pages; each page links two neighbours in its domain and one
page in the next domain, so cross-domain questions have a real answer path.
The needle: 'Payments Ledger' (payments) and 'Shipment Tracking' (logistics)
both cite the 'Idempotency Key' page in the platform domain.
"""
import sys
from pathlib import Path

DOMAINS = {
    "payments": ["Payments Ledger", "Refund Flow", "Chargeback Handling", "Payment Gateway Adapter", "Currency Rounding",
                 "Fraud Score", "Settlement Batch", "Payout Schedule", "Card Tokenization", "3-D Secure Step",
                 "Invoice Numbering", "Tax Calculation", "Payment Retry Policy", "Wallet Balance", "Ledger Reconciliation"],
    "logistics": ["Shipment Tracking", "Carrier Selection", "Label Printing", "Warehouse Slotting", "Pick Path",
                  "Delivery Window", "Returns Intake", "Customs Declaration", "Parcel Weighing", "Route Planning",
                  "Last Mile Handoff", "Proof of Delivery", "Stock Reservation", "Backorder Rules", "Cross Docking"],
    "platform": ["Idempotency Key", "Rate Limiter", "Feature Flags", "Audit Log", "Secrets Rotation",
                 "Service Mesh", "Health Checks", "Blue Green Deploy", "Schema Migration", "Request Tracing",
                 "Dead Letter Queue", "Retry Budget", "Circuit Breaker", "Config Service", "Tenant Isolation"],
    "identity": ["Session Tokens", "Role Mapping", "Single Sign-On", "Password Policy", "MFA Enrolment",
                 "Account Recovery", "Consent Records", "API Keys", "Service Accounts", "Login Throttling",
                 "Device Trust", "Permission Audit", "User Merge", "Profile Export", "Account Deletion"],
}
NEEDLE = {"Payments Ledger": "Idempotency Key", "Shipment Tracking": "Idempotency Key"}

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "wiki" / "concepts"
root.mkdir(parents=True, exist_ok=True)
names = list(DOMAINS)
lines = []
for d_i, (domain, pages) in enumerate(DOMAINS.items()):
    nxt = DOMAINS[names[(d_i + 1) % len(names)]]
    for i, title in enumerate(pages):
        links = [pages[(i + 1) % 15], pages[(i + 2) % 15], nxt[i]]
        if title in NEEDLE:
            links.append(NEEDLE[title])
        rel = "".join(f'\n  - "[[{l}]]"' for l in links)
        body = (f"{title} is part of the {domain} domain of the order platform.\n\n"
                + (f"It relies on [[{NEEDLE[title]}]] so that a retried request never double-applies.\n\n" if title in NEEDLE else "")
                + "See also: " + ", ".join(f"[[{l}]]" for l in links[:3]) + ".\n")
        (root / f"{title}.md").write_text(
            f'---\ntype: concept\ntitle: "{title}"\ncreated: 2026-08-01\nupdated: 2026-08-01\ntags:\n  - concept\n  - {domain}\n'
            f'status: developing\nrelated:{rel}\n---\n\n# {title}\n\n{body}')
        lines.append(f"- [[{title}]] ({domain})")
idx = Path(sys.argv[1] if len(sys.argv) > 1 else ".") / "wiki" / "index.md"
idx.write_text(idx.read_text() + "\n## Platform concepts (generated)\n\n" + "\n".join(lines) + "\n")
