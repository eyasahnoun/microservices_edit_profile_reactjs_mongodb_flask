import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AdminInterface.css'; // Importez votre fichier de styles


const AdminDashboard = () => {
  const [users, setUsers] = useState([]);
  const [editingUserId, setEditingUserId] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    phone: '',
    email: '',
    address: ''
  });

  


  useEffect(() => {
    const token = sessionStorage.getItem('token');
    
    if (token) {
      fetchUsers();
      console.log(token);
    }
  }, []);

  const fetchUsers = async () => {
    try {
      const token = sessionStorage.getItem('token');
      
      if (token) {
        const config = {
          headers: {
            Authorization: `Bearer ${token}`
          }
        };
        
        const response = await axios.get('http://localhost:5001/users', config);
        setUsers(response.data);
      } else {
        console.error('Token missing');
      }
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  const handleChange = event => {
    const { name, value } = event.target;
    setFormData(prevFormData => ({
      ...prevFormData,
      [name]: value
    }));
  };

 
  const createUser = async () => {
    try {
      const token = sessionStorage.getItem('token');
  
      if (token) {
        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
            'Content-Type': 'application/json', // Add this line
          },
        };
  
        console.log('Sending formData:', formData); // Log the formData being sent
  
        const response = await axios.post('http://localhost:5001/admin', formData, config);
        // Mettre à jour la liste des utilisateurs après l'ajout
        fetchUsers();
        console.log('Adding successful');
      }
    } catch (error) {
      console.error('Error creating user:', error);
      console.log('Error response data:', error.response.data);
    }
  };

  
  
    const handleSaveUser = async () => {
      try {
        const token = sessionStorage.getItem('token');
    
        if (token) {
          const config = {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          };
    
          const response = await axios.put(`http://localhost:5001/admin/${formData._id}`, formData, config);
          // Mettre à jour la liste des utilisateurs après la mise à jour
          fetchUsers();
          // Réinitialiser le formulaire d'édition
          setFormData({
            name: '',
            phone: '',
            email: '',
            address: ''
          });
        }
      } catch (error) {
        console.error('Error updating user:', error);
        console.log('Error response data:', error.response.data);
        }
    };
    
    const handleDeactivateUser = async (userId) => {
      try {
        const token = sessionStorage.getItem('token');

      if (token) {
        const config = {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        };
        const response = await axios.put(`http://localhost:5001/admin/${userId}/deactivate`, null, config);
        // Mettre à jour la liste des utilisateurs après la désactivation
        fetchUsers();
      }
      } catch (error) {
        console.error('Error deactivating user:', error);
      }
    };
  

  return (
    <div className="admin-dashboard">
      <h1>Admin Dashboard</h1>
      <h2>Add User</h2>
      <form className="add-user-form">
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleChange}
          placeholder="Name"
        />
        <input
          type="text"
          name="phone"
          value={formData.phone}
          onChange={handleChange}
          placeholder="Phone"
        />
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Email"
        />
        <input
          type="text"
          name="address"
          value={formData.address}
          onChange={handleChange}
          placeholder="Address"
        />
        <button type="button" onClick={createUser}>
          Add User
        </button>
      </form>
      <h2>List users</h2>
      <table className="user-table" >
        <thead>
          <tr>
            <th colSpan={2}>name</th>
            <th colSpan={2}>Email</th>
            <th colSpan={2}>phone</th>
            <th colSpan={2}>address</th>
            {/* Ajoutez d'autres en-têtes en fonction des propriétés des utilisateurs */}
          </tr>
        </thead>
        <tbody>
          {users.map(user => (
            <tr key={user._id}>
              <td colSpan={2}>{user.name}</td>
              <td colSpan={2}>{user.email}</td>
              <td colSpan={2}>{user.phone}</td>
              <td colSpan={2}>{user.address}</td>
              {/* Ajoutez d'autres cellules en fonction des propriétés des utilisateurs */}
    <td className="edit-buttons" > 
    <button className="edit-button"type="button" onClick={() => {
  setEditingUserId(user._id);
  // Update formData with user's information
  setFormData({
    _id: user._id, 
    name: user.name,
    phone: user.phone,
    email: user.email,
    address: user.address
  });
}}>
  Edit
</button>


<button className="deactivate-button"onClick={() => handleDeactivateUser(user._id)}>Deactivate</button>
{editingUserId === user._id && (
  <React.Fragment>
    <input
      type="text"
      name="name"
      value={formData.name}
      onChange={handleChange}
      placeholder="Name"
    />
    <input
      type="email"
      name="email"
      value={formData.email}
      onChange={handleChange}
      placeholder="email"
    />
    <input
      type="text"
      name="phone"
      value={formData.phone}
      onChange={handleChange}
      placeholder="phone"
    />
    <input
      type="text"
      name="address"
      value={formData.address}
      onChange={handleChange}
      placeholder="Address"
    />
    <button className="save-button"type="button" onClick={handleSaveUser}>
      Save
    </button>
  </React.Fragment>
 )}
 </td>
</tr>
))}
</tbody>
</table>
</div>
);
};
export default AdminDashboard;
