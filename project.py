import os
import time

from selenium.common import TimeoutException
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Constants
ARTISTS_FILE = "artists.txt"
URL = "https://www.accuradio.com/alternative-rock/"
WAIT_TIME_SECONDS = 180


# Function to extract the song artist using Selenium
def extract_artist(driver):
    try:
        artist_element = WebDriverWait(driver, 15).until(
            ec.visibility_of_element_located((By.ID, "songartist"))
        )
        return artist_element.text.strip()
    except TimeoutException:
        print("Timeout occurred while waiting for artist element to be visible.")
        return None


# Function to check if the artist is already in the text file
def is_artist_in_file(artist):
    with open(ARTISTS_FILE, "r") as file:
        return artist in file.read().splitlines()


# Function to add artist to the text file
def add_artist_to_file(artist):
    with open(ARTISTS_FILE, "a") as file:
        file.write(artist + "\n")
        print(f"Artist {artist} added to the file.")


# Function to start a new instance of Chrome web browser
def start_chrome():
    return webdriver.Chrome()


# Function to open the webpage and agree to terms
def open_webpage(driver, url):
    driver.get(url)
    agree_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.XPATH, '//button[@mode="primary" and @size="large"]/span[text()="AGREE"]'))
    )
    agree_button.click()


# Function to click the play button
def click_play_button(driver):
    play_button = WebDriverWait(driver, 10).until(
        ec.element_to_be_clickable((By.CLASS_NAME, 'ChannelHeading__ImageContainer-sc-17o11wq-2'))
    )
    play_button.click()


def main():
    # Check if artists.txt exists, if not, create it
    if not os.path.exists(ARTISTS_FILE):
        with open(ARTISTS_FILE, "w"):
            pass  # Create an empty file

    driver = start_chrome()
    open_webpage(driver, URL)
    time.sleep(5)  # Wait for the player to load

    click_play_button(driver)

    while True:
        print("Checking for artist name...")
        artist = extract_artist(driver)
        if artist:
            if not is_artist_in_file(artist):
                add_artist_to_file(artist)
            else:
                print(f"Artist {artist} already exists in the file.")

        pbar = tqdm(total=WAIT_TIME_SECONDS, desc="Waiting")
        for _ in range(WAIT_TIME_SECONDS):
            pbar.update(1)
            time.sleep(1)
        pbar.close()


if __name__ == "__main__":
    main()
