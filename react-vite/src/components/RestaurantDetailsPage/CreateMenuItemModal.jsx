import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { thunkCreateMenuItem } from '../../redux/menuItem';
import { useModal } from '../../context/Modal';
import './CreateMenuItemModal.css'

const CreateMenuItemModal = ({ restaurantId }) => {
  const dispatch = useDispatch();
  const { setModalContent } = useModal();

  // State for the form fields
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [imageUrl, setImageUrl] = useState('');

  const [errors, setErrors] = useState([]);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate form fields
    const validationErrors = [];
    if (!name) validationErrors.push("Name is required");
    if (!price || isNaN(price) || price <= 0) validationErrors.push("Price must be a positive number");
    if (validationErrors.length) {
      setErrors(validationErrors);
      return;
    }

    // Dispatch the thunk to create the menu item
    await dispatch(thunkCreateMenuItem({ restaurantId, name, description, price: parseFloat(price), imageUrl }));

    // Close the modal after successful creation
    setModalContent(null);
  };

  return (
    <div className="create-menu-item-modal">
      <h2>Add Menu Item</h2>

      {errors.length > 0 && (
        <div className="error-messages">
          <ul>
            {errors.map((error, idx) => (
              <li key={idx}>{error}</li>
            ))}
          </ul>
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            id="name"
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Menu Item Name"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Menu Item Description"
          />
        </div>

        <div className="form-group">
          <label htmlFor="price">Price:</label>
          <input
            id="price"
            type="number"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            placeholder="Price"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="imageUrl">Image URL (optional):</label>
          <input
            id="imageUrl"
            type="url"
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            placeholder="Image URL"
          />
        </div>

        <div className="modal-actions">
          <button type="submit" className="submit-button">Create Menu Item</button>
          <button
            type="button"
            className="cancel-button"
            onClick={() => setModalContent(null)}
          >
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
};

export default CreateMenuItemModal;