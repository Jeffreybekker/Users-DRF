<h1>CRUD API project for Artists and Albums</h1>
<h2>Description</h2>
<p>In this small project you can read, create and deletes artists and albums of your choice.</p>
<p>The point of the project was being able to use the CRUD operations with the usage of Insomnia.</p>

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
        <code>```/api/albums/<id>/```</code>
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
