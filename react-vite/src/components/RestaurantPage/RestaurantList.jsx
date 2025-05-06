import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { thunkFetchRestaurants } from '../../redux/restaurant';
import { Link } from 'react-router-dom';
import thunk from 'redux-thunk';

const RestaurantList = () => {
  const dispatch = useDispatch();
  const restaurants = useSelector(state => Object.values(state.restaurants || {}));

  useEffect(() => {
    dispatch(thunkFetchRestaurants());
  }, [dispatch]);

  if (!restaurants || restaurants.length === 0) {
    return <div>Loading restaurants...</div>;
  }

  return (
    <div className="restaurant-list">
      <h1>All Restaurants</h1>
      {restaurants.map(restaurant => (
        <div key={restaurant.id} className="restaurant-card">
          <Link to={`/restaurants/${restaurant.id}`}>
            <h2>{restaurant.name}</h2>
          </Link>
          <p>{restaurant.category}</p>
          <p>{restaurant.address}</p>
        </div>
      ))}
    </div>
  );
};

export default RestaurantList;