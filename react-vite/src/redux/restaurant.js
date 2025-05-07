// Action Types
const LOAD_RESTAURANTS = 'restaurants/LOAD_RESTAURANTS';
const ADD_RESTAURANT = 'restaurants/ADD_RESTAURANT';
const UPDATE_RESTAURANT = 'restaurants/UPDATE_RESTAURANT';
const DELETE_RESTAURANT = 'restaurants/DELETE_RESTAURANT';

// Action Creators
const loadRestaurants = (restaurants) => ({
  type: LOAD_RESTAURANTS,
  payload: restaurants
});

const addRestaurant = (restaurant) => ({
  type: ADD_RESTAURANT,
  payload: restaurant
});

const updateRestaurant = (restaurant) => ({
  type: UPDATE_RESTAURANT,
  payload: restaurant
});

const deleteRestaurant = (restaurantId) => ({
  type: DELETE_RESTAURANT,
  payload: restaurantId
});

// Thunks
export const thunkFetchRestaurants = () => async (dispatch) => {
    try {
      const res = await fetch('/api/restaurants/');
  
      if (res.ok) {
        const data = await res.json();
        console.log("Restaurants:", data)
        dispatch(loadRestaurants(data));
      } else {
        const errorText = await res.text();
        console.error('Fetch failed:', res.status, errorText);
      }
    } catch (err) {
      console.error('Unexpected fetch error:', err);
    }
  };

export const thunkCreateRestaurant = (restaurantData) => async (dispatch) => {
  const res = await fetch('/api/restaurants/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(restaurantData)
  });

  if (res.ok) {
    const data = await res.json();
    dispatch(addRestaurant(data));
    return data;
  } else {
    const errorData = await res.json();
    return errorData;
  }
};

export const thunkUpdateRestaurant = (restaurantId, restaurantData) => async (dispatch) => {
  const res = await fetch(`/api/restaurants/${restaurantId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(restaurantData)
  });

  if (res.ok) {
    const data = await res.json();
    dispatch(updateRestaurant(data));
    return data;
  } else {
    const errorData = await res.json();
    return errorData;
  }
};

export const thunkDeleteRestaurant = (restaurantId) => async (dispatch) => {
  const res = await fetch(`/api/restaurants/${restaurantId}`, {
    method: 'DELETE'
  });

  if (res.ok) {
    dispatch(deleteRestaurant(restaurantId));
    return true;
  } else {
    return false;
  }
};

// Reducer
const initialState = {};

function restaurantsReducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_RESTAURANTS: {
      const newState = {};
      action.payload.forEach(restaurant => {
        newState[restaurant.id] = restaurant;
      });
      return newState;
    }
    case ADD_RESTAURANT:
      return { ...state, [action.payload.id]: action.payload };
    case UPDATE_RESTAURANT:
      return { ...state, [action.payload.id]: action.payload };
    case DELETE_RESTAURANT: {
      const newState = { ...state };
      delete newState[action.payload];
      return newState;
    }
    default:
      return state;
  }
}

export default restaurantsReducer