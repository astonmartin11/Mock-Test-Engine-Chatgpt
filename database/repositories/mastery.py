from __future__ import annotations

from typing import Any

from database.connection import execute_returning, fetch_all, fetch_one


class MasteryRepository:

    def get(
        self,
        user_id: str,
        topic_id: str,
    ) -> dict[str, Any] | None:
        return fetch_one(
            '''
            SELECT *
            FROM topic_mastery
            WHERE user_id = %s
              AND topic_id = %s
            LIMIT 1;
            ''',
            (user_id, topic_id),
        )

    def list_for_user_subject(
        self,
        user_id: str,
        subject_id: str,
    ) -> list[dict[str, Any]]:
        return fetch_all(
            '''
            SELECT
                tm.*,
                t.name AS topic_name,
                t.subject_id
            FROM topic_mastery tm
            JOIN topics t ON t.id = tm.topic_id
            WHERE tm.user_id = %s
              AND t.subject_id = %s
            ORDER BY tm.mastery_score ASC, t.name ASC;
            ''',
            (user_id, subject_id),
        )

    def top_grey_areas(
        self,
        user_id: str,
        subject_id: str,
        limit: int = 5,
    ) -> list[dict[str, Any]]:
        if limit < 1:
            return []

        return fetch_all(
            '''
            SELECT
                tm.*,
                t.name AS topic_name,
                t.subject_id
            FROM topic_mastery tm
            JOIN topics t ON t.id = tm.topic_id
            WHERE tm.user_id = %s
              AND t.subject_id = %s
              AND tm.is_grey_area = TRUE
            ORDER BY
                tm.mastery_score ASC,
                tm.confidence ASC,
                tm.low_score_streak DESC
            LIMIT %s;
            ''',
            (user_id, subject_id, limit),
        )

    def upsert_initial(
        self,
        user_id: str,
        topic_id: str,
    ) -> dict[str, Any]:
        return execute_returning(
            '''
            INSERT INTO topic_mastery (
                user_id,
                topic_id
            )
            VALUES (%s, %s)
            ON CONFLICT (user_id, topic_id)
            DO UPDATE SET
                updated_at = NOW()
            RETURNING *;
            ''',
            (user_id, topic_id),
        )
