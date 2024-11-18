# API Endpoints

### GET /search/list
### GET /search/list/`page`
Retrieve all Magic: The Gathering cards for a given page.

**Parameters:**
- `page` (int, optional): The page number to retrieve cards from. Defaults to 1.

**Response:**
- `200 OK`: A JSON response containing a list of cards, where each card is represented as a dictionary with the following keys:
  - `id` (str): The unique identifier of the card.
  - `name` (str): The name of the card.
  - `imageUrl` (str): The URL of the card's image.
  - `set` (str): The set to which the card belongs.

---
### GET /search/`name`
Search for a Magic: The Gathering card by its name.

**Parameters:**
- `name` (str): The name of the card to search for.

**Response:**
- `200 OK`: A JSON response containing the card details if found, including:
  - `id` (str): The unique identifier of the card.
  - `name` (str): The name of the card.
  - `imageUrl` (str): The URL of the card's image.
  - `set` (str): The set to which the card belongs.
- `404 Not Found`: A JSON response with an error message if the card is not found.

---
### POST /collection/
Adds a card to the collection.

**Request Body:**
- A JSON object representing the card to be added, with the following keys:
  - `id` (int): The unique identifier of the card.
  - `name` (str): The name of the card.
  - `imageUrl` (str): The URL of the card's image.
  - `set` (str): The set to which the card belongs.

**Response:**
- `201 Created`: A JSON response with a message indicating the card was added.

---
### GET /collection/
Retrieve a list of cards from the collection repository.

**Response:**
- `200 OK`: A JSON response containing a list of cards, where each card is represented as a dictionary with the following keys:
  - `id` (int): The unique identifier of the card.
  - `name` (str): The name of the card.
  - `imageUrl` (str): The URL of the card's image.
  - `set` (str): The set to which the card belongs.

---
### DELETE /collection/`id`
Deletes a card from the collection.

**Parameters:**
- `id` (int): The ID of the card to delete from the collection.

**Response:**
- `200 OK`: A JSON response with a message indicating the card was deleted.
