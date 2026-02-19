from dataclasses import dataclass, field
from enum import Enum 
from typing import List, Dict, Any

from pytest import Class


class Severity(Enum):
    """Severity levels for audit findings. Higher values mean mre serious issues that can hinder the reprducibility of the experiement."""
    INFO = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __gt__(sef, other):
        return self.value > other.value

    def __str__(self):
        return self.name
    
@dataclass
class Finding:
    """A single integrity issue discovered during the audit."""
    check_name = str
    severity: Severity
    message: str
    recommendation: str
    affected_rows: List[int] = field(default_factory=list)
    affected_columns: List[str] = field(default_factory=list)
    detail: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Converts the findings into a plan dictionary for a JSON output."""
        return {
            "check_name": self.check_name,
            "severity": self.severity.name,
            "message": self.message,
            "recommendation": self.recommendation,
            "affected_rows": self.affected_rows,
            "affected_columns": self.affected_columns,
            "detail": self.detail
        }
    
@dataclass
class RiskScore: 
    """The aggregated risk score for one audit run."""
    raw_score: int
    normalised_score: float
    risk_band: str # 'Low', 'Medium' or 'High'
    finding_counts: Dict[str, int] = field(defailt_factory = dict)
    sensetivity: str = 'standard'
    
@dataclass
class AuditResult:
    """The result of an audit run, including all findings and the overall risk score."""
    dataset_path: str
    timestamp: str
    ingestion_log: List[str] 
    dataset_summary: Dict[str, Any] 
    findings: List[Finding]
    risk_score: RiskScore

