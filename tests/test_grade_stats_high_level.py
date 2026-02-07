import pytest
from logger.logger import Logger


class TestGradeStatsFilters:
    def test_stats_filter_by_student(
        self,
        university_service,
        group_factory,
        student_factory,
        teacher_factory,
        grade_factory,
    ):
        Logger.info("### Arrange: group, students, teacher, grades")
        g1 = group_factory()

        s1 = student_factory(g1.id)
        s2 = student_factory(g1.id)

        t1 = teacher_factory()

        g_a = grade_factory(t1.id, s1.id).grade
        g_b = grade_factory(t1.id, s1.id).grade
        _noise = grade_factory(t1.id, s2.id).grade

        expected_grades = [g_a, g_b]
        expected_count = len(expected_grades)
        expected_min = min(expected_grades)
        expected_max = max(expected_grades)
        expected_avg = sum(expected_grades) / expected_count

        Logger.info("### Act: get stats by student_id")
        stats = university_service.get_grade_stats(student_id=s1.id)

        Logger.info("### Assert")
        assert stats.count == expected_count, (
            f"[student_id={s1.id}] Expected count={expected_count}, actual={stats.count}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.min == expected_min, (
            f"[student_id={s1.id}] Expected min={expected_min}, actual={stats.min}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.max == expected_max, (
            f"[student_id={s1.id}] Expected max={expected_max}, actual={stats.max}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.avg == pytest.approx(expected_avg), (
            f"[student_id={s1.id}] Expected avg≈{expected_avg}, actual={stats.avg}. "
            f"Expected grades={expected_grades}"
        )

    def test_stats_filter_by_teacher(
        self,
        university_service,
        group_factory,
        student_factory,
        teacher_factory,
        grade_factory,
    ):
        Logger.info("### Arrange: group, students, teachers, grades")
        g1 = group_factory()

        s1 = student_factory(g1.id)
        s2 = student_factory(g1.id)

        t1 = teacher_factory()
        t2 = teacher_factory()  # noise teacher

        g1v = grade_factory(t1.id, s1.id).grade
        g2v = grade_factory(t1.id, s2.id).grade
        g3v = grade_factory(t1.id, s2.id).grade
        _noise = grade_factory(t2.id, s1.id).grade

        expected_grades = [g1v, g2v, g3v]
        expected_count = len(expected_grades)
        expected_min = min(expected_grades)
        expected_max = max(expected_grades)
        expected_avg = sum(expected_grades) / expected_count

        Logger.info("### Act: get stats by teacher_id")
        stats = university_service.get_grade_stats(teacher_id=t1.id)

        Logger.info("### Assert")
        assert stats.count == expected_count, (
            f"[teacher_id={t1.id}] Expected count={expected_count}, actual={stats.count}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.min == expected_min, (
            f"[teacher_id={t1.id}] Expected min={expected_min}, actual={stats.min}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.max == expected_max, (
            f"[teacher_id={t1.id}] Expected max={expected_max}, actual={stats.max}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.avg == pytest.approx(expected_avg), (
            f"[teacher_id={t1.id}] Expected avg≈{expected_avg}, actual={stats.avg}. "
            f"Expected grades={expected_grades}"
        )

    def test_stats_filter_by_group(
        self,
        university_service,
        group_factory,
        student_factory,
        teacher_factory,
        grade_factory,
    ):
        Logger.info("### Arrange: 2 groups, students, teacher, grades")
        g1 = group_factory()
        g2 = group_factory()

        s11 = student_factory(g1.id)
        s12 = student_factory(g1.id)
        s21 = student_factory(g2.id)

        t1 = teacher_factory()

        g1v = grade_factory(t1.id, s11.id).grade
        g2v = grade_factory(t1.id, s12.id).grade
        g3v = grade_factory(t1.id, s12.id).grade
        _noise = grade_factory(t1.id, s21.id).grade

        expected_grades = [g1v, g2v, g3v]
        expected_count = len(expected_grades)
        expected_min = min(expected_grades)
        expected_max = max(expected_grades)
        expected_avg = sum(expected_grades) / expected_count

        Logger.info("### Act: get stats by group_id")
        stats = university_service.get_grade_stats(group_id=g1.id)

        Logger.info("### Assert")
        assert stats.count == expected_count, (
            f"[group_id={g1.id}] Expected count={expected_count}, actual={stats.count}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.min == expected_min, (
            f"[group_id={g1.id}] Expected min={expected_min}, actual={stats.min}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.max == expected_max, (
            f"[group_id={g1.id}] Expected max={expected_max}, actual={stats.max}. "
            f"Expected grades={expected_grades}"
        )
        assert stats.avg == pytest.approx(expected_avg), (
            f"[group_id={g1.id}] Expected avg≈{expected_avg}, actual={stats.avg}. "
            f"Expected grades={expected_grades}"
        )
