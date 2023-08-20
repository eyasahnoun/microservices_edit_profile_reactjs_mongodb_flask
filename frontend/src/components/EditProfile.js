import React from 'react';

const EditProfile = ({ token, handleEditProfile }) => {
  return (
    <div>
      <h1>Edit Profile</h1>
      <button onClick={handleEditProfile}>Edit Profile</button>
    </div>
  );
};

export default EditProfile;
