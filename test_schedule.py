import pytest
import allure
from schedule import SCHEDULE, hours_in_day, is_correct_types, get_subjects


@pytest.fixture
def schedule():
    return SCHEDULE


@allure.feature("Тест часов в дне")
class TestHoursInDay:
    @allure.story("Тест часов для понедельника")
    def test_monday_hours(self, schedule):
        assert hours_in_day(schedule, "понедельник") == 3.5

    @allure.story("Тест часов для вторника")
    def test_tuesday_hours(self, schedule):
        assert hours_in_day(schedule, "вторник") == 2

    @allure.story("Тест часов для воскресенья")
    def test_sunday_hours(self, schedule):
        assert hours_in_day(schedule, "воскресенье") == 1


@allure.feature("Тест типов")
class TestIsCorrectTypes:
    @allure.story("Тест типов для понедельника")
    def test_monday_types(self, schedule):
        assert is_correct_types(schedule, "понедельник") is True

    @allure.story("Тест типов для вторника")
    def test_tuesday_types(self, schedule):
        assert is_correct_types(schedule, "вторник") is True

    @allure.story("Тест типов для среды")
    def test_wednesday_types(self, schedule):
        assert is_correct_types(schedule, "среда") is True

    @allure.story("Тест типов для четверга")
    def test_thursday_types(self, schedule):
        assert is_correct_types(schedule, "четверг") is True

    @allure.story("Тест типов для пятницы")
    def test_friday_types(self, schedule):
        assert is_correct_types(schedule, "пятница") is False

    @allure.story("Тест типов для субботы")
    @pytest.mark.skip(reason="Суббота не описана правилами спецификации")
    def test_saturday_types(self, schedule):
        assert is_correct_types(schedule, "суббота") is True

    @allure.story("Тест типов для воскресенья")
    @pytest.mark.skip(
        reason="Реализация разрешает 'лекция' в воскресенье, хотя спецификация разрешает только 'мероприятие'"
    )
    def test_sunday_types(self, schedule):
        assert is_correct_types(schedule, "воскресенье") is True

@allure.feature("Тест получения предметов")
class TestGetSubjects:
    @allure.story("Тест получения предметов для понедельника")
    def test_monday_subjects(self, schedule):
        assert get_subjects(schedule, "понедельник") == [
            "Математика",
            "Программирование",
            "История",
        ]

    @allure.story("Тест получения предметов для вторника")
    def test_tuesday_subjects(self, schedule):
        assert get_subjects(schedule, "вторник") == [
            "Физика",
        ]

    @allure.story("Тест получения предметов для пятницы")
    def test_friday_subjects(self, schedule):
        assert get_subjects(schedule, "пятница") == [
            "Программирование",
            "Математика",
        ]
