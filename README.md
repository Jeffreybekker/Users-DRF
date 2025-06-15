<h1>CRUD API project for Artists and Albums</h1>
<h2>Description</h2>
<p>In this small project you can read, create and deletes artists and albums of your choice.</p>
<p>The point of the project was being able to use the CRUD operations with the usage of Insomnia.</p>

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Jeffreybekker/Users-DRF.git
    cd Users-DRF
    ```

2. Create a virtual environment and install dependencies:
    If you do not have pipenv installed, install it first:
    ```bash
    pip install pipenv
    ```
    Then install dependencies using the `Pipfile` and `Pipfile.lock`:
    ```bash
    pipenv install
    ```
    This will also create and set up the virtual environment.

3. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

4. Create a `.env` file in the root of the project with the following content:
    ```env
    SECRET_KEY='your_secret_key'
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    ```

5. Generate a Django `SECRET_KEY` (optional):
    Start the Python shell:
    ```bash
    python
    ```
    And paste the following:
    ```python
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
    ```
    Copy the generated key and use it at `SECRET_KEY` in your `.env`-file.

6. Run the development server:
    ```bash
    python manage.py runserver
    ```
    Visit: [http://127.0.0.1:8000/artists](http://127.0.0.1:8000/artists)

7. Create superuser to be able to login in the Admin panel:
    ```
    python manage.py createsuperuser
    ```
    Simply follow the steps in the terminal. This login you'll use to access the Admin panel.

<h2>API Endpoints</h2>
<table>
  <thead>
    <tr>
      <th>Endpoint</th>
      <th>HTTP Method</th>
      <th>CRUD Method</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <code>/api/artists/</code>
      </td>
      <td>GET</td>
      <td>READ</td>
      <td>Get all artists</td>
    </tr>
    <tr>
      <td>
        <code>/api/artists/</code>
      </td>
      <td>POST</td>
      <td>CREATE</td>
      <td>Create new artist</td>
    </tr>
    <tr>
      <td>
        <code>/api/artists/:id>/</code>
      </td>
      <td>GET</td>
      <td>READ</td>
      <td>Get an artist</td>
    </tr>
    <tr>
      <td>
        <code>/api/artists/:id>/</code>
      </td>
      <td>PUT</td>
      <td>UPDATE</td>
      <td>Updates an artist</td>
    </tr>
    <tr>
      <td>
        <code>/api/artists/:id>/</code>
      </td>
      <td>DELETE</td>
      <td>DELETE</td>
      <td>Deletes an artist</td>
    </tr>
    <tr>
      <td>
        <code>/api/albums/</code>
      </td>
      <td>GET</td>
      <td>READ</td>
      <td>Get all albums</td>
    </tr>
    <tr>
      <td>
        <code>/api/albums/</code>
      </td>
      <td>POST</td>
      <td>CREATE</td>
      <td>Creates an album</td>
    </tr>
    <tr>
      <td>
        <code>/api/albums/:id>/</code>
      </td>
      <td>GET</td>
      <td>READ</td>
      <td>Get album from artist</td>
    </tr>
    <tr>
      <td>
        <code>/api/albums/:id>/</code>
      </td>
      <td>PUT</td>
      <td>UPDATE</td>
      <td>Updates album from artist</td>
    </tr>
    <tr>
      <td>
        <code>/api/albums/:id>/</code>
      </td>
      <td>DELETE</td>
      <td>DELETE</td>
      <td>Deletes album from artist</td>
    </tr>
  </tbody>
</table>
