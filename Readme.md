# Demo server:

This is a `Readme` file, every repository will have one, it explains details about the repository, about the technologies used in it, as well as details about the service and the API it has to communicate with the outside world.

## To run the server:

- Make sure you have Python 3 installed
- Create a Python virtual environment by running:

```shell
python -m venv env
```

- Activate the virtual environment:

```shell
source env/bin/activate
```

- Install the libraries needed:

```shell
pip install -r requirements.txt
```

- Run the server locally:

```shell
sh run.sh
```

## See the API:

To view the requests the server allows, go to ` http://127.0.0.1:8000/docs` **after you run the server**.
There you will see all of the available requests and you can try them out.

## Quick explanation:

- The server has the following endpoints:
  - `GET`: `/` --> which returns the message _"Hello World"_
  - `GET`: `/users` --> This returns a map with our fake users
  - `GET`: `/user/{id}` --> This returns a specific users from our map based on the `id`:
    To use it you need to send an `id` in the GET request: `users/1`
    If the `id` exists you will get their details:
    ```json
    {
      "name": "John Doe",
      "age": 25
    }
    ```
    If it does not exist, you will get the following:
    ```json
    { "message": "Not found", "code": 404 }
    ```
  - `POST`: `/users/{id}` --> This request adds a user to our map:
    To use it, you need to send an `id` in the URL like: `users/4`
    Then also send a request body in the following structure:
    ```json
    {
      "name": "Jane Doe",
      "age": 25
    }
    ```
  - `DELETE`: `/users/{id}` --> This deletes a user with a specific `id`:
    To use it you need to send an `id` for the user you want to delete, as well as the `password`:
    The url would be: `/users/1` and the body of the request would be:
    ```json
    { "password": "123" }
    ```
- The password is `1234` you can see it in the code.
- Our map initially when running the service starts with the following values:

```json
{
  "1": { "name": "John Doe", "age": 25 },
  "2": { "name": "Elizabeth Windsor", "age": 90 }
}
```
