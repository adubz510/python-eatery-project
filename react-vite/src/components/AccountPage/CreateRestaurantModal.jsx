import { useState } from "react";
import { useDispatch } from "react-redux";
import { thunkCreateRestaurant } from "../../redux/restaurant";
import "./CreateRestaurantModal.css";
import thunk from "redux-thunk";

function CreateRestaurantModal({ closeModal }) {
  const dispatch = useDispatch();
  
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [category, setCategory] = useState("");
  const [priceRange, setPriceRange] = useState("");
  const [address, setAddress] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [zipCode, setZipCode] = useState("");
  const [lat, setLat] = useState("");
  const [lng, setLng] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    const newRestaurant = {
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
    
    dispatch(thunkCreateRestaurant(newRestaurant)); // Dispatch Redux action for creating restaurant
    closeModal(); // Close modal after submission
  };

  return (
    <div className="modal-overlay">
      <div className="modal-container">
        <h2>Create a New Restaurant</h2>
        <form onSubmit={handleSubmit}>
          <input 
            type="text" 
            placeholder="Restaurant Name" 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
            required
          />
          <textarea 
            placeholder="Description" 
            value={description} 
            onChange={(e) => setDescription(e.target.value)} 
            required
          />
          <input 
            type="text" 
            placeholder="Category" 
            value={category} 
            onChange={(e) => setCategory(e.target.value)} 
            required
          />
          <input 
            type="text" 
            placeholder="Price Range" 
            value={priceRange} 
            onChange={(e) => setPriceRange(e.target.value)} 
          />
          <input 
            type="text" 
            placeholder="Address" 
            value={address} 
            onChange={(e) => setAddress(e.target.value)} 
            required
          />
          <input 
            type="text" 
            placeholder="City" 
            value={city} 
            onChange={(e) => setCity(e.target.value)} 
            required
          />
          <input 
            type="text" 
            placeholder="State" 
            value={state} 
            onChange={(e) => setState(e.target.value)} 
            required
          />
          <input 
            type="text" 
            placeholder="Zip Code" 
            value={zipCode} 
            onChange={(e) => setZipCode(e.target.value)} 
            required
          />
          <input 
            type="number" 
            step="any" 
            placeholder="Latitude" 
            value={lat} 
            onChange={(e) => setLat(e.target.value)} 
          />
          <input 
            type="number" 
            step="any" 
            placeholder="Longitude" 
            value={lng} 
            onChange={(e) => setLng(e.target.value)} 
          />
          <button type="submit">Create Restaurant</button>
        </form>
        <button onClick={closeModal}>Cancel</button>
      </div>
    </div>
  );
}

export default CreateRestaurantModal;