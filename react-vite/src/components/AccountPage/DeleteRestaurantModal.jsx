import { useDispatch } from "react-redux";
import { thunkDeleteRestaurant } from "../../redux/restaurant";
import "./DeleteRestaurantModal.css";

function DeleteRestaurantModal({ restaurant, closeModal }) {
  const dispatch = useDispatch();

  const handleDelete = () => {
    dispatch(thunkDeleteRestaurant(restaurant.id)); // Dispatch Redux action for deleting restaurant
    closeModal(); // Close modal after deletion
  };

  return (
    <div className="modal-overlay">
      <div className="modal-container">
        <h2>Are you sure you want to delete this restaurant?</h2>
        <p>{restaurant.name}</p>
        <button onClick={handleDelete}>Delete</button>
        <button onClick={closeModal}>Cancel</button>
      </div>
    </div>
  );
}

export default DeleteRestaurantModal;