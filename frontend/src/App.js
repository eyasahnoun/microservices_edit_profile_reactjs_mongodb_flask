import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import AdminInterface from './components/adminInterface';
import './App.css'; // Importez votre fichier de styles

const App = () => {
  const [message, setMessage] = useState('');
  const [tokenLoaded, setTokenLoaded] = useState(false); // État pour indiquer si le token a été chargé

  useEffect(() => {
    // Récupérer le token depuis le stockage de session
    const token = sessionStorage.getItem('token');

    // Vérifier si le token est chargé
    if (token) {
      setTokenLoaded(true);
    }
  }, []);

  const handleEditProfile = () => {
    if (!tokenLoaded) {
      setMessage('Token manquant');
    } else {
      // Le reste du code pour gérer la modification de profil
      setMessage('');
    }
  };

  return (
    <div className="app">
      <Router>
        <Switch>
          <Route exact path="/">
            <div className="landing">
              <h1>Edit Profile</h1>
              <Link to="/AdminInterface">
                <button className="edit-profile-button" onClick={handleEditProfile} disabled={!tokenLoaded}>Edit Profile</button>
              </Link>
            </div>
          </Route>
          <Route path="/AdminInterface" component={AdminInterface} />
        </Switch>
      </Router>
    </div>
  );
};

export default App;
