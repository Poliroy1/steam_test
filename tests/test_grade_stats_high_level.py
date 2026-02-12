import pytest

from logger.logger import Logger


class TestGradeStatsFiltersByStudent:
    def test_student_stats_count(self, university_service, grade_stats_dataset):
        student = grade_stats_dataset["students"]["a1"]
        expected = grade_stats_dataset["expected"]["by_student_a1"]

        Logger.info("### Act")
        stats = university_service.get_grade_stats(student_id=student.id)

        Logger.info("### Assert")
        assert stats.count == len(expected), (
            f"[student_id={student.id}] Expected count={len(expected)}, actual={stats.count}. "
            f"Expected grades={expected}"
        )

    def test_student_stats_min(self, university_service, grade_stats_dataset):
        student = grade_stats_dataset["students"]["a1"]
        expected = grade_stats_dataset["expected"]["by_student_a1"]

        stats = university_service.get_grade_stats(student_id=student.id)

        assert stats.min == min(expected), (
            f"[student_id={student.id}] Expected min={min(expected)}, actual={stats.min}. Expected grades={expected}"
        )

    def test_student_stats_max(self, university_service, grade_stats_dataset):
        student = grade_stats_dataset["students"]["a1"]
        expected = grade_stats_dataset["expected"]["by_student_a1"]

        stats = university_service.get_grade_stats(student_id=student.id)

        assert stats.max == max(expected), (
            f"[student_id={student.id}] Expected max={max(expected)}, actual={stats.max}. Expected grades={expected}"
        )

    def test_student_stats_avg(self, university_service, grade_stats_dataset):
        student = grade_stats_dataset["students"]["a1"]
        expected = grade_stats_dataset["expected"]["by_student_a1"]

        stats = university_service.get_grade_stats(student_id=student.id)

        expected_avg = sum(expected) / len(expected)
        assert stats.avg == pytest.approx(expected_avg), (
            f"[student_id={student.id}] Expected avg≈{expected_avg}, actual={stats.avg}. Expected grades={expected}"
        )


class TestGradeStatsFiltersByTeacher:
    def test_teacher_stats_count(self, university_service, grade_stats_dataset):
        teacher = grade_stats_dataset["teachers"]["main"]
        expected = grade_stats_dataset["expected"]["by_teacher_main"]

        stats = university_service.get_grade_stats(teacher_id=teacher.id)

        assert stats.count == len(expected), (
            f"[teacher_id={teacher.id}] Expected count={len(expected)}, actual={stats.count}. "
            f"Expected grades={expected}"
        )

    def test_teacher_stats_min(self, university_service, grade_stats_dataset):
        teacher = grade_stats_dataset["teachers"]["main"]
        expected = grade_stats_dataset["expected"]["by_teacher_main"]

        stats = university_service.get_grade_stats(teacher_id=teacher.id)

        assert stats.min == min(expected), (
            f"[teacher_id={teacher.id}] Expected min={min(expected)}, actual={stats.min}. Expected grades={expected}"
        )

    def test_teacher_stats_max(self, university_service, grade_stats_dataset):
        teacher = grade_stats_dataset["teachers"]["main"]
        expected = grade_stats_dataset["expected"]["by_teacher_main"]

        stats = university_service.get_grade_stats(teacher_id=teacher.id)

        assert stats.max == max(expected), (
            f"[teacher_id={teacher.id}] Expected max={max(expected)}, actual={stats.max}. Expected grades={expected}"
        )

    def test_teacher_stats_avg(self, university_service, grade_stats_dataset):
        teacher = grade_stats_dataset["teachers"]["main"]
        expected = grade_stats_dataset["expected"]["by_teacher_main"]

        stats = university_service.get_grade_stats(teacher_id=teacher.id)

        expected_avg = sum(expected) / len(expected)
        assert stats.avg == pytest.approx(expected_avg), (
            f"[teacher_id={teacher.id}] Expected avg≈{expected_avg}, actual={stats.avg}. Expected grades={expected}"
        )


class TestGradeStatsFiltersByGroup:
    def test_group_stats_count(self, university_service, grade_stats_dataset):
        group = grade_stats_dataset["groups"]["a"]
        expected = grade_stats_dataset["expected"]["by_group_a"]

        stats = university_service.get_grade_stats(group_id=group.id)

        assert stats.count == len(expected), (
            f"[group_id={group.id}] Expected count={len(expected)}, actual={stats.count}. Expected grades={expected}"
        )

    def test_group_stats_min(self, university_service, grade_stats_dataset):
        group = grade_stats_dataset["groups"]["a"]
        expected = grade_stats_dataset["expected"]["by_group_a"]

        stats = university_service.get_grade_stats(group_id=group.id)

        assert stats.min == min(expected), (
            f"[group_id={group.id}] Expected min={min(expected)}, actual={stats.min}. Expected grades={expected}"
        )

    def test_group_stats_max(self, university_service, grade_stats_dataset):
        group = grade_stats_dataset["groups"]["a"]
        expected = grade_stats_dataset["expected"]["by_group_a"]

        stats = university_service.get_grade_stats(group_id=group.id)

        assert stats.max == max(expected), (
            f"[group_id={group.id}] Expected max={max(expected)}, actual={stats.max}. Expected grades={expected}"
        )

    def test_group_stats_avg(self, university_service, grade_stats_dataset):
        group = grade_stats_dataset["groups"]["a"]
        expected = grade_stats_dataset["expected"]["by_group_a"]

        stats = university_service.get_grade_stats(group_id=group.id)

        expected_avg = sum(expected) / len(expected)
        assert stats.avg == pytest.approx(expected_avg), (
            f"[group_id={group.id}] Expected avg≈{expected_avg}, actual={stats.avg}. Expected grades={expected}"
        )
