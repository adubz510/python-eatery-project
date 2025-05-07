import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import CreateRestaurantModal from './CreateRestaurantModal';
import UpdateRestaurantModal from './UpdateRestaurantModal';
import DeleteRestaurantModal from './DeleteRestaurantModal';
import { thunkFetchUserRestaurants } from '../../redux/restaurant';

const AccountPage = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const userRestaurants = useSelector(state => Object.values(state.restaurants.userRestaurants || {}));

  const [showCreateModal, setShowCreateModal] = useState(false);
  const [showUpdateModal, setShowUpdateModal] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [selectedRestaurant, setSelectedRestaurant] = useState(null);

  useEffect(() => {
    if (user) dispatch(thunkFetchUserRestaurants());
  }, [dispatch, user]);

  const handleCreateRestaurant = () => {
    setShowCreateModal(true);
  };

  const handleUpdateRestaurant = (restaurant) => {
    setSelectedRestaurant(restaurant);
    setShowUpdateModal(true);
  };

  const handleDeleteRestaurant = (restaurant) => {
    setSelectedRestaurant(restaurant);
    setShowDeleteModal(true);
  };

  return (
    <div className="account-page">
      <h1>Your Restaurants</h1>
      <button onClick={handleCreateRestaurant}>Create Restaurant</button>

      <div className="restaurant-list">
        {userRestaurants.length === 0 ? (
          <p>You have not created any restaurants yet.</p>
        ) : (
          userRestaurants.map((restaurant) => {
            // Get the first image URL or use a placeholder
            const imageUrl = restaurant.images && restaurant.images.length > 0
              ? restaurant.images[0].url
              : 'https://via.placeholder.com/300x200?text=No+Image';

            return (
              <div key={restaurant.id} className="restaurant-card">
                <img
                  src={imageUrl}
                  alt={restaurant.name}
                  className="restaurant-image"
                />
                <div className="restaurant-info">
                  <h2>{restaurant.name}</h2>
                  <p>{restaurant.category} | {restaurant.city}</p>
                </div>
                <button onClick={() => handleUpdateRestaurant(restaurant)}>Update</button>
                <button onClick={() => handleDeleteRestaurant(restaurant)}>Delete</button>
              </div>
            );
          })
        )}
      </div>

      {showCreateModal && (
        <CreateRestaurantModal setShowModal={setShowCreateModal} />
      )}
      {showUpdateModal && (
        <UpdateRestaurantModal
          setShowModal={setShowUpdateModal}
          restaurant={selectedRestaurant}
        />
      )}
      {showDeleteModal && (
        <DeleteRestaurantModal
          setShowModal={setShowDeleteModal}
          restaurant={selectedRestaurant}
        />
      )}
    </div>
  );
};

export default AccountPage;