import pytest
from project import extract_artist, is_artist_in_file, add_artist_to_file, start_chrome, open_webpage, click_play_button

# Constants
ARTISTS_FILE = "test_artists.txt"
URL = "https://www.accuradio.com/alternative-rock/"
WAIT_TIME = 3


@pytest.fixture(scope="module")
def driver():
    # Setup
    driver = start_chrome()
    yield driver
    # Teardown
    driver.quit()


def test_extract_artist(driver):
    assert extract_artist(driver) is None


def test_is_artist_in_file():
    # Create a temporary artists.txt file with some data
    with open(ARTISTS_FILE, "w") as file:
        file.write("Artist1\nArtist2\nArtist3\n")

    assert is_artist_in_file("Artist1") == True
    assert is_artist_in_file("NonexistentArtist") == False


def test_add_artist_to_file():
    # Add an artist to the file and check if it exists
    artist = "NewArtist"
    add_artist_to_file(artist)
    with open(ARTISTS_FILE, "r") as file:
        artists = file.read()
        assert artist in artists


def test_open_webpage(driver):
    # Check if the webpage is successfully opened
    open_webpage(driver, URL)
    assert driver.current_url == URL


def test_click_play_button(driver):
    # Check if the play button is clickable
    click_play_button(driver)


if __name__ == "__main__":
    pytest.main()
