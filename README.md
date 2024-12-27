<h1>CRUD API project for Artists and Albums</h1>
<h2>Description</h2>
<p>This is a small project to refresh the basics of APIs.</p>
<p>The key point of the project was being able to use the CRUD operations using Insomnia.</p>

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
        <code>/api/users/</code>
      </td>
      <td>GET</td>
      <td>READ</td>
      <td>Get all users</td>
    </tr>
    <tr>
      <td>
        <code>/api/users/</code>
      </td>
      <td>POST</td>
      <td>CREATE</td>
      <td>Create new user</td>
    </tr>
    <tr>
      <td>
        <code>/api/users/<id>/</code>
      </td>
      <td>GET</td>
      <td>READ</td>
      <td>Get a specific user</td>
    </tr>
    <tr>
      <td>
        <code>/api/users/<id>/</code>
      </td>
      <td>PUT</td>
      <td>UPDATE</td>
      <td>Updates a specific user</td>
    </tr>
    <tr>
      <td>
        <code>/api/users/<int:id>/</code>
      </td>
      <td>DELETE</td>
      <td>DELETE</td>
      <td>Deletes a specific user</td>
    </tr>
  </tbody>
</table>
