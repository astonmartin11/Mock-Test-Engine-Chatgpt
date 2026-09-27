from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any


@dataclass(frozen=True)
class User:
    id: str
    auth_provider: str
    auth_subject: str
    email: str | None
    display_name: str | None
    is_active: bool
    is_admin: bool


@dataclass(frozen=True)
class Subject:
    id: str
    user_id: str
    name: str
    code: str | None
    description: str | None
    active: bool


@dataclass(frozen=True)
class Topic:
    id: str
    subject_id: str
    parent_topic_id: str | None
    name: str
    normalized_name: str
    description: str | None
    syllabus_weight: Decimal


@dataclass(frozen=True)
class TopicMastery:
    id: str
    user_id: str
    topic_id: str
    mastery_score: Decimal
    raw_ema_score: Decimal
    confidence: Decimal
    attempt_count: int
    low_score_streak: int
    recent_score: Decimal | None
    highest_score: Decimal | None
    is_grey_area: bool
    last_attempt_at: datetime | None
