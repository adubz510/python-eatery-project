import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Link, useLocation } from 'react-router-dom';
import { thunkFetchRestaurants } from '../../redux/restaurant';
import './RestaurantPage.css'; // assuming shared styling

const SearchResultsPage = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(thunkFetchRestaurants());
  }, [dispatch]);

  const restaurants = useSelector((state) => Object.values(state.restaurants || {}));
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const searchTerm = queryParams.get('query')?.toLowerCase() || '';

  const filteredRestaurants = restaurants.filter((restaurant) => {
    const nameMatch = restaurant.name?.toLowerCase().includes(searchTerm);
    const categoryMatch = restaurant.category?.toLowerCase().includes(searchTerm);
    const menuMatch = restaurant.menuItems?.some(item =>
      item.name?.toLowerCase().includes(searchTerm)
    );
    return nameMatch || categoryMatch || menuMatch;
  });

  if (filteredRestaurants.length === 0) {
    return <div className="restaurant-list-container">No results found for "{searchTerm}"</div>;
  }

  return (
    <div className="restaurant-list-container">
      <h1>Search Results for "{searchTerm}"</h1>
      <div className="restaurant-grid">
        {filteredRestaurants.map((restaurant) => (
          <Link
            key={restaurant.id}
            to={`/restaurants/${restaurant.id}`}
            className="restaurant-card"
          >
            <img
              src={
                restaurant.images?.length > 0
                  ? restaurant.images[0].url
                  : '/default-restaurant.jpg'
              }
              alt={restaurant.name}
              className="restaurant-image"
            />
            <div className="restaurant-info">
              <h2>{restaurant.name}</h2>
              <p className="category">{restaurant.category}</p>
              <p className="address">{restaurant.address}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default SearchResultsPage;