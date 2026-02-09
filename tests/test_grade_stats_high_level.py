import pytest
from logger.logger import Logger


class TestGradeStatsFilters:
    def test_stats_filter_by_student(self, university_service, grade_stats_dataset):
        student = grade_stats_dataset["students"]["a1"]
        expected = grade_stats_dataset["expected"]["by_student_a1"]

        Logger.info("### Act: get stats by student_id")
        stats = university_service.get_grade_stats(student_id=student.id)

        Logger.info("### Assert")
        assert stats.count == len(expected), (
            f"[student_id={student.id}] Expected count={len(expected)}, actual={stats.count}. "
            f"Expected grades={expected}"
        )
        assert stats.min == min(expected), (
            f"[student_id={student.id}] Expected min={min(expected)}, actual={stats.min}. "
            f"Expected grades={expected}"
        )
        assert stats.max == max(expected), (
            f"[student_id={student.id}] Expected max={max(expected)}, actual={stats.max}. "
            f"Expected grades={expected}"
        )
        expected_avg = sum(expected) / len(expected)
        assert stats.avg == pytest.approx(expected_avg), (
            f"[student_id={student.id}] Expected avg≈{expected_avg}, actual={stats.avg}. "
            f"Expected grades={expected}"
        )

    def test_stats_filter_by_teacher(self, university_service, grade_stats_dataset):
        teacher = grade_stats_dataset["teachers"]["main"]
        expected = grade_stats_dataset["expected"]["by_teacher_main"]

        Logger.info("### Act: get stats by teacher_id")
        stats = university_service.get_grade_stats(teacher_id=teacher.id)

        Logger.info("### Assert")
        assert stats.count == len(expected), (
            f"[teacher_id={teacher.id}] Expected count={len(expected)}, actual={stats.count}. "
            f"Expected grades={expected}"
        )
        assert stats.min == min(expected), (
            f"[teacher_id={teacher.id}] Expected min={min(expected)}, actual={stats.min}. "
            f"Expected grades={expected}"
        )
        assert stats.max == max(expected), (
            f"[teacher_id={teacher.id}] Expected max={max(expected)}, actual={stats.max}. "
            f"Expected grades={expected}"
        )
        expected_avg = sum(expected) / len(expected)
        assert stats.avg == pytest.approx(expected_avg), (
            f"[teacher_id={teacher.id}] Expected avg≈{expected_avg}, actual={stats.avg}. "
            f"Expected grades={expected}"
        )

    def test_stats_filter_by_group(self, university_service, grade_stats_dataset):
        group = grade_stats_dataset["groups"]["a"]
        expected = grade_stats_dataset["expected"]["by_group_a"]

        Logger.info("### Act: get stats by group_id")
        stats = university_service.get_grade_stats(group_id=group.id)

        Logger.info("### Assert")
        assert stats.count == len(expected), (
            f"[group_id={group.id}] Expected count={len(expected)}, actual={stats.count}. "
            f"Expected grades={expected}"
        )
        assert stats.min == min(expected), (
            f"[group_id={group.id}] Expected min={min(expected)}, actual={stats.min}. "
            f"Expected grades={expected}"
        )
        assert stats.max == max(expected), (
            f"[group_id={group.id}] Expected max={max(expected)}, actual={stats.max}. "
            f"Expected grades={expected}"
        )
        expected_avg = sum(expected) / len(expected)
        assert stats.avg == pytest.approx(expected_avg), (
            f"[group_id={group.id}] Expected avg≈{expected_avg}, actual={stats.avg}. "
            f"Expected grades={expected}"
        )