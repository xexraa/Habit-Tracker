# Habit Tracker

![habits tracker](https://user-images.githubusercontent.com/121942715/219853323-160a53b7-19f2-4820-b6f5-3afabcdb9a98.png)

## Web project.

The main premise of this application is to track your habits

## What does this project have?

1. It has a built-in current day control, today's day is highlighted
2. You can easily add a new entry via the button at the top or bottom of the page
3. Each entry is set as unexecuted by default
4. After marking the entry, it will be considered as done.
5. Entries added on the current day will be automatically added to future days, but not to past ones
6. After pressing the red button, we get the opportunity to select which habits we want to remove from the database

## What else is in it?

- On smaller screens the picture will adapt
- The bottom buttons blink when you hover over them
- After hovering over the top links, the color changes with a delay of 0.5s
- Non-today dates have a distinct color different from the main one when hovered over

## What sources did I use?

**Python:**

- flask
- python-dotenv
- pymongo[srv]
- gunicorn (needed mainly to place a page on render.com)

**Programs:**

- MongoDBCompass
- GIT
- VSC

**Pages that were helpful:**

- render.com
- cloud.mongodb.com
- midjourney.com