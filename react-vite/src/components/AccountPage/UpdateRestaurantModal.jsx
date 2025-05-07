import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { thunkUpdateRestaurant } from "../../redux/restaurant";
import "./UpdateRestaurantModal.css";

function UpdateRestaurantModal({ restaurant, closeModal }) {
  const dispatch = useDispatch();
  
  const [name, setName] = useState(restaurant.name);
  const [description, setDescription] = useState(restaurant.description);
  const [category, setCategory] = useState(restaurant.category);
  const [priceRange, setPriceRange] = useState(restaurant.price_range);
  const [address, setAddress] = useState(restaurant.address);
  const [city, setCity] = useState(restaurant.city);
  const [state, setState] = useState(restaurant.state);
  const [zipCode, setZipCode] = useState(restaurant.zip_code);
  const [lat, setLat] = useState(restaurant.lat);
  const [lng, setLng] = useState(restaurant.lng);

  useEffect(() => {
    setName(restaurant.name);
    setDescription(restaurant.description);
    setCategory(restaurant.category);
    setPriceRange(restaurant.price_range);
    setAddress(restaurant.address);
    setCity(restaurant.city);
    setState(restaurant.state);
    setZipCode(restaurant.zip_code);
    setLat(restaurant.lat);
    setLng(restaurant.lng);
  }, [restaurant]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const updatedRestaurant = {
      id: restaurant.id,
      name,
      description,
      category,
      priceRange,
      address,
      city,
      state,
      zipCode,
      lat,
      lng,
    };
    
    dispatch(thunkUpdateRestaurant(updatedRestaurant)); // Dispatch Redux action for updating restaurant
    closeModal(); // Close modal after submission
  };

  return (
    <div className="modal-overlay">
      <div className="modal-container">
        <h2>Update Restaurant</h2>
        <form onSubmit={handleSubmit}>
          <input 
            type="text" 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
            required
          />
          <textarea 
            value={description} 
            onChange={(e) => setDescription(e.target.value)} 
            required
          />
          <input 
            type="text" 
            value={category} 
            onChange={(e) => setCategory(e.target.value)} 
            required
          />
          <input 
            type="text" 
            value={priceRange} 
            onChange={(e) => setPriceRange(e.target.value)} 
          />
          <input 
            type="text" 
            value={address} 
            onChange={(e) => setAddress(e.target.value)} 
            required
          />
          <input 
            type="text" 
            value={city} 
            onChange={(e) => setCity(e.target.value)} 
            required
          />
          <input 
            type="text" 
            value={state} 
            onChange={(e) => setState(e.target.value)} 
            required
          />
          <input 
            type="text" 
            value={zipCode} 
            onChange={(e) => setZipCode(e.target.value)} 
            required
          />
          <input 
            type="number" 
            step="any" 
            value={lat} 
            onChange={(e) => setLat(e.target.value)} 
          />
          <input 
            type="number" 
            step="any" 
            value={lng} 
            onChange={(e) => setLng(e.target.value)} 
          />
          <button type="submit">Update Restaurant</button>
        </form>
        <button onClick={closeModal}>Cancel</button>
      </div>
    </div>
  );
}

export default UpdateRestaurantModal;