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

  const [address, setAddress] = React.useState("");

  const handleSearch = () => {
    if (address.trim()) {
      navigate(`/restaurants?address=${encodeURIComponent(address)}`);
    }
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

        <div className="header-buttons">
          <button className="browse-btn" onClick={() => navigate('/restaurants')}>
          Browse Restaurants
        </button>

        

        {!user && (
          <div className="auth-buttons">
            <button className="login-btn" onClick={openLoginModal}>Log In</button>
            <button className="signup-btn" onClick={openSignupModal}>Sign Up</button>
          </div>
        )}
        </div>
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
              value={address}
              onChange={(e) => setAddress(e.target.value)}
            />
          </div>
          <button className="search-btn" onClick={handleSearch}>Search here</button>
        </div>
      </main>
    </div>
  );
};

export default HomePage;