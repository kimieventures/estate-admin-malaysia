"""Audit Trail — rekod append-only rantaian-hash (tamper-evident).

Reka bentuk: rangka-pembangunan-sistem.md §6 — setiap rekod memuat hash
rekod terdahulu; pengubahan silam dikesan oleh verify().
"""
import hashlib
import json
from datetime import datetime, timezone

_FIELDS = ("ts", "actor", "role", "action", "stage", "legal_basis", "payload")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _canonical(body: dict) -> str:
    """Serialisasi deterministik — kunci sama menghasilkan hash sama (rekomputasi bebas)."""
    return json.dumps(body, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


class AuditTrail:
    """Rantaian rekod pintu/tindakan — append-only, tiada API padam/ubah."""

    def __init__(self) -> None:
        self.records: list[dict] = []

    def append(self, actor: str, role: str, action: str, stage: str | None = None,
               legal_basis: str | None = None, payload: dict | None = None) -> str:
        """Tambah rekod; pulangkan hash rekod."""
        prev = self.records[-1]["hash"] if self.records else "GENESIS"
        body = {
            "ts": _now(),
            "actor": actor,
            "role": role,
            "action": action,
            "stage": stage,
            "legal_basis": legal_basis,
            "payload": payload or {},
        }
        rec_hash = hashlib.sha256((prev + _canonical(body)).encode("utf-8")).hexdigest()
        self.records.append({**body, "prev_hash": prev, "hash": rec_hash})
        return rec_hash

    def verify(self) -> tuple[bool, dict | None]:
        """Semak rantaian; pulangkan (ok, rekod_rosak). Pengubahan silam => False."""
        prev = "GENESIS"
        for rec in self.records:
            body = {k: rec.get(k) for k in _FIELDS}
            if rec["prev_hash"] != prev:
                return False, rec
            expected = hashlib.sha256((prev + _canonical(body)).encode("utf-8")).hexdigest()
            if rec["hash"] != expected:
                return False, rec
            prev = rec["hash"]
        return True, None

    def chain(self) -> list[str]:
        """Paparan ringkas rantaian hash (12 aksara pertama)."""
        return [r["hash"][:12] for r in self.records]

    def export_lines(self) -> list[str]:
        """Eksport rekod (untuk audit pack)."""
        return [
            f"{i:>3} {r['ts']} {r['role']:<15} {r['action']:<18} {r['stage'] or '-'} :: {r['hash'][:12]}"
            for i, r in enumerate(self.records)
        ]
