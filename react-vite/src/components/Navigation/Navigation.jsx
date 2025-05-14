import { NavLink, useNavigate } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import { useState } from "react";
import "./Navigation.css";

function Navigation() {
  const [searchQuery, setSearchQuery] = useState("");
  const navigate = useNavigate();

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/search?query=${encodeURIComponent(searchQuery.trim())}`);
      setSearchQuery("");
    }
  };

  return (
    <nav className="nav-wrapper">
      <div className="nav-left">
        <NavLink to="/" className="nav-link">Home</NavLink>

        <button
          className="browse-btn"
          onClick={() => navigate("/restaurants")}
        >
          Browse Restaurants
        </button>

        <div className="profile-button-wrapper">
          <ProfileButton />
        </div>
      </div>

      <form onSubmit={handleSearchSubmit} className="search-bar">
        <div className="input-group">
          <span className="icon">🔍</span>
          <input
            type="text"
            className="address-input"
            placeholder="Search restaurants..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
        <button className="search-btn" type="submit">Search</button>
      </form>
    </nav>
  );
}

export default Navigation;