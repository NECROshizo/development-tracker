import pytest
from course.models import Theme


def test_testings():
	assert 1 == 1


@pytest.mark.django_db
def test_create_theme_with_valid_data():
	theme = Theme.objects.create(title="Theme 1", price=10.00)

	assert theme.title == "Theme 1"
	assert theme.price == 10.00
