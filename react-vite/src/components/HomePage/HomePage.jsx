import React from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useSelector } from 'react-redux'; 
import { FaLocationArrow } from 'react-icons/fa';
import './HomePage.css';
import { useModal } from '../../context/Modal'; // For modal context 
import ProfileButton from '../Navigation/ProfileButton';
import LoginFormModal from '../LoginFormModal';
import SignupFormModal from '../SignupFormModal';


const HomePage = () => {
  const navigate = useNavigate();
  const { setModalContent } = useModal(); // Using modal context if needed

  const user = useSelector((state) => state.session.user); // Accessing user from Redux

  const handleSearch = () => {
    // Navigate to restaurants page (can add query params here)
    navigate('/restaurants');
  };

  const openLoginModal = () => {
    setModalContent(<LoginFormModal />);
  };

  const openSignupModal = () => {
    setModalContent(<SignupFormModal />);
  };

  return (
    <div className="homepage">    
      <header className="homepage-header">
      <div className="logo">
        <ProfileButton />
      </div>

      {!user && (
      <div className="auth-buttons">
        <button className="login-btn" onClick={openLoginModal}>Log In</button>
        <button className="signup-btn" onClick={openSignupModal}>Sign Up</button>
      </div>
      )}

      </header>

      <main className="homepage-main">
        <h1 className="homepage-title">Find Restaurants Near You</h1>

        <div className="search-bar">
          <div className="input-group">
            <FaLocationArrow className="icon" />
            <input
              type="text"
              placeholder="Enter delivery address"
              className="address-input"
            />
          </div>
          <button className="search-btn" onClick={handleSearch}>Search here</button>
        </div>
      </main>
    </div>
  );
};

export default HomePage;